"""
Registry centralizado de ferramentas (tools) disponíveis para agents.

Este módulo define todas as ferramentas disponíveis e quais agents podem usá-las,
fornecendo validação e configuração centralizada.
"""

from __future__ import annotations

from enum import Enum
from typing import List, Set

from ..exceptions import InvalidConfigError, ToolNotFoundError


class AgentType(str, Enum):
    """Tipos de agents disponíveis no sistema."""

    STRATEGY = "strategy"
    PROCESS = "process"
    ORCHESTRATOR = "orchestrator"


class ToolRegistry:
    """
    Registry centralizado de ferramentas disponíveis para agents.

    Define quais tools estão disponíveis para cada tipo de agent,
    fornecendo validação e configuração.
    """

    # ========================================================================
    # File System Tools
    # ========================================================================

    FILE_SYSTEM_TOOLS: Set[str] = {
        "ls",  # Listar diretórios
        "read_file",  # Ler arquivos
        "write_file",  # Escrever arquivos
        "edit_file",  # Editar arquivos
        "glob",  # Buscar arquivos por padrão
    }

    # ========================================================================
    # Search Tools
    # ========================================================================

    SEARCH_TOOLS: Set[str] = {
        "grep",  # Buscar texto em arquivos
        "internal_base_search",  # Busca interna na base de conhecimento
    }

    # ========================================================================
    # Content Tools
    # ========================================================================

    CONTENT_TOOLS: Set[str] = {
        "markdown_summarizer",  # Sumarizar conteúdo markdown
    }

    # ========================================================================
    # Todas as Tools
    # ========================================================================

    ALL_TOOLS: Set[str] = FILE_SYSTEM_TOOLS | SEARCH_TOOLS | CONTENT_TOOLS

    # ========================================================================
    # Tools por Tipo de Agent
    # ========================================================================

    # Process agents: operações básicas de leitura/escrita
    PROCESS_TOOLS: Set[str] = FILE_SYSTEM_TOOLS

    # Strategy agents: inclui ferramentas de busca avançada
    STRATEGY_TOOLS: Set[str] = FILE_SYSTEM_TOOLS | SEARCH_TOOLS

    # Orchestrator agents: acesso completo a todas as ferramentas
    ORCHESTRATOR_TOOLS: Set[str] = ALL_TOOLS

    @classmethod
    def get_tools_for_agent_type(cls, agent_type: AgentType | str) -> List[str]:
        """
        Retorna lista de tools disponíveis para o tipo de agent.

        Args:
            agent_type: Tipo do agent (strategy, process, orchestrator)

        Returns:
            Lista de nomes de tools disponíveis

        Raises:
            ValueError: Se o tipo de agent for inválido
        """
        if isinstance(agent_type, str):
            try:
                agent_type = AgentType(agent_type.lower())
            except ValueError as exc:
                valid_types = ", ".join(t.value for t in AgentType)
                raise InvalidConfigError(
                    "agent_type",
                    agent_type,
                    reason=f"Tipos válidos: {valid_types}",
                ) from exc

        tool_map = {
            AgentType.PROCESS: cls.PROCESS_TOOLS,
            AgentType.STRATEGY: cls.STRATEGY_TOOLS,
            AgentType.ORCHESTRATOR: cls.ORCHESTRATOR_TOOLS,
        }

        return sorted(tool_map[agent_type])

    @classmethod
    def validate_tool_name(cls, tool_name: str) -> bool:
        """
        Valida se o nome da tool é reconhecido.

        Args:
            tool_name: Nome da tool para validar

        Returns:
            True se a tool é válida, False caso contrário
        """
        return tool_name in cls.ALL_TOOLS

    @classmethod
    def validate_tool_names(cls, tool_names: List[str]) -> List[str]:
        """
        Valida uma lista de nomes de tools e retorna os inválidos.

        Args:
            tool_names: Lista de nomes de tools para validar

        Returns:
            Lista de nomes de tools inválidos (vazia se todas forem válidas)
        """
        invalid = []
        for tool_name in tool_names:
            if not cls.validate_tool_name(tool_name):
                invalid.append(tool_name)
        return invalid

    @classmethod
    def get_tool_description(cls, tool_name: str) -> str:
        """
        Retorna descrição da ferramenta.

        Args:
            tool_name: Nome da tool

        Returns:
            Descrição da ferramenta ou mensagem de erro se não encontrada
        """
        descriptions = {
            # File System Tools
            "ls": "Lista arquivos e diretórios",
            "read_file": "Lê conteúdo de arquivos",
            "write_file": "Escreve conteúdo em arquivos",
            "edit_file": "Edita arquivos existentes",
            "glob": "Busca arquivos por padrão glob",
            # Search Tools
            "grep": "Busca texto em arquivos (regex support)",
            "internal_base_search": "Busca na base de conhecimento interna (process/, strategies/, drive/)",
            # Content Tools
            "markdown_summarizer": "Sumariza conteúdo markdown",
        }

        return descriptions.get(tool_name, f"Tool desconhecida: {tool_name}")

    @classmethod
    def get_all_tool_names(cls) -> List[str]:
        """
        Retorna lista com todos os nomes de tools disponíveis.

        Returns:
            Lista ordenada de nomes de tools
        """
        return sorted(cls.ALL_TOOLS)

    @classmethod
    def get_tools_by_category(cls) -> dict[str, List[str]]:
        """
        Retorna tools agrupadas por categoria.

        Returns:
            Dicionário com categorias como chaves e listas de tools como valores
        """
        return {
            "file_system": sorted(cls.FILE_SYSTEM_TOOLS),
            "search": sorted(cls.SEARCH_TOOLS),
            "content": sorted(cls.CONTENT_TOOLS),
        }


# ========================================================================
# Convenience Constants
# ========================================================================

AGENT_TYPES = AgentType


# ========================================================================
# Convenience Functions
# ========================================================================


def get_tools_for_agent(agent_type: AgentType | str) -> List[str]:
    """
    Função de conveniência para obter tools para um agent.

    Args:
        agent_type: Tipo do agent (strategy, process, orchestrator)

    Returns:
        Lista de nomes de tools disponíveis

    Raises:
        ValueError: Se o tipo de agent for inválido

    Examples:
        >>> get_tools_for_agent("process")
        ['edit_file', 'glob', 'ls', 'read_file', 'write_file']

        >>> get_tools_for_agent(AgentType.STRATEGY)
        ['edit_file', 'glob', 'grep', 'internal_base_search', 'ls', 'read_file', 'write_file']
    """
    return ToolRegistry.get_tools_for_agent_type(agent_type)


def validate_tool_name(tool_name: str) -> bool:
    """
    Função de conveniência para validar nome de tool.

    Args:
        tool_name: Nome da tool para validar

    Returns:
        True se a tool é válida, False caso contrário

    Examples:
        >>> validate_tool_name("read_file")
        True

        >>> validate_tool_name("invalid_tool")
        False
    """
    return ToolRegistry.validate_tool_name(tool_name)


def validate_tool_names(tool_names: List[str]) -> List[str]:
    """
    Função de conveniência para validar lista de tools.

    Args:
        tool_names: Lista de nomes de tools para validar

    Returns:
        Lista de nomes de tools inválidos (vazia se todas forem válidas)

    Examples:
        >>> validate_tool_names(["read_file", "write_file"])
        []

        >>> validate_tool_names(["read_file", "invalid_tool"])
        ['invalid_tool']
    """
    return ToolRegistry.validate_tool_names(tool_names)


__all__ = [
    "AGENT_TYPES",
    "AgentType",
    "ToolRegistry",
    "get_tools_for_agent",
    "validate_tool_name",
    "validate_tool_names",
]
