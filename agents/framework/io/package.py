"""
Empacotamento de artefatos em arquivos compactados.

Cria arquivos ZIP com os artefatos gerados durante a execução.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

from agents.framework.core.context import AgentContext
from agents.framework.core.exceptions import FileOperationError


class PackageService:
    """
    Serviço para empacotamento de artefatos em arquivos ZIP.

    Permite criar arquivos compactados com os outputs gerados
    durante a execução de estratégias e processos.
    """

    def __init__(self, context: AgentContext):
        """
        Inicializa o serviço de empacotamento.

        Args:
            context: Contexto do agente
        """
        self.context = context

    def package_strategy_artifacts(
        self, output_name: Optional[str] = None
    ) -> Path:
        """
        Empacota todos os artefatos da estratégia em um arquivo ZIP.

        Args:
            output_name: Nome do arquivo (sem extensão). Se None, usa
                        "{strategy_name}AgentOutputs"

        Returns:
            Path do arquivo ZIP criado

        Raises:
            FileOperationError: Se houver erro ao criar o pacote
        """
        strategy_folder = self.context.strategy_root
        strategy_folder.mkdir(parents=True, exist_ok=True)

        archive_name = output_name or f"{self.context.strategy_name}AgentOutputs"
        archive_path = strategy_folder / archive_name

        try:
            # Remove arquivo existente se houver
            zip_path = archive_path.with_suffix(".zip")
            if zip_path.exists():
                zip_path.unlink()

            # Cria o arquivo ZIP
            result = shutil.make_archive(
                str(archive_path), "zip", root_dir=str(strategy_folder)
            )
            return Path(result)
        except Exception as exc:
            raise FileOperationError(
                operation="package",
                path=str(archive_path),
                reason=f"Falha ao empacotar artefatos da estratégia '{self.context.strategy_name}'",
                original_error=exc,
            ) from exc

    def package_process_artifacts(
        self, output_name: Optional[str] = None
    ) -> Path:
        """
        Empacota artefatos de um processo específico em um arquivo ZIP.

        Args:
            output_name: Nome do arquivo (sem extensão). Se None, usa
                        "{process_code}Outputs"

        Returns:
            Path do arquivo ZIP criado

        Raises:
            ValueError: Se process_code não estiver definido no contexto
            FileOperationError: Se houver erro ao criar o pacote
        """
        if not self.context.process_code:
            raise ValueError("process_code não está definido no contexto")

        process_folder = self.context.process_root
        if not process_folder:
            raise ValueError("process_root é None no contexto")

        process_folder.mkdir(parents=True, exist_ok=True)

        archive_name = output_name or f"{self.context.process_code}Outputs"
        archive_path = process_folder.parent / archive_name

        try:
            # Remove arquivo existente se houver
            zip_path = archive_path.with_suffix(".zip")
            if zip_path.exists():
                zip_path.unlink()

            # Cria o arquivo ZIP
            result = shutil.make_archive(
                str(archive_path), "zip", root_dir=str(process_folder)
            )
            return Path(result)
        except Exception as exc:
            raise FileOperationError(
                operation="package",
                path=str(archive_path),
                reason=f"Falha ao empacotar artefatos do processo '{self.context.process_code}'",
                original_error=exc,
            ) from exc

    def package_custom_folder(
        self, folder: Path, output_name: str, output_dir: Optional[Path] = None
    ) -> Path:
        """
        Empacota uma pasta customizada em um arquivo ZIP.

        Args:
            folder: Pasta a ser empacotada
            output_name: Nome do arquivo (sem extensão)
            output_dir: Diretório onde salvar o ZIP (padrão: mesmo da pasta)

        Returns:
            Path do arquivo ZIP criado

        Raises:
            FileNotFoundError: Se a pasta não existir
            FileOperationError: Se houver erro ao criar o pacote
        """
        if not folder.exists():
            raise FileNotFoundError(f"Pasta não encontrada: {folder}")

        if not folder.is_dir():
            raise ValueError(f"Path não é um diretório: {folder}")

        output_dir = output_dir or folder.parent
        archive_path = output_dir / output_name

        try:
            # Remove arquivo existente se houver
            zip_path = archive_path.with_suffix(".zip")
            if zip_path.exists():
                zip_path.unlink()

            # Cria o arquivo ZIP
            result = shutil.make_archive(
                str(archive_path), "zip", root_dir=str(folder)
            )
            return Path(result)
        except Exception as exc:
            raise FileOperationError(
                operation="package",
                path=str(archive_path),
                reason=f"Falha ao empacotar pasta '{folder}'",
                original_error=exc,
            ) from exc

    def create_archive(self, source_dir: Path, output_path: Path) -> Path:
        """
        Compatibilidade com código legado: cria ZIP para uma pasta arbitrária.

        Args:
            source_dir: Pasta a ser empacotada
            output_path: Caminho base (sem .zip) do arquivo de saída

        Returns:
            Path do arquivo ZIP criado
        """
        return self.package_custom_folder(
            folder=source_dir,
            output_name=output_path.name,
            output_dir=output_path.parent,
        )


# =============================================================================
# Função de compatibilidade (compatibilidade com código antigo)
# =============================================================================


def package_artifacts(
    context_name: str,
    strategy_name: str,
    base_path: Path,
    output_name: Optional[str] = None,
) -> Path:
    """
    DEPRECATED: Use PackageService.package_strategy_artifacts().

    Mantido por compatibilidade com código antigo.
    """
    from agents import BASE_PATH as DEFAULT_BASE_PATH

    base = base_path if base_path else DEFAULT_BASE_PATH

    strategy_folder = base / "drive" / context_name / strategy_name
    strategy_folder.mkdir(parents=True, exist_ok=True)

    archive_name = output_name or f"{strategy_name}AgentOutputs"
    archive_path = strategy_folder / archive_name

    if archive_path.with_suffix(".zip").exists():
        archive_path.with_suffix(".zip").unlink()

    result = shutil.make_archive(
        str(archive_path), "zip", root_dir=str(strategy_folder)
    )
    return Path(result)


__all__ = [
    "PackageService",
    "package_artifacts",  # deprecated
]
