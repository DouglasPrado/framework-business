"""
Objetos de valor para contexto e configuração de agentes.

Este módulo define objetos imutáveis (frozen dataclasses) que carregam
informação de contexto e configuração através do framework.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Any

# Calcular BASE_PATH (raiz do repositório)
import sys
from pathlib import Path as _Path
_agents_root = _Path(__file__).resolve().parents[2]
if str(_agents_root) not in sys.path:
    sys.path.insert(0, str(_agents_root))

# BASE_PATH: raiz do repositório
BASE_PATH = _agents_root


# =============================================================================
# AgentContext - Contexto de Execução
# =============================================================================


@dataclass(frozen=True)
class AgentContext:
    """
    Contexto imutável de execução de um agente.

    Este objeto carrega toda informação de contexto necessária para
    executar um agente: nome do contexto, estratégia, processo e caminhos.

    Attributes:
        context_name: Nome normalizado do contexto (ex: "AutomarticlesAutomacao")
        context_description: Descrição detalhada fornecida pelo usuário
        strategy_name: Nome da estratégia sendo executada (ex: "ZeroUm")
        process_code: Código do processo específico (ex: "00-ProblemHypothesisExpress")
        base_path: Caminho base do repositório (padrão: BASE_PATH)
        metadata: Metadados adicionais arbitrários

    Examples:
        >>> ctx = AgentContext(
        ...     context_name="AutomarticlesAutomacao",
        ...     context_description="Automatizar blog com IA",
        ...     strategy_name="ZeroUm",
        ...     process_code="00-ProblemHypothesisExpress"
        ... )
        >>> ctx.workspace_root
        PosixPath('/path/to/drive/AutomarticlesAutomacao')
    """

    context_name: str
    context_description: str
    strategy_name: str
    process_code: Optional[str] = None
    base_path: Path = field(default=BASE_PATH)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Valida os campos após inicialização."""
        if not self.context_name:
            raise ValueError("context_name não pode ser vazio")
        if not self.strategy_name:
            raise ValueError("strategy_name não pode ser vazio")
        # Converte base_path para Path se for string
        if isinstance(object.__getattribute__(self, "base_path"), str):
            object.__setattr__(
                self, "base_path", Path(object.__getattribute__(self, "base_path"))
            )

    @property
    def workspace_root(self) -> Path:
        """
        Retorna o diretório raiz do workspace para este contexto.

        Returns:
            Path para drive/<context_name>/
        """
        return self.base_path / "drive" / self.context_name

    @property
    def strategy_root(self) -> Path:
        """
        Retorna o diretório raiz da estratégia no workspace.

        Returns:
            Path para drive/<context_name>/<strategy_name>/
        """
        return self.workspace_root / self.strategy_name

    @property
    def process_root(self) -> Optional[Path]:
        """
        Retorna o diretório do processo específico, se houver.

        Returns:
            Path para drive/<context_name>/<strategy_name>/<process_code>/
            ou None se process_code não estiver definido
        """
        if self.process_code:
            return self.strategy_root / self.process_code
        return None

    @property
    def strategy_definition_path(self) -> Path:
        """
        Retorna o caminho para a definição da estratégia.

        Returns:
            Path para strategies/<strategy_name>/
        """
        return self.base_path / "strategies" / self.strategy_name

    @property
    def process_definition_path(self) -> Optional[Path]:
        """
        Retorna o caminho para a definição do processo, se houver.

        Returns:
            Path para process/<strategy_name>/<process_code>/
            ou None se process_code não estiver definido
        """
        if self.process_code:
            return self.base_path / "process" / self.strategy_name / self.process_code
        return None

    def with_process(self, process_code: str) -> "AgentContext":
        """
        Cria novo contexto com process_code diferente.

        Args:
            process_code: Código do novo processo

        Returns:
            Novo AgentContext com process_code atualizado
        """
        return AgentContext(
            context_name=self.context_name,
            context_description=self.context_description,
            strategy_name=self.strategy_name,
            process_code=process_code,
            base_path=self.base_path,
            metadata=self.metadata.copy(),
        )

    def with_metadata(self, **kwargs: Any) -> "AgentContext":
        """
        Cria novo contexto com metadados adicionais.

        Args:
            **kwargs: Metadados a serem adicionados/atualizados

        Returns:
            Novo AgentContext com metadata atualizado
        """
        new_metadata = self.metadata.copy()
        new_metadata.update(kwargs)
        return AgentContext(
            context_name=self.context_name,
            context_description=self.context_description,
            strategy_name=self.strategy_name,
            process_code=self.process_code,
            base_path=self.base_path,
            metadata=new_metadata,
        )


# =============================================================================
# RunConfig - Configuração de Execução
# =============================================================================


@dataclass(frozen=True)
class RunConfig:
    """
    Configuração imutável de execução de um agente.

    Este objeto carrega todas as configurações que afetam como um agente
    é executado: modelo LLM, temperatura, modo de raciocínio, ferramentas, etc.

    Attributes:
        model: Nome do modelo LLM (ex: "gpt-4o", "gpt-4o-mini")
        temperature: Temperatura para geração (0.0 a 1.0)
        reasoning_mode: Modo de raciocínio ("simple" ou "reflection")
        tools: Lista de nomes de ferramentas disponíveis
        max_tokens: Máximo de tokens na resposta
        enable_todos: Se deve trackear TODOs
        enable_tracing: Se deve habilitar tracing (LangSmith)
        cost_per_1k_input: Custo por 1k tokens de input (USD)
        cost_per_1k_output: Custo por 1k tokens de output (USD)
        extra_config: Configurações adicionais arbitrárias

    Examples:
        >>> config = RunConfig(
        ...     model="gpt-4o",
        ...     temperature=0.7,
        ...     reasoning_mode="reflection",
        ...     tools=["ls", "read", "write"]
        ... )
        >>> config.is_reflection_mode
        True
    """

    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    reasoning_mode: str = "simple"
    tools: List[str] = field(default_factory=list)
    max_tokens: Optional[int] = None
    enable_todos: bool = True
    enable_tracing: bool = False
    cost_per_1k_input: float = 0.0
    cost_per_1k_output: float = 0.0
    extra_config: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Valida os campos após inicialização."""
        if not self.model:
            raise ValueError("model não pode ser vazio")
        if not 0.0 <= self.temperature <= 1.0:
            raise ValueError("temperature deve estar entre 0.0 e 1.0")
        if self.reasoning_mode not in ("simple", "reflection"):
            raise ValueError("reasoning_mode deve ser 'simple' ou 'reflection'")
        if self.cost_per_1k_input < 0 or self.cost_per_1k_output < 0:
            raise ValueError("custos não podem ser negativos")

    @property
    def is_reflection_mode(self) -> bool:
        """Retorna True se está em modo de reflexão."""
        return self.reasoning_mode == "reflection"

    @property
    def is_simple_mode(self) -> bool:
        """Retorna True se está em modo simples."""
        return self.reasoning_mode == "simple"

    def with_model(self, model: str) -> "RunConfig":
        """
        Cria nova configuração com modelo diferente.

        Args:
            model: Nome do novo modelo

        Returns:
            Novo RunConfig com modelo atualizado
        """
        return RunConfig(
            model=model,
            temperature=self.temperature,
            reasoning_mode=self.reasoning_mode,
            tools=self.tools.copy(),
            max_tokens=self.max_tokens,
            enable_todos=self.enable_todos,
            enable_tracing=self.enable_tracing,
            cost_per_1k_input=self.cost_per_1k_input,
            cost_per_1k_output=self.cost_per_1k_output,
            extra_config=self.extra_config.copy(),
        )

    def with_reasoning_mode(self, mode: str) -> "RunConfig":
        """
        Cria nova configuração com modo de raciocínio diferente.

        Args:
            mode: "simple" ou "reflection"

        Returns:
            Novo RunConfig com reasoning_mode atualizado

        Raises:
            ValueError: Se mode não for válido
        """
        if mode not in ("simple", "reflection"):
            raise ValueError("mode deve ser 'simple' ou 'reflection'")
        return RunConfig(
            model=self.model,
            temperature=self.temperature,
            reasoning_mode=mode,
            tools=self.tools.copy(),
            max_tokens=self.max_tokens,
            enable_todos=self.enable_todos,
            enable_tracing=self.enable_tracing,
            cost_per_1k_input=self.cost_per_1k_input,
            cost_per_1k_output=self.cost_per_1k_output,
            extra_config=self.extra_config.copy(),
        )

    def with_tools(self, tools: List[str]) -> "RunConfig":
        """
        Cria nova configuração com lista de ferramentas diferente.

        Args:
            tools: Nova lista de ferramentas

        Returns:
            Novo RunConfig com tools atualizado
        """
        return RunConfig(
            model=self.model,
            temperature=self.temperature,
            reasoning_mode=self.reasoning_mode,
            tools=tools,
            max_tokens=self.max_tokens,
            enable_todos=self.enable_todos,
            enable_tracing=self.enable_tracing,
            cost_per_1k_input=self.cost_per_1k_input,
            cost_per_1k_output=self.cost_per_1k_output,
            extra_config=self.extra_config.copy(),
        )

    def with_extra_config(self, **kwargs: Any) -> "RunConfig":
        """
        Cria nova configuração com extra_config adicional.

        Args:
            **kwargs: Configurações a serem adicionadas/atualizadas

        Returns:
            Novo RunConfig com extra_config atualizado
        """
        new_extra = self.extra_config.copy()
        new_extra.update(kwargs)
        return RunConfig(
            model=self.model,
            temperature=self.temperature,
            reasoning_mode=self.reasoning_mode,
            tools=self.tools.copy(),
            max_tokens=self.max_tokens,
            enable_todos=self.enable_todos,
            enable_tracing=self.enable_tracing,
            cost_per_1k_input=self.cost_per_1k_input,
            cost_per_1k_output=self.cost_per_1k_output,
            extra_config=new_extra,
        )


# =============================================================================
# Convenience Factories
# =============================================================================


def create_context_from_cli_args(
    context_name: str,
    strategy_name: str,
    context_description: str = "",
    process_code: Optional[str] = None,
) -> AgentContext:
    """
    Factory para criar AgentContext a partir de argumentos CLI.

    Args:
        context_name: Nome do contexto
        strategy_name: Nome da estratégia
        context_description: Descrição do contexto
        process_code: Código do processo (opcional)

    Returns:
        AgentContext configurado
    """
    return AgentContext(
        context_name=context_name,
        context_description=context_description,
        strategy_name=strategy_name,
        process_code=process_code,
    )


def create_run_config_from_settings(settings: Any) -> RunConfig:
    """
    Factory para criar RunConfig a partir de Settings.

    Args:
        settings: Objeto de configurações (ex: Settings())

    Returns:
        RunConfig configurado com valores do settings
    """
    return RunConfig(
        model=getattr(settings, "llm_model", "gpt-4o-mini"),
        temperature=getattr(settings, "llm_temperature", 0.7),
        reasoning_mode=getattr(settings, "reasoning_mode", "simple"),
        enable_todos=getattr(settings, "enable_todos", True),
        enable_tracing=getattr(settings, "langsmith_tracing", False),
        cost_per_1k_input=getattr(settings, "zeroum_cost_per_1k_input", 0.0),
        cost_per_1k_output=getattr(settings, "zeroum_cost_per_1k_output", 0.0),
    )
