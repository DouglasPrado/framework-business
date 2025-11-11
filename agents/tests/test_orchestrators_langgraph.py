from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, List

from agents.generic.orchestrator import GenericStrategyOrchestrator
from agents.zero_um.orchestrator import ZeroUmOrchestrator


class _StubProblemHypothesisExpressAgent:
    def __init__(self, context_name: str, context_description: str, pipeline_dir: Path) -> None:
        self.context_name = context_name
        self.context_description = context_description
        self.pipeline_dir = pipeline_dir

    def run(self) -> Dict[str, Any]:
        manifest = {
            "process": "00-ProblemHypothesisExpress",
            "strategy": "ZeroUm",
            "context": self.context_name,
            "status": "completed",
            "notes": "stubbed",
        }
        manifest_path = Path(self.pipeline_dir) / "00-ProblemHypothesisExpress-manifest.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


class OrchestratorGraphFlowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = TemporaryDirectory()
        self.base_path = Path(self.tmp_dir.name)
        self._prepare_strategy("ZeroUm", ["00-ProblemHypothesisExpress"])

    def tearDown(self) -> None:
        self.tmp_dir.cleanup()

    def _prepare_strategy(self, strategy: str, processes: List[str]) -> None:
        strategy_dir = self.base_path / "strategies" / strategy
        strategy_dir.mkdir(parents=True, exist_ok=True)
        (strategy_dir / "process.MD").write_text("prompt", encoding="utf-8")

        for process in processes:
            process_dir = self.base_path / "process" / strategy / process
            process_dir.mkdir(parents=True, exist_ok=True)

    def test_zero_um_orchestrator_runs_complete_graph(self) -> None:
        orchestrator = ZeroUmOrchestrator(
            context_name="Ctx",
            context_description="Descricao",
            base_path=self.base_path,
        )
        orchestrator.subagents["00-ProblemHypothesisExpress"] = _StubProblemHypothesisExpressAgent

        result = orchestrator.run()

        self.assertEqual(len(result["manifests"]), 1)
        self.assertTrue(Path(result["consolidated"]).exists())
        self.assertTrue(Path(result["archive"]).exists())

    def test_generic_orchestrator_runs_complete_graph(self) -> None:
        orchestrator = GenericStrategyOrchestrator(
            strategy_name="ZeroUm",
            context_name="Ctx",
            context_description="Descricao",
            base_path=self.base_path,
        )

        result = orchestrator.run()

        self.assertEqual(len(result["manifests"]), 1)
        self.assertTrue(Path(result["consolidated"]).exists())
        self.assertTrue(Path(result["archive"]).exists())
        manifest_path = (
            self.base_path
            / "drive"
            / "Ctx"
            / "_pipeline"
            / "00-ProblemHypothesisExpress-manifest.json"
        )
        self.assertTrue(manifest_path.exists())


if __name__ == "__main__":
    unittest.main()
