"""Instrumentação para execução de processos com LangGraph."""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Iterable, List, Optional

try:  # pragma: no cover - fallback para ambientes sem langchain instalado
    from langchain.callbacks.base import BaseCallbackHandler
    from langchain.callbacks.manager import CallbackManager
except ImportError:  # pragma: no cover - fornece stubs mínimos
    class BaseCallbackHandler:  # type: ignore[override]
        """Stub que espelha a interface principal do LangChain."""

        def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:  # noqa: D401
            """Método vazio para compatibilidade."""

        def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:  # type: ignore[override]
            """Método vazio para compatibilidade."""

        def on_chain_error(self, error: BaseException, **kwargs: Any) -> None:  # noqa: D401
            """Método vazio para compatibilidade."""

    class CallbackManager:  # type: ignore[override]
        """Gerenciador mínimo que propaga eventos para callbacks registrados."""

        def __init__(self, callbacks: Iterable[BaseCallbackHandler]) -> None:
            self.callbacks = list(callbacks)

        def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
            for callback in self.callbacks:
                callback.on_chain_start(serialized, inputs, **kwargs)

        def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
            for callback in self.callbacks:
                callback.on_chain_end(outputs, **kwargs)

        def on_chain_error(self, error: BaseException, **kwargs: Any) -> None:
            for callback in self.callbacks:
                callback.on_chain_error(error, **kwargs)
from langgraph.graph import END, StateGraph


@dataclass
class MetricsRecord:
    """Registro individual de execução de um nó."""

    node: str
    status: str
    duration_seconds: float
    tokens: int
    error: Optional[str]
    timestamp: str
    cost: Optional[float] = None


@dataclass
class MetricsSummary:
    """Resumo agregado dos registros coletados."""

    records: List[MetricsRecord] = field(default_factory=list)

    def totals(self) -> Dict[str, Any]:
        total_duration = sum(record.duration_seconds for record in self.records)
        total_tokens = sum(record.tokens for record in self.records)
        total_cost = sum(record.cost or 0.0 for record in self.records)
        return {
            "duracao_total_segundos": total_duration,
            "total_tokens": total_tokens,
            "custo_total": total_cost,
        }

    def as_dict(self) -> Dict[str, Any]:
        return {
            "registros": [record.__dict__ for record in self.records],
            **self.totals(),
        }


class MetricsCollector:
    """Coleta duração e tokens por nó com opção de cálculo de custo."""

    @dataclass
    class _Timer:
        collector: "MetricsCollector"
        node: str
        started_at: float

        def stop(
            self,
            *,
            status: str,
            tokens: int,
            error: Optional[str] = None,
        ) -> None:
            self.collector._register(
                node=self.node,
                status=status,
                started_at=self.started_at,
                tokens=tokens,
                error=error,
            )

    def __init__(
        self,
        *,
        process: str,
        context: str,
        logger: Optional[logging.Logger] = None,
        cost_calculator: Optional[Callable[[int], float]] = None,
    ) -> None:
        self.process = process
        self.context = context
        self.logger = logger or logging.getLogger(__name__)
        self.cost_calculator = cost_calculator
        self._records: List[MetricsRecord] = []

    def start(self, node: str) -> "MetricsCollector._Timer":
        return MetricsCollector._Timer(self, node, time.perf_counter())

    def _register(
        self,
        *,
        node: str,
        status: str,
        started_at: float,
        tokens: int,
        error: Optional[str],
    ) -> None:
        finished = time.perf_counter()
        duration = finished - started_at
        timestamp = datetime.now(timezone.utc).isoformat()
        cost = self.cost_calculator(tokens) if self.cost_calculator else None
        record = MetricsRecord(
            node=node,
            status=status,
            duration_seconds=duration,
            tokens=tokens,
            error=error,
            timestamp=timestamp,
            cost=cost,
        )
        self._records.append(record)
        payload = {
            "evento": "metrics",
            "processo": self.process,
            "contexto": self.context,
            "no": node,
            "status": status,
            "duracao_segundos": duration,
            "tokens": tokens,
            "timestamp": timestamp,
        }
        if error:
            payload["erro"] = error
        if cost is not None:
            payload["custo_estimado"] = cost
        self.logger.info(json.dumps(payload, ensure_ascii=False))

    def summary(self) -> MetricsSummary:
        return MetricsSummary(records=list(self._records))


class GraphCallbackHandler(BaseCallbackHandler):
    """Callback que envia logs estruturados para cada nó do LangGraph."""

    def __init__(
        self,
        *,
        process: str,
        context: str,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        super().__init__()
        self.process = process
        self.context = context
        self.logger = logger or logging.getLogger(__name__)
        self._stack: List[str] = []

    def _emit(self, event: str, node: str, payload: Dict[str, Any]) -> None:
        data = {
            "evento": event,
            "processo": self.process,
            "contexto": self.context,
            "no": node,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "dados": self._sanitize(payload),
        }
        self.logger.info(json.dumps(data, ensure_ascii=False))

    def _sanitize(self, payload: Any, *, max_length: int = 400) -> Any:
        if isinstance(payload, str):
            if len(payload) <= max_length:
                return payload
            return payload[: max_length - 3] + "..."
        if isinstance(payload, dict):
            return {key: self._sanitize(value, max_length=max_length) for key, value in payload.items()}
        if isinstance(payload, (list, tuple)):
            return [self._sanitize(item, max_length=max_length) for item in payload]
        return payload

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
        node = str(serialized.get("name", "no"))
        self._stack.append(node)
        self._emit("node_start", node, {"entradas": inputs})

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        node = self._stack.pop() if self._stack else "desconhecido"
        self._emit("node_end", node, {"saidas": outputs})

    def on_chain_error(self, error: BaseException, **kwargs: Any) -> None:
        node = self._stack.pop() if self._stack else "desconhecido"
        self._emit("node_error", node, {"erro": repr(error)})


@dataclass
class GraphExecutionResult:
    """Resultado final da execução do grafo."""

    state: Dict[str, Any]
    metrics: MetricsSummary

    def as_dict(self) -> Dict[str, Any]:
        return {
            "state": self.state,
            "metrics": self.metrics.as_dict(),
        }


class ProcessGraphRunner:
    """Monta um LangGraph padrão para execução de processos com fallback."""

    def __init__(
        self,
        *,
        process: str,
        context: str,
        metrics_collector: MetricsCollector,
        callback_handlers: Iterable[BaseCallbackHandler],
    ) -> None:
        self.process = process
        self.context = context
        self.metrics_collector = metrics_collector
        self.callback_handlers = list(callback_handlers)

    def _wrap_node(self, name: str, func: Callable[[Dict[str, Any]], Dict[str, Any]]) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
        def wrapped(state: Dict[str, Any]) -> Dict[str, Any]:
            manager = CallbackManager(self.callback_handlers)
            manager.on_chain_start({"name": name}, state)
            timer = self.metrics_collector.start(name)
            try:
                result = func(state)
            except Exception as exc:  # pragma: no cover - proteção defensiva
                manager.on_chain_error(exc)
                timer.stop(status="erro", tokens=0, error=str(exc))
                raise
            status = "sucesso"
            if isinstance(result, dict):
                status = str(result.get("status", status))
            manager.on_chain_end(result)
            tokens = 0
            if isinstance(result, dict) and isinstance(result.get("node_tokens"), int):
                tokens = result["node_tokens"]
            timer.stop(status=status, tokens=tokens, error=result.get("error") if isinstance(result, dict) else None)
            return result

        return wrapped

    def run(
        self,
        *,
        prepare: Callable[[Dict[str, Any]], Dict[str, Any]],
        llm_call: Callable[[Dict[str, Any]], Dict[str, Any]],
        fallback: Callable[[Dict[str, Any]], Dict[str, Any]],
        finalize: Callable[[Dict[str, Any]], Dict[str, Any]],
        route_after_llm: Callable[[Dict[str, Any]], str],
        initial_state: Optional[Dict[str, Any]] = None,
    ) -> GraphExecutionResult:
        graph = StateGraph(dict)
        graph.add_node("preparar", self._wrap_node("preparar", prepare))
        graph.add_node("executar_llm", self._wrap_node("executar_llm", llm_call))
        graph.add_node("fallback_local", self._wrap_node("fallback_local", fallback))
        graph.add_node("finalizar", self._wrap_node("finalizar", finalize))

        graph.set_entry_point("preparar")
        graph.add_edge("preparar", "executar_llm")
        graph.add_conditional_edges(
            "executar_llm",
            route_after_llm,
            {
                "sucesso": "finalizar",
                "fallback": "fallback_local",
            },
        )
        graph.add_edge("fallback_local", "finalizar")
        graph.add_edge("finalizar", END)

        app = graph.compile()
        final_state = app.invoke(initial_state or {})
        return GraphExecutionResult(state=final_state, metrics=self.metrics_collector.summary())


def create_metrics_callbacks(
    *,
    process: str,
    context: str,
    logger: Optional[logging.Logger] = None,
    extra_callbacks: Optional[Iterable[BaseCallbackHandler]] = None,
) -> List[BaseCallbackHandler]:
    """
    Fabrica uma lista de callbacks padrão para instrumentar grafos LangGraph.

    Args:
        process: Código do processo em execução
        context: Nome do contexto (drive/<Contexto>/)
        logger: Logger opcional para reutilização
        extra_callbacks: Callbacks adicionais a serem anexados
    """
    callbacks: List[BaseCallbackHandler] = [
        GraphCallbackHandler(
            process=process,
            context=context,
            logger=logger or logging.getLogger(__name__),
        )
    ]
    if extra_callbacks:
        callbacks.extend(extra_callbacks)
    return callbacks


def run_graph_with_logging(
    *,
    process: str,
    context: str,
    prepare: Callable[[Dict[str, Any]], Dict[str, Any]],
    llm_call: Callable[[Dict[str, Any]], Dict[str, Any]],
    fallback: Callable[[Dict[str, Any]], Dict[str, Any]],
    finalize: Callable[[Dict[str, Any]], Dict[str, Any]],
    route_after_llm: Callable[[Dict[str, Any]], str],
    initial_state: Optional[Dict[str, Any]] = None,
    cost_calculator: Optional[Callable[[int], float]] = None,
    extra_callbacks: Optional[Iterable[BaseCallbackHandler]] = None,
    logger: Optional[logging.Logger] = None,
) -> GraphExecutionResult:
    """
    Executa um grafo LangGraph com callbacks e métricas configurados automaticamente.

    Retorna o estado final e o resumo de métricas coletadas.
    """
    metrics = MetricsCollector(
        process=process,
        context=context,
        logger=logger,
        cost_calculator=cost_calculator,
    )
    callbacks = create_metrics_callbacks(
        process=process,
        context=context,
        logger=logger,
        extra_callbacks=extra_callbacks,
    )
    runner = ProcessGraphRunner(
        process=process,
        context=context,
        metrics_collector=metrics,
        callback_handlers=callbacks,
    )
    return runner.run(
        prepare=prepare,
        llm_call=llm_call,
        fallback=fallback,
        finalize=finalize,
        route_after_llm=route_after_llm,
        initial_state=initial_state,
    )
