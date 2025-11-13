"""
Adapter para LangGraph (infraestrutura de orquestração baseada em grafos).

Este módulo fornece uma camada de abstração sobre LangGraph,
facilitando a criação de workflows baseados em estado.
"""

from __future__ import annotations

import asyncio
import inspect
from typing import Any, Awaitable, Callable, Dict, Mapping, MutableMapping, TypedDict, cast, Optional

# Import condicional do LangGraph
try:
    from langgraph.graph import END, StateGraph
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False
    StateGraph = None  # type: ignore
    END = None  # type: ignore


# =============================================================================
# State Types
# =============================================================================


class OrchestrationState(TypedDict, total=False):
    """
    Estado compartilhado entre os nós do grafo de orquestração.

    Attributes:
        manifests: Lista de manifestos gerados
        consolidated: Relatório consolidado
        archive: Path do arquivo de artefatos
    """

    manifests: list[dict[str, Any]]
    consolidated: str
    archive: str


class OrchestrationHandlers(TypedDict):
    """
    Handlers esperados pelo grafo de orquestração padrão.

    Attributes:
        coletar_contexto: Handler para coleta de contexto
        gerar_hipotese: Handler para geração de hipótese
        validar_resultado: Handler para validação
    """

    coletar_contexto: Callable[[MutableMapping[str, Any]], Any]
    gerar_hipotese: Callable[[MutableMapping[str, Any]], Any]
    validar_resultado: Callable[[MutableMapping[str, Any]], Any]


# =============================================================================
# LangGraph Orchestration
# =============================================================================


class LangGraphOrchestration:
    """
    Wrapper para StateGraph do LangGraph.

    Fornece uma interface conveniente para criar e executar
    workflows baseados em estado usando LangGraph.

    Examples:
        >>> handlers = {
        ...     "coletar_contexto": collect_handler,
        ...     "gerar_hipotese": generate_handler,
        ...     "validar_resultado": validate_handler,
        ... }
        >>> graph = LangGraphOrchestration(handlers)
        >>> result = graph.run()
    """

    def __init__(self, handlers: OrchestrationHandlers) -> None:
        """
        Inicializa o grafo de orquestração.

        Args:
            handlers: Dicionário com handlers para cada nó

        Raises:
            ImportError: Se LangGraph não estiver instalado
        """
        if not LANGGRAPH_AVAILABLE:
            raise ImportError(
                "LangGraph não está instalado. "
                "Instale com: pip install langgraph"
            )

        self.handlers = handlers
        self._app = self._compile_graph()

    def _compile_graph(self):
        """Compila o grafo de orquestração."""
        graph: StateGraph[Dict[str, Any]] = StateGraph(dict)

        # Adiciona nós
        graph.add_node("coletar_contexto", self._wrap(self.handlers["coletar_contexto"]))
        graph.add_node("gerar_hipotese", self._wrap(self.handlers["gerar_hipotese"]))
        graph.add_node("validar_resultado", self._wrap(self.handlers["validar_resultado"]))

        # Define fluxo
        graph.set_entry_point("coletar_contexto")
        graph.add_edge("coletar_contexto", "gerar_hipotese")
        graph.add_edge("gerar_hipotese", "validar_resultado")
        graph.add_edge("validar_resultado", END)

        return graph.compile()

    def _wrap(
        self, handler: Callable[[MutableMapping[str, Any]], Any]
    ) -> Callable[[Mapping[str, Any]], Awaitable[Mapping[str, Any]]]:
        """
        Wrapper para handlers síncronos/assíncronos.

        Args:
            handler: Handler a ser encapsulado

        Returns:
            Handler async compatível com LangGraph
        """

        async def _invoke(state: Mapping[str, Any]) -> Mapping[str, Any]:
            result = handler(dict(state))
            if inspect.isawaitable(result):
                result = await cast(Awaitable[Mapping[str, Any]], result)
            return self._normalize_result(result)

        return _invoke

    def _normalize_result(self, result: Any) -> Mapping[str, Any]:
        """
        Normaliza resultado de handler para dicionário.

        Args:
            result: Resultado do handler

        Returns:
            Dicionário normalizado

        Raises:
            TypeError: Se resultado não for mapeamento válido
        """
        if result is None:
            return {}
        if isinstance(result, Mapping):
            return dict(result)
        raise TypeError(
            "Handlers do grafo devem retornar um mapeamento com as chaves atualizadas."
        )

    async def arun(
        self, initial_state: Optional[OrchestrationState] = None
    ) -> OrchestrationState:
        """
        Executa o grafo de forma assíncrona.

        Args:
            initial_state: Estado inicial (opcional)

        Returns:
            Estado final após execução

        Examples:
            >>> result = await graph.arun({"input": "data"})
        """
        state: Dict[str, Any] = dict(initial_state or {})
        final_state = await self._app.ainvoke(state)
        return cast(OrchestrationState, final_state)

    def run(
        self, initial_state: Optional[OrchestrationState] = None
    ) -> OrchestrationState:
        """
        Executa o grafo de forma síncrona.

        Args:
            initial_state: Estado inicial (opcional)

        Returns:
            Estado final após execução

        Examples:
            >>> result = graph.run({"input": "data"})
        """
        return asyncio.run(self.arun(initial_state))


# =============================================================================
# Convenience Functions
# =============================================================================


def create_orchestration_graph(
    handlers: OrchestrationHandlers,
) -> LangGraphOrchestration:
    """
    Factory para criar grafo de orquestração.

    Args:
        handlers: Handlers para cada nó do grafo

    Returns:
        LangGraphOrchestration configurado

    Examples:
        >>> graph = create_orchestration_graph(handlers)
        >>> result = graph.run()
    """
    return LangGraphOrchestration(handlers)


__all__ = [
    "OrchestrationState",
    "OrchestrationHandlers",
    "LangGraphOrchestration",
    "create_orchestration_graph",
]
