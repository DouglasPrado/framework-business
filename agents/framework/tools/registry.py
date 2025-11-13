"""Registry de ferramentas disponíveis para os agents."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Iterable, List, Sequence, Set, Union

from agents.framework.core.exceptions import InvalidConfigError

if TYPE_CHECKING:  # pragma: no cover
    from langchain_core.tools import BaseTool
else:
    try:
        from langchain_core.tools import BaseTool
    except ImportError:
        BaseTool = None  # type: ignore

# Import condicional das ferramentas builtin
try:
    from agents.framework.tools.builtin.content import CONTENT_TOOLS
    from agents.framework.tools.builtin.filesystem import FILE_SYSTEM_TOOLS, SEARCH_TOOLS
    from agents.framework.tools.builtin.execution import EXECUTION_TOOLS
except ImportError:  # pragma: no cover - caso langchain não esteja instalado
    CONTENT_TOOLS = []  # type: ignore
    FILE_SYSTEM_TOOLS = []  # type: ignore
    SEARCH_TOOLS = []  # type: ignore
    EXECUTION_TOOLS = []  # type: ignore


class AgentType(str, Enum):
    STRATEGY = "strategy"
    PROCESS = "process"
    ORCHESTRATOR = "orchestrator"
    AUTONOMOUS = "autonomous"  # Full access to all tools including execution


class ToolRegistry:
    FILE_SYSTEM: Sequence[BaseTool] = tuple(FILE_SYSTEM_TOOLS)
    SEARCH: Sequence[BaseTool] = tuple(SEARCH_TOOLS)
    CONTENT: Sequence[BaseTool] = tuple(CONTENT_TOOLS)
    EXECUTION: Sequence[BaseTool] = tuple(EXECUTION_TOOLS)

    @classmethod
    def _resolve_agent_type(cls, agent_type: Union[AgentType, str]) -> AgentType:
        if isinstance(agent_type, AgentType):
            return agent_type
        try:
            return AgentType(agent_type.lower())
        except ValueError as exc:
            valid = ", ".join(t.value for t in AgentType)
            raise InvalidConfigError("agent_type", agent_type, reason=f"Tipos válidos: {valid}") from exc

    @classmethod
    def _tools_for(cls, agent_type: Union[AgentType, str]) -> Sequence[BaseTool]:
        resolved = cls._resolve_agent_type(agent_type)
        mapping = {
            AgentType.PROCESS: cls.FILE_SYSTEM,
            AgentType.STRATEGY: tuple(list(cls.FILE_SYSTEM) + list(cls.SEARCH)),
            AgentType.ORCHESTRATOR: tuple(list(cls.FILE_SYSTEM) + list(cls.SEARCH) + list(cls.CONTENT)),
            AgentType.AUTONOMOUS: tuple(
                list(cls.FILE_SYSTEM) + list(cls.SEARCH) + list(cls.CONTENT) + list(cls.EXECUTION)
            ),
        }
        return mapping[resolved]

    @classmethod
    def get_tools(cls, agent_type: Union[AgentType, str]) -> List[BaseTool]:
        return list(cls._tools_for(agent_type))

    @classmethod
    def get_tool_names(cls, agent_type: Union[AgentType, str]) -> List[str]:
        return [tool.name for tool in cls._tools_for(agent_type)]

    @classmethod
    def validate_tool_name(cls, tool_name: str) -> bool:
        return tool_name in cls.get_all_tool_names()

    @classmethod
    def validate_tool_names(cls, tool_names: Iterable[str]) -> List[str]:
        known = set(cls.get_all_tool_names())
        return [name for name in tool_names if name not in known]

    @classmethod
    def get_all_tool_names(cls) -> List[str]:
        names: Set[str] = set()
        for tool in (*cls.FILE_SYSTEM, *cls.SEARCH, *cls.CONTENT, *cls.EXECUTION):
            names.add(tool.name)
        return sorted(names)

    @classmethod
    def get_tools_by_category(cls) -> dict[str, List[str]]:
        return {
            "file_system": [tool.name for tool in cls.FILE_SYSTEM],
            "search": [tool.name for tool in cls.SEARCH],
            "content": [tool.name for tool in cls.CONTENT],
            "execution": [tool.name for tool in cls.EXECUTION],
        }


def get_tools(agent_type: Union[AgentType, str]) -> List[BaseTool]:
    return ToolRegistry.get_tools(agent_type)


def get_tools_for_agent_type(agent_type: Union[AgentType, str]) -> List[str]:
    return ToolRegistry.get_tool_names(agent_type)


def get_tools_for_agent(agent_type: Union[AgentType, str]) -> List[BaseTool]:
    """
    Alias para get_tools() - função de conveniência.

    Args:
        agent_type: Tipo do agente (strategy, process, orchestrator)

    Returns:
        Lista de ferramentas disponíveis para o tipo de agente
    """
    return get_tools(agent_type)


def validate_tool_name(tool_name: str) -> bool:
    return ToolRegistry.validate_tool_name(tool_name)


def validate_tool_names(tool_names: Iterable[str]) -> List[str]:
    return ToolRegistry.validate_tool_names(tool_names)


AGENT_TYPES = AgentType

__all__ = [
    "AGENT_TYPES",
    "AgentType",
    "ToolRegistry",
    "get_tools",
    "get_tools_for_agent",
    "get_tools_for_agent_type",
    "validate_tool_name",
    "validate_tool_names",
]
