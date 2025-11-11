"""
Módulo de operações de I/O (Input/Output) para agents.

Contém utilitários para leitura, escrita e manipulação de arquivos.
"""

from .drive_writer import ensure_process_folder, ensure_strategy_folder, write_artifact
from .manifest import ManifestHandler
from .package import package_artifacts
from .reporting import format_process_summary, write_consolidated_report

__all__ = [
    "ensure_process_folder",
    "ensure_strategy_folder",
    "write_artifact",
    "ManifestHandler",
    "package_artifacts",
    "format_process_summary",
    "write_consolidated_report",
]
