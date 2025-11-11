"""Camada mínima de deepagents usada pelos scripts locais."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from textwrap import dedent
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from ..llm_factory import build_llm
from .reasoning import (
    create_draft_prompt,
    create_reflection_prompt,
    create_refinement_prompt,
    format_thinking_traces,
    get_reasoning_config,
)


# Stub types para compatibilidade
class ToolLike:
    """Tipo stub para ferramentas."""
    def __init__(self, name: str, description: str, func: Any):
        self.name = name
        self.description = description
        self.func = func


# Alias para DeepAgent
DeepAgent = Any


def _clean(text: str, limit: int = 280) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else f"{text[: limit - 3]}..."


def _extract_context_description(instructions: str) -> str:
    match = re.search(r"## Contexto informado\s+(.+?)(?:\n## |\Z)", instructions, flags=re.S)
    if match:
        return _clean(match.group(1))
    return "Não informado"


def _fallback_summary(system_prompt: str, instructions: str, tool_names: Sequence[str]) -> str:
    sections = re.findall(r"^#{1,3}\s+(.+)$", instructions, flags=re.MULTILINE)
    context_match = re.search(r"Contexto destino:\s*(.+)", instructions)
    context = context_match.group(1).strip().rstrip(".") if context_match else "Não informado"
    context_description = _extract_context_description(instructions)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    listed_tools = ", ".join(tool_names) if tool_names else "ls, read_file, write_file"

    lines = [
        "# Plano Automatizado",
        f"Contexto (pasta): {context}",
        f"Contexto (descrição): {context_description}",
        f"Gerado em: {now}",
        "",
        "## Diretrizes do sistema",
        f"- Prompt-base: {_clean(system_prompt)}",
        f"- Ferramentas previstas: {_clean(listed_tools)}",
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


def _is_tool_instance(tool: Any) -> bool:
    return hasattr(tool, "name") and callable(getattr(tool, "__call__", None))


def _normalize_tools(tools: Iterable[Any]) -> Tuple[List[ToolLike], List[str]]:
    normalized: List[ToolLike] = []
    display_names: List[str] = []
    for entry in tools:
        if _is_tool_instance(entry):
            normalized.append(entry)  # type: ignore[arg-type]
            display_names.append(getattr(entry, "name", repr(entry)))
            continue
        if callable(entry):
            name = getattr(entry, "__name__", "custom_tool")
            tool = ToolLike(name=name, description=f"Ferramenta customizada {name}.", func=entry)  # type: ignore[arg-type]
            normalized.append(tool)
            display_names.append(name)
            continue
        if isinstance(entry, str):
            display_names.append(entry)
            continue
        display_names.append(repr(entry))
    return normalized, display_names


@dataclass
class _LangChainAgent:
    system_prompt: str
    tools: Iterable[Any] | None = None
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.4
    llm_config: Optional[Dict[str, Any]] = None
    llm_instance: Any = None

    def __post_init__(self) -> None:
        self._llm_error: Optional[Exception] = None
        self._llm = None
        self._executor = None
        self._tool_display_names: List[str] = []
        self._messages: List[Dict[str, str]] = []

        # Normalizar ferramentas se fornecidas
        if self.tools:
            _, self._tool_display_names = _normalize_tools(self.tools)

        if self.llm_instance is not None:
            self._llm = self.llm_instance
            return
        config = dict(self.llm_config or {})
        config.setdefault("model", self.model_name)
        config.setdefault("temperature", self.temperature)
        should_try = bool(config) or bool(os.getenv("OPENAI_API_KEY"))
        if not should_try:
            return
        try:
            self._llm = build_llm(config)
        except Exception as exc:  # pragma: no cover - falha deve permitir fallback
            self._llm_error = exc

    def _record_user_message(self, content: str) -> None:
        """Registra mensagem do usuário no histórico."""
        self._messages.append({"role": "user", "content": content})

    def _record_ai_message(self, content: str) -> None:
        """Registra mensagem da IA no histórico."""
        self._messages.append({"role": "assistant", "content": content})

    def run(self, instructions: str) -> str:
        self._record_user_message(instructions)
        if self._executor is not None:
            result = self._executor.invoke({"input": instructions})
            if isinstance(result, dict) and "output" in result:
                response = str(result["output"])
            else:
                response = str(result)
            self._record_ai_message(response)
            return response
        if self._llm is None:
            response = _fallback_summary(self.system_prompt, instructions, self._tool_display_names)
            self._record_ai_message(response)
            return response
        composed_prompt = dedent(
            f"""
            {self.system_prompt.strip()}

            Ferramentas virtuais disponíveis: {', '.join(self._tool_display_names) or 'ls/read/write'}.
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
            text = "\n".join(part.get("text", "") for part in content if isinstance(part, dict))
        elif isinstance(content, str):
            text = content
        else:
            text = str(response)
        self._record_ai_message(text)
        return text

    def run_with_reflection(
        self,
        instructions: str,
        validator_content: str = "",
        process_code: str = "Process",
    ) -> Dict[str, Any]:
        """
        Executa raciocínio estendido com padrão de reflexão (draft → critique → refine).

        Args:
            instructions: Instruções completas do processo
            validator_content: Conteúdo do validator.MD para referência na crítica
            process_code: Código do processo para contexto

        Returns:
            Dicionário com:
                - content: Conteúdo final refinado
                - draft: Rascunho inicial
                - critique: Crítica gerada
                - thinking_traces: Métricas de cada estágio
        """
        self._record_user_message(instructions)

        if self._llm is None:
            # Fallback: modo simples sem reflexão
            response = _fallback_summary(self.system_prompt, instructions, self._tool_display_names)
            self._record_ai_message(response)
            return {
                "content": response,
                "draft": "",
                "critique": "",
                "thinking_traces": {"mode": "fallback"},
            }

        # Estágio 1: Gerar rascunho
        draft_prompt = create_draft_prompt(
            self.system_prompt,
            instructions,
            self._tool_display_names,
        )
        draft_config = get_reasoning_config("draft")
        draft_llm = build_llm(draft_config)
        draft_response = draft_llm.invoke(draft_prompt)
        draft = self._extract_content(draft_response)
        draft_tokens = self._estimate_tokens(draft)

        # Estágio 2: Refletir sobre o rascunho
        reflection_prompt = create_reflection_prompt(
            draft,
            validator_content,
            instructions,
            process_code,
        )
        critique_config = get_reasoning_config("reflection")
        critique_llm = build_llm(critique_config)
        critique_response = critique_llm.invoke(reflection_prompt)
        critique = self._extract_content(critique_response)
        critique_tokens = self._estimate_tokens(critique)

        # Estágio 3: Refinar com base na crítica
        refinement_prompt = create_refinement_prompt(
            draft,
            critique,
            instructions,
        )
        refined_config = get_reasoning_config("refinement")
        refined_llm = build_llm(refined_config)
        refined_response = refined_llm.invoke(refinement_prompt)
        refined = self._extract_content(refined_response)
        refined_tokens = self._estimate_tokens(refined)

        # Registrar resultado final
        self._record_ai_message(refined)

        # Preparar thinking traces
        traces = format_thinking_traces(
            draft_tokens=draft_tokens,
            critique_tokens=critique_tokens,
            refined_tokens=refined_tokens,
            draft_length=len(draft),
            critique_length=len(critique),
            refined_length=len(refined),
        )

        return {
            "content": refined,
            "draft": draft,
            "critique": critique,
            "thinking_traces": traces,
        }

    def _extract_content(self, response: Any) -> str:
        """Extrai conteúdo textual de resposta do LLM."""
        content = getattr(response, "content", None)
        if isinstance(content, list):
            return "\n".join(part.get("text", "") for part in content if isinstance(part, dict))
        elif isinstance(content, str):
            return content
        return str(response)

    def _estimate_tokens(self, text: str) -> int:
        """Estima número de tokens em um texto (aproximação simples)."""
        if not text:
            return 0
        # Aproximação: ~4 caracteres por token em inglês, ~5 em português
        return max(1, len(text) // 5)


def create_deep_agent(
    system_prompt: str,
    tools: List[str] | None = None,
    llm_config: Optional[Dict[str, Any]] = None,
    llm_instance: Any = None,
):
    return _LangChainAgent(
        system_prompt=system_prompt,
        tools=tools or [],
        llm_config=llm_config,
        llm_instance=llm_instance,
    )
