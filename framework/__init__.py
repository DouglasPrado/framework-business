"""
Framework reutilizável para criação de agentes de IA.

Este pacote contém toda a infraestrutura reutilizável para construir
agentes de IA que executam processos de negócio.
"""

from pathlib import Path

# BASE_PATH: raiz do repositório (usado por ferramentas de filesystem)
BASE_PATH = Path(__file__).resolve().parents[1]

from framework import config, core, io, llm, observability, orchestration, tools
from framework.config import Settings, get_settings, reload_settings
from framework.core import (
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
