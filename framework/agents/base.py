"""
Classe base para agentes e subagentes do framework.

Fornece funcionalidade comum para todos os agentes, incluindo:
- Carregamento automático de conhecimento do processo
- Configuração padrão de LLM
- Integração com ferramentas do framework
- Utilitários para gerenciamento de arquivos e diretórios
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Any, Dict, List

from framework.llm.factory import build_llm
from framework.tools import AgentType, get_tools
from framework.io.knowledge import ProcessKnowledgeManager

logger = logging.getLogger(__name__)


class BaseAgent:
    """
    Classe base para agentes e subagentes do framework.

    Fornece:
    - Carregamento automático de conhecimento do processo
    - LLM pré-configurado com monitoramento
    - Acesso a ferramentas do framework
    - Utilitários para gerenciamento de arquivos

    Attributes:
        process_name: Nome do processo (ex: "05-CheckoutSetup")
        strategy_name: Nome da estratégia (ex: "ZeroUm")
        workspace_root: Diretório raiz do workspace
        process_dir: Diretório do processo no workspace
        data_dir: Diretório _DATA do processo
        llm: Instância do LLM configurado
        tools: Lista de ferramentas disponíveis
    """

    # Deve ser sobrescrito pelas subclasses
    process_name: str = ""  # Ex: "05-CheckoutSetup"
    strategy_name: str = ""  # Ex: "ZeroUm"

    def __init__(
        self,
        workspace_root: Path,
        process_name: Optional[str] = None,
        strategy_name: Optional[str] = None,
        agent_type: AgentType = AgentType.PROCESS,
        enable_tools: bool = True,
        load_knowledge: bool = True,
        llm_config: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Inicializa o agente.

        Args:
            workspace_root: Diretório raiz do workspace (drive/<Contexto>)
            process_name: Nome do processo (sobrescreve atributo da classe)
            strategy_name: Nome da estratégia (sobrescreve atributo da classe)
            agent_type: Tipo de agente (define permissões de ferramentas)
            enable_tools: Se True, habilita ferramentas do framework
            load_knowledge: Se True, carrega conhecimento do processo automaticamente
            llm_config: Configuração customizada do LLM (opcional)
        """
        self.workspace_root = Path(workspace_root)
        self.enable_tools = enable_tools
        self.agent_type = agent_type

        # Sobrescrever nomes se fornecidos
        if process_name:
            self.process_name = process_name
        if strategy_name:
            self.strategy_name = strategy_name

        # Configurar LLM
        default_llm_config = {
            "agent_context": {
                "subagent": self.process_name,
                "strategy": self.strategy_name
            }
        }

        # Mesclar com configuração customizada
        if llm_config:
            default_llm_config.update(llm_config)
            # Preservar agent_context
            if "agent_context" in llm_config:
                default_llm_config["agent_context"].update(llm_config["agent_context"])

        self.llm = build_llm(default_llm_config)

        # Obter ferramentas baseado no tipo de agente
        self.tools = get_tools(agent_type) if enable_tools else []

        # Configurar diretórios do processo
        self.process_dir = workspace_root / self.process_name if self.process_name else workspace_root
        self.data_dir = self.process_dir / "_DATA"

        # Carregar conhecimento do processo
        self._process_knowledge: Optional[str] = None
        if load_knowledge and self.process_name and self.strategy_name:
            self._load_process_knowledge()

    def _load_process_knowledge(self) -> None:
        """
        Carrega conhecimento específico do processo.

        O conhecimento é carregado de process/<strategy>/<process>/*.MD
        e armazenado em self._process_knowledge.
        """
        try:
            # Descobrir base_path (subir 2 níveis do workspace: drive/<Contexto> -> raiz)
            base_path = self.workspace_root.parents[1]

            # Criar manager de conhecimento
            knowledge_manager = ProcessKnowledgeManager(
                base_path=base_path,
                strategy_name=self.strategy_name,
                process_name=self.process_name
            )

            # Carregar conhecimento padrão
            self._process_knowledge = knowledge_manager.load_default_knowledge()

            logger.info(
                f"Conhecimento do processo {self.process_name} carregado com sucesso"
            )

        except Exception as e:
            logger.warning(
                f"Não foi possível carregar conhecimento do processo {self.process_name}: {e}"
            )
            self._process_knowledge = ""

    @property
    def process_knowledge(self) -> str:
        """
        Retorna o conhecimento do processo carregado.

        Returns:
            String com conhecimento consolidado do processo
        """
        return self._process_knowledge or ""

    def get_enhanced_prompt(self, base_prompt: str) -> str:
        """
        Enriquece um prompt com o conhecimento do processo.

        Args:
            base_prompt: Prompt base a ser enriquecido

        Returns:
            Prompt enriquecido com conhecimento do processo

        Example:
            prompt = self.get_enhanced_prompt('''
                Sua tarefa é configurar um checkout.

                Contexto:
                - Produto: {product_name}
                - Preço: {price}
            ''')
        """
        if not self.process_knowledge:
            return base_prompt

        enhanced = f"""
# CONHECIMENTO DO PROCESSO

{self.process_knowledge}

{'='*80}

# TAREFA

{base_prompt}
"""
        return enhanced

    def invoke_llm(self, prompt: str, enhance_with_knowledge: bool = True) -> str:
        """
        Invoca o LLM com um prompt, opcionalmente enriquecido com conhecimento.

        Args:
            prompt: Prompt a enviar
            enhance_with_knowledge: Se True, adiciona conhecimento do processo ao prompt

        Returns:
            Resposta do LLM como string
        """
        if enhance_with_knowledge:
            prompt = self.get_enhanced_prompt(prompt)

        response = self.llm.invoke(prompt)

        # Extrair conteúdo da resposta
        content = getattr(response, "content", response)

        # Normalizar resposta (pode vir como lista ou string)
        if isinstance(content, list):
            parts = []
            for chunk in content:
                if isinstance(chunk, dict) and "text" in chunk:
                    parts.append(chunk["text"])
                else:
                    parts.append(str(chunk))
            return "\n".join(parts).strip()

        return str(content).strip()

    def setup_directories(self, additional_dirs: Optional[List[str]] = None) -> None:
        """
        Cria estrutura de diretórios do processo.

        Args:
            additional_dirs: Lista de diretórios adicionais relativos a data_dir

        Example:
            self.setup_directories(["evidencias", "assets"])
        """
        # Diretórios base
        self.process_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # Diretórios adicionais
        if additional_dirs:
            for dir_name in additional_dirs:
                (self.data_dir / dir_name).mkdir(parents=True, exist_ok=True)

    def save_document(self, filename: str, content: str, in_data_dir: bool = False) -> Path:
        """
        Salva um documento no processo.

        Args:
            filename: Nome do arquivo
            content: Conteúdo do arquivo
            in_data_dir: Se True, salva em _DATA/, senão em raiz do processo

        Returns:
            Path do arquivo salvo

        Example:
            path = self.save_document("01-resultado.MD", content)
        """
        if in_data_dir:
            path = self.data_dir / filename
        else:
            path = self.process_dir / filename

        path.write_text(content.strip() + "\n", encoding="utf-8")
        logger.info(f"Documento salvo: {path}")
        return path

    def read_document(self, path: Path) -> str:
        """
        Lê um documento com tratamento de erro.

        Args:
            path: Caminho do arquivo

        Returns:
            Conteúdo do arquivo

        Example:
            content = self.read_document(Path("file.MD"))
        """
        try:
            return path.read_text(encoding='utf-8')
        except Exception as e:
            logger.warning(f"Erro ao ler {path}: {e}")
            return ""

    def format_list(self, items: List[Any], separator: str = ", ") -> str:
        """
        Formata uma lista para uso em prompts.

        Args:
            items: Lista de itens
            separator: Separador entre itens

        Returns:
            String formatada

        Example:
            formatted = self.format_list(["item1", "item2"])
            # "item1, item2"
        """
        if not items:
            return "Nenhum item fornecido"
        return separator.join(str(item) for item in items)
