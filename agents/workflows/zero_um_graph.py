"""Fluxos orquestrados da estratégia ZeroUm utilizando LangGraph."""

from __future__ import annotations

from typing import Any, Dict, List, TypedDict

from langgraph.graph import END, START, StateGraph

from ..ZeroUm.orchestrator import ZeroUmOrchestrator


class ZeroUmGraphState(TypedDict, total=False):
    """Estado compartilhado entre os nós do LangGraph da estratégia ZeroUm."""

    orchestrator: ZeroUmOrchestrator
    result: Dict[str, Any]
    manifests: List[Dict[str, Any]]
    summary: Dict[str, List[str]]


def build_zero_um_graph(orchestrator: ZeroUmOrchestrator) -> StateGraph[ZeroUmGraphState]:
    """Monta o grafo responsável por executar a estratégia ZeroUm ponta a ponta."""

    graph: StateGraph[ZeroUmGraphState] = StateGraph(ZeroUmGraphState)

    def attach_orchestrator(state: ZeroUmGraphState) -> ZeroUmGraphState:
        return {"orchestrator": orchestrator}

    def execute_strategy(state: ZeroUmGraphState) -> ZeroUmGraphState:
        result = orchestrator.run()
        manifests = result.get("manifests", [])
        return {"result": result, "manifests": manifests}

    def summarize_results(state: ZeroUmGraphState) -> ZeroUmGraphState:
        manifests = state.get("manifests", [])
        completed = [m["process"] for m in manifests if m.get("status") == "completed"]
        pending = [m["process"] for m in manifests if m.get("status") != "completed"]
        summary = {"completed": completed, "pending": pending}
        return {"summary": summary}

    graph.add_node("attach_orchestrator", attach_orchestrator)
    graph.add_node("execute_strategy", execute_strategy)
    graph.add_node("summarize_results", summarize_results)

    graph.add_edge(START, "attach_orchestrator")
    graph.add_edge("attach_orchestrator", "execute_strategy")
    graph.add_edge("execute_strategy", "summarize_results")
    graph.add_edge("summarize_results", END)

    return graph.compile()
