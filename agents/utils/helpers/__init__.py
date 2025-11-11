"""
Módulo de utilitários auxiliares gerais.

Contém funções auxiliares diversas, como normalização de contexto
e validação de ambiente.
"""

from .context import normalize_context_name
from .env_validation import validate_sensitive_environment

__all__ = [
    "normalize_context_name",
    "validate_sensitive_environment",
]
