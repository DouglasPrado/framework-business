"""Integração oficial com o pacote langchain-ai/deepagents."""

from __future__ import annotations

import logging
from typing import Any, Dict, Iterable, Optional, Sequence

from framework.llm.factory import build_llm

logger = logging.getLogger(__name__)

try:  # pragma: no cover - dependência opcional
    from deepagents import create_deep_agent as _official_create_deep_agent
    from langgraph.graph.state import CompiledStateGraph as DeepAgent
    _DEEPAGENTS_AVAILABLE = True
except ImportError:  # pragma: no cover - ambiente sem dependências
    logger.warning(
        "O pacote 'deepagents' não está instalado. "
        "Funcionalidades de DeepAgent não estarão disponíveis. "
        "Instale com: pip install \"deepagents @ git+https://github.com/langchain-ai/deepagents.git\""
    )
    _official_create_deep_agent = None
    DeepAgent = None  # type: ignore
    _DEEPAGENTS_AVAILABLE = False
except Exception as exc:  # pragma: no cover - erros inesperados ao carregar deepagents
    logger.error("Erro ao inicializar deepagents: %s", exc)
    _official_create_deep_agent = None
    DeepAgent = None  # type: ignore
    _DEEPAGENTS_AVAILABLE = False

__all__ = ["DeepAgent", "create_deep_agent"]


def _prepare_model(llm_config: Optional[Dict[str, Any]], llm_instance: Any) -> Any:
    if llm_instance is not None:
        return llm_instance
    config = dict(llm_config or {})
    try:
        return build_llm(config)
    except Exception as exc:  # pragma: no cover - comunicação direta ao operador
        logger.error("Falha ao construir LLM customizado para deepagents: %s", exc)
        raise RuntimeError(
            "Não foi possível construir o LLM informado em llm_config. "
            "Verifique OPENAI_API_KEY, modelo e dependências instaladas."
        ) from exc


def _prepare_official_tools(tools: Optional[Iterable[Any]]) -> Optional[Sequence[Any]]:
    if not tools:
        return None
    real_tools = [tool for tool in tools if hasattr(tool, "name")]
    return real_tools or None


def create_deep_agent(
    system_prompt: str,
    tools: Optional[Iterable[Any]] = None,
    llm_config: Optional[Dict[str, Any]] = None,
    llm_instance: Any = None,
) -> Any:  # Retorna DeepAgent quando disponível
    """
    Cria um DeepAgent oficial configurado com os utilitários do framework.

    Args:
        system_prompt: Prompt base aplicado ao agente.
        tools: Sequência de ferramentas compatíveis com LangChain.
        llm_config: Configuração opcional para construção do LLM (quando llm_instance não é fornecido).
        llm_instance: Instância pré-criada de LLM (sobrescreve a construção via llm_config).

    Returns:
        Instância compilada de DeepAgent pronta para execução.

    Raises:
        RuntimeError: Se deepagents não estiver instalado
    """
    if not _DEEPAGENTS_AVAILABLE:
        raise RuntimeError(
            "O pacote 'deepagents' não está instalado. "
            "Instale com: pip install \"deepagents @ git+https://github.com/langchain-ai/deepagents.git\""
        )

    model = _prepare_model(llm_config, llm_instance)
    prepared_tools = _prepare_official_tools(tools)

    try:
        return _official_create_deep_agent(
            model=model,
            tools=prepared_tools,
            system_prompt=system_prompt,
        )
    except Exception as exc:  # pragma: no cover - propagado para o operador
        logger.exception("Falha ao instanciar deepagent oficial.")
        raise RuntimeError(
            "Não foi possível instanciar o deepagent oficial. "
            "Revise system_prompt, ferramentas e credenciais do modelo."
        ) from exc
