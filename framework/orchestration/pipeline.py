"""
Pipeline de execução para processos de agentes.

Este módulo implementa um pipeline flexível com stages configuráveis,
permitindo que processos customizem o ciclo de vida de execução.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from framework.core.context import AgentContext, RunConfig
from framework.core.exceptions import ProcessExecutionError

logger = logging.getLogger(__name__)


# =============================================================================
# Result Classes
# =============================================================================


@dataclass
class StageResult:
    """
    Resultado da execução de um stage.

    Attributes:
        stage_name: Nome do stage executado
        success: Se o stage foi bem-sucedido
        data: Dados retornados pelo stage
        error: Erro ocorrido (se houver)
        metadata: Metadados adicionais
    """

    stage_name: str
    success: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[Exception] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PipelineResult:
    """
    Resultado da execução do pipeline completo.

    Attributes:
        success: Se o pipeline foi bem-sucedido
        stages: Lista de resultados de cada stage
        final_state: Estado final do pipeline
        error: Erro que interrompeu o pipeline (se houver)
    """

    success: bool
    stages: List[StageResult]
    final_state: Dict[str, Any]
    error: Optional[Exception] = None

    @classmethod
    def from_state(cls, state: Dict[str, Any]) -> PipelineResult:
        """Cria PipelineResult a partir do estado final."""
        stages = state.get("_stages", [])
        error = state.get("_error")
        success = error is None

        return cls(
            success=success,
            stages=stages,
            final_state=state,
            error=error,
        )


# =============================================================================
# Pipeline Stage (Base Class)
# =============================================================================


class PipelineStage(ABC):
    """
    Classe base para stages do pipeline.

    Cada stage recebe contexto, configuração e estado, executa sua lógica,
    e retorna o estado atualizado.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Nome do stage para logging e debugging."""
        pass

    @abstractmethod
    def execute(
        self,
        context: AgentContext,
        config: RunConfig,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Executa o stage do pipeline.

        Args:
            context: Contexto do agente (imutável)
            config: Configuração de execução (imutável)
            state: Estado atual do pipeline (mutável)

        Returns:
            Estado atualizado após execução do stage

        Raises:
            Exception: Qualquer erro durante a execução
        """
        pass

    def on_success(self, state: Dict[str, Any]) -> None:
        """Hook chamado quando o stage é bem-sucedido."""
        pass

    def on_error(self, error: Exception, state: Dict[str, Any]) -> None:
        """Hook chamado quando o stage falha."""
        pass


# =============================================================================
# Standard Pipeline Stages
# =============================================================================


class PrepareStage(PipelineStage):
    """
    Stage de preparação.

    Responsável por preparar inputs, validar pré-condições e
    inicializar recursos necessários.
    """

    @property
    def name(self) -> str:
        return "prepare"

    def execute(
        self,
        context: AgentContext,
        config: RunConfig,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Prepara o ambiente para execução."""
        logger.info(f"[{self.name}] Preparando execução para {context.context_name}")

        # Implementação padrão: apenas marca como preparado
        state["prepared"] = True
        state["context_name"] = context.context_name
        state["strategy_name"] = context.strategy_name

        return state


class PlanStage(PipelineStage):
    """
    Stage de planejamento.

    Responsável por analisar requisitos, criar plano de execução
    e preparar prompts para LLM.
    """

    @property
    def name(self) -> str:
        return "plan"

    def execute(
        self,
        context: AgentContext,
        config: RunConfig,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Cria plano de execução."""
        logger.info(f"[{self.name}] Planejando execução")

        # Implementação padrão: marca como planejado
        state["planned"] = True
        state["plan"] = {"steps": [], "estimated_time": 0}

        return state


class ExecuteStage(PipelineStage):
    """
    Stage de execução.

    Responsável por executar o agente, invocar LLM,
    e processar resultados.
    """

    @property
    def name(self) -> str:
        return "execute"

    def execute(
        self,
        context: AgentContext,
        config: RunConfig,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Executa o agente."""
        logger.info(f"[{self.name}] Executando agente")

        # Implementação padrão: marca como executado
        state["executed"] = True
        state["results"] = {}

        return state


class ValidateStage(PipelineStage):
    """
    Stage de validação.

    Responsável por validar resultados, verificar qualidade
    e aplicar regras de validação.
    """

    @property
    def name(self) -> str:
        return "validate"

    def execute(
        self,
        context: AgentContext,
        config: RunConfig,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Valida resultados."""
        logger.info(f"[{self.name}] Validando resultados")

        # Implementação padrão: sempre válido
        state["validated"] = True
        state["validation_errors"] = []

        return state


class PersistStage(PipelineStage):
    """
    Stage de persistência.

    Responsável por salvar artefatos, gerar manifestos
    e persistir resultados.
    """

    @property
    def name(self) -> str:
        return "persist"

    def execute(
        self,
        context: AgentContext,
        config: RunConfig,
        state: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Persiste resultados."""
        logger.info(f"[{self.name}] Persistindo resultados")

        # Implementação padrão: marca como persistido
        state["persisted"] = True
        state["artifacts"] = []

        return state


# =============================================================================
# Process Pipeline
# =============================================================================


class ProcessPipeline:
    """
    Pipeline configurável para execução de processos.

    Permite customização de stages e fluxo de execução,
    mantendo flexibilidade para diferentes tipos de processos.
    """

    def __init__(
        self,
        stages: Optional[List[PipelineStage]] = None,
        stop_on_error: bool = True,
    ):
        """
        Inicializa o pipeline.

        Args:
            stages: Lista de stages a executar. Se None, usa stages padrão.
            stop_on_error: Se True, para execução ao primeiro erro
        """
        self.stages = stages or self._default_stages()
        self.stop_on_error = stop_on_error

    @staticmethod
    def _default_stages() -> List[PipelineStage]:
        """Retorna stages padrão do pipeline."""
        return [
            PrepareStage(),
            PlanStage(),
            ExecuteStage(),
            ValidateStage(),
            PersistStage(),
        ]

    def run(
        self,
        context: AgentContext,
        config: RunConfig,
        initial_state: Optional[Dict[str, Any]] = None,
    ) -> PipelineResult:
        """
        Executa o pipeline completo.

        Args:
            context: Contexto do agente
            config: Configuração de execução
            initial_state: Estado inicial (opcional)

        Returns:
            PipelineResult com resultados de todos os stages

        Examples:
            >>> pipeline = ProcessPipeline()
            >>> result = pipeline.run(context, config)
            >>> if result.success:
            ...     print("Pipeline executado com sucesso!")
        """
        state = initial_state or {}
        state["_stages"] = []
        state["_error"] = None

        logger.info(
            f"Iniciando pipeline com {len(self.stages)} stages "
            f"para {context.context_name}"
        )

        for stage in self.stages:
            try:
                logger.debug(f"Executando stage: {stage.name}")
                state = stage.execute(context, config, state)

                # Registra sucesso do stage
                stage_result = StageResult(
                    stage_name=stage.name,
                    success=True,
                    data={"stage_output": state.get(f"{stage.name}_output")},
                )
                state["_stages"].append(stage_result)

                stage.on_success(state)

            except Exception as exc:
                logger.error(f"Erro no stage {stage.name}: {exc}", exc_info=True)

                # Registra falha do stage
                stage_result = StageResult(
                    stage_name=stage.name,
                    success=False,
                    error=exc,
                )
                state["_stages"].append(stage_result)

                stage.on_error(exc, state)

                if self.stop_on_error:
                    state["_error"] = exc
                    logger.error("Pipeline interrompido devido a erro")
                    break

        # Cria resultado final
        result = PipelineResult.from_state(state)

        if result.success:
            logger.info(
                f"Pipeline concluído com sucesso. "
                f"{len(result.stages)} stages executados."
            )
        else:
            logger.error(
                f"Pipeline falhou no stage {result.stages[-1].stage_name}. "
                f"Erro: {result.error}"
            )

        return result

    def add_stage(self, stage: PipelineStage, position: Optional[int] = None) -> None:
        """
        Adiciona um stage ao pipeline.

        Args:
            stage: Stage a ser adicionado
            position: Posição onde inserir (None = no final)
        """
        if position is None:
            self.stages.append(stage)
        else:
            self.stages.insert(position, stage)

    def remove_stage(self, stage_name: str) -> None:
        """
        Remove um stage do pipeline pelo nome.

        Args:
            stage_name: Nome do stage a ser removido
        """
        self.stages = [s for s in self.stages if s.name != stage_name]

    def get_stage(self, stage_name: str) -> Optional[PipelineStage]:
        """
        Retorna um stage pelo nome.

        Args:
            stage_name: Nome do stage

        Returns:
            Stage encontrado ou None
        """
        for stage in self.stages:
            if stage.name == stage_name:
                return stage
        return None


__all__ = [
    "PipelineStage",
    "PrepareStage",
    "PlanStage",
    "ExecuteStage",
    "ValidateStage",
    "PersistStage",
    "ProcessPipeline",
    "StageResult",
    "PipelineResult",
]
