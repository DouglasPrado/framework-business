"""
Gerenciamento de workspace para agentes.

Abstrai operações de criação de diretórios e escrita de artefatos,
usando AgentContext para determinar caminhos.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from framework.core.context import AgentContext
from framework.core.exceptions import FileOperationError


class WorkspaceManager:
    """
    Gerencia o workspace de execução de agentes.

    Responsável por criar diretórios, escrever artefatos numerados
    e manter a estrutura padrão do workspace.
    """

    def __init__(self, context: AgentContext):
        """
        Inicializa o gerenciador de workspace.

        Args:
            context: Contexto do agente
        """
        self.context = context

    def ensure_workspace_root(self) -> Path:
        """
        Garante que o diretório raiz do workspace existe.

        Returns:
            Path para drive/<context_name>/

        Raises:
            FileOperationError: Se não conseguir criar o diretório
        """
        try:
            path = self.context.workspace_root
            path.mkdir(parents=True, exist_ok=True)
            return path
        except Exception as exc:
            raise FileOperationError(
                operation="mkdir",
                path=str(self.context.workspace_root),
                reason="Falha ao criar workspace root",
                original_error=exc,
            ) from exc

    def ensure_strategy_folder(self) -> Path:
        """
        Garante que o diretório da estratégia existe.

        Returns:
            Path para drive/<context_name>/<strategy_name>/

        Raises:
            FileOperationError: Se não conseguir criar o diretório
        """
        try:
            path = self.context.strategy_root
            path.mkdir(parents=True, exist_ok=True)
            return path
        except Exception as exc:
            raise FileOperationError(
                operation="mkdir",
                path=str(self.context.strategy_root),
                reason="Falha ao criar strategy folder",
                original_error=exc,
            ) from exc

    def ensure_workspace(self) -> Path:
        """
        Compatibilidade com código legado: garante workspace, estratégia e _pipeline.

        Returns:
            Path para o diretório raiz do workspace
        """
        root = self.ensure_workspace_root()
        self.ensure_strategy_folder()
        self.get_pipeline_folder()
        return root

    def ensure_process_folder(self) -> Path:
        """
        Garante que o diretório do processo existe.

        Returns:
            Path para drive/<context_name>/<strategy_name>/<process_code>/

        Raises:
            ValueError: Se process_code não estiver definido no contexto
            FileOperationError: Se não conseguir criar o diretório
        """
        if not self.context.process_code:
            raise ValueError("process_code não está definido no contexto")

        try:
            path = self.context.process_root
            if path:
                path.mkdir(parents=True, exist_ok=True)
                return path
            raise ValueError("process_root é None")
        except ValueError:
            raise
        except Exception as exc:
            raise FileOperationError(
                operation="mkdir",
                path=str(self.context.process_root),
                reason="Falha ao criar process folder",
                original_error=exc,
            ) from exc

    def get_pipeline_folder(self) -> Path:
        """
        Retorna o diretório _pipeline para armazenar metadados.

        Returns:
            Path para drive/<context_name>/_pipeline/

        Raises:
            FileOperationError: Se não conseguir criar o diretório
        """
        try:
            path = self.context.workspace_root / "_pipeline"
            path.mkdir(parents=True, exist_ok=True)
            return path
        except Exception as exc:
            raise FileOperationError(
                operation="mkdir",
                path=str(self.context.workspace_root / "_pipeline"),
                reason="Falha ao criar pipeline folder",
                original_error=exc,
            ) from exc

    def next_prefixed_name(
        self, folder: Path, slug: str, extension: str = ".MD"
    ) -> Path:
        """
        Calcula o próximo nome numerado (01-, 02-, etc.) dentro da pasta.

        Args:
            folder: Pasta onde o arquivo será criado
            slug: Slug base para o nome do arquivo
            extension: Extensão do arquivo (padrão: .MD)

        Returns:
            Path com o próximo nome numerado disponível

        Examples:
            >>> manager.next_prefixed_name(Path("/path"), "problem-hypothesis")
            PosixPath('/path/01-problem-hypothesis.MD')
        """
        folder.mkdir(parents=True, exist_ok=True)

        pattern = re.compile(r"^(\d{2})-", re.IGNORECASE)
        highest = 0
        for item in folder.iterdir():
            match = pattern.match(item.name)
            if match:
                highest = max(highest, int(match.group(1)))

        slugified = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
        next_index = highest + 1
        filename = f"{next_index:02d}-{slugified}{extension}"
        return folder / filename

    def write_artifact(
        self,
        folder: Path,
        slug: str,
        content: str,
        extension: str = ".MD",
    ) -> Path:
        """
        Escreve um artefato numerado na pasta especificada.

        Args:
            folder: Pasta onde o arquivo será criado
            slug: Slug base para o nome do arquivo
            content: Conteúdo do artefato
            extension: Extensão do arquivo (padrão: .MD)

        Returns:
            Path do arquivo criado

        Raises:
            FileOperationError: Se houver erro ao escrever o arquivo
        """
        try:
            target = self.next_prefixed_name(folder, slug, extension)
            target.write_text(content, encoding="utf-8")
            return target
        except Exception as exc:
            raise FileOperationError(
                operation="write",
                path=str(folder / f"*{extension}"),
                reason=f"Falha ao escrever artefato '{slug}'",
                original_error=exc,
            ) from exc

    def write_numbered_artifact(
        self,
        number: int,
        slug: str,
        content: str,
        folder: Optional[Path] = None,
        extension: str = ".MD",
    ) -> Path:
        """
        Escreve artefato com número específico (não calcula próximo).

        Args:
            number: Número do artefato (ex: 1 para 01-)
            slug: Slug base para o nome do arquivo
            content: Conteúdo do artefato
            folder: Pasta onde escrever (padrão: process_root)
            extension: Extensão do arquivo (padrão: .MD)

        Returns:
            Path do arquivo criado

        Raises:
            ValueError: Se folder não for fornecido e process_root for None
            FileOperationError: Se houver erro ao escrever o arquivo
        """
        if folder is None:
            folder = self.context.process_root
            if folder is None:
                raise ValueError(
                    "folder não fornecido e process_root é None no contexto"
                )

        try:
            folder.mkdir(parents=True, exist_ok=True)
            slugified = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
            filename = f"{number:02d}-{slugified}{extension}"
            target = folder / filename
            target.write_text(content, encoding="utf-8")
            return target
        except Exception as exc:
            raise FileOperationError(
                operation="write",
                path=str(folder / f"{number:02d}-*{extension}"),
                reason=f"Falha ao escrever artefato numerado '{slug}'",
                original_error=exc,
            ) from exc

    def read_artifact(self, path: Path) -> str:
        """
        Lê o conteúdo de um artefato.

        Args:
            path: Caminho do artefato

        Returns:
            Conteúdo do artefato

        Raises:
            FileNotFoundError: Se o artefato não existir
            FileOperationError: Se houver erro ao ler o arquivo
        """
        try:
            return path.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Artefato não encontrado: {path}") from exc
        except Exception as exc:
            raise FileOperationError(
                operation="read",
                path=str(path),
                reason="Falha ao ler artefato",
                original_error=exc,
            ) from exc

    def list_artifacts(
        self, folder: Optional[Path] = None, pattern: str = "*"
    ) -> list[Path]:
        """
        Lista artefatos em uma pasta.

        Args:
            folder: Pasta a listar (padrão: process_root)
            pattern: Padrão glob para filtrar (padrão: "*")

        Returns:
            Lista de Paths dos artefatos encontrados

        Raises:
            ValueError: Se folder não for fornecido e process_root for None
        """
        if folder is None:
            folder = self.context.process_root
            if folder is None:
                raise ValueError(
                    "folder não fornecido e process_root é None no contexto"
                )

        if not folder.exists():
            return []

        return sorted(folder.glob(pattern))


# =============================================================================
# Funções de conveniência (compatibilidade com código antigo)
# =============================================================================


def ensure_strategy_folder(
    context_name: str, strategy_name: str, base_path: Path
) -> Path:
    """
    Função de compatibilidade - use WorkspaceManager.ensure_strategy_folder().

    DEPRECATED: Esta função será removida em versões futuras.
    Use WorkspaceManager com AgentContext.
    """
    from . import BASE_PATH as DEFAULT_BASE_PATH

    base = base_path if base_path else DEFAULT_BASE_PATH
    from framework.core.context import AgentContext

    ctx = AgentContext(
        context_name=context_name,
        context_description="",
        strategy_name=strategy_name,
        base_path=base,
    )
    return WorkspaceManager(ctx).ensure_strategy_folder()


def ensure_process_folder(context_name: str, process_code: str, base_path: Path) -> Path:
    """
    Função de compatibilidade - use WorkspaceManager.ensure_process_folder().

    DEPRECATED: Esta função será removida em versões futuras.
    Use WorkspaceManager com AgentContext.
    """
    from . import BASE_PATH as DEFAULT_BASE_PATH

    base = base_path if base_path else DEFAULT_BASE_PATH
    from framework.core.context import AgentContext

    # Para processos, usamos o process_code também como strategy_name temporariamente
    ctx = AgentContext(
        context_name=context_name,
        context_description="",
        strategy_name=process_code.split("/")[0] if "/" in process_code else process_code,
        process_code=process_code,
        base_path=base,
    )
    return WorkspaceManager(ctx).ensure_process_folder()


__all__ = [
    "WorkspaceManager",
    "ensure_strategy_folder",  # deprecated
    "ensure_process_folder",  # deprecated
]
