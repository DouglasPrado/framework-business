"""
Gerenciador de conhecimento para estratégias.

Carrega e consolida arquivos de conhecimento (markdown) que são usados
para enriquecer o contexto dos LLMs durante a análise e seleção de subagentes.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Optional, Union

logger = logging.getLogger(__name__)


class KnowledgeLoader:
    """
    Carregador genérico de conhecimento a partir de arquivos markdown.

    Permite carregar múltiplos arquivos de conhecimento de uma estratégia
    e consolidá-los em um único texto formatado para uso em prompts de LLM.
    """

    def __init__(self, base_path: Path) -> None:
        """
        Inicializa o carregador de conhecimento.

        Args:
            base_path: Caminho base onde os arquivos de conhecimento estão localizados
        """
        self.base_path = Path(base_path)

    def load_file(
        self,
        file_path: Union[str, Path],
        title: Optional[str] = None
    ) -> Optional[str]:
        """
        Carrega um único arquivo de conhecimento.

        Args:
            file_path: Caminho do arquivo (relativo ao base_path ou absoluto)
            title: Título opcional para o arquivo (padrão: nome do arquivo)

        Returns:
            Conteúdo do arquivo com título, ou None se falhar
        """
        # Resolver caminho
        if isinstance(file_path, str):
            file_path = Path(file_path)

        # Se não for absoluto, considerar relativo ao base_path
        if not file_path.is_absolute():
            file_path = self.base_path / file_path

        # Definir título
        if title is None:
            title = file_path.name

        # Tentar ler arquivo
        if not file_path.exists():
            logger.warning(f"Arquivo de conhecimento não encontrado: {file_path}")
            return None

        try:
            content = file_path.read_text(encoding='utf-8')
            logger.info(f"Carregado conhecimento de {file_path.name}")

            # Formatar com título e separador
            formatted = f"\n## {title}\n\n{content}\n\n{'='*80}\n"
            return formatted

        except Exception as e:
            logger.warning(f"Erro ao ler {file_path}: {e}")
            return None

    def load_files(
        self,
        files: Union[List[str], List[Path], Dict[str, str]]
    ) -> str:
        """
        Carrega múltiplos arquivos de conhecimento.

        Args:
            files: Lista de caminhos ou dicionário {caminho: título}

        Returns:
            String com todo o conhecimento consolidado

        Examples:
            # Lista de arquivos
            knowledge = loader.load_files([
                "knowledge.MD",
                "process-analysis.md"
            ])

            # Dicionário com títulos customizados
            knowledge = loader.load_files({
                "knowledge.MD": "Base de Conhecimento",
                "process-analysis.md": "Análise de Processos"
            })
        """
        knowledge_content = "# CONHECIMENTO DA ESTRATÉGIA\n\n"

        # Se for lista, converter para dicionário
        if isinstance(files, list):
            files = {str(f): None for f in files}

        # Carregar cada arquivo
        for file_path, title in files.items():
            content = self.load_file(file_path, title)
            if content:
                knowledge_content += content

        return knowledge_content

    def load_strategy_knowledge(
        self,
        strategy_name: str,
        knowledge_files: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Carrega conhecimento de uma estratégia específica.

        Conveniência para carregar arquivos padrão de uma estratégia.

        Args:
            strategy_name: Nome da estratégia (ex: "ZeroUm")
            knowledge_files: Dicionário opcional {arquivo: título}.
                           Se None, usa arquivos padrão (knowledge.MD, README.MD, etc)

        Returns:
            String com conhecimento consolidado

        Example:
            loader = KnowledgeLoader(base_path / "strategies")
            knowledge = loader.load_strategy_knowledge("ZeroUm")
        """
        strategy_path = self.base_path / strategy_name

        # Arquivos padrão se não especificado
        if knowledge_files is None:
            knowledge_files = {
                "knowledge.MD": "Base de Conhecimento",
                "process-analysis.md": "Análise de Processos",
                "README.MD": "Visão Geral da Estratégia",
                "tasks.MD": "Checklist Operacional"
            }

        # Atualizar base_path temporariamente para a estratégia
        original_base = self.base_path
        self.base_path = strategy_path

        try:
            knowledge = self.load_files(knowledge_files)
            return knowledge
        finally:
            # Restaurar base_path original
            self.base_path = original_base

    @classmethod
    def load_from_paths(
        cls,
        files: List[Union[str, Path]],
        titles: Optional[List[str]] = None
    ) -> str:
        """
        Método estático para carregar arquivos com caminhos absolutos.

        Útil quando você tem caminhos completos e não quer criar uma instância.

        Args:
            files: Lista de caminhos absolutos
            titles: Lista opcional de títulos (mesmo tamanho que files)

        Returns:
            String com conhecimento consolidado

        Example:
            knowledge = KnowledgeLoader.load_from_paths([
                "/path/to/knowledge.MD",
                "/path/to/process.MD"
            ], titles=["Conhecimento", "Processos"])
        """
        # Criar loader temporário com base vazia
        loader = cls(Path("/"))

        # Preparar dicionário
        if titles is None:
            titles = [None] * len(files)

        files_dict = {str(f): t for f, t in zip(files, titles)}

        return loader.load_files(files_dict)


class StrategyKnowledgeManager:
    """
    Gerenciador de conhecimento específico para estratégias.

    Wrapper de alto nível que facilita o uso do KnowledgeLoader
    no contexto de estratégias de negócio.
    """

    def __init__(self, base_path: Path, strategy_name: str) -> None:
        """
        Inicializa o gerenciador.

        Args:
            base_path: Caminho base do repositório
            strategy_name: Nome da estratégia (ex: "ZeroUm")
        """
        self.base_path = Path(base_path)
        self.strategy_name = strategy_name
        self.strategy_path = self.base_path / "strategies" / strategy_name
        self.loader = KnowledgeLoader(self.strategy_path)

    def load_default_knowledge(self) -> str:
        """
        Carrega arquivos padrão de conhecimento da estratégia.

        Returns:
            Conhecimento consolidado
        """
        default_files = {
            "knowledge.MD": "Base de Conhecimento",
            "process-analysis.md": "Análise de Processos",
            "README.MD": "Visão Geral da Estratégia",
            "tasks.MD": "Checklist Operacional"
        }

        return self.loader.load_files(default_files)

    def load_custom_knowledge(self, files: Dict[str, str]) -> str:
        """
        Carrega arquivos customizados de conhecimento.

        Args:
            files: Dicionário {arquivo: título}

        Returns:
            Conhecimento consolidado
        """
        return self.loader.load_files(files)

    def load_specific_files(self, *filenames: str) -> str:
        """
        Carrega arquivos específicos (sem títulos customizados).

        Args:
            filenames: Nomes dos arquivos a carregar

        Returns:
            Conhecimento consolidado

        Example:
            manager = StrategyKnowledgeManager(base_path, "ZeroUm")
            knowledge = manager.load_specific_files(
                "knowledge.MD",
                "tasks.MD"
            )
        """
        files = {f: None for f in filenames}
        return self.loader.load_files(files)


class ProcessKnowledgeManager:
    """
    Gerenciador de conhecimento para processos específicos.

    Carrega conhecimento de um processo individual localizado em
    process/<Strategy>/<ProcessName>/*.MD
    """

    def __init__(self, base_path: Path, strategy_name: str, process_name: str) -> None:
        """
        Inicializa o gerenciador de conhecimento de processo.

        Args:
            base_path: Caminho base do repositório
            strategy_name: Nome da estratégia (ex: "ZeroUm")
            process_name: Nome do processo (ex: "05-CheckoutSetup")
        """
        self.base_path = Path(base_path)
        self.strategy_name = strategy_name
        self.process_name = process_name
        self.process_path = self.base_path / "process" / strategy_name / process_name
        self.loader = KnowledgeLoader(self.process_path)

    def load_default_knowledge(self) -> str:
        """
        Carrega arquivos padrão de conhecimento do processo.

        Arquivos padrão:
        - knowledge.MD: Base de conhecimento do processo
        - process.MD: Definição detalhada do processo
        - tasks.MD: Checklist operacional
        - validator.MD: Critérios de validação
        - README.MD: Visão geral

        Returns:
            Conhecimento consolidado
        """
        default_files = {
            "knowledge.MD": "Base de Conhecimento do Processo",
            "process.MD": "Definição do Processo",
            "tasks.MD": "Checklist Operacional",
            "validator.MD": "Critérios de Validação",
            "README.MD": "Visão Geral"
        }

        return self.loader.load_files(default_files)

    def load_custom_knowledge(self, files: Dict[str, str]) -> str:
        """
        Carrega arquivos customizados de conhecimento.

        Args:
            files: Dicionário {arquivo: título}

        Returns:
            Conhecimento consolidado
        """
        return self.loader.load_files(files)

    def load_specific_files(self, *filenames: str) -> str:
        """
        Carrega arquivos específicos (sem títulos customizados).

        Args:
            filenames: Nomes dos arquivos a carregar

        Returns:
            Conhecimento consolidado

        Example:
            manager = ProcessKnowledgeManager(
                base_path,
                "ZeroUm",
                "05-CheckoutSetup"
            )
            knowledge = manager.load_specific_files(
                "knowledge.MD",
                "process.MD"
            )
        """
        files = {f: None for f in filenames}
        return self.loader.load_files(files)
