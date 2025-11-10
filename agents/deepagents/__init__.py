"""Camada mínima de deepagents usada pelos scripts locais."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import datetime
from textwrap import dedent
from typing import List

try:  # pragma: no cover - dependência opcional
    from langchain_openai import ChatOpenAI
except ImportError:  # pragma: no cover
    ChatOpenAI = None


def _clean(text: str, limit: int = 280) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else f"{text[: limit - 3]}..."


def _extract_context_description(instructions: str) -> str:
    match = re.search(r"## Contexto informado\s+(.+?)(?:\n## |\Z)", instructions, flags=re.S)
    if match:
        return _clean(match.group(1))
    return "Não informado"


def _fallback_summary(system_prompt: str, instructions: str) -> str:
    sections = re.findall(r"^#{1,3}\s+(.+)$", instructions, flags=re.MULTILINE)
    context_match = re.search(r"Contexto destino:\s*(.+)", instructions)
    context = context_match.group(1).strip().rstrip(".") if context_match else "Não informado"
    context_description = _extract_context_description(instructions)
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Plano Automatizado",
        f"Contexto (pasta): {context}",
        f"Contexto (descrição): {context_description}",
        f"Gerado em: {now}",
        "",
        "## Diretrizes do sistema",
        f"- Prompt-base: {_clean(system_prompt)}",
        f"- Ferramentas previstas: {_clean(', '.join(sections[:1]) or 'ls, read_file, write_file')}",
        "",
        "## Frentes priorizadas",
    ]
    for idx, section in enumerate(sections[:6], start=1):
        lines.append(f"- Frente {idx}: {section}")
    if not sections:
        lines.append("- Revisar instruções e transformar em entregáveis objetivos.")
    lines.extend(
        [
            "",
            "## Próximas entregas",
            "- Documentar aprendizados e atualizar manifestos.",
            "- Preparar inputs para o próximo processo dependente.",
        ]
    )
    return "\n".join(lines)


@dataclass
class _LangChainAgent:
    system_prompt: str
    tools: List[str]
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.4

    def __post_init__(self) -> None:
        self._llm = None
        if ChatOpenAI is not None and os.getenv("OPENAI_API_KEY"):
            self._llm = ChatOpenAI(model=self.model_name, temperature=self.temperature)

    def run(self, instructions: str) -> str:
        if self._llm is None:
            return _fallback_summary(self.system_prompt, instructions)
        composed_prompt = dedent(
            f"""
            {self.system_prompt.strip()}

            Ferramentas virtuais disponíveis: {', '.join(self.tools) or 'ls/read/write'}.
            Regras: respeite AGENTS.MD, escreva em português, sem tabelas e sem emojis.

            ### Entrada
            {instructions.strip()}

            ### Saída Esperada
            Produza o artefato final pronto para publicação, contextualizado ao drive indicado.
            """
        ).strip()
        response = self._llm.invoke(composed_prompt)
        content = getattr(response, "content", None)
        if isinstance(content, list):
            return "\n".join(part.get("text", "") for part in content if isinstance(part, dict))
        if isinstance(content, str):
            return content
        return str(response)


def create_deep_agent(system_prompt: str, tools: List[str] | None = None):
    return _LangChainAgent(system_prompt=system_prompt, tools=tools or [])
