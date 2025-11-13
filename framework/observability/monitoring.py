"""
Sistema central de monitoramento para o framework de agentes.

Captura e armazena eventos de:
- Chamadas LLM (modelo, tokens, latência, custo)
- Execuções de ferramentas (nome, args, resultado, tempo)
- Execuções de agentes (duração, métricas agregadas)
"""

import time
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional
from pathlib import Path
import json
from contextlib import contextmanager


@dataclass
class LLMCallEvent:
    """Evento de chamada LLM."""
    event_type: str = "llm_call"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    call_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    # Contexto do agente
    agent_context: Dict[str, Any] = field(default_factory=dict)

    # Configuração do LLM
    llm_config: Dict[str, Any] = field(default_factory=dict)

    # Input
    input_data: Dict[str, Any] = field(default_factory=dict)

    # Output
    output_data: Dict[str, Any] = field(default_factory=dict)

    # Usage (tokens e custo)
    usage: Dict[str, Any] = field(default_factory=dict)

    # Performance
    performance: Dict[str, Any] = field(default_factory=dict)

    # Tools
    tools: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolCallEvent:
    """Evento de execução de ferramenta."""
    event_type: str = "tool_call"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    call_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    parent_llm_call_id: Optional[str] = None

    # Contexto do agente
    agent_context: Dict[str, Any] = field(default_factory=dict)

    # Tool info
    tool: Dict[str, Any] = field(default_factory=dict)

    # Performance
    performance: Dict[str, Any] = field(default_factory=dict)

    # Security
    security: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentExecutionEvent:
    """Evento de execução de agente."""
    event_type: str = "agent_execution"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    execution_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    agent_type: str = ""
    agent_name: str = ""

    # Contexto
    context: Dict[str, Any] = field(default_factory=dict)

    # Execution info
    execution: Dict[str, Any] = field(default_factory=dict)

    # Subagents (para orchestrators)
    subagents_executed: List[Dict[str, Any]] = field(default_factory=list)

    # Métricas agregadas
    metrics: Dict[str, Any] = field(default_factory=dict)


class MonitoringManager:
    """
    Gerenciador central de monitoramento.

    Responsável por:
    - Coletar eventos de LLM calls, tool calls e agent executions
    - Agregar métricas por contexto/sessão
    - Persistir dados para análise posterior
    """

    _instance: Optional['MonitoringManager'] = None
    _enabled: bool = True

    def __init__(self):
        self.events: List[Any] = []
        self.current_llm_call_id: Optional[str] = None
        self.current_agent_execution_id: Optional[str] = None
        self._start_times: Dict[str, float] = {}

    @classmethod
    def get_instance(cls) -> 'MonitoringManager':
        """Retorna singleton instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def set_enabled(cls, enabled: bool):
        """Habilita ou desabilita monitoramento globalmente."""
        cls._enabled = enabled

    @classmethod
    def is_enabled(cls) -> bool:
        """Verifica se monitoramento está habilitado."""
        return cls._enabled

    def record_llm_call(
        self,
        agent_context: Optional[Dict[str, Any]] = None,
        llm_config: Optional[Dict[str, Any]] = None,
        input_data: Optional[Dict[str, Any]] = None,
        output_data: Optional[Dict[str, Any]] = None,
        usage: Optional[Dict[str, Any]] = None,
        performance: Optional[Dict[str, Any]] = None,
        tools: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Registra uma chamada LLM.

        Returns:
            call_id para correlação com tool calls
        """
        if not self._enabled:
            return ""

        event = LLMCallEvent(
            agent_context=agent_context or {},
            llm_config=llm_config or {},
            input_data=input_data or {},
            output_data=output_data or {},
            usage=usage or {},
            performance=performance or {},
            tools=tools or {},
        )

        self.events.append(event)
        self.current_llm_call_id = event.call_id
        return event.call_id

    def record_tool_call(
        self,
        tool_name: str,
        tool_args: Optional[Dict[str, Any]] = None,
        tool_result: Any = None,
        success: bool = True,
        error: Optional[str] = None,
        execution_ms: Optional[float] = None,
        agent_context: Optional[Dict[str, Any]] = None,
        security_info: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Registra uma execução de ferramenta.

        Returns:
            call_id do evento
        """
        if not self._enabled:
            return ""

        # Sanitizar argumentos (truncar conteúdos grandes)
        sanitized_args = self._sanitize_args(tool_args or {})

        # Sanitizar resultado
        sanitized_result = self._sanitize_result(tool_result)

        event = ToolCallEvent(
            parent_llm_call_id=self.current_llm_call_id,
            agent_context=agent_context or {},
            tool={
                "name": tool_name,
                "args": sanitized_args,
                "result": sanitized_result,
                "success": success,
                "error": error,
            },
            performance={
                "execution_ms": execution_ms,
            },
            security=security_info or {},
        )

        self.events.append(event)
        return event.call_id

    def record_agent_execution(
        self,
        agent_type: str,
        agent_name: str,
        context: Optional[Dict[str, Any]] = None,
        execution: Optional[Dict[str, Any]] = None,
        subagents_executed: Optional[List[Dict[str, Any]]] = None,
        metrics: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Registra uma execução de agente.

        Returns:
            execution_id
        """
        if not self._enabled:
            return ""

        event = AgentExecutionEvent(
            agent_type=agent_type,
            agent_name=agent_name,
            context=context or {},
            execution=execution or {},
            subagents_executed=subagents_executed or [],
            metrics=metrics or {},
        )

        self.events.append(event)
        self.current_agent_execution_id = event.execution_id
        return event.execution_id

    @contextmanager
    def track_llm_call(self, call_id: str):
        """Context manager para rastrear uma chamada LLM."""
        old_call_id = self.current_llm_call_id
        self.current_llm_call_id = call_id
        try:
            yield
        finally:
            self.current_llm_call_id = old_call_id

    @contextmanager
    def track_agent_execution(self, execution_id: str):
        """Context manager para rastrear uma execução de agente."""
        old_execution_id = self.current_agent_execution_id
        self.current_agent_execution_id = execution_id
        try:
            yield
        finally:
            self.current_agent_execution_id = old_execution_id

    def start_timer(self, timer_id: str):
        """Inicia um timer."""
        self._start_times[timer_id] = time.time()

    def stop_timer(self, timer_id: str) -> float:
        """Para um timer e retorna o tempo decorrido em ms."""
        if timer_id not in self._start_times:
            return 0.0

        elapsed = (time.time() - self._start_times[timer_id]) * 1000
        del self._start_times[timer_id]
        return elapsed

    def get_events(self, event_type: Optional[str] = None) -> List[Any]:
        """
        Retorna eventos registrados.

        Args:
            event_type: Filtrar por tipo (llm_call, tool_call, agent_execution)
        """
        if event_type:
            return [e for e in self.events if e.event_type == event_type]
        return self.events

    def get_metrics_summary(self) -> Dict[str, Any]:
        """
        Retorna resumo de métricas agregadas.
        """
        llm_calls = [e for e in self.events if e.event_type == "llm_call"]
        tool_calls = [e for e in self.events if e.event_type == "tool_call"]
        agent_executions = [e for e in self.events if e.event_type == "agent_execution"]

        # Agregar tokens e custos
        total_input_tokens = sum(e.usage.get("input_tokens", 0) for e in llm_calls)
        total_output_tokens = sum(e.usage.get("output_tokens", 0) for e in llm_calls)
        total_tokens = sum(e.usage.get("total_tokens", 0) for e in llm_calls)
        total_cost = sum(e.usage.get("cost_usd", 0) for e in llm_calls)

        # Agregar latências
        llm_latencies = [e.performance.get("latency_ms", 0) for e in llm_calls if e.performance.get("latency_ms")]
        avg_llm_latency = sum(llm_latencies) / len(llm_latencies) if llm_latencies else 0

        tool_latencies = [e.performance.get("execution_ms", 0) for e in tool_calls if e.performance.get("execution_ms")]
        avg_tool_latency = sum(tool_latencies) / len(tool_latencies) if tool_latencies else 0

        # Top tools usadas
        tool_usage = {}
        for e in tool_calls:
            tool_name = e.tool.get("name", "unknown")
            tool_usage[tool_name] = tool_usage.get(tool_name, 0) + 1

        return {
            "total_events": len(self.events),
            "llm_calls": {
                "count": len(llm_calls),
                "total_input_tokens": total_input_tokens,
                "total_output_tokens": total_output_tokens,
                "total_tokens": total_tokens,
                "total_cost_usd": round(total_cost, 4),
                "avg_latency_ms": round(avg_llm_latency, 2),
            },
            "tool_calls": {
                "count": len(tool_calls),
                "avg_execution_ms": round(avg_tool_latency, 2),
                "tool_usage": tool_usage,
            },
            "agent_executions": {
                "count": len(agent_executions),
            }
        }

    def clear(self):
        """Limpa todos os eventos registrados."""
        self.events.clear()
        self.current_llm_call_id = None
        self.current_agent_execution_id = None
        self._start_times.clear()

    def export_to_json(self, filepath: Path):
        """
        Exporta eventos para arquivo JSON.
        """
        filepath.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "exported_at": datetime.utcnow().isoformat() + "Z",
            "summary": self.get_metrics_summary(),
            "events": [asdict(e) for e in self.events],
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _sanitize_args(self, args: Dict[str, Any], max_length: int = 500) -> Dict[str, Any]:
        """Sanitiza argumentos, truncando valores grandes."""
        sanitized = {}
        for key, value in args.items():
            if isinstance(value, str) and len(value) > max_length:
                sanitized[key] = value[:max_length] + f"... [TRUNCATED {len(value) - max_length} chars]"
            else:
                sanitized[key] = value
        return sanitized

    def _sanitize_result(self, result: Any, max_length: int = 1000) -> Any:
        """Sanitiza resultado, truncando se necessário."""
        if isinstance(result, str) and len(result) > max_length:
            return result[:max_length] + f"... [TRUNCATED {len(result) - max_length} chars]"
        return result


# Instância global (singleton)
monitoring = MonitoringManager.get_instance()


def monitor_tool_call(func):
    """
    Decorator para monitorar execução de ferramentas.

    Usage:
        @monitor_tool_call
        def my_tool(arg1, arg2):
            return result
    """
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not MonitoringManager.is_enabled():
            return func(*args, **kwargs)

        mon = MonitoringManager.get_instance()
        tool_name = func.__name__

        # Combinar args e kwargs para logging
        import inspect
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        tool_args = dict(bound_args.arguments)

        # Iniciar timer
        timer_id = f"tool_{tool_name}_{uuid.uuid4()}"
        mon.start_timer(timer_id)

        success = True
        error = None
        result = None

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            success = False
            error = str(e)
            raise
        finally:
            execution_ms = mon.stop_timer(timer_id)

            mon.record_tool_call(
                tool_name=tool_name,
                tool_args=tool_args,
                tool_result=result,
                success=success,
                error=error,
                execution_ms=execution_ms,
            )

    return wrapper
