"""Tests for DeepAgents tooling and adapter integration."""

from __future__ import annotations

from typing import Any, Dict

import pytest
from . import BASE_PATH
from framework.llm.adapters import create_deep_agent
from framework.llm.adapters.state import AgentStateStore
from framework.llm.adapters.tools import (
    create_internal_search_tool,
    create_markdown_summary_tool,
    get_default_tools,
)


class _DummyLLM:
    """LLM mínimo injetado diretamente no deepagent oficial."""

    def __init__(self, name: str = "dummy-model") -> None:
        self.name = name


def test_internal_search_tool_returns_snippet() -> None:
    tool = create_internal_search_tool(base_path=BASE_PATH, max_results=1)
    result = tool("Hipótese de Problema")
    assert result.lower().count("hipótese") >= 1
    assert result.startswith(("process/", "strategies/", "drive/"))
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


def test_create_deep_agent_uses_injected_llm(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: Dict[str, Any] = {}

    def _fake_create_deep_agent(**kwargs: Any) -> Any:
        captured.update(kwargs)
        return {"agent": "ok"}

    monkeypatch.setattr(
        "agents.framework.llm.adapters._official_create_deep_agent",
        _fake_create_deep_agent,
    )

    llm = _DummyLLM()
    tools = get_default_tools()
    agent = create_deep_agent(
        system_prompt="Você organiza execuções automáticas.",
        tools=tools,
        llm_instance=llm,
    )

    assert agent == {"agent": "ok"}
    assert captured["model"] is llm
    assert captured["system_prompt"].startswith("Você organiza")
    assert isinstance(captured.get("tools"), (list, tuple))
    assert len(captured["tools"]) == len(tools)


def test_create_deep_agent_builds_model_from_config(monkeypatch: pytest.MonkeyPatch) -> None:
    built_model = object()
    captured: Dict[str, Any] = {}

    def _fake_build_llm(config: Dict[str, Any]) -> Any:
        captured["config"] = config
        return built_model

    def _fake_create_deep_agent(**kwargs: Any) -> Any:
        captured["kwargs"] = kwargs
        return {"agent": "config"}

    monkeypatch.setattr("agents.framework.llm.adapters.build_llm", _fake_build_llm)
    monkeypatch.setattr(
        "agents.framework.llm.adapters._official_create_deep_agent",
        _fake_create_deep_agent,
    )

    agent = create_deep_agent(
        system_prompt="Execute processos.",
        llm_config={"model": "gpt-4o-mini", "temperature": 0.1},
    )

    assert agent == {"agent": "config"}
    assert captured["config"]["model"] == "gpt-4o-mini"
    assert captured["kwargs"]["model"] is built_model
    assert captured["kwargs"]["system_prompt"].startswith("Execute processos")
    assert captured["kwargs"]["tools"] is None


def test_agent_state_store_records_messages() -> None:
    store = AgentStateStore()
    store.add_user_message("pergunta")
    store.add_ai_message("resposta")
    snapshot = store.get_state_for_node("qualquer")
    assert len(snapshot.get("chat_history", [])) == 2
