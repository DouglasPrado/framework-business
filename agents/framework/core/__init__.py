"""
Core components do framework de agentes.

Este módulo contém as abstrações fundamentais, protocolos e classes base
que definem a arquitetura do framework.
"""

from agents.framework.core.context import AgentContext, RunConfig
from agents.framework.core.decorators import (
    handle_agent_errors,
    log_execution,
    retry_on_failure,
)
from agents.framework.core.exceptions import (
    AgentError,
    ConfigurationError,
    InvalidConfigError,
    LLMError,
    LLMInvocationError,
    MissingConfigError,
    ProcessError,
    ProcessExecutionError,
    StrategyError,
    ToolError,
)
from agents.framework.core.protocols import (
    ArtifactWriter,
    ManifestFormatter,
    OrchestratorPlugin,
    PipelineStage,
    ProcessDefinitionLoader,
)

__all__ = [
    # Context and Config
    "AgentContext",
    "RunConfig",
    # Protocols
    "ProcessDefinitionLoader",
    "ArtifactWriter",
    "ManifestFormatter",
    "OrchestratorPlugin",
    "PipelineStage",
    # Exceptions
    "AgentError",
    "ConfigurationError",
    "MissingConfigError",
    "InvalidConfigError",
    "LLMError",
    "LLMInvocationError",
    "ProcessError",
    "ProcessExecutionError",
    "StrategyError",
    "ToolError",
    # Decorators
    "handle_agent_errors",
    "log_execution",
    "retry_on_failure",
]
