"""
Módulo de I/O do framework.

Gerencia operações de leitura/escrita de artefatos, manifestos e workspace.
"""

from agents.framework.io.workspace import WorkspaceManager
from agents.framework.io.manifest import ManifestStore
from agents.framework.io.package import PackageService

__all__ = [
    "WorkspaceManager",
    "ManifestStore",
    "PackageService",
]
