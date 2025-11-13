"""Orquestrador genérico refatorado usando o framework."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from framework.core.context import AgentContext, RunConfig
from framework.orchestration.graph import OrchestrationGraph
from framework.io.workspace import WorkspaceManager
from framework.io.manifest import ManifestStore
from framework.io.package import PackageService
from framework.observability import MetricsCollector, TracingManager

logger = logging.getLogger(__name__)


class GenericStrategyOrchestrator:
    """
    Orquestrador genérico para estratégias sem subagentes dedicados.

    Utiliza o framework para criar manifestos placeholder e consolidar processos.
    """

    def __init__(
        self,
        strategy_name: str,
        context_name: str,
        context_description: str = "",
        base_path: Optional[Path] = None,
    ) -> None:
        """
        Inicializa o orquestrador genérico.

        Args:
            strategy_name: Nome da estratégia
            context_name: Nome do contexto de execução
            context_description: Descrição do contexto
            base_path: Caminho base (padrão: agents/)
        """
        # Criar contexto imutável
        self.context = AgentContext(
            context_name=context_name,
            context_description=context_description,
            strategy_name=strategy_name,
            base_path=base_path or Path(__file__).parent.parent.parent.parent,
        )

        # Componentes do framework
        self.workspace = WorkspaceManager(self.context)
        self.manifest_store = ManifestStore.from_context(self.context)
        self.package_service = PackageService(self.context)
        self.metrics = MetricsCollector()
        self.tracing = TracingManager()

    def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
        """
        Executa a estratégia genérica.

        Args:
            config: Configuração de execução (opcional)

        Returns:
            Dicionário com manifests, consolidated e archive
        """
        if config is None:
            config = RunConfig()

        # Iniciar tracing
        if self.tracing.is_enabled:
            self.tracing.start_trace(
                f"generic_strategy_{self.context.strategy_name}_{self.context.context_name}"
            )

        self.metrics.start_timer("generic_strategy")

        try:
            # Criar grafo de orquestração
            graph = OrchestrationGraph.from_handlers({
                "collect_context": self._collect_context,
                "generate_hypothesis": self._generate_hypothesis,
                "validate_result": self._validate_result,
            })

            # Executar grafo
            final_state = graph.execute(initial_state={})

            # Registrar métricas
            elapsed = self.metrics.stop_timer("generic_strategy")
            logger.info(
                f"Estratégia {self.context.strategy_name} concluída em {elapsed:.2f}s"
            )

            return {
                "manifests": final_state.get("manifests", []),
                "consolidated": final_state.get("consolidated", ""),
                "archive": final_state.get("archive", ""),
                "metrics": self.metrics.get_summary(),
            }

        finally:
            if self.tracing.is_enabled:
                self.tracing.end_trace()

    def _collect_context(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara workspace e estrutura básica.

        Args:
            state: Estado atual da orquestração

        Returns:
            Estado atualizado com manifests vazios
        """
        logger.info(
            "Preparando workspace para estratégia %s",
            self.context.strategy_name,
        )

        # Garantir que workspace existe
        self.workspace.ensure_workspace()
        pipeline_dir = self.context.workspace_root / "_pipeline"
        pipeline_dir.mkdir(parents=True, exist_ok=True)

        return {"manifests": []}

    def _generate_hypothesis(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera manifestos placeholder para processos sem subagentes.

        Args:
            state: Estado atual

        Returns:
            Estado com manifests placeholder
        """
        logger.info("Gerando manifestos placeholder para processos")

        # Carregar processos da estratégia
        processes = self._load_strategy_processes()

        manifests: List[Dict[str, Any]] = []
        for process in processes:
            manifest = {
                "process": process["code"],
                "strategy": self.context.strategy_name,
                "context": self.context.context_name,
                "status": "awaiting_subagent",
                "notes": "Registre um subagente dedicado antes da execução automática.",
                "artifacts": [],
            }

            # Salvar manifesto usando ManifestStore
            manifest_name = f"{process['code']}-manifest.json"
            self.manifest_store.write(manifest_name, manifest)
            manifests.append(manifest)

            logger.info(
                "Manifesto placeholder criado para %s",
                process["code"],
            )

        return {"manifests": manifests}

    def _validate_result(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Valida resultados, gera consolidado e empacota artefatos.

        Args:
            state: Estado com manifests

        Returns:
            Estado final com consolidated e archive
        """
        manifests: List[Dict[str, Any]] = list(state.get("manifests", []))

        # Escrever relatório consolidado
        consolidated = self._write_consolidated(manifests)

        # Empacotar artefatos
        archive = self._package_artifacts()

        logger.info("Consolidado salvo em %s", consolidated)
        logger.info("Pacote final gerado em %s", archive)

        return {
            "manifests": manifests,
            "consolidated": str(consolidated),
            "archive": str(archive),
        }

    def _write_consolidated(self, manifests: List[Dict[str, Any]]) -> Path:
        """
        Escreve relatório consolidado com nota sobre subagentes.

        Args:
            manifests: Lista de manifestos (placeholders)

        Returns:
            Caminho do arquivo consolidado
        """
        lines = [
            f"# Consolidado: {self.context.strategy_name}",
            f"## Contexto: {self.context.context_name}",
            "",
            self.context.context_description or "Sem descrição adicional.",
            "",
            "## Aviso",
            "",
            "Nenhum subagente dedicado foi configurado ainda para esta estratégia.",
            "Utilize este arquivo como checklist provisório.",
            "",
            "## Processos Registrados",
            "",
        ]

        for manifest in manifests:
            process = manifest.get("process", "desconhecido")
            status = manifest.get("status", "desconhecido")
            lines.append(f"- **{process}**: {status}")

            notes = manifest.get("notes", "")
            if notes:
                lines.append(f"  - {notes}")

            lines.append("")

        lines.extend([
            "",
            "## Próximos Passos",
            "",
            "1. Registre subagentes dedicados para cada processo",
            "2. Configure a estratégia no registry de plugins",
            "3. Execute novamente para gerar artefatos automaticamente",
        ])

        content = "\n".join(lines)

        # Usar workspace manager para escrever
        consolidated_path = self.context.workspace_root / "00-consolidado.MD"
        consolidated_path.write_text(content, encoding="utf-8")

        return consolidated_path

    def _package_artifacts(self) -> Path:
        """
        Empacota todos os artefatos do workspace.

        Returns:
            Caminho do arquivo ZIP
        """
        output_filename = (
            f"{self.context.context_name}_{self.context.strategy_name}_outputs.zip"
        )
        archive_path = self.context.workspace_root / output_filename

        self.package_service.create_archive(
            source_dir=self.context.workspace_root,
            output_path=archive_path,
        )

        return archive_path

    def _load_strategy_processes(self) -> List[Dict[str, Any]]:
        """
        Carrega definições de processos da estratégia.

        Returns:
            Lista de processos (vazia por padrão para estratégias genéricas)
        """
        # TODO: Integrar com ProcessDefinitionLoader do framework
        # Por enquanto, retorna lista vazia (estratégia sem processos pré-definidos)
        logger.warning(
            "Estratégia %s não possui processos pré-definidos",
            self.context.strategy_name,
        )
        return []
