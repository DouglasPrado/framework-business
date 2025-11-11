"""Camada mínima de deepagents usada pelos scripts locais."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from textwrap import dedent
from typing import Any, Iterable, List, Sequence, Tuple

try:  # pragma: no cover - dependência opcional
    from langchain_openai import ChatOpenAI
except ImportError:  # pragma: no cover
    ChatOpenAI = None  # type: ignore

try:  # pragma: no cover - utilizado apenas quando LangChain está instalado
    from langchain.agents import AgentExecutor, create_tool_calling_agent  # type: ignore
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # type: ignore
except ImportError:  # pragma: no cover
    AgentExecutor = None  # type: ignore
    create_tool_calling_agent = None  # type: ignore
    ChatPromptTemplate = None  # type: ignore
    MessagesPlaceholder = None  # type: ignore

from .state import AgentStateStore
from .tools import ToolLike, get_default_tools


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
    state_store: AgentStateStore | None = None

    def __post_init__(self) -> None:
        provided_tools = self.tools or []
        self.state_store = self.state_store or AgentStateStore()
        self.tools, self._tool_display_names = _normalize_tools(provided_tools)
        if not self.tools:
            default_tools = get_default_tools()
            defaults, default_names = _normalize_tools(default_tools)
            self.tools.extend(defaults)
            self._tool_display_names.extend(default_names)
        self._llm = None
        self._executor = None
        if ChatOpenAI is not None and os.getenv("OPENAI_API_KEY"):
            self._llm = ChatOpenAI(model=self.model_name, temperature=self.temperature)
            self._setup_executor()

    def _setup_executor(self) -> None:
        if self._llm is None:
            return
        if create_tool_calling_agent is None or ChatPromptTemplate is None:
            return
        memory = self.state_store.memory if self.state_store else None
        messages = [("system", dedent(
            f"""
            {self.system_prompt.strip()}

            Ferramentas virtuais disponíveis: {', '.join(self._tool_display_names) or 'ls/read/write'}.
            Regras: respeite AGENTS.MD, escreva em português, sem tabelas e sem emojis.
            """
        ).strip())]
        if memory is not None and hasattr(memory, "memory_key") and MessagesPlaceholder is not None:
            messages.append(MessagesPlaceholder(variable_name=getattr(memory, "memory_key", "chat_history")))
        messages.append(("human", "{input}"))
        prompt = ChatPromptTemplate.from_messages(messages)
        agent = create_tool_calling_agent(self._llm, list(self.tools), prompt)
        kwargs: dict[str, Any] = {"agent": agent, "tools": list(self.tools), "verbose": False}
        if memory is not None and hasattr(memory, "load_memory_variables"):
            kwargs["memory"] = memory
        kwargs["handle_parsing_errors"] = True
        self._executor = AgentExecutor(**kwargs)

    def _record_user_message(self, instructions: str) -> None:
        if self.state_store is not None:
            self.state_store.add_user_message(instructions)

    def _record_ai_message(self, response: str) -> None:
        if self.state_store is not None:
            self.state_store.add_ai_message(response)

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


def create_deep_agent(
    system_prompt: str,
    tools: Iterable[Any] | None = None,
    state_store: AgentStateStore | None = None,
    *,
    model_name: str = "gpt-4o-mini",
    temperature: float = 0.4,
):
    return _LangChainAgent(
        system_prompt=system_prompt,
        tools=tools,
        model_name=model_name,
        temperature=temperature,
        state_store=state_store,
    )
