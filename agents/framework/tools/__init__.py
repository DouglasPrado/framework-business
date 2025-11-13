"""
Módulo de ferramentas (tools) do framework.

Gerencia o registro e disponibilização de ferramentas para agentes.
"""

from agents.framework.tools.registry import (
    AgentType,
    ToolRegistry,
    get_tools,
    get_tools_for_agent,
    get_tools_for_agent_type,
    validate_tool_name,
    validate_tool_names,
)

__all__ = [
    "AgentType",
    "ToolRegistry",
    "get_tools",
    "get_tools_for_agent",
    "get_tools_for_agent_type",
    "validate_tool_name",
    "validate_tool_names",
]
