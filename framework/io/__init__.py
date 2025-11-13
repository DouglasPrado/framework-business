"""
Módulo de I/O do framework.

Gerencia operações de leitura/escrita de artefatos, manifestos e workspace.
"""

from framework.io.workspace import WorkspaceManager
from framework.io.manifest import ManifestStore
from framework.io.package import PackageService
from framework.io.knowledge import KnowledgeLoader, StrategyKnowledgeManager

__all__ = [
    "WorkspaceManager",
    "ManifestStore",
    "PackageService",
    "KnowledgeLoader",
    "StrategyKnowledgeManager",
]
