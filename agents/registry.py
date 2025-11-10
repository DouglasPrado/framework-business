"""Registro central dos orquestradores disponíveis."""

from __future__ import annotations

from typing import Callable, Dict

from .base import StrategyAgent
from .generic.orchestrator import GenericStrategyOrchestrator
from .zero_um.orchestrator import ZeroUmOrchestrator

StrategyFactory = Callable[[str, str], StrategyAgent]


def _generic_factory(strategy_name: str) -> StrategyFactory:
    def _factory(context_name: str, context_description: str) -> StrategyAgent:
        return GenericStrategyOrchestrator(
            strategy_name=strategy_name,
            context_name=context_name,
            context_description=context_description,
        )

    return _factory


STRATEGY_REGISTRY: Dict[str, StrategyFactory] = {
    "ZeroUm": lambda context_name, context_description: ZeroUmOrchestrator(
        context_name=context_name,
        context_description=context_description,
    ),
    "Branding": _generic_factory("Branding"),
    "MVPBuilder": _generic_factory("MVPBuilder"),
    "Naming": _generic_factory("Naming"),
}
