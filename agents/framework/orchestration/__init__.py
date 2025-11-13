"""
Módulo de orquestração do framework.

Gerencia pipelines de execução, grafos de orquestração e sistema de plugins.
"""

from agents.framework.orchestration.pipeline import (
    ExecuteStage,
    PersistStage,
    PipelineResult,
    PipelineStage,
    PlanStage,
    PrepareStage,
    ProcessPipeline,
    StageResult,
    ValidateStage,
)
from agents.framework.orchestration.registry import (
    PluginMetadata,
    PluginRegistry,
    get_process_registry,
    get_strategy_registry,
)
from agents.framework.orchestration.graph import (
    GraphEdge,
    GraphNode,
    OrchestrationGraph,
)

# Import condicional do LangGraph adapter
try:
    from agents.framework.orchestration.langgraph_adapter import (
        LangGraphOrchestration,
        OrchestrationHandlers,
        OrchestrationState,
        create_orchestration_graph,
    )

    _LANGGRAPH_AVAILABLE = True
except ImportError:
    _LANGGRAPH_AVAILABLE = False
    LangGraphOrchestration = None  # type: ignore
    OrchestrationState = None  # type: ignore
    OrchestrationHandlers = None  # type: ignore
    create_orchestration_graph = None  # type: ignore

__all__ = [
    # Pipeline
    "ProcessPipeline",
    "PipelineStage",
    "PrepareStage",
    "PlanStage",
    "ExecuteStage",
    "ValidateStage",
    "PersistStage",
    "StageResult",
    "PipelineResult",
    # Registry
    "PluginRegistry",
    "PluginMetadata",
    "get_strategy_registry",
    "get_process_registry",
    # Graph
    "OrchestrationGraph",
    "GraphNode",
    "GraphEdge",
]

# Adiciona exports de LangGraph se disponível
if _LANGGRAPH_AVAILABLE:
    __all__.extend(
        [
            "LangGraphOrchestration",
            "OrchestrationState",
            "OrchestrationHandlers",
            "create_orchestration_graph",
        ]
    )
