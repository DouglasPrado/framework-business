"""
Framework reutilizável para criação de agentes de IA.

Este pacote contém toda a infraestrutura reutilizável para construir
agentes de IA que executam processos de negócio.
"""

from agents.framework import config, core, io, llm, observability, orchestration, tools
from agents.framework.config import Settings, get_settings, reload_settings
from agents.framework.core import (
    AgentContext,
    AgentError,
    ConfigurationError,
    RunConfig,
    handle_agent_errors,
    log_execution,
    retry_on_failure,
)

__version__ = "0.1.0"

__all__ = [
    # Submodules
    "core",
    "config",
    "io",
    "llm",
    "orchestration",
    "observability",
    "tools",
    # Core exports
    "AgentContext",
    "RunConfig",
    "AgentError",
    "ConfigurationError",
    "handle_agent_errors",
    "log_execution",
    "retry_on_failure",
    # Config exports
    "Settings",
    "get_settings",
    "reload_settings",
]
