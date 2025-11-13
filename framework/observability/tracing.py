"""
Sistema de tracing para agentes.

Este módulo integra com LangSmith e outros sistemas de tracing
para observabilidade de execução de agentes.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from framework.config import get_settings

logger = logging.getLogger(__name__)


# =============================================================================
# Tracing Manager
# =============================================================================


class TracingManager:
    """
    Gerenciador de tracing para execução de agentes.

    Integra com LangSmith quando habilitado via configuração.

    Examples:
        >>> tracing = TracingManager()
        >>> if tracing.is_enabled:
        ...     tracing.start_trace("process_execution")
        ...     # ... código
        ...     tracing.end_trace()
    """

    def __init__(self):
        """Inicializa o gerenciador de tracing."""
        self.settings = get_settings(validate=False)
        self._current_trace: Optional[str] = None
        self._trace_stack: List[str] = []

    @property
    def is_enabled(self) -> bool:
        """Verifica se tracing está habilitado."""
        return self.settings.langsmith_tracing

    def start_trace(
        self,
        name: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Inicia um novo trace.

        Args:
            name: Nome do trace
            metadata: Metadados adicionais (opcional)

        Examples:
            >>> tracing.start_trace("agent_execution", {"agent": "process"})
        """
        if not self.is_enabled:
            return

        self._trace_stack.append(name)
        self._current_trace = name

        logger.debug(
            f"Iniciando trace: {name} (nível {len(self._trace_stack)})",
            extra={"trace_metadata": metadata},
        )

    def end_trace(self) -> None:
        """
        Finaliza o trace atual.

        Examples:
            >>> tracing.start_trace("operation")
            >>> # ... código
            >>> tracing.end_trace()
        """
        if not self.is_enabled or not self._trace_stack:
            return

        trace_name = self._trace_stack.pop()
        logger.debug(f"Finalizando trace: {trace_name}")

        self._current_trace = self._trace_stack[-1] if self._trace_stack else None

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Adiciona metadados ao trace atual.

        Args:
            key: Chave do metadado
            value: Valor do metadado

        Examples:
            >>> tracing.add_metadata("tokens_used", 1500)
        """
        if not self.is_enabled or not self._current_trace:
            return

        logger.debug(
            f"Metadado adicionado ao trace {self._current_trace}: {key}={value}"
        )

    def log_event(self, event: str, data: Optional[Dict[str, Any]] = None) -> None:
        """
        Registra um evento no trace atual.

        Args:
            event: Nome do evento
            data: Dados do evento (opcional)

        Examples:
            >>> tracing.log_event("llm_call", {"model": "gpt-4o", "tokens": 1000})
        """
        if not self.is_enabled:
            return

        logger.info(
            f"Evento: {event}",
            extra={
                "trace": self._current_trace,
                "event_data": data,
            },
        )

    def get_config(self) -> Dict[str, Any]:
        """
        Retorna configuração de tracing para LangChain/LangSmith.

        Returns:
            Dicionário com configuração de callbacks

        Examples:
            >>> config = tracing.get_config()
            >>> llm = ChatOpenAI(**config)
        """
        if not self.is_enabled:
            return {}

        # Retorna configuração para LangChain
        return self.settings.get_langchain_config()


__all__ = ["TracingManager"]
