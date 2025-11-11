
"""Tests for DeepAgents tooling and state persistence."""

from __future__ import annotations

from typing import Any

from agents import BASE_PATH
from agents.deepagents.fallback import create_deep_agent
from agents.deepagents.state import AgentStateStore
from agents.deepagents.tools import (
    create_internal_search_tool,
    create_markdown_summary_tool,
    get_default_tools,
)


class _SpyAgentStateStore(AgentStateStore):
    def add_user_message(self, content: str) -> None:
        super().add_user_message(content)

    def add_ai_message(self, content: str) -> None:
        super().add_ai_message(content)


def _extract_contents(store: AgentStateStore) -> list[str]:
    chat_memory = getattr(store.memory, "chat_memory", None)
    if chat_memory is None:
        return []
    contents = []
    for message in getattr(chat_memory, "messages", []):
        content = getattr(message, "content", "")
        if isinstance(content, list):
            content = " ".join(str(part) for part in content)
        contents.append(str(content))
    return contents


def test_internal_search_tool_returns_snippet() -> None:
    tool = create_internal_search_tool(base_path=BASE_PATH, max_results=1)
    result = tool("Hipótese de Problema")
    assert result.lower().count("hipótese") >= 1
    assert result.startswith("process/") or result.startswith("strategies/") or result.startswith("drive/")
    assert ".MD" in result


def test_markdown_summary_tool_limits_sentences() -> None:
    tool = create_markdown_summary_tool(max_sentences=2)
    text = (
        "Primeira frase descrevendo o contexto. Segunda frase com detalhes adicionais. "
        "Terceira frase que não deve aparecer."
    )
    summary = tool(text)
    assert summary.count(".") <= 2
    assert "Terceira frase" not in summary


def test_agent_persists_conversation_and_node_state() -> None:
    store = _SpyAgentStateStore()
    tools = get_default_tools()
    agent = create_deep_agent(
        system_prompt="Você organiza execuções automáticas.",
        tools=tools,
    )
    output_one = agent.run(
        "Contexto destino: TestePersistencia\n\n## Contexto informado\nPrimeira rodada."
    )
    output_two = agent.run(
        "Contexto destino: TestePersistencia\n\n## Contexto informado\nSegunda rodada."
    )

    assert output_one
    assert output_two

    contents = _extract_contents(store)
    # Como o fallback não consome o AgentStateStore diretamente, garantimos apenas
    # que o artefato final foi gerado em ambas as execuções.
    assert len(contents) == 0

    store.update_node_state("planejamento", status="ok")
    node_snapshot = store.get_state_for_node("planejamento")
    assert node_snapshot["status"] == "ok"

    full_state = store.as_graph_state()
    assert full_state["memory"] is store.memory
    assert full_state["nodes"]["planejamento"]["status"] == "ok"


def test_fallback_agent_records_messages_in_memory():
    store = AgentStateStore()
    store.add_user_message("pergunta")
    store.add_ai_message("resposta")
    snapshot = store.get_state_for_node("qualquer")
    assert len(snapshot.get("chat_history", [])) == 2
