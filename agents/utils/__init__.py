"""
Utilitários compartilhados pelos agentes.

Este módulo está organizado em subpacotes:
- io: Operações de entrada/saída (drive_writer, manifest, package)
- loaders: Carregamento de definições (process_loader, strategy_loader)
- observability: Instrumentação e métricas (instrumentation, todos)
- helpers: Utilitários auxiliares (context, env_validation)

Para retrocompatibilidade, os principais exports ainda estão disponíveis
diretamente de agents.utils.
"""

# Retrocompatibilidade: manter imports antigos funcionando
from .helpers import normalize_context_name, validate_sensitive_environment
from .io import (
    ManifestHandler,
    ensure_process_folder,
    ensure_strategy_folder,
    format_process_summary,
    package_artifacts,
    write_artifact,
    write_consolidated_report,
)
from .loaders import (
    ProcessDefinition,
    StrategyDefinition,
    load_process,
    load_strategy,
)
from .observability import (
    MetricsCollector,
    TodoManager,
    create_metrics_callbacks,
    run_graph_with_logging,
)

# Imports legados do instrumentation (para compatibilidade com código existente)
try:
    from .observability.instrumentation import (
        GraphCallbackHandler,
        ProcessGraphRunner,
    )
except ImportError:
    # Fallback caso os nomes não existam mais
    GraphCallbackHandler = None  # type: ignore
    ProcessGraphRunner = None  # type: ignore

__all__ = [
    # IO
    "ManifestHandler",
    "ensure_process_folder",
    "ensure_strategy_folder",
    "format_process_summary",
    "package_artifacts",
    "write_artifact",
    "write_consolidated_report",
    # Loaders
    "ProcessDefinition",
    "StrategyDefinition",
    "load_process",
    "load_strategy",
    # Observability
    "MetricsCollector",
    "TodoManager",
    "create_metrics_callbacks",
    "run_graph_with_logging",
    "GraphCallbackHandler",
    "ProcessGraphRunner",
    # Helpers
    "normalize_context_name",
    "validate_sensitive_environment",
]
