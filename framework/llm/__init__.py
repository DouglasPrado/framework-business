"""
Módulo LLM do framework.

Gerencia a criação, configuração e execução de Large Language Models.
"""

from framework.llm.factory import build_llm, create_llm_with_tracing
from framework.llm.adapters import DeepAgent, create_deep_agent

__all__ = [
    "build_llm",
    "create_llm_with_tracing",
    "DeepAgent",
    "create_deep_agent",
]
