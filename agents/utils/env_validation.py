"""Validação de variáveis sensíveis necessárias para execução dos agentes LLM."""

from __future__ import annotations

import os
from typing import Iterable


SENSITIVE_ENV_VARS = ("OPENAI_API_KEY",)
TRACE_FLAG = "LANGCHAIN_TRACING_V2"
TRACE_DEPENDENCIES = ("LANGCHAIN_ENDPOINT", "LANGCHAIN_API_KEY", "LANGCHAIN_PROJECT")
SKIP_FLAG = "AGENTS_SKIP_SECRET_CHECK"


def _missing_variables(candidates: Iterable[str]) -> list[str]:
    """Retorna variáveis sem valor (string vazia conta como ausente)."""

    missing = []
    for name in candidates:
        value = os.getenv(name)
        if value is None or value.strip() == "":
            missing.append(name)
    return missing


def _is_truthy(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in {"1", "true", "yes", "on"}


def validate_sensitive_environment() -> None:
    """Garante que as variáveis sensíveis estejam definidas antes de executar agentes LLM.

    Levanta ``EnvironmentError`` quando alguma variável obrigatória estiver ausente. O
    comportamento pode ser ignorado definindo ``AGENTS_SKIP_SECRET_CHECK=1``.
    """

    if _is_truthy(os.getenv(SKIP_FLAG)):
        return

    missing = _missing_variables(SENSITIVE_ENV_VARS)

    trace_flag_value = os.getenv(TRACE_FLAG)
    if trace_flag_value is not None:
        missing.extend(_missing_variables((TRACE_FLAG,)))
        if _is_truthy(trace_flag_value):
            missing.extend(_missing_variables(TRACE_DEPENDENCIES))

    if missing:
        formatted = ", ".join(sorted(set(missing)))
        raise EnvironmentError(
            "Variáveis de ambiente obrigatórias ausentes: "
            f"{formatted}. Configure-as ou exporte {SKIP_FLAG}=1 para executar em modo offline."
        )


__all__ = [
    "SENSITIVE_ENV_VARS",
    "TRACE_DEPENDENCIES",
    "TRACE_FLAG",
    "SKIP_FLAG",
    "validate_sensitive_environment",
]
