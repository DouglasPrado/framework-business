"""Orquestrador genérico baseado na arquitetura de LANGCHAIN.MD."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, MutableMapping, Optional

from ..base import StrategyAgent
from ..orchestrators import OrchestrationGraph, OrchestrationState
from ..utils.io import (
    ensure_strategy_folder,
    package_artifacts,
    write_consolidated_report,
)


class GenericStrategyOrchestrator(StrategyAgent):
    """Cria manifestos e consolida processos para estratégias sem subagentes próprios."""

    def __init__(
        self,
        strategy_name: str,
        context_name: str,
        context_description: str = "",
        orchestrator_prompt: str | None = None,
        llm_config: Dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            strategy_name=strategy_name,
            context_name=context_name,
            context_description=context_description,
            orchestrator_prompt=orchestrator_prompt,
            llm_config=llm_config,
        )

    def run(self) -> Dict[str, Any]:
        graph = OrchestrationGraph(
            {
                "coletar_contexto": self.coletar_contexto,
                "gerar_hipotese": self.gerar_hipotese,
                "validar_resultado": self.validar_resultado,
            }
        )
        final_state = graph.run()
        return {
            "manifests": final_state.get("manifests", []),
            "consolidated": final_state.get("consolidated", ""),
            "archive": final_state.get("archive", ""),
        }

    def coletar_contexto(self, state: MutableMapping[str, Any]) -> OrchestrationState:
        self.bootstrap()
        ensure_strategy_folder(
            self.context_name, self.strategy_name, base_path=self.base_path
        )
        return {"manifests": []}

    def gerar_hipotese(self, state: MutableMapping[str, Any]) -> OrchestrationState:
        manifests: List[Dict[str, Any]] = []
        for process in self.processes:
            manifest = {
                "process": process["code"],
                "strategy": self.strategy_name,
                "context": self.context_name,
                "status": "awaiting_subagent",
                "notes": "Registre um subagente dedicado antes da execução automática.",
            }
            self.manifest_handler.write(process["manifest"], manifest)
            manifests.append(manifest)
        return {"manifests": manifests}

    def validar_resultado(self, state: MutableMapping[str, Any]) -> OrchestrationState:
        manifests: List[Dict[str, Any]] = list(state.get("manifests", []))
        consolidated = self._write_consolidated(manifests)
        archive = package_artifacts(
            self.context_name,
            self.strategy_name,
            base_path=self.base_path,
        )
        return {
            "manifests": manifests,
            "consolidated": str(consolidated),
            "archive": str(archive),
        }

    def _write_consolidated(self, manifests: List[Dict[str, Any]]) -> Path:
        """Escreve relatório consolidado usando função compartilhada."""
        consolidated_path = self.drive_dir / "00-consolidado.MD"
        additional_notes = (
            "Nenhum subagente dedicado foi configurado ainda. "
            "Utilize este arquivo como checklist provisório."
        )
        return write_consolidated_report(
            strategy_name=self.strategy_name,
            context_name=self.context_name,
            context_description=self.context_description,
            manifests=manifests,
            output_path=consolidated_path,
            additional_notes=additional_notes,
        )
