"""
Utilitários compartilhados pelos agentes.

Este módulo está organizado em subpacotes:
- io: Operações de entrada/saída (drive_writer, manifest, package)
- loaders: Carregamento de definições (process_loader, strategy_loader)
- observability: Utilidades leves (todos)
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
from .observability import TodoManager

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
    "TodoManager",
    # Helpers
    "normalize_context_name",
    "validate_sensitive_environment",
]
