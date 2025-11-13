# Quick Fix - Autonomous Execution

## Problema Encontrado

Ao tentar executar:
```bash
python agents/scripts/run_autonomous_task.py --task "..." --context "..."
```

**Erro:**
```
TypeError: AgentContext.__init__() missing 1 required positional argument: 'context_description'
```

## ✅ Fix Aplicado

Corrigido em `agents/business/strategies/task_execution/orchestrator.py`:

**Antes:**
```python
self.context = AgentContext(
    context_name=context_name,
    strategy_name="TaskExecution",
    process_code=None,
    base_path=base_path,
    ...
)
```

**Depois:**
```python
self.context = AgentContext(
    context_name=context_name,
    context_description=task_description,  # ✅ ADICIONADO
    strategy_name="TaskExecution",
    process_code=None,
    base_path=base_path,
    ...
)
```

## Como Usar Agora

### Opção 1: Com Virtual Environment (Recomendado)

Se você tem o venv configurado com todas as dependências:

```bash
source agents/.venv/bin/activate
python agents/scripts/run_autonomous_task.py \
  --task "List all Python files in agents/framework/tools" \
  --context "ToolsTest" \
  --max-iterations 5
```

### Opção 2: Teste Direto da Implementação

Criar um script de teste simples:

```python
# test_autonomous.py
from pathlib import Path
from agents.framework.core.context import AgentContext
from agents.framework.orchestration.autonomous import AutonomousAgent

# Criar contexto
context = AgentContext(
    context_name="TestSimple",
    context_description="Test task",
    strategy_name="TaskExecution",
    process_code=None,
    base_path=Path("drive"),
)

# Criar agente
agent = AutonomousAgent(
    context=context,
    task_description="List all Python files in agents/framework/tools directory",
    max_iterations=5,
    enable_recovery=True,
)

# Executar
result = agent.execute()

# Ver resultado
print(f"Success: {result.success}")
print(f"Steps: {len(result.plan.steps) if result.plan else 0}")
for step in (result.plan.steps if result.plan else []):
    print(f"  {step.number}. [{step.status}] {step.description}")
```

Executar:
```bash
source agents/.venv/bin/activate
python test_autonomous.py
```

### Opção 3: Usando Orchestrator Diretamente

```python
# test_orchestrator.py
from pathlib import Path
from agents.business.strategies.task_execution.orchestrator import TaskExecutionOrchestrator

orchestrator = TaskExecutionOrchestrator(
    context_name="TestOrchestrator",
    task_description="List all Python files in agents/framework/tools",
    base_path=Path("drive"),
    max_iterations=5,
)

result = orchestrator.run()

print(f"Success: {result['success']}")
print(f"Complexity: {result['complexity']}")
print(f"Report: {result.get('consolidated')}")
```

## Dependências Necessárias

Para usar o autonomous execution, certifique-se de ter:

```bash
# Entrar no venv
source agents/.venv/bin/activate

# Instalar dependências básicas (se necessário)
pip install langchain langchain-core langchain-openai
pip install openai

# Opcional: deepagents (se framework requer)
pip install "deepagents @ git+https://github.com/langchain-ai/deepagents.git"

# Configurar API key
export OPENAI_API_KEY="sua-api-key"
```

## Verificar Instalação

```bash
python3 -c "
from agents.framework.orchestration.autonomous import AutonomousAgent
from agents.business.strategies.task_execution.orchestrator import TaskExecutionOrchestrator
print('✓ Imports OK')
"
```

Se aparecer `✓ Imports OK`, tudo está funcionando!

## Estrutura de Arquivos Corrigida

```
agents/
├── business/strategies/task_execution/
│   ├── __init__.py
│   └── orchestrator.py  ✅ CORRIGIDO (linha 76)
├── framework/
│   ├── orchestration/
│   │   └── autonomous.py
│   ├── security/
│   │   ├── __init__.py
│   │   └── controls.py
│   └── tools/builtin/
│       └── execution.py
└── scripts/
    └── run_autonomous_task.py

docs/
├── AUTONOMOUS_EXECUTION.md
├── EXECUTION_TOOLS.md
└── SECURITY_CONTROLS.md
```

## Status: ✅ PRONTO

O fix foi aplicado. A implementação está completa e pronta para uso assim que as dependências estiverem instaladas.

**Próximo passo:** Configure o virtual environment e teste!
