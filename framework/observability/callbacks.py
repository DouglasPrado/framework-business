"""
Callbacks LangChain para monitoramento de chamadas LLM.

Integra com o MonitoringManager para capturar automaticamente:
- Início e fim de chamadas LLM
- Tokens e custos
- Latência
- Tool calls realizados
"""

from typing import Any, Dict, List, Optional
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult
from langchain_core.messages import BaseMessage
import time

from .monitoring import MonitoringManager


class MonitoringCallbackHandler(BaseCallbackHandler):
    """
    Callback handler para monitorar chamadas LLM via LangChain.

    Captura automaticamente:
    - Modelo e configurações
    - Prompts de entrada
    - Respostas geradas
    - Tokens e custos
    - Latência
    - Tool calls
    """

    def __init__(self, agent_context: Optional[Dict[str, Any]] = None):
        """
        Args:
            agent_context: Contexto do agente (context_name, strategy_name, etc)
        """
        super().__init__()
        self.agent_context = agent_context or {}
        self._call_start_times: Dict[str, float] = {}
        self._monitoring = MonitoringManager.get_instance()

    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        *,
        run_id: Any,
        parent_run_id: Optional[Any] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """Chamado quando LLM inicia."""
        if not MonitoringManager.is_enabled():
            return

        # Registrar início do timer
        self._call_start_times[str(run_id)] = time.time()

    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: Any,
        parent_run_id: Optional[Any] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """Chamado quando chat model inicia."""
        if not MonitoringManager.is_enabled():
            return

        # Registrar início do timer
        self._call_start_times[str(run_id)] = time.time()

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: Any,
        parent_run_id: Optional[Any] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """Chamado quando LLM termina."""
        if not MonitoringManager.is_enabled():
            return

        run_id_str = str(run_id)

        # Calcular latência
        latency_ms = 0.0
        if run_id_str in self._call_start_times:
            latency_ms = (time.time() - self._call_start_times[run_id_str]) * 1000
            del self._call_start_times[run_id_str]

        # Extrair informações da resposta
        if not response.generations:
            return

        generation = response.generations[0][0]
        output_text = generation.text if hasattr(generation, 'text') else str(generation)

        # Extrair usage metadata (tokens)
        llm_output = response.llm_output or {}
        token_usage = llm_output.get('token_usage', {})

        input_tokens = token_usage.get('prompt_tokens', 0)
        output_tokens = token_usage.get('completion_tokens', 0)
        total_tokens = token_usage.get('total_tokens', input_tokens + output_tokens)

        # Calcular custo (estimativa baseada em modelo)
        model_name = llm_output.get('model_name', 'unknown')
        cost_usd = self._estimate_cost(model_name, input_tokens, output_tokens)

        # Calcular tokens/segundo
        tokens_per_second = 0.0
        if latency_ms > 0:
            tokens_per_second = (output_tokens / latency_ms) * 1000

        # Extrair tool calls se existirem
        tools_available = []
        tools_called = []
        tool_call_count = 0

        if hasattr(generation, 'message'):
            message = generation.message

            # Tools disponíveis (se especificadas no kwargs)
            if 'invocation_params' in kwargs:
                tools_param = kwargs['invocation_params'].get('tools', [])
                tools_available = [t.get('function', {}).get('name', 'unknown') for t in tools_param]

            # Tool calls realizadas
            if hasattr(message, 'tool_calls') and message.tool_calls:
                tools_called = [tc.get('name', 'unknown') for tc in message.tool_calls]
                tool_call_count = len(message.tool_calls)

        # Registrar no MonitoringManager
        self._monitoring.record_llm_call(
            agent_context=self.agent_context,
            llm_config={
                "model": model_name,
                "temperature": llm_output.get('temperature'),
                "max_tokens": llm_output.get('max_tokens'),
            },
            input_data={
                "prompt_length": len(str(kwargs.get('prompts', ['']))),
            },
            output_data={
                "content": output_text[:1000],  # Primeiros 1000 chars
                "content_length": len(output_text),
                "finish_reason": llm_output.get('finish_reason', 'unknown'),
            },
            usage={
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens,
                "cost_usd": cost_usd,
            },
            performance={
                "latency_ms": round(latency_ms, 2),
                "tokens_per_second": round(tokens_per_second, 2),
            },
            tools={
                "tools_available": tools_available,
                "tools_called": tools_called,
                "tool_call_count": tool_call_count,
            }
        )

    def on_llm_error(
        self,
        error: BaseException,
        *,
        run_id: Any,
        parent_run_id: Optional[Any] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """Chamado quando LLM falha."""
        if not MonitoringManager.is_enabled():
            return

        run_id_str = str(run_id)

        # Calcular latência até o erro
        latency_ms = 0.0
        if run_id_str in self._call_start_times:
            latency_ms = (time.time() - self._call_start_times[run_id_str]) * 1000
            del self._call_start_times[run_id_str]

        # Registrar erro
        self._monitoring.record_llm_call(
            agent_context=self.agent_context,
            llm_config={
                "model": "unknown",
            },
            output_data={
                "error": str(error),
                "error_type": type(error).__name__,
            },
            performance={
                "latency_ms": round(latency_ms, 2),
            }
        )

    def _estimate_cost(self, model_name: str, input_tokens: int, output_tokens: int) -> float:
        """
        Estima custo baseado no modelo e tokens.

        Preços aproximados (USD por 1M tokens) - atualizar conforme necessário:
        - gpt-4o: $2.50 input, $10.00 output
        - gpt-4o-mini: $0.15 input, $0.60 output
        - gpt-4-turbo: $10.00 input, $30.00 output
        - gpt-3.5-turbo: $0.50 input, $1.50 output
        """
        pricing = {
            'gpt-4o': (2.50, 10.00),
            'gpt-4o-mini': (0.15, 0.60),
            'gpt-4-turbo': (10.00, 30.00),
            'gpt-4-turbo-preview': (10.00, 30.00),
            'gpt-3.5-turbo': (0.50, 1.50),
            'gpt-3.5-turbo-16k': (3.00, 4.00),
        }

        # Encontrar pricing para o modelo (case insensitive, partial match)
        model_lower = model_name.lower()
        input_cost_per_1m = 0.0
        output_cost_per_1m = 0.0

        for model_key, (in_price, out_price) in pricing.items():
            if model_key in model_lower:
                input_cost_per_1m = in_price
                output_cost_per_1m = out_price
                break

        # Se não encontrou, usar preço default conservador (gpt-4o)
        if input_cost_per_1m == 0.0:
            input_cost_per_1m = 2.50
            output_cost_per_1m = 10.00

        # Calcular custo total
        input_cost = (input_tokens / 1_000_000) * input_cost_per_1m
        output_cost = (output_tokens / 1_000_000) * output_cost_per_1m

        return round(input_cost + output_cost, 6)


def create_monitoring_callback(agent_context: Optional[Dict[str, Any]] = None) -> MonitoringCallbackHandler:
    """
    Factory function para criar callback de monitoramento.

    Args:
        agent_context: Contexto do agente (context_name, strategy_name, process_code, subagent)

    Returns:
        MonitoringCallbackHandler configurado
    """
    return MonitoringCallbackHandler(agent_context=agent_context)
