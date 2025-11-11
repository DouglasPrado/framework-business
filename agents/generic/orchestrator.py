"""Orquestrador genérico baseado na arquitetura de LANGCHAIN.MD."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, MutableMapping, Optional

from ..base import StrategyAgent
from ..orchestrators import OrchestrationGraph, OrchestrationState
from ..utils.drive_writer import ensure_strategy_folder
from ..utils.package import package_artifacts


class GenericStrategyOrchestrator(StrategyAgent):
    """Cria manifestos e consolida processos para estratégias sem subagentes próprios."""

    def __init__(
        self,
        strategy_name: str,
        context_name: str,
        context_description: str = "",
        orchestrator_prompt: str | None = None,
        base_path: Optional[Path] = None,
    ) -> None:
        init_kwargs: Dict[str, Any] = {}
        if base_path is not None:
            init_kwargs["base_path"] = base_path
        super().__init__(
            strategy_name=strategy_name,
            context_name=context_name,
            context_description=context_description,
            orchestrator_prompt=orchestrator_prompt,
            **init_kwargs,
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
        consolidated_path = self.drive_dir / "00-consolidado.MD"
        lines = [
            f"# Execução da estratégia {self.strategy_name}",
            "",
            f"Contexto: {self.context_name}",
            "",
            "## Descrição do contexto",
            self.context_description or "Contexto adicional não informado.",
            "",
            "## Processos mapeados",
        ]
        for manifest in manifests:
            lines.append(
                f"- {manifest['process']}: status {manifest['status']}"
            )
        lines.append(
            "\nNenhum subagente dedicado foi configurado ainda. Utilize este arquivo como checklist provisório."
        )
        consolidated_path.write_text("\n".join(lines), encoding="utf-8")
        return consolidated_path
