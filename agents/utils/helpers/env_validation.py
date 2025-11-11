"""Validação de variáveis sensíveis necessárias para execução dos agentes LLM."""

from __future__ import annotations

from agents.config import get_settings
from agents.config.settings import reload_settings
from agents.exceptions import ConfigurationError

SKIP_FLAG = "AGENTS_SKIP_SECRET_CHECK"
TRACE_FLAG = "LANGCHAIN_TRACING_V2"
TRACE_DEPENDENCIES = [
    "LANGCHAIN_ENDPOINT",
    "LANGCHAIN_API_KEY",
    "LANGCHAIN_PROJECT",
]


def validate_sensitive_environment() -> None:
    """
    Garante que as variáveis sensíveis estejam definidas antes de executar agentes LLM.

    Levanta EnvironmentError quando alguma configuração obrigatória estiver ausente.
    O comportamento pode ser ignorado definindo AGENTS_SKIP_SECRET_CHECK=true.
    """
    try:
        # Recarrega configurações para refletir mudanças recentes no ambiente (útil em testes)
        reload_settings(validate=False)
        get_settings(validate=True)
    except ConfigurationError as exc:
        raise EnvironmentError(str(exc)) from exc


__all__ = [
    "SKIP_FLAG",
    "TRACE_FLAG",
    "TRACE_DEPENDENCIES",
    "validate_sensitive_environment",
]
