"""
Protocolos e interfaces abstratas do framework.

Este módulo define os contratos que componentes customizados devem seguir
para se integrar ao framework de agentes.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Protocol, runtime_checkable


# =============================================================================
# Process Definition Loading
# =============================================================================


@runtime_checkable
class ProcessDefinitionLoader(Protocol):
    """
    Protocolo para carregadores de definições de processo.

    Implementações customizadas podem carregar definições de diferentes
    formatos (Markdown, YAML, JSON, banco de dados, etc.).
    """

    def load(self, path: Path) -> Dict[str, Any]:
        """
        Carrega definição de processo de um caminho.

        Args:
            path: Caminho para a definição do processo

        Returns:
            Dicionário com os metadados e conteúdo do processo

        Raises:
            FileNotFoundError: Se o caminho não existir
            ValueError: Se o formato for inválido
        """
        ...

    def validate(self, definition: Dict[str, Any]) -> bool:
        """
        Valida se uma definição de processo está completa e correta.

        Args:
            definition: Definição a ser validada

        Returns:
            True se válida, False caso contrário
        """
        ...


# =============================================================================
# Artifact Writing
# =============================================================================


@runtime_checkable
class ArtifactWriter(Protocol):
    """
    Protocolo para escritores de artefatos.

    Abstrai a forma como artefatos são persistidos (filesystem, S3, etc.).
    """

    def write(self, content: str, metadata: Dict[str, Any]) -> Path:
        """
        Escreve um artefato com seus metadados.

        Args:
            content: Conteúdo do artefato
            metadata: Metadados (nome, número, tipo, etc.)

        Returns:
            Caminho onde o artefato foi escrito

        Raises:
            IOError: Se houver erro ao escrever
        """
        ...

    def read(self, path: Path) -> str:
        """
        Lê um artefato de um caminho.

        Args:
            path: Caminho do artefato

        Returns:
            Conteúdo do artefato

        Raises:
            FileNotFoundError: Se o artefato não existir
        """
        ...


# =============================================================================
# Manifest Formatting
# =============================================================================


@runtime_checkable
class ManifestFormatter(Protocol):
    """
    Protocolo para formatadores de manifesto.

    Permite diferentes formatos de manifesto (JSON, YAML, TOML, etc.).
    """

    def format(self, data: Dict[str, Any]) -> str:
        """
        Formata dados de manifesto para string.

        Args:
            data: Dados do manifesto

        Returns:
            String formatada
        """
        ...

    def parse(self, content: str) -> Dict[str, Any]:
        """
        Faz parse de manifesto de string para dicionário.

        Args:
            content: Conteúdo do manifesto

        Returns:
            Dicionário com dados parseados

        Raises:
            ValueError: Se o formato for inválido
        """
        ...


# =============================================================================
# Pipeline Stages
# =============================================================================


@runtime_checkable
class PipelineStage(Protocol):
    """
    Protocolo para stages de um pipeline de execução.

    Cada stage recebe contexto, configuração e estado, e retorna
    estado atualizado.
    """

    def execute(
        self,
        context: "AgentContext",  # Forward reference
        config: "RunConfig",  # Forward reference
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
        ...

    @property
    def name(self) -> str:
        """Nome do stage para logging e debugging."""
        ...


# =============================================================================
# Orchestrator Plugin
# =============================================================================


class OrchestratorPlugin(ABC):
    """
    Classe base abstrata para plugins de orquestrador.

    Orquestradores customizados devem herdar desta classe e implementar
    os métodos abstratos.
    """

    @abstractmethod
    def bootstrap(self, context: "AgentContext") -> None:
        """
        Inicializa o orquestrador (cria diretórios, valida config, etc.).

        Args:
            context: Contexto do agente
        """
        pass

    @abstractmethod
    def execute(self, config: "RunConfig") -> Dict[str, Any]:
        """
        Executa a estratégia completa.

        Args:
            config: Configuração de execução

        Returns:
            Resultado da execução com métricas e artefatos
        """
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Limpa recursos após execução."""
        pass


# =============================================================================
# Tool Provider
# =============================================================================


@runtime_checkable
class ToolProvider(Protocol):
    """
    Protocolo para provedores de ferramentas.

    Permite registrar e fornecer ferramentas customizadas para agentes.
    """

    def get_tools(self, agent_type: str) -> List[Callable]:
        """
        Retorna ferramentas disponíveis para um tipo de agente.

        Args:
            agent_type: Tipo do agente (ex: "strategy", "process")

        Returns:
            Lista de funções de ferramentas
        """
        ...

    def register_tool(self, name: str, func: Callable, agent_types: List[str]) -> None:
        """
        Registra uma nova ferramenta.

        Args:
            name: Nome da ferramenta
            func: Função implementando a ferramenta
            agent_types: Tipos de agente que podem usar a ferramenta
        """
        ...


# =============================================================================
# Observability
# =============================================================================


@runtime_checkable
class TodoProvider(Protocol):
    """
    Protocolo para provedores de TODO tracking.

    Permite diferentes implementações de tracking (JSON, DB, API, etc.).
    """

    def create_task(self, description: str, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Cria uma nova task.

        Args:
            description: Descrição da task
            metadata: Metadados adicionais

        Returns:
            ID da task criada
        """
        ...

    def update_status(self, task_id: str, status: str) -> None:
        """
        Atualiza status de uma task.

        Args:
            task_id: ID da task
            status: Novo status (pending, in_progress, completed, failed)
        """
        ...

    def get_tasks(self) -> List[Dict[str, Any]]:
        """
        Retorna todas as tasks.

        Returns:
            Lista de tasks com seus metadados
        """
        ...


@runtime_checkable
class MetricsProvider(Protocol):
    """
    Protocolo para provedores de métricas.

    Permite coletar e reportar métricas de execução.
    """

    def record_metric(self, name: str, value: float, tags: Optional[Dict[str, str]] = None) -> None:
        """
        Registra uma métrica.

        Args:
            name: Nome da métrica
            value: Valor da métrica
            tags: Tags para categorização
        """
        ...

    def get_metrics(self, name: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retorna métricas registradas.

        Args:
            name: Filtrar por nome (opcional)

        Returns:
            Lista de métricas
        """
        ...


# =============================================================================
# Forward references for type hints
# =============================================================================

# Estas classes serão definidas em context.py
# Importações circulares são evitadas usando forward references
if False:  # TYPE_CHECKING equivalente
    from framework.core.context import AgentContext, RunConfig
