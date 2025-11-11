"""
Módulo de configuração centralizada para o framework de agents.

Este módulo consolida todas as configurações e variáveis de ambiente
utilizadas pelo sistema de agents.
"""

from .settings import Settings, get_settings

__all__ = ["Settings", "get_settings"]
