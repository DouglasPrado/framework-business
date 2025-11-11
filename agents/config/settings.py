"""
Configuração centralizada do sistema de agents.

Consolida todas as variáveis de ambiente e configurações utilizadas
pelos agents, orquestradores e utilitários.
"""

import os
from dataclasses import dataclass, field
from typing import Optional

from ..exceptions import InvalidConfigError, MissingConfigError


@dataclass
class Settings:
    """
    Configurações centralizadas do sistema de agents.

    Todas as configurações são carregadas de variáveis de ambiente com
    valores padrão apropriados.
    """

    # ========================================================================
    # LLM Configuration
    # ========================================================================

    llm_model: str = field(
        default_factory=lambda: os.getenv("AGENTS_LLM_MODEL", "gpt-4o-mini")
    )
    """Modelo LLM padrão a ser utilizado pelos agents"""

    llm_temperature: float = field(
        default_factory=lambda: float(os.getenv("AGENTS_LLM_TEMPERATURE", "0.4"))
    )
    """Temperatura padrão para geração de texto"""

    # ========================================================================
    # Reasoning Configuration
    # ========================================================================

    reasoning_mode: str = field(
        default_factory=lambda: os.getenv("AGENTS_REASONING_MODE", "simple")
    )
    """Modo de raciocínio: 'simple' ou 'reflection'"""

    reasoning_model: str = field(
        default_factory=lambda: os.getenv("AGENTS_REASONING_MODEL", "gpt-4o-mini")
    )
    """Modelo específico para raciocínio/reflexão"""

    # ========================================================================
    # API Keys
    # ========================================================================

    openai_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY")
    )
    """Chave de API da OpenAI"""

    # ========================================================================
    # LangChain Configuration
    # ========================================================================

    langchain_tracing: bool = field(
        default_factory=lambda: os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
    )
    """Ativar tracing do LangChain"""

    langchain_endpoint: Optional[str] = field(
        default_factory=lambda: os.getenv("LANGCHAIN_ENDPOINT")
    )
    """Endpoint do LangSmith"""

    langchain_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("LANGCHAIN_API_KEY")
    )
    """Chave de API do LangSmith"""

    langchain_project: Optional[str] = field(
        default_factory=lambda: os.getenv("LANGCHAIN_PROJECT")
    )
    """Nome do projeto no LangSmith"""

    # ========================================================================
    # Feature Flags
    # ========================================================================

    enable_todos: bool = field(
        default_factory=lambda: os.getenv("AGENTS_ENABLE_TODOS", "false").lower() == "true"
    )
    """Ativar sistema de TODOs"""

    todo_verbose: bool = field(
        default_factory=lambda: os.getenv("AGENTS_TODO_VERBOSE", "false").lower() == "true"
    )
    """Modo verboso para TODOs"""

    disable_context_ai: bool = field(
        default_factory=lambda: os.getenv("AGENTS_DISABLE_CONTEXT_AI", "false").lower() == "true"
    )
    """Desabilitar normalização de contexto via AI"""

    skip_secret_check: bool = field(
        default_factory=lambda: os.getenv("AGENTS_SKIP_SECRET_CHECK", "false").lower() == "true"
    )
    """Pular validação de variáveis secretas (apenas para desenvolvimento)"""

    # ========================================================================
    # Cost Tracking
    # ========================================================================

    zeroum_cost_per_1k_tokens: float = field(
        default_factory=lambda: float(os.getenv("ZEROUM_COST_PER_1K_TOKENS", "0.0"))
    )
    """Custo por 1K tokens para estratégia ZeroUm"""

    llm_cost_per_1k_tokens: float = field(
        default_factory=lambda: float(os.getenv("LLM_COST_PER_1K_TOKENS", "0.0"))
    )
    """Custo por 1K tokens para LLM genérico"""

    # ========================================================================
    # Validation
    # ========================================================================

    def validate(self) -> None:
        """
        Valida as configurações carregadas.

        Raises:
            MissingConfigError: Se configuração obrigatória estiver ausente
            InvalidConfigError: Se configuração tiver valor inválido
        """
        # Validar API Key (se não estiver em modo skip)
        if not self.skip_secret_check and not self.openai_api_key:
            raise MissingConfigError(
                "OPENAI_API_KEY",
                hint="Configure a variável de ambiente ou use AGENTS_SKIP_SECRET_CHECK=true para desenvolvimento",
            )

        # Validar reasoning mode
        valid_modes = ["simple", "reflection"]
        if self.reasoning_mode not in valid_modes:
            raise InvalidConfigError(
                "AGENTS_REASONING_MODE",
                self.reasoning_mode,
                reason=f"Valores válidos: {', '.join(valid_modes)}",
            )

        # Validar temperatura
        if not 0.0 <= self.llm_temperature <= 2.0:
            raise InvalidConfigError(
                "AGENTS_LLM_TEMPERATURE",
                self.llm_temperature,
                reason="Deve estar entre 0.0 e 2.0",
            )

        # Validar configuração do LangChain (se tracing ativado)
        if self.langchain_tracing:
            if not self.langchain_api_key:
                raise MissingConfigError(
                    "LANGCHAIN_API_KEY",
                    hint="Necessário quando LANGCHAIN_TRACING_V2=true",
                )

    def get_langchain_config(self) -> dict:
        """
        Retorna configuração para LangChain.

        Returns:
            Dicionário com configurações do LangChain
        """
        config = {}

        if self.langchain_tracing:
            config["callbacks"] = []  # Callbacks serão adicionados pelo instrumentation

        return config


# Singleton instance
_settings: Optional[Settings] = None


def get_settings(validate: bool = True) -> Settings:
    """
    Retorna a instância singleton das configurações.

    Args:
        validate: Se True, valida as configurações ao carregar

    Returns:
        Instância de Settings configurada

    Raises:
        ValueError: Se validate=True e alguma configuração for inválida
    """
    global _settings

    if _settings is None:
        _settings = Settings()
        if validate:
            _settings.validate()

    return _settings


def reload_settings(validate: bool = True) -> Settings:
    """
    Força o recarregamento das configurações.

    Útil para testes ou quando variáveis de ambiente são alteradas em runtime.

    Args:
        validate: Se True, valida as configurações ao carregar

    Returns:
        Nova instância de Settings configurada
    """
    global _settings
    _settings = None
    return get_settings(validate=validate)
