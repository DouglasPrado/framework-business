"""Integração com o pacote oficial langchain-ai/deepagents com fallback local."""

from __future__ import annotations

import logging
from typing import Any, Dict, Iterable, Optional, Sequence

from ..llm_factory import build_llm
from .fallback import (  # type: ignore[F401]
    DeepAgent as _FallbackDeepAgent,
    create_deep_agent as _fallback_create_deep_agent,
)

logger = logging.getLogger(__name__)

try:  # pragma: no cover - dependência opcional
    from deepagents import create_deep_agent as _official_create_deep_agent
    from langgraph.graph.state import CompiledStateGraph as _OfficialDeepAgent
    _IMPORT_ERROR: Optional[Exception] = None
    _OFFICIAL_AVAILABLE = True
except Exception as exc:  # pragma: no cover - ambiente sem dependências
    _official_create_deep_agent = None  # type: ignore[assignment]
    _OfficialDeepAgent = _FallbackDeepAgent  # type: ignore[assignment]
    _IMPORT_ERROR = exc
    _OFFICIAL_AVAILABLE = False

DeepAgent = _OfficialDeepAgent if _OFFICIAL_AVAILABLE else _FallbackDeepAgent
"""Tipo exportado para compatibilidade com os demais módulos."""


def _prepare_model(llm_config: Optional[Dict[str, Any]], llm_instance: Any) -> Any:
    if llm_instance is not None:
        return llm_instance
    config = dict(llm_config or {})
    try:
        return build_llm(config)
    except Exception as exc:  # pragma: no cover - fallback quando build falha
        logger.warning("Falha ao construir LLM customizado. Usando fallback local. Detalhes: %s", exc)
        raise


def _prepare_official_tools(tools: Iterable[Any] | None) -> Sequence[Any] | None:
    if not tools:
        return None
    real_tools = [tool for tool in tools if hasattr(tool, "name")]
    return real_tools or None


def create_deep_agent(
    system_prompt: str,
    tools: Iterable[Any] | None = None,
    llm_config: Optional[Dict[str, Any]] = None,
    llm_instance: Any = None,
) -> DeepAgent:
    """Cria um deep agent usando o pacote oficial quando disponível."""

    # TEMPORÁRIO: Forçar uso do fallback até resolver compatibilidade com deepagents oficial
    # if _OFFICIAL_AVAILABLE and _official_create_deep_agent is not None:
    #     try:
    #         model = _prepare_model(llm_config, llm_instance)
    #     except Exception:
    #         return _fallback_create_deep_agent(
    #             system_prompt=system_prompt,
    #             tools=tools,
    #             llm_config=llm_config,
    #             llm_instance=llm_instance,
    #         )
    #     prepared_tools = _prepare_official_tools(tools)
    #     try:
    #         return _official_create_deep_agent(
    #             model=model,
    #             tools=prepared_tools,
    #             system_prompt=system_prompt,
    #         )
    #     except Exception as exc:  # pragma: no cover - fallback seguro
    #         logger.warning(
    #             "Falha ao instanciar deepagent oficial. Voltando para fallback local. Detalhes: %s",
    #             exc,
    #         )

    if _IMPORT_ERROR:
        logger.debug("Pacote deepagents indisponível. Usando fallback. Motivo: %s", _IMPORT_ERROR)

    return _fallback_create_deep_agent(
        system_prompt=system_prompt,
        tools=tools,
        llm_config=llm_config,
        llm_instance=llm_instance,
    )


__all__ = ["DeepAgent", "create_deep_agent"]
