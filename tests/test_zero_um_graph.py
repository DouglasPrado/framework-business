"""Testes end-to-end da estratégia ZeroUm utilizando LangGraph com dados sintéticos."""

from __future__ import annotations

import json
import zipfile

import pytest

from agents.workflows import build_zero_um_graph
from agents.zero_um.orchestrator import ZeroUmOrchestrator
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - apenas para type checkers
    from .conftest import FakeLLM


def _create_synthetic_zero_um(base_path: Path) -> None:
    strategy_dir = base_path / "strategies" / "ZeroUm"
    process_dir = base_path / "process" / "ZeroUm" / "00-ProblemHypothesisExpress"
    strategy_dir.mkdir(parents=True, exist_ok=True)
    process_dir.mkdir(parents=True, exist_ok=True)

    (strategy_dir / "process.MD").write_text(
        "# Estratégia ZeroUm\n\nExecutar ProblemHypothesisExpress com artefatos em drive/.",
        encoding="utf-8",
    )

    contents = {
        "process.MD": "Objetivo sintético do processo.",
        "knowledge.MD": "Conhecimentos necessários documentados.",
        "tasks.MD": "- Passo único para validar a hipótese.",
        "validator.MD": "- Checklist simples para confirmar execução.",
    }
    for filename, text in contents.items():
        (process_dir / filename).write_text(text, encoding="utf-8")


def _read_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.usefixtures("mock_deep_agent")
def test_zero_um_graph_runs_end_to_end(tmp_path: Path, fake_llm: "FakeLLM") -> None:
    base_path = tmp_path / "repo"
    _create_synthetic_zero_um(base_path)

    orchestrator = ZeroUmOrchestrator(
        context_name="CtxSintetico",
        context_description="Contexto fictício para validar o fluxo.",
        base_path=base_path,
    )

    graph = build_zero_um_graph(orchestrator)
    final_state = graph.invoke({})

    result = final_state["result"]
    manifests = result["manifests"]
    assert manifests and manifests[0]["status"] == "completed"

    manifest_path = base_path / "drive" / "CtxSintetico" / "_pipeline" / "00-ProblemHypothesisExpress-manifest.json"
    assert manifest_path.exists()
    manifest_payload = _read_manifest(manifest_path)
    assert manifest_payload["status"] == "completed"

    artifacts_dir = base_path / "drive" / "CtxSintetico" / "00-ProblemHypothesisExpress"
    generated_files = list(artifacts_dir.glob("*.MD"))
    assert generated_files
    artifact_content = generated_files[0].read_text(encoding="utf-8")
    assert "Resultado automatizado" in artifact_content

    consolidated_path = Path(result["consolidated"])
    archive_path = Path(result["archive"])
    assert consolidated_path.exists()
    assert archive_path.exists()

    with zipfile.ZipFile(archive_path) as zf:
        assert any(name.endswith(".MD") for name in zf.namelist())

    summary = final_state["summary"]
    assert summary["completed"] == ["00-ProblemHypothesisExpress"]
    assert summary["pending"] == []

    assert fake_llm.calls, "LLM sintético deveria ter sido acionado pelo subagente."
    assert any("Objetivo sintético" in call["instructions"] for call in fake_llm.calls)
