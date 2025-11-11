"""Orquestrador da estratégia ZeroUm com base no plano de LANGCHAIN.MD."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List

from ..base import StrategyAgent
from ..utils.drive_writer import ensure_strategy_folder
from ..utils.package import package_artifacts
from .subagents.problem_hypothesis_express import ProblemHypothesisExpressAgent

logger = logging.getLogger(__name__)


class ZeroUmOrchestrator(StrategyAgent):
    strategy_name = "ZeroUm"

    def __init__(
        self,
        context_name: str,
        context_description: str = "",
        orchestrator_prompt: str | None = None,
        llm_config: Dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            strategy_name=self.strategy_name,
            context_name=context_name,
            context_description=context_description,
            orchestrator_prompt=orchestrator_prompt,
            llm_config=llm_config,
        )
        self.subagents: Dict[str, type[ProblemHypothesisExpressAgent]] = {
            "00-ProblemHypothesisExpress": ProblemHypothesisExpressAgent,
        }

    def run(self) -> Dict[str, Any]:
        logger.info("Preparando diretórios e carregando processos da estratégia %s", self.strategy_name)
        self.bootstrap()
        ensure_strategy_folder(self.context_name, self.strategy_name)
        manifests: List[Dict[str, Any]] = []
        for process in self.processes:
            code = process["code"]
            cls = self.subagents.get(code)
            if cls is None:
                logger.info("Processo %s ainda não possui subagente. Pulando.", code)
                continue  # Processo ainda não possui subagente dedicado
            logger.info("Disparando subagente %s para o contexto %s", code, self.context_name)
            agent = cls(
                context_name=self.context_name,
                context_description=self.context_description,
                pipeline_dir=self.pipeline_dir,
                llm_config=self.llm_config,
            )
            manifest = agent.run()
            manifests.append(manifest)
            logger.info(
                "Subagente %s concluiu execução com status %s",
                manifest["process"],
                manifest.get("status", "desconhecido"),
            )

        consolidated = self._write_consolidated(manifests)
        archive = package_artifacts(self.context_name, self.strategy_name)
        logger.info("Consolidado salvo em %s", consolidated)
        logger.info("Pacote final gerado em %s", archive)

        return {
            "manifests": manifests,
            "consolidated": str(consolidated),
            "archive": str(archive),
        }

    def _write_consolidated(self, manifests: List[Dict[str, Any]]) -> Path:
        consolidated_path = self.drive_dir / "00-consolidado.MD"
        lines = [
            f"# Execução da estratégia {self.strategy_name}",
            "",
            f"Contexto: {self.context_name}",
            "",
            "## Descrição do contexto",
            self.context_description or "Contexto adicional não informado.",
            "",
            "## Processos orquestrados",
        ]
        for manifest in manifests:
            lines.append(
                f"- {manifest['process']}: status {manifest.get('status', 'pendente')}"
            )
        consolidated_path.write_text("\n".join(lines), encoding="utf-8")
        return consolidated_path
