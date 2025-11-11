"""Fixtures compartilhadas para os testes do framework de agentes."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@dataclass
class FakeLLM:
    """Simula um LLM registrando chamadas e retornando respostas pré-programadas."""

    queue: List[Any] = field(default_factory=list)
    calls: List[Dict[str, Any]] = field(default_factory=list)

    def queue_response(self, payload: Any) -> None:
        self.queue.append(payload)

    def generate(self, *, system_prompt: str, instructions: str, tools: List[str]) -> Any:
        self.calls.append(
            {
                "system_prompt": system_prompt,
                "instructions": instructions,
                "tools": list(tools),
            }
        )
        if self.queue:
            return self.queue.pop(0)
        intro = "# Resultado automatizado\n\n"
        resumo = instructions.strip().splitlines()[:4]
        corpo = "\n".join(resumo)
        return f"{intro}{corpo}\n\nFerramentas: {', '.join(tools) if tools else 'nenhuma'}"


@dataclass
class MockDeepAgent:
    """Replica a interface esperada por `create_deep_agent` usando o `FakeLLM`."""

    llm: FakeLLM
    system_prompt: str
    tools: List[str]

    def run(self, instructions: str) -> Any:
        return self.llm.generate(
            system_prompt=self.system_prompt,
            instructions=instructions,
            tools=self.tools,
        )


@pytest.fixture
def fake_llm() -> FakeLLM:
    return FakeLLM()


@pytest.fixture
def mock_deep_agent(fake_llm: FakeLLM, monkeypatch: pytest.MonkeyPatch) -> FakeLLM:
    def _builder(system_prompt: str, tools: List[str] | None = None, **_: Any) -> MockDeepAgent:
        return MockDeepAgent(llm=fake_llm, system_prompt=system_prompt, tools=tools or [])

    monkeypatch.setattr("agents.base.create_deep_agent", _builder)
    monkeypatch.setattr("agents.utils.context.create_deep_agent", _builder, raising=False)
    monkeypatch.setattr("agents.deepagents.create_deep_agent", _builder, raising=False)

    try:
        import deepagents  # type: ignore
    except ImportError:
        deepagents = None
    if deepagents is not None:
        monkeypatch.setattr(deepagents, "create_deep_agent", _builder, raising=False)

    return fake_llm


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "llm: testes que exigem chaves reais de modelo")


def pytest_runtest_setup(item: pytest.Item) -> None:
    if "llm" in item.keywords and not os.getenv("OPENAI_API_KEY"):
        pytest.skip("Teste de LLM real desabilitado sem OPENAI_API_KEY definido.")
