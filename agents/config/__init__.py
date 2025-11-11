"""
Módulo de configuração centralizada para o framework de agents.

Este módulo consolida todas as configurações e variáveis de ambiente
utilizadas pelo sistema de agents.
"""

from pathlib import Path

try:
    from dotenv import load_dotenv
    # Carregar .env do diretório agents/
    _agents_dir = Path(__file__).parent.parent
    _env_path = _agents_dir / ".env"
    if _env_path.exists():
        load_dotenv(_env_path)
except ImportError:
    # python-dotenv não instalado, variáveis de ambiente
    # devem ser configuradas manualmente
    pass

from .settings import Settings, get_settings

__all__ = ["Settings", "get_settings"]
