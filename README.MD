# Framework Business - Agent Framework

Framework reutilizável para criação de agentes IA com separação clara entre framework (75%) e lógica de negócio (25%).

## 🚀 Quick Start

```bash
# Da raiz do projeto
cd /Users/douglasprado/www/framework-business

# 1. Instalar
./install.sh

# 2. Ativar ambiente
source agents/.venv/bin/activate

# 3. Executar
python3 agents/scripts/run_strategy_agent.py zeroum MeuProjeto -d "Descrição"
```

## 📦 Estrutura

```
agents/
├── framework/          # Framework reutilizável (75%)
│   ├── core/          # Context, protocols, exceptions, decorators
│   ├── io/            # Workspace, manifest, package
│   ├── llm/           # LLM factory e adapters
│   ├── orchestration/ # Pipeline, graph, registry
│   ├── observability/ # TODOs, metrics, tracing
│   └── tools/         # Tool registry
│
├── business/           # Lógica de negócio (25%)
│   ├── strategies/
│   │   ├── zeroum/    # ZeroUmOrchestrator
│   │   └── generic/   # GenericStrategyOrchestrator
│   └── examples/
│       ├── simple_agent_example.py
│       └── zeroum_example.py
│
├── scripts/
│   └── run_strategy_agent.py  # CLI
│
└── tests/             # Testes
```

## 💻 Uso

### Via CLI

```bash
# Ver ajuda
python3 agents/scripts/run_strategy_agent.py --help

# Executar ZeroUm
python3 agents/scripts/run_strategy_agent.py zeroum MeuProjeto \
  -d "Descrição do projeto"

# Executar Generic
python3 agents/scripts/run_strategy_agent.py generic MeuProjeto \
  -s MinhaEstrategia -d "Descrição"

# Modo silencioso + salvar JSON
python3 agents/scripts/run_strategy_agent.py zeroum Teste \
  -d "Teste" -q -o resultado.json
```

### Via Python

```python
from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator

# Criar orchestrator
orch = ZeroUmOrchestrator(
    context_name="MeuProjeto",
    context_description="Descrição detalhada",
)

# Executar
result = orch.run()

# Resultados
print(f"Consolidado: {result['consolidated']}")
print(f"Archive: {result['archive']}")
print(f"Métricas: {result['metrics']}")
```

### Exemplos

```bash
# Exemplo simples
python3 agents/business/examples/simple_agent_example.py

# Exemplo ZeroUm
python3 agents/business/examples/zeroum_example.py
```

## 🎯 Estratégias Disponíveis

### ZeroUm
Validação de problema e hipótese para novos produtos/serviços.

**Output**:
- Consolidado: `drive/<contexto>/00-consolidado.MD`
- Archive: `drive/<contexto>/<contexto>_ZeroUm_outputs.zip`
- Pipeline: `drive/<contexto>/_pipeline/`

### Generic
Estratégia genérica configurável para casos customizados.

## 📖 Como Criar Novo Agente

```python
from agents.framework.core.context import AgentContext
from agents.framework.io.workspace import WorkspaceManager
from agents.framework.observability import MetricsCollector

# 1. Criar contexto
context = AgentContext(
    context_name="MeuAgente",
    context_description="Descrição",
    strategy_name="MinhaEstrategia",
)

# 2. Usar componentes
workspace = WorkspaceManager(context)
metrics = MetricsCollector()

# 3. Implementar lógica
metrics.start_timer("execution")
workspace.ensure_workspace()
# ... sua lógica ...
elapsed = metrics.stop_timer("execution")
```

Ver [business/examples/simple_agent_example.py](business/examples/simple_agent_example.py) para exemplo completo.

## 🧪 Testes

```bash
# Teste de validação (da raiz)
PYTHONPATH=/Users/douglasprado/www/framework-business \
  python3 test_final_cleanup.py

# Testes unitários (requer pytest)
cd agents
pytest tests/ -v
```

## 🔧 Requisitos

- Python 3.9+
- langchain
- langchain-openai
- langgraph
- openai

## ⚙️ Configuração

Crie `agents/.env`:

```bash
# Obrigatório para usar LLMs
OPENAI_API_KEY=sk-...

# Opcional
AGENTS_LLM_MODEL=gpt-4o-mini
AGENTS_LLM_TEMPERATURE=0.7

# LangSmith (opcional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=framework-business
```

## 📚 Documentação

### Principais Documentos
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Guia completo de migração
- [FACADES_REMOVED.md](FACADES_REMOVED.md) - Remoção de facades
- [LEGACY_REMOVAL_COMPLETE.md](LEGACY_REMOVAL_COMPLETE.md) - Remoção de legacy
- [business/examples/README.md](business/examples/README.md) - Guia de exemplos

### Documentação da Raiz
- [../PROJECT_STATUS.md](../PROJECT_STATUS.md) - Status do projeto
- [../FINAL_STRUCTURE.md](../FINAL_STRUCTURE.md) - Estrutura completa
- [../SCRIPTS_UPDATED.md](../SCRIPTS_UPDATED.md) - Documentação dos scripts

## 🏆 Status

**Versão**: 2.0.0
**Status**: ✅ PRODUÇÃO (LIMPO)
**Testes**: 5/5 passando

- ✅ Zero código deprecated
- ✅ Zero código legado
- ✅ Zero facades
- ✅ 100% framework limpo
- ✅ Documentação completa

## 🎉 O Framework Está Pronto!

O framework está completamente limpo, testado e pronto para uso em produção! 🚀
