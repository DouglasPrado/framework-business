# Sistema de Monitoramento de Agentes

Sistema abrangente para monitorar execuções de agentes, chamadas LLM e uso de ferramentas no framework de agentes.

## Visão Geral

O sistema de monitoramento captura automaticamente:
- **Chamadas LLM**: modelo, tokens, latência, custo, ferramentas usadas
- **Execuções de ferramentas**: nome, argumentos, resultados, tempo de execução
- **Execuções de agentes**: duração, métricas agregadas, subagentes executados

## Arquitetura

```
observability/
├── monitoring.py      # Classes base e MonitoringManager
├── callbacks.py       # Integração LangChain
├── exporters.py       # Exportação de dados (JSON, CSV, relatórios)
├── metrics.py         # MetricsCollector (existente)
├── tracing.py         # TracingManager (existente)
└── todos.py           # TODO tracking (existente)
```

## Configuração

### Variáveis de Ambiente

```bash
# Habilitar/desabilitar monitoramento (padrão: true)
AGENTS_MONITORING_ENABLED=true

# Nível de detalhamento (padrão: detailed)
# Opções: basic, detailed, verbose
AGENTS_MONITORING_LEVEL=detailed

# Path customizado para exportação (opcional)
# Padrão: drive/{context}/_monitoring/
AGENTS_MONITORING_EXPORT_PATH=/custom/path
```

### Configuração Programática

```python
from framework.observability.monitoring import MonitoringManager

# Desabilitar monitoramento
MonitoringManager.set_enabled(False)

# Habilitar novamente
MonitoringManager.set_enabled(True)

# Verificar status
is_enabled = MonitoringManager.is_enabled()
```

## Uso Básico

### Monitoramento Automático de LLM

O monitoramento de chamadas LLM é automático quando você usa `build_llm()`:

```python
from framework.llm.factory import build_llm

# O callback de monitoramento é adicionado automaticamente
llm = build_llm({
    "model": "gpt-4o-mini",
    "temperature": 0.4,
    "agent_context": {  # Opcional: contexto para correlação
        "context_name": "MeuProjeto",
        "strategy_name": "ZeroUm",
        "subagent": "problem_hypothesis_express",
    }
})

# Cada invocação é monitorada automaticamente
response = llm.invoke("Qual é o sentido da vida?")
```

### Monitoramento de Ferramentas

Ferramentas já vêm com monitoramento aplicado via decorator:

```python
from framework.observability.monitoring import monitor_tool_call

@monitor_tool_call
def my_custom_tool(arg1: str, arg2: int) -> str:
    """Minha ferramenta customizada."""
    # Execução monitorada automaticamente
    return f"Resultado: {arg1} - {arg2}"
```

### Monitoramento Manual

Para casos customizados, você pode registrar eventos manualmente:

```python
from framework.observability.monitoring import MonitoringManager

mon = MonitoringManager.get_instance()

# Registrar chamada LLM
call_id = mon.record_llm_call(
    agent_context={"context_name": "MeuContexto"},
    llm_config={"model": "gpt-4o-mini", "temperature": 0.4},
    usage={"input_tokens": 100, "output_tokens": 50, "cost_usd": 0.0001},
    performance={"latency_ms": 500.0},
)

# Registrar execução de ferramenta
mon.record_tool_call(
    tool_name="read_file",
    tool_args={"path": "/path/to/file"},
    tool_result="File content...",
    success=True,
    execution_ms=15.0,
)

# Registrar execução de agente
mon.record_agent_execution(
    agent_type="strategy_orchestrator",
    agent_name="ZeroUmOrchestrator",
    context={"context_name": "MeuContexto"},
    execution={"duration_seconds": 120, "status": "completed"},
    metrics={"total_llm_calls": 5, "total_cost_usd": 0.05},
)
```

## Exportação de Dados

### Exportar Tudo (Recomendado)

```python
from framework.observability.exporters import export_all
from pathlib import Path

# Exportar JSON, CSV e relatório resumido
files = export_all(
    base_directory=Path("drive/MeuProjeto/_monitoring"),
    formats=['json', 'csv', 'summary']  # Opcional, padrão: todos
)

print(f"JSON: {files['json']}")
print(f"CSV: {files['csv']}")
print(f"Summary: {files['summary']}")
```

### Exportar Formatos Individuais

```python
from framework.observability.exporters import (
    export_to_json,
    export_to_csv,
    export_summary_report,
)

# JSON estruturado
json_file = export_to_json(
    filepath=Path("monitoring_data.json"),
    pretty=True  # Formato legível
)

# CSVs separados por tipo de evento
csv_files = export_to_csv(
    directory=Path("csv_exports")
)
# Retorna: {'llm_calls': Path, 'tool_calls': Path, 'agent_executions': Path}

# Relatório resumido em texto
summary_file = export_summary_report(
    filepath=Path("summary.txt")
)
```

## Análise de Dados

### Obter Métricas Agregadas

```python
from framework.observability.monitoring import MonitoringManager

mon = MonitoringManager.get_instance()

# Resumo completo
summary = mon.get_metrics_summary()

print(f"Total de eventos: {summary['total_events']}")
print(f"LLM calls: {summary['llm_calls']['count']}")
print(f"Tokens totais: {summary['llm_calls']['total_tokens']}")
print(f"Custo total: ${summary['llm_calls']['total_cost_usd']:.4f}")
print(f"Latência média LLM: {summary['llm_calls']['avg_latency_ms']:.2f}ms")
print(f"Tool calls: {summary['tool_calls']['count']}")
print(f"Tempo médio tool: {summary['tool_calls']['avg_execution_ms']:.2f}ms")

# Top ferramentas mais usadas
for tool_name, count in summary['tool_calls']['tool_usage'].items():
    print(f"  {tool_name}: {count} vezes")
```

### Filtrar Eventos

```python
# Obter apenas eventos LLM
llm_events = mon.get_events("llm_call")

# Obter apenas eventos de tool calls
tool_events = mon.get_events("tool_call")

# Obter apenas eventos de agent executions
agent_events = mon.get_events("agent_execution")

# Obter todos os eventos
all_events = mon.get_events()
```

### Limpar Dados

```python
# Limpar todos os eventos (útil entre sessões)
mon.clear()
```

## Formato dos Dados

### LLM Call Event

```json
{
  "event_type": "llm_call",
  "timestamp": "2025-11-13T10:30:45.123Z",
  "call_id": "uuid",
  "agent_context": {
    "context_name": "MeuProjeto",
    "strategy_name": "ZeroUm",
    "process_code": "00-ProblemHypothesisExpress",
    "subagent": "problem_hypothesis_express"
  },
  "llm_config": {
    "model": "gpt-4o-mini",
    "temperature": 0.4,
    "max_tokens": null
  },
  "usage": {
    "input_tokens": 500,
    "output_tokens": 300,
    "total_tokens": 800,
    "cost_usd": 0.0024
  },
  "performance": {
    "latency_ms": 2345.0,
    "tokens_per_second": 128.0
  },
  "tools": {
    "tools_available": ["ls", "read_file", "write_file"],
    "tools_called": ["read_file"],
    "tool_call_count": 1
  }
}
```

### Tool Call Event

```json
{
  "event_type": "tool_call",
  "timestamp": "2025-11-13T10:30:45.567Z",
  "call_id": "uuid",
  "parent_llm_call_id": "uuid",
  "tool": {
    "name": "write_file",
    "args": {"path": "file.txt", "content": "[TRUNCATED]"},
    "result": "/path/to/file.txt",
    "success": true,
    "error": null
  },
  "performance": {
    "execution_ms": 15.0
  }
}
```

### Agent Execution Event

```json
{
  "event_type": "agent_execution",
  "timestamp": "2025-11-13T10:30:00.000Z",
  "execution_id": "uuid",
  "agent_type": "strategy_orchestrator",
  "agent_name": "ZeroUmOrchestrator",
  "context": {
    "context_name": "MeuProjeto",
    "workspace_root": "/path/to/workspace"
  },
  "execution": {
    "started_at": "2025-11-13T10:30:00.000Z",
    "completed_at": "2025-11-13T10:32:15.000Z",
    "duration_seconds": 135,
    "status": "completed"
  },
  "metrics": {
    "total_llm_calls": 12,
    "total_tool_calls": 8,
    "total_tokens": 15000,
    "total_cost_usd": 0.045
  }
}
```

## Arquivos CSV Exportados

### llm_calls.csv

```
timestamp,call_id,context_name,model,input_tokens,output_tokens,total_tokens,cost_usd,latency_ms
2025-11-13T10:30:45.123Z,uuid,MeuProjeto,gpt-4o-mini,500,300,800,0.0024,2345.0
```

### tool_calls.csv

```
timestamp,call_id,context_name,tool_name,success,execution_ms,error
2025-11-13T10:30:45.567Z,uuid,MeuProjeto,write_file,true,15.0,
```

### agent_executions.csv

```
timestamp,execution_id,agent_type,agent_name,duration_seconds,total_llm_calls,total_cost_usd
2025-11-13T10:30:00.000Z,uuid,strategy_orchestrator,ZeroUmOrchestrator,135,12,0.045
```

## Relatório Resumido (summary.txt)

```
================================================================================
RELATÓRIO DE MONITORAMENTO - AGENTES
================================================================================

Gerado em: 2025-11-13T10:32:00.000Z

RESUMO GERAL
--------------------------------------------------------------------------------
Total de eventos: 25

CHAMADAS LLM
--------------------------------------------------------------------------------
  Quantidade: 12
  Tokens input: 6,000
  Tokens output: 3,500
  Tokens total: 9,500
  Custo total: $0.0285
  Latência média: 1,234.56ms

EXECUÇÕES DE FERRAMENTAS
--------------------------------------------------------------------------------
  Quantidade: 13
  Tempo médio: 12.34ms

  Top 10 ferramentas mais usadas:
    - read_file: 5 vezes
    - write_file: 4 vezes
    - ls: 2 vezes
    - glob: 1 vezes
    - grep: 1 vezes

EXECUÇÕES DE AGENTES
--------------------------------------------------------------------------------
  Quantidade: 1

================================================================================
```

## Casos de Uso

### 1. Debugging de Agentes

```python
# Exportar dados após execução
export_all(Path("drive/Debug/_monitoring"))

# Analisar CSV para identificar gargalos
# - Latências altas em llm_calls.csv
# - Ferramentas lentas em tool_calls.csv
```

### 2. Otimização de Custos

```python
summary = mon.get_metrics_summary()

# Identificar processos caros
for event in mon.get_events("llm_call"):
    if event.usage.get("cost_usd", 0) > 0.01:
        print(f"Call caro: {event.call_id} - ${event.usage['cost_usd']:.4f}")
```

### 3. Análise de Performance

```python
# Identificar chamadas LLM lentas
slow_calls = [
    e for e in mon.get_events("llm_call")
    if e.performance.get("latency_ms", 0) > 5000
]

print(f"Chamadas lentas (>5s): {len(slow_calls)}")
```

### 4. Auditoria de Uso

```python
# Exportar relatório mensal
export_summary_report(Path(f"reports/monitoring_{month}.txt"))

# Analisar uso de ferramentas
summary = mon.get_metrics_summary()
total_tool_calls = summary['tool_calls']['count']
tool_distribution = summary['tool_calls']['tool_usage']
```

## Integração com Orquestradores

Os orquestradores da estratégia ZeroUm já estão integrados:

```python
from business.strategies.zeroum.orchestrator import ZeroUmOrchestrator

# Monitoramento é automático
orchestrator = ZeroUmOrchestrator(
    context_name="MeuProjeto",
    context_description="Descrição do projeto"
)

result = orchestrator.run()

# Exportar dados de monitoramento
from framework.observability.exporters import export_all

export_all(Path(f"drive/{orchestrator.context.context_name}/_monitoring"))
```

## Troubleshooting

### Monitoramento não está capturando eventos

1. Verificar se está habilitado:
   ```python
   MonitoringManager.set_enabled(True)
   ```

2. Verificar se callbacks estão sendo adicionados ao LLM:
   ```python
   # build_llm() adiciona automaticamente se monitoring estiver habilitado
   llm = build_llm({"model": "gpt-4o-mini"})
   ```

### Dados não estão sendo exportados

1. Verificar permissões do diretório
2. Verificar se há eventos registrados:
   ```python
   mon = MonitoringManager.get_instance()
   print(f"Eventos: {len(mon.events)}")
   ```

### Performance degradada

O monitoramento tem overhead mínimo (<5%), mas se necessário:

1. Desabilitar para testes de performance:
   ```python
   MonitoringManager.set_enabled(False)
   ```

2. Usar nível 'basic' em vez de 'detailed':
   ```bash
   AGENTS_MONITORING_LEVEL=basic
   ```

## Roadmap

Futuras melhorias planejadas:

- [ ] Dashboard web interativo
- [ ] Exportação para Prometheus
- [ ] Alertas automáticos (custos, latência)
- [ ] Comparação entre execuções
- [ ] Visualizações gráficas (tempo, custo, tokens)
- [ ] Integração com ferramentas de BI
- [ ] Análise de tendências ao longo do tempo

## Contribuindo

Para adicionar monitoramento em novos componentes:

1. Para ferramentas: adicione decorator `@monitor_tool_call`
2. Para LLMs customizados: passe `agent_context` em `build_llm()`
3. Para eventos customizados: use `mon.record_*()` diretamente

## Licença

Parte do framework-business de agentes.
