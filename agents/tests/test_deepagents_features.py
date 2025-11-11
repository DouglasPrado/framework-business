"""Tests for DeepAgents tooling and state persistence."""

from __future__ import annotations

from typing import Any

from agents import BASE_PATH
from agents.deepagents import create_deep_agent
from agents.deepagents.state import AgentStateStore
from agents.deepagents.tools import (
    create_internal_search_tool,
    create_markdown_summary_tool,
    get_default_tools,
)


def _extract_contents(messages: Any) -> list[str]:
    contents: list[str] = []
    for message in messages:
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
    store = AgentStateStore()
    tools = get_default_tools()
    agent = create_deep_agent(
        system_prompt="Você organiza execuções automáticas.",
        tools=tools,
        state_store=store,
    )
    output_one = agent.run(
        "Contexto destino: TestePersistencia\n\n## Contexto informado\nPrimeira rodada."
    )
    output_two = agent.run(
        "Contexto destino: TestePersistencia\n\n## Contexto informado\nSegunda rodada."
    )

    assert "Plano Automatizado" in output_one
    assert "Plano Automatizado" in output_two

    messages = getattr(store.memory, "chat_memory").messages
    contents = _extract_contents(messages)
    assert any("Primeira rodada" in content for content in contents)
    assert any("Segunda rodada" in content for content in contents)

    store.update_node_state("planejamento", status="ok")
    node_snapshot = store.get_state_for_node("planejamento")
    assert node_snapshot["status"] == "ok"

    graph_state = store.get_state_for_node("planejamento")
    assert isinstance(graph_state.get("chat_history"), list)

    full_state = store.as_graph_state()
    assert full_state["memory"] is store.memory
    assert full_state["nodes"]["planejamento"]["status"] == "ok"

    summary_names = [name for name in contents if "Plano Automatizado" in name]
    assert summary_names  # garante que as respostas foram registradas
