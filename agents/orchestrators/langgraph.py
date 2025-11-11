"""Infraestrutura compartilhada para orquestração usando LangGraph."""

from __future__ import annotations

import asyncio
import inspect
from typing import Any, Awaitable, Callable, Dict, Mapping, MutableMapping, TypedDict, cast

from langgraph.graph import END, StateGraph


class OrchestrationState(TypedDict, total=False):
    """Estado compartilhado entre os nós do grafo de orquestração."""

    manifests: list[dict[str, Any]]
    consolidated: str
    archive: str


class OrchestrationHandlers(TypedDict):
    """Handlers esperados pelo grafo de orquestração padrão."""

    coletar_contexto: Callable[[MutableMapping[str, Any]], Any]
    gerar_hipotese: Callable[[MutableMapping[str, Any]], Any]
    validar_resultado: Callable[[MutableMapping[str, Any]], Any]


class OrchestrationGraph:
    """Wrapper conveniente envolvendo um ``StateGraph`` do LangGraph."""

    def __init__(self, handlers: OrchestrationHandlers) -> None:
        self.handlers = handlers
        self._app = self._compile_graph()

    def _compile_graph(self):
        graph: StateGraph[Dict[str, Any]] = StateGraph(dict)
        graph.add_node("coletar_contexto", self._wrap(self.handlers["coletar_contexto"]))
        graph.add_node("gerar_hipotese", self._wrap(self.handlers["gerar_hipotese"]))
        graph.add_node("validar_resultado", self._wrap(self.handlers["validar_resultado"]))

        graph.set_entry_point("coletar_contexto")
        graph.add_edge("coletar_contexto", "gerar_hipotese")
        graph.add_edge("gerar_hipotese", "validar_resultado")
        graph.add_edge("validar_resultado", END)
        return graph.compile()

    def _wrap(self, handler: Callable[[MutableMapping[str, Any]], Any]) -> Callable[[Mapping[str, Any]], Awaitable[Mapping[str, Any]]]:
        async def _invoke(state: Mapping[str, Any]) -> Mapping[str, Any]:
            result = handler(dict(state))
            if inspect.isawaitable(result):
                result = await cast(Awaitable[Mapping[str, Any]], result)
            return self._normalize_result(result)

        return _invoke

    def _normalize_result(self, result: Any) -> Mapping[str, Any]:
        if result is None:
            return {}
        if isinstance(result, Mapping):
            return dict(result)
        raise TypeError(
            "Handlers do grafo devem retornar um mapeamento com as chaves atualizadas."
        )

    async def arun(self, initial_state: OrchestrationState | None = None) -> OrchestrationState:
        state: Dict[str, Any] = dict(initial_state or {})
        final_state = await self._app.ainvoke(state)
        return cast(OrchestrationState, final_state)

    def run(self, initial_state: OrchestrationState | None = None) -> OrchestrationState:
        return asyncio.run(self.arun(initial_state))
