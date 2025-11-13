# Exemplos de Uso do Framework

Este diretório contém exemplos práticos de como usar o framework de agentes.

## Exemplos Disponíveis

### 1. Simple Agent Example (`simple_agent_example.py`)

Demonstra como criar um agente customizado do zero usando apenas os componentes do framework.

**Componentes utilizados:**

- `AgentContext`: Contexto imutável de execução
- `WorkspaceManager`: Gerenciamento de workspace e artefatos
- `ManifestStore`: Armazenamento de manifestos
- `MetricsCollector`: Coleta de métricas de execução
- `TodoManager`: Gerenciamento de tarefas
- `TracingManager`: Tracing para observabilidade
- `build_llm()`: Factory para criação de LLMs

**Como executar:**

```bash
cd agents
python3 -m business.examples.simple_agent_example
```

**O que o exemplo faz:**

1. Cria um agente customizado sem regras de negócio
2. Prepara workspace automaticamente
3. Processa contexto usando LLM
4. Gera artefatos no formato markdown
5. Publica manifesto com métricas
6. Registra TODOs para tracking

## Estrutura Básica de um Agente

Todo agente construído com o framework segue esta estrutura:

```python
from pathlib import Path
from typing import Optional, Dict, Any

from framework.core.context import AgentContext, RunConfig
from framework.io.workspace import WorkspaceManager
from framework.observability import MetricsCollector

class MeuAgente:
    def __init__(
        self,
        context_name: str,
        context_description: str = "",
        base_path: Optional[Path] = None,
    ):
        # 1. Criar contexto imutável
        self.context = AgentContext(
            context_name=context_name,
            context_description=context_description,
            strategy_name="MinhaEstrategia",
            base_path=base_path,
        )

        # 2. Inicializar componentes do framework
        self.workspace = WorkspaceManager(self.context)
        self.metrics = MetricsCollector()

    def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
        # 3. Implementar lógica do agente
        self.metrics.start_timer("execution")

        # ... sua lógica aqui ...

        elapsed = self.metrics.stop_timer("execution")
        return {"status": "success", "execution_time": elapsed}
```

## Componentes do Framework

### Core (`agents.framework.core`)

**AgentContext**

- Contexto imutável de execução
- Propriedades: `context_name`, `strategy_name`, `workspace_root`, `pipeline_dir`

**RunConfig**

- Configuração imutável de execução
- Opções: `max_retries`, `timeout`, `verbose`

**Decorators**

- `@handle_agent_errors`: Tratamento automático de erros
- `@log_execution`: Logging automático de execução
- `@retry_on_failure`: Retry automático em caso de falha

### I/O (`agents.framework.io`)

**WorkspaceManager**

- `ensure_workspace()`: Garante que workspace existe
- `write_artifact()`: Escreve artefato com nome sequencial
- `list_artifacts()`: Lista artefatos no workspace

**ManifestStore**

- `write(name, data)`: Salva manifesto
- `read(name)`: Lê manifesto
- `from_context(context)`: Factory method

**PackageService**

- `create_archive()`: Empacota workspace em ZIP

### Observability (`agents.framework.observability`)

**MetricsCollector**

- `start_timer(name)`: Inicia timer
- `stop_timer(name)`: Para timer e registra métrica
- `record_token_usage()`: Registra uso de tokens
- `get_summary()`: Retorna resumo de métricas

**TodoManager**

- `add_todo(task, status)`: Adiciona TODO
- `update_status(id, status)`: Atualiza status
- `mark_completed(id)`: Marca como completado
- `get_summary()`: Retorna resumo

**TracingManager**

- `start_trace(name)`: Inicia trace
- `end_trace()`: Finaliza trace
- `add_metadata(key, value)`: Adiciona metadados

### Orchestration (`agents.framework.orchestration`)

**ProcessPipeline**

- Pipeline flexível com estágios configuráveis
- `run(context, config)`: Executa pipeline

**OrchestrationGraph**

- Grafo de orquestração com handlers
- `from_handlers(handlers)`: Factory method
- `execute(initial_state)`: Executa grafo

**PluginRegistry**

- Registro dinâmico de plugins
- `register(name, plugin)`: Registra plugin
- `discover_plugins()`: Descobre via entrypoints

## Boas Práticas

### 1. Use AgentContext para configuração

```python
# ✅ Correto - contexto imutável
context = AgentContext(
    context_name="MeuContexto",
    strategy_name="MinhaEstrategia",
)

# ❌ Evite - configuração mutável
config = {
    "context_name": "MeuContexto",
    "strategy_name": "MinhaEstrategia",
}
```

### 2. Sempre registre métricas

```python
# ✅ Correto - com métricas
self.metrics.start_timer("processing")
result = self.process()
self.metrics.stop_timer("processing")

# ❌ Evite - sem métricas
result = self.process()
```

### 3. Use decorators para cross-cutting concerns

```python
# ✅ Correto - com decorators
@handle_agent_errors
@log_execution
def run(self):
    return self.process()

# ❌ Evite - tratamento manual em cada método
def run(self):
    try:
        logger.info("Starting...")
        return self.process()
    except Exception as e:
        logger.error(f"Error: {e}")
        raise
```

### 4. Aproveite TodoManager para tracking

```python
# ✅ Correto - com TODOs
self.todo_manager.add_todo("Processar dados", status="pending")
self.todo_manager.update_status("todo-001", "in_progress")
result = self.process()
self.todo_manager.mark_completed("todo-001")

# ❌ Evite - sem tracking
result = self.process()
```

## Próximos Passos

1. Explore o código dos exemplos
2. Adapte para seu caso de uso
3. Consulte a documentação de cada componente em `agents/framework/`
4. Veja estratégias reais em `agents/business/strategies/`

## Suporte

Para dúvidas ou problemas:

1. Consulte a documentação em `agents/framework/`
2. Veja outros exemplos em `agents/business/strategies/`
3. Revise os testes em `tests/`
