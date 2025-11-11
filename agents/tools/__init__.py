"""Facade para gerenciamento de ferramentas dos agents."""

from __future__ import annotations

from typing import List

from langchain_core.tools import BaseTool

from .registry import (
    AGENT_TYPES,
    AgentType,
    ToolRegistry,
    get_tools,
    get_tools_for_agent_type,
    validate_tool_name,
    validate_tool_names,
)

__all__ = [
    "AGENT_TYPES",
    "AgentType",
    "ToolRegistry",
    "get_tools_for_agent",
    "get_tool_names_for_agent",
    "validate_tool_name",
    "validate_tool_names",
]


def get_tools_for_agent(agent_type: AgentType | str) -> List[BaseTool]:
    return get_tools(agent_type)


def get_tool_names_for_agent(agent_type: AgentType | str) -> List[str]:
    return get_tools_for_agent_type(agent_type)
