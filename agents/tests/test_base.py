from __future__ import annotations

import importlib
import sys
import types
from pathlib import Path

import pytest


class _DummyAgent:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.calls: list[str] = []

    def run(self, instructions: str) -> str:
        self.calls.append(instructions)
        return instructions


def _install_stub(monkeypatch: pytest.MonkeyPatch, create_callable) -> types.ModuleType:
    module = types.ModuleType("deepagents")
    module.DeepAgent = _DummyAgent  # type: ignore[attr-defined]
    module.create_deep_agent = create_callable  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "deepagents", module)
    return module


def test_process_agent_accepts_injected_deep_agent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def _unexpected_create(**_: object) -> None:  # pragma: no cover - garante que não é chamado
        raise AssertionError("create_deep_agent não deve ser chamado quando já existe instância")

    stub = _install_stub(monkeypatch, _unexpected_create)
    monkeypatch.delitem(sys.modules, "agents.base", raising=False)

    base = importlib.import_module("agents.base")

    injected = stub.DeepAgent(system_prompt="manual", tools=[])  # type: ignore[call-arg]
    process_agent = base.ProcessAgent(
        process_code="00-Test",
        strategy_name="Strategy",
        context_name="Context",
        context_description="Desc",
        base_path=tmp_path,
        prompt="Prompt",
        language_agent=injected,
    )

    assert process_agent.build_agent() is injected

    monkeypatch.delitem(sys.modules, "agents.base", raising=False)


def test_strategy_agent_reuses_injected_deep_agent(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def _unexpected_create(**_: object) -> None:  # pragma: no cover - garante que não é chamado
        raise AssertionError("create_deep_agent não deve ser chamado quando já existe instância")

    stub = _install_stub(monkeypatch, _unexpected_create)
    monkeypatch.delitem(sys.modules, "agents.base", raising=False)

    base = importlib.import_module("agents.base")

    orchestrator = stub.DeepAgent(system_prompt="manual", tools=[])  # type: ignore[call-arg]
    agent = base.StrategyAgent(
        strategy_name="Strategy",
        context_name="Context",
        context_description="Desc",
        orchestrator_prompt="Prompt",
        base_path=tmp_path,
        processes=[],
        orchestrator_agent=orchestrator,
    )

    assert agent.build_orchestrator() is orchestrator

    monkeypatch.delitem(sys.modules, "agents.base", raising=False)


def test_base_import_uses_fallback_when_deepagents_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delitem(sys.modules, "agents.base", raising=False)
    monkeypatch.delitem(sys.modules, "deepagents", raising=False)

    module = importlib.import_module("agents.base")

    assert hasattr(module, "create_deep_agent")
