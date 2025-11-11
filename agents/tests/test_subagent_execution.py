from __future__ import annotations

import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict

import pytest

from agents.ZeroUm.subagents.problem_hypothesis_express import ProblemHypothesisExpressAgent


def _prepare_process(tmp: Path) -> Path:
    process_dir = tmp / "process" / "ZeroUm" / "00-ProblemHypothesisExpress"
    process_dir.mkdir(parents=True, exist_ok=True)
    (process_dir / "process.MD").write_text("Processo", encoding="utf-8")
    (process_dir / "knowledge.MD").write_text("Conhecimento", encoding="utf-8")
    (process_dir / "tasks.MD").write_text("- Passo 1", encoding="utf-8")
    (process_dir / "validator.MD").write_text("Critérios", encoding="utf-8")
    return process_dir


def _prepare_strategy(tmp: Path) -> None:
    strategy_dir = tmp / "strategies" / "ZeroUm"
    strategy_dir.mkdir(parents=True, exist_ok=True)
    (strategy_dir / "process.MD").write_text("prompt", encoding="utf-8")


def _make_agent(tmp: Path, context: str = "Ctx") -> ProblemHypothesisExpressAgent:
    _prepare_process(tmp)
    _prepare_strategy(tmp)
    pipeline_dir = tmp / "drive" / context / "_pipeline"
    return ProblemHypothesisExpressAgent(
        context_name=context,
        context_description="Descricao",
        pipeline_dir=pipeline_dir,
        base_path=tmp,
    )


def test_subagent_generates_manifest_with_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    def _broken_run(*_: Any, **__: Any) -> Dict[str, Any]:
        raise RuntimeError("LLM indisponível")

    monkeypatch.setenv("AGENTS_REASONING_MODE", "simple")
    monkeypatch.setenv("AGENTS_SKIP_SECRET_CHECK", "1")

    with TemporaryDirectory() as tmp_dir:
        base = Path(tmp_dir)
        agent = _make_agent(base)
        monkeypatch.setattr(agent, "_invoke_agent", _broken_run)

        manifest = agent.run()

        assert manifest["status"] == "fallback"
        assert manifest["metrics"]["total_tokens"] >= 0
        manifest_path = base / "drive" / "Ctx" / "_pipeline" / "00-ProblemHypothesisExpress-manifest.json"
        assert manifest_path.exists()

        # Conteúdo do artefato deve existir mesmo em fallback
        artifact_dir = base / "drive" / "Ctx" / "00-ProblemHypothesisExpress"
        assert any(artifact_dir.iterdir())


def test_subagent_runs_with_dummy_agent(monkeypatch: pytest.MonkeyPatch) -> None:
    class _DummyAgent:
        def __init__(self, **_: Any) -> None:
            self.calls: list[str] = []

        def run(self, instructions: str) -> Dict[str, Any]:
            self.calls.append(instructions)
            return {"content": "resultado", "token_usage": 123}

    monkeypatch.setenv("AGENTS_REASONING_MODE", "simple")
    monkeypatch.setenv("AGENTS_SKIP_SECRET_CHECK", "1")
    monkeypatch.setattr(
        "agents.ZeroUm.subagents.problem_hypothesis_express.ProblemHypothesisExpressAgent.build_agent",
        lambda self: _DummyAgent(),
    )

    with TemporaryDirectory() as tmp_dir:
        base = Path(tmp_dir)
        agent = _make_agent(base, context="Ctx2")

        manifest = agent.run()

        assert manifest["status"] == "completed"
        assert manifest["metrics"]["total_tokens"] == 123
        artifact_dir = base / "drive" / "Ctx2" / "00-ProblemHypothesisExpress"
        assert any(artifact_dir.iterdir())
