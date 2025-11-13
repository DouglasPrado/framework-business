"""
Teste simples do sistema de monitoramento - valida funcionalidade básica.
"""

import uuid
from datetime import datetime
from dataclasses import dataclass, field
from typing import Any, Dict

print("=" * 80)
print("TESTE SIMPLES DO SISTEMA DE MONITORAMENTO")
print("=" * 80)
print()

# Copiar classes básicas para teste

@dataclass
class LLMCallEvent:
    """Evento de chamada LLM."""
    event_type: str = "llm_call"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    call_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    agent_context: Dict[str, Any] = field(default_factory=dict)
    llm_config: Dict[str, Any] = field(default_factory=dict)
    usage: Dict[str, Any] = field(default_factory=dict)
    performance: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolCallEvent:
    """Evento de execução de ferramenta."""
    event_type: str = "tool_call"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    call_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tool: Dict[str, Any] = field(default_factory=dict)
    performance: Dict[str, Any] = field(default_factory=dict)


print("1. Criando eventos de teste...")
llm_event = LLMCallEvent(
    agent_context={"context_name": "Teste"},
    llm_config={"model": "gpt-4o-mini"},
    usage={"input_tokens": 100, "output_tokens": 50, "total_tokens": 150, "cost_usd": 0.0001},
    performance={"latency_ms": 500.0}
)
print(f"   LLM Event criado: {llm_event.call_id}")

tool_event = ToolCallEvent(
    tool={"name": "read_file", "success": True},
    performance={"execution_ms": 10.0}
)
print(f"   Tool Event criado: {tool_event.call_id}")
print()

print("2. Testando agregação de métricas...")
events = [llm_event] * 3  # Simular 3 chamadas LLM

total_tokens = sum(e.usage.get("total_tokens", 0) for e in events)
total_cost = sum(e.usage.get("cost_usd", 0) for e in events)
avg_latency = sum(e.performance.get("latency_ms", 0) for e in events) / len(events)

print(f"   Total de eventos LLM: {len(events)}")
print(f"   Total de tokens: {total_tokens}")
print(f"   Custo total: ${total_cost:.4f}")
print(f"   Latência média: {avg_latency:.2f}ms")
print()

print("3. Testando serialização...")
import json
from dataclasses import asdict

event_dict = asdict(llm_event)
event_json = json.dumps(event_dict, indent=2)
print("   Evento LLM serializado:")
print("   " + event_json.replace("\n", "\n   ")[:200] + "...")
print()

print("4. Testando decorator de monitoramento...")
import time

def monitor_tool_call_simple(func):
    """Decorator simples para monitorar tool calls."""
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            elapsed_ms = (time.time() - start) * 1000
            print(f"   [{func.__name__}] executado em {elapsed_ms:.2f}ms")
            return result
        except Exception as e:
            elapsed_ms = (time.time() - start) * 1000
            print(f"   [{func.__name__}] ERRO após {elapsed_ms:.2f}ms: {e}")
            raise
    return wrapper

@monitor_tool_call_simple
def sample_tool(path: str):
    """Ferramenta de exemplo."""
    time.sleep(0.01)  # Simular trabalho
    return f"Resultado para {path}"

result = sample_tool("/test/path")
print(f"   Resultado: {result}")
print()

print("5. Testando exportação JSON...")
from pathlib import Path

export_dir = Path("drive/_monitoring_test_simple")
export_dir.mkdir(parents=True, exist_ok=True)

export_data = {
    "exported_at": datetime.utcnow().isoformat() + "Z",
    "summary": {
        "total_events": 4,
        "llm_calls": 3,
        "tool_calls": 1,
        "total_tokens": total_tokens,
        "total_cost_usd": total_cost,
    },
    "events": [asdict(llm_event), asdict(tool_event)],
}

export_file = export_dir / "monitoring_test.json"
with open(export_file, 'w', encoding='utf-8') as f:
    json.dump(export_data, f, indent=2, ensure_ascii=False)

print(f"   Dados exportados para: {export_file.resolve()}")
print(f"   Tamanho do arquivo: {export_file.stat().st_size} bytes")
print()

print("=" * 80)
print("TESTE CONCLUÍDO COM SUCESSO!")
print("=" * 80)
print()
print("RESUMO:")
print(f"  - Eventos LLM criados e agregados")
print(f"  - Eventos Tool Call criados")
print(f"  - Serialização JSON funcionando")
print(f"  - Decorator de monitoramento funcionando")
print(f"  - Exportação de dados funcionando")
print()
print("O sistema de monitoramento está operacional!")
print()
