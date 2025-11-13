"""
Gerenciamento de manifestos para agentes.

Persistência de metadados de execução em formato JSON.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from agents.framework.core.context import AgentContext
from agents.framework.core.exceptions import FileOperationError


@dataclass
class ManifestStore:
    """
    Armazena e recupera manifestos de execução em formato JSON.

    Manifestos são salvos em drive/<context>/_pipeline/ e contêm
    metadados sobre processos executados.
    """

    base_folder: Path

    def __post_init__(self) -> None:
        """Garante que o diretório base existe."""
        self.base_folder.mkdir(parents=True, exist_ok=True)

    @classmethod
    def from_context(cls, context: AgentContext) -> ManifestStore:
        """
        Factory para criar ManifestStore a partir de AgentContext.

        Args:
            context: Contexto do agente

        Returns:
            ManifestStore configurado para o contexto
        """
        pipeline_folder = context.workspace_root / "_pipeline"
        return cls(base_folder=pipeline_folder)

    def path_for(self, manifest_name: str) -> Path:
        """
        Retorna o caminho completo para um manifesto.

        Args:
            manifest_name: Nome do manifesto (ex: "00-Process-manifest.json")

        Returns:
            Path completo do manifesto
        """
        return self.base_folder / manifest_name

    def write(self, manifest_name: str, payload: Dict[str, Any]) -> Path:
        """
        Escreve um manifesto em formato JSON.

        Args:
            manifest_name: Nome do manifesto
            payload: Dicionário com dados do manifesto

        Returns:
            Path do arquivo escrito

        Raises:
            FileOperationError: Se houver erro ao escrever
        """
        try:
            target = self.path_for(manifest_name)
            content = json.dumps(payload, indent=2, ensure_ascii=False)
            target.write_text(content, encoding="utf-8")
            return target
        except Exception as exc:
            raise FileOperationError(
                operation="write",
                path=str(target),
                reason=f"Falha ao escrever manifesto '{manifest_name}'",
                original_error=exc,
            ) from exc

    def read(self, manifest_name: str) -> Dict[str, Any]:
        """
        Lê um manifesto de JSON.

        Args:
            manifest_name: Nome do manifesto

        Returns:
            Dicionário com dados do manifesto

        Raises:
            FileNotFoundError: Se o manifesto não existir
            FileOperationError: Se houver erro ao ler
        """
        target = self.path_for(manifest_name)
        if not target.exists():
            raise FileNotFoundError(
                f"Manifesto {manifest_name} não encontrado em {self.base_folder}"
            )

        try:
            content = target.read_text(encoding="utf-8")
            return json.loads(content)
        except json.JSONDecodeError as exc:
            raise FileOperationError(
                operation="read",
                path=str(target),
                reason=f"JSON inválido no manifesto '{manifest_name}'",
                original_error=exc,
            ) from exc
        except Exception as exc:
            raise FileOperationError(
                operation="read",
                path=str(target),
                reason=f"Falha ao ler manifesto '{manifest_name}'",
                original_error=exc,
            ) from exc

    def exists(self, manifest_name: str) -> bool:
        """
        Verifica se um manifesto existe.

        Args:
            manifest_name: Nome do manifesto

        Returns:
            True se o manifesto existir, False caso contrário
        """
        return self.path_for(manifest_name).exists()

    def list_manifests(self, pattern: str = "*-manifest.json") -> List[str]:
        """
        Lista todos os manifestos na pasta.

        Args:
            pattern: Padrão glob para filtrar (padrão: "*-manifest.json")

        Returns:
            Lista com nomes dos manifestos encontrados
        """
        return sorted(p.name for p in self.base_folder.glob(pattern))

    def delete(self, manifest_name: str) -> None:
        """
        Remove um manifesto.

        Args:
            manifest_name: Nome do manifesto

        Raises:
            FileNotFoundError: Se o manifesto não existir
            FileOperationError: Se houver erro ao deletar
        """
        target = self.path_for(manifest_name)
        if not target.exists():
            raise FileNotFoundError(
                f"Manifesto {manifest_name} não encontrado em {self.base_folder}"
            )

        try:
            target.unlink()
        except Exception as exc:
            raise FileOperationError(
                operation="delete",
                path=str(target),
                reason=f"Falha ao deletar manifesto '{manifest_name}'",
                original_error=exc,
            ) from exc


# =============================================================================
# Função de compatibilidade (compatibilidade com código antigo)
# =============================================================================


@dataclass
class ManifestHandler:
    """
    DEPRECATED: Use ManifestStore.

    Mantido por compatibilidade com código antigo.
    """

    base_folder: Path

    def __post_init__(self) -> None:
        self.base_folder.mkdir(parents=True, exist_ok=True)

    def path_for(self, manifest_name: str) -> Path:
        return self.base_folder / manifest_name

    def write(self, manifest_name: str, payload: Dict[str, Any]) -> Path:
        target = self.path_for(manifest_name)
        target.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        return target

    def read(self, manifest_name: str) -> Dict[str, Any]:
        target = self.path_for(manifest_name)
        if not target.exists():
            raise FileNotFoundError(
                f"Manifesto {manifest_name} não encontrado em {self.base_folder}"
            )
        return json.loads(target.read_text(encoding="utf-8"))

    def list_manifests(self) -> List[str]:
        return sorted(p.name for p in self.base_folder.glob("*-manifest.json"))


__all__ = [
    "ManifestStore",
    "ManifestHandler",  # deprecated
]
