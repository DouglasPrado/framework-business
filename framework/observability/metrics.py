"""
Sistema de coleta de métricas para agentes.

Este módulo fornece coleta, armazenamento e reporting de métricas
de execução de agentes (tempo, tokens, custo, etc.).
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from framework.core.protocols import MetricsProvider


# =============================================================================
# Metric Data Classes
# =============================================================================


@dataclass
class Metric:
    """
    Representa uma métrica coletada.

    Attributes:
        name: Nome da métrica
        value: Valor da métrica
        timestamp: Timestamp da coleta
        tags: Tags para categorização
        metadata: Metadados adicionais
    """

    name: str
    value: float
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    tags: Dict[str, str] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Converte métrica para dicionário."""
        return {
            "name": self.name,
            "value": self.value,
            "timestamp": self.timestamp.isoformat(),
            "tags": self.tags,
            "metadata": self.metadata,
        }


@dataclass
class TokenMetrics:
    """
    Métricas específicas de tokens LLM.

    Attributes:
        input_tokens: Tokens de input
        output_tokens: Tokens de output
        total_tokens: Total de tokens
        cost_input: Custo de input
        cost_output: Custo de output
        total_cost: Custo total
    """

    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    cost_input: float = 0.0
    cost_output: float = 0.0
    total_cost: float = 0.0

    def add_usage(
        self,
        input_tokens: int,
        output_tokens: int,
        cost_per_1k_input: float = 0.0,
        cost_per_1k_output: float = 0.0,
    ) -> None:
        """
        Adiciona uso de tokens.

        Args:
            input_tokens: Tokens de input usados
            output_tokens: Tokens de output gerados
            cost_per_1k_input: Custo por 1k tokens de input (USD)
            cost_per_1k_output: Custo por 1k tokens de output (USD)
        """
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.total_tokens = self.input_tokens + self.output_tokens

        # Calcula custos
        self.cost_input += (input_tokens / 1000.0) * cost_per_1k_input
        self.cost_output += (output_tokens / 1000.0) * cost_per_1k_output
        self.total_cost = self.cost_input + self.cost_output

    def to_dict(self) -> Dict[str, Any]:
        """Converte para dicionário."""
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "cost_input": self.cost_input,
            "cost_output": self.cost_output,
            "total_cost": self.total_cost,
        }


# =============================================================================
# Metrics Collector
# =============================================================================


class MetricsCollector:
    """
    Coletor de métricas para execução de agentes.

    Implementa MetricsProvider protocol e fornece funcionalidades
    adicionais para tracking de tempo, tokens e custos.

    Examples:
        >>> collector = MetricsCollector()
        >>> collector.record_metric("execution_time", 5.2, tags={"agent": "process"})
        >>> collector.token_metrics.add_usage(1000, 500, 0.01, 0.03)
        >>> summary = collector.get_summary()
    """

    def __init__(self):
        """Inicializa o coletor de métricas."""
        self.metrics: List[Metric] = []
        self.token_metrics = TokenMetrics()
        self._timers: Dict[str, float] = {}

    def record_metric(
        self,
        name: str,
        value: float,
        tags: Optional[Dict[str, str]] = None,
        **metadata: Any,
    ) -> None:
        """
        Registra uma métrica.

        Args:
            name: Nome da métrica
            value: Valor da métrica
            tags: Tags para categorização (opcional)
            **metadata: Metadados adicionais

        Examples:
            >>> collector.record_metric("latency", 0.5, tags={"endpoint": "/api"})
        """
        metric = Metric(
            name=name,
            value=value,
            tags=tags or {},
            metadata=metadata,
        )
        self.metrics.append(metric)

    def get_metrics(self, name: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retorna métricas registradas.

        Args:
            name: Filtrar por nome (opcional)

        Returns:
            Lista de métricas em formato de dicionário
        """
        if name:
            return [m.to_dict() for m in self.metrics if m.name == name]
        return [m.to_dict() for m in self.metrics]

    def start_timer(self, name: str) -> None:
        """
        Inicia um timer.

        Args:
            name: Nome do timer

        Examples:
            >>> collector.start_timer("process_execution")
            >>> # ... código a medir
            >>> collector.stop_timer("process_execution")
        """
        self._timers[name] = time.time()

    def stop_timer(self, name: str, tags: Optional[Dict[str, str]] = None) -> float:
        """
        Para um timer e registra a métrica.

        Args:
            name: Nome do timer
            tags: Tags adicionais (opcional)

        Returns:
            Tempo decorrido em segundos

        Raises:
            KeyError: Se timer não foi iniciado
        """
        if name not in self._timers:
            raise KeyError(f"Timer '{name}' não foi iniciado")

        elapsed = time.time() - self._timers[name]
        del self._timers[name]

        # Registra métrica de tempo
        self.record_metric(f"{name}_duration", elapsed, tags=tags, unit="seconds")

        return elapsed

    def record_token_usage(
        self,
        input_tokens: int,
        output_tokens: int,
        cost_per_1k_input: float = 0.0,
        cost_per_1k_output: float = 0.0,
        tags: Optional[Dict[str, str]] = None,
    ) -> None:
        """
        Registra uso de tokens.

        Args:
            input_tokens: Tokens de input
            output_tokens: Tokens de output
            cost_per_1k_input: Custo por 1k tokens de input
            cost_per_1k_output: Custo por 1k tokens de output
            tags: Tags adicionais (opcional)

        Examples:
            >>> collector.record_token_usage(1000, 500, 0.01, 0.03)
        """
        # Atualiza métricas de tokens
        self.token_metrics.add_usage(
            input_tokens, output_tokens, cost_per_1k_input, cost_per_1k_output
        )

        # Registra métricas individuais
        metric_tags = tags or {}
        self.record_metric("input_tokens", float(input_tokens), tags=metric_tags)
        self.record_metric("output_tokens", float(output_tokens), tags=metric_tags)
        self.record_metric(
            "token_cost",
            self.token_metrics.total_cost,
            tags=metric_tags,
            currency="USD",
        )

    def get_summary(self) -> Dict[str, Any]:
        """
        Retorna sumário de todas as métricas.

        Returns:
            Dicionário com sumário completo

        Examples:
            >>> summary = collector.get_summary()
            >>> print(f"Total cost: ${summary['tokens']['total_cost']:.4f}")
        """
        return {
            "total_metrics": len(self.metrics),
            "tokens": self.token_metrics.to_dict(),
            "metrics_by_name": self._group_metrics_by_name(),
            "collected_at": datetime.now(timezone.utc).isoformat(),
        }

    def _group_metrics_by_name(self) -> Dict[str, List[float]]:
        """Agrupa métricas por nome."""
        grouped: Dict[str, List[float]] = {}
        for metric in self.metrics:
            if metric.name not in grouped:
                grouped[metric.name] = []
            grouped[metric.name].append(metric.value)
        return grouped

    def reset(self) -> None:
        """Reseta todas as métricas coletadas."""
        self.metrics.clear()
        self.token_metrics = TokenMetrics()
        self._timers.clear()


__all__ = [
    "Metric",
    "TokenMetrics",
    "MetricsCollector",
]
