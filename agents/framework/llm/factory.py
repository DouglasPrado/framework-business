"""
Fábrica centralizada de modelos de linguagem para os agentes.

Este módulo fornece funções para criar instâncias de LLM configuradas
com observabilidade, tracing e callbacks.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional

from agents.framework.config import get_settings

try:  # pragma: no cover - dependência opcional
    from langchain_openai import ChatOpenAI
except ImportError:  # pragma: no cover
    ChatOpenAI = None  # type: ignore

try:  # pragma: no cover - fallback para instalações antigas de langchain
    from langchain_community.chat_models import ChatOpenAI as CommunityChatOpenAI
except ImportError:  # pragma: no cover
    CommunityChatOpenAI = None  # type: ignore

try:  # pragma: no cover - tracing opcional
    from langchain.callbacks.tracers.langchain import LangChainTracer
except ImportError:  # pragma: no cover
    LangChainTracer = None  # type: ignore

try:  # pragma: no cover - observabilidade opcional
    from langsmith.callbacks import LangSmithCallbackHandler
except ImportError:  # pragma: no cover
    LangSmithCallbackHandler = None  # type: ignore


def build_llm(config: Optional[Mapping[str, Any]] = None) -> Any:
    """
    Constrói um LLM configurado para uso pelos agentes.

    Args:
        config: Dicionário com parâmetros adicionais. Chaves reconhecidas:
            - provider: backend desejado (apenas "openai" por enquanto)
            - model ou model_name: modelo a ser utilizado
            - temperature: temperatura numérica
            - max_tokens: limite de tokens de saída
            - api_key e base_url: sobrescritas de autenticação
            - observability: configurações para callbacks automáticos
            - callbacks: callbacks adicionais definidos manualmente
            - builder: função customizada para construir LLM

    Returns:
        Instância compatível com LangChain pronta para uso

    Raises:
        ValueError: Se provider não for suportado
        RuntimeError: Se dependências necessárias não estiverem instaladas

    Examples:
        >>> llm = build_llm({"model": "gpt-4o", "temperature": 0.7})
        >>> llm = build_llm({"provider": "openai", "observability": {"langsmith": True}})
    """
    cfg: MutableMapping[str, Any] = dict(config or {})
    provider = str(cfg.get("provider", "openai")).lower()

    if provider not in {"openai", "openai_compat", "openai-compatible"}:
        if callable(cfg.get("builder")):
            return cfg["builder"](cfg)
        raise ValueError(f"Provider '{provider}' não suportado pela build_llm().")

    settings = get_settings(validate=False)
    llm_cls = _resolve_chat_openai()
    params: Dict[str, Any] = {}
    params["model"] = cfg.get("model") or cfg.get("model_name") or settings.llm_model

    temperature = _resolve_temperature(cfg)
    if temperature is not None:
        params["temperature"] = temperature

    if "max_tokens" in cfg and cfg["max_tokens"] is not None:
        params["max_tokens"] = cfg["max_tokens"]

    if "timeout" in cfg and cfg["timeout"] is not None:
        params["timeout"] = cfg["timeout"]

    if cfg.get("api_key"):
        params["api_key"] = cfg["api_key"]
    if cfg.get("base_url"):
        params["base_url"] = cfg["base_url"]
    if cfg.get("default_headers"):
        params["default_headers"] = cfg["default_headers"]

    callbacks = _build_callbacks(cfg)
    if callbacks:
        params["callbacks"] = callbacks

    return llm_cls(**params)


def create_llm_with_tracing(
    model: str,
    temperature: float = 0.7,
    project_name: Optional[str] = None,
    **kwargs: Any,
) -> Any:
    """
    Cria um LLM com tracing habilitado automaticamente.

    Args:
        model: Nome do modelo (ex: "gpt-4o", "gpt-4o-mini")
        temperature: Temperatura para geração (padrão: 0.7)
        project_name: Nome do projeto no LangSmith (opcional)
        **kwargs: Argumentos adicionais para build_llm()

    Returns:
        Instância de LLM com tracing configurado

    Examples:
        >>> llm = create_llm_with_tracing("gpt-4o", temperature=0.5, project_name="MyProject")
    """
    config: Dict[str, Any] = {
        "model": model,
        "temperature": temperature,
        **kwargs,
    }

    # Habilita tracing se configurado
    settings = get_settings(validate=False)
    if settings.langchain_tracing:
        config["observability"] = {
            "langsmith": {
                "project_name": project_name or settings.langchain_project,
            }
        }

    return build_llm(config)


def _resolve_chat_openai():
    """Resolve qual classe ChatOpenAI usar."""
    if ChatOpenAI is not None:
        return ChatOpenAI
    if CommunityChatOpenAI is not None:
        return CommunityChatOpenAI
    raise RuntimeError(
        "Dependência langchain_openai não encontrada. "
        "Instale langchain-openai para usar ChatOpenAI."
    )


def _resolve_temperature(cfg: Mapping[str, Any]) -> Optional[float]:
    """Resolve temperatura a partir de config ou settings."""
    if cfg.get("temperature") is not None:
        return float(cfg["temperature"])
    settings = get_settings(validate=False)
    return settings.llm_temperature


def _build_callbacks(cfg: Mapping[str, Any]) -> List[Any]:
    """Constrói lista de callbacks a partir de configuração."""
    callbacks: List[Any] = []
    user_callbacks = cfg.get("callbacks")
    if isinstance(user_callbacks, Iterable) and not isinstance(
        user_callbacks, (str, bytes)
    ):
        callbacks.extend(list(user_callbacks))

    observability = cfg.get("observability") or {}
    if observability:
        callbacks.extend(_langchain_callbacks(observability))
        callbacks.extend(_langsmith_callbacks(observability))

    return callbacks


def _langchain_callbacks(observability: Mapping[str, Any]) -> List[Any]:
    """Cria callbacks do LangChain Tracer."""
    tracer_cfg = observability.get("langchain_tracer")
    if not tracer_cfg:
        return []
    if LangChainTracer is None:
        raise RuntimeError(
            "LangChainTracer solicitado mas langchain não está "
            "instalado com suporte a tracing."
        )
    if tracer_cfg is True:
        tracer_kwargs: Dict[str, Any] = {}
    elif isinstance(tracer_cfg, Mapping):
        tracer_kwargs = {
            key: tracer_cfg[key]
            for key in ("project_name", "session_name", "client")
            if tracer_cfg.get(key) is not None
        }
    elif isinstance(tracer_cfg, str):
        tracer_kwargs = {"project_name": tracer_cfg}
    else:
        raise TypeError(
            "Configuração de langchain_tracer deve ser bool, str ou mapeamento."
        )
    return [LangChainTracer(**tracer_kwargs)]


def _langsmith_callbacks(observability: Mapping[str, Any]) -> List[Any]:
    """Cria callbacks do LangSmith."""
    smith_cfg = observability.get("langsmith")
    if not smith_cfg:
        return []
    if LangSmithCallbackHandler is None:
        raise RuntimeError(
            "LangSmithCallbackHandler solicitado mas langsmith não está instalado."
        )
    if smith_cfg is True:
        handler_kwargs: Dict[str, Any] = {}
    elif isinstance(smith_cfg, Mapping):
        handler_kwargs = {
            key: smith_cfg[key]
            for key in ("project_name", "tags", "metadata", "client")
            if smith_cfg.get(key) is not None
        }
    else:
        raise TypeError("Configuração de langsmith deve ser bool ou mapeamento.")
    return [LangSmithCallbackHandler(**handler_kwargs)]


__all__ = ["build_llm", "create_llm_with_tracing"]
