# Framework de Agentes de IA

Framework reutilizável para criação de agentes de IA que executam processos de negócio.

## 📦 Estrutura

```
framework/
├── core/              # Componentes fundamentais
│   ├── context.py     # AgentContext, RunConfig (objetos de valor)
│   ├── protocols.py   # Interfaces e protocolos
│   ├── exceptions.py  # Hierarquia de exceções
│   └── decorators.py  # Decorators cross-cutting
├── config.py          # Configuração centralizada
├── agents/            # Classes base para agentes
│   └── base.py        # BaseAgent (genérico e reutilizável)
├── io/                # Operações de I/O
│   ├── workspace.py   # WorkspaceManager
│   ├── manifest.py    # ManifestStore
│   └── package.py     # PackageService
├── llm/               # Large Language Models
│   ├── factory.py     # build_llm(), create_llm_with_tracing()
│   └── adapters/      # Integração oficial deepagents + utilidades (state, tools)
├── tools/             # Ferramentas para agentes
│   ├── registry.py    # ToolRegistry, AgentType
│   └── builtin/       # Ferramentas built-in
├── orchestration/     # Pipeline e orquestração
└── observability/     # TODOs, métricas, tracing
```

## 🚀 Uso Rápido

### Core Components

```python
from framework.core import AgentContext, RunConfig

# Criar contexto de execução
ctx = AgentContext(
    context_name="AutomarticlesAutomacao",
    context_description="Automatizar blog com IA",
    strategy_name="ZeroUm",
    process_code="00-ProblemHypothesisExpress"
)

# Criar configuração de execução
config = RunConfig(
    model="gpt-4o",
    temperature=0.7,
    reasoning_mode="reflection",
    tools=["ls", "read", "write"]
)
```

### Workspace Management

```python
from framework.io import WorkspaceManager

# Gerenciar workspace
manager = WorkspaceManager(ctx)
manager.ensure_strategy_folder()
artifact_path = manager.write_artifact(
    folder=ctx.process_root,
    slug="problem-hypothesis",
    content="# Minha Hipótese...",
)
```

### LLM Creation

```python
from framework.llm import build_llm, create_deep_agent

# Criar LLM simples
llm = build_llm({"model": "gpt-4o", "temperature": 0.7})

# Criar agente com ferramentas
agent = create_deep_agent(
    system_prompt="Você é um assistente útil",
    tools=[...],
    llm_config={"model": "gpt-4o"}
)
```

### Tools Registry

```python
from framework.tools import AgentType, get_tools

# Obter ferramentas para um tipo de agente
tools = get_tools(AgentType.PROCESS)
# Retorna: [ls, read, write, glob, grep]
```

### Base Agent

```python
from framework.agents import BaseAgent
from pathlib import Path

# Criar agente customizado
class MyCustomAgent(BaseAgent):
    process_name = "01-MyProcess"
    strategy_name = "MyStrategy"

# Instanciar
agent = MyCustomAgent(
    workspace_root=Path("drive/MyProject"),
    enable_tools=True,
    load_knowledge=True
)

# Usar funcionalidades prontas
agent.setup_directories(["assets", "outputs"])
agent.save_document("result.MD", "# Resultado...")
content = agent.invoke_llm("Analyze this data...")
```

## 🧠 Runtime DeepAgents e Templates

- `agents/framework/llm/adapters/__init__.py` conecta diretamente o framework ao pacote oficial `deepagents`, delegando a execução ao LangGraph (sem fallbacks locais).
- `agents/framework/llm/adapters/tools.py` expõe utilitários como `create_internal_search_tool` e `create_markdown_summary_tool`, prontos para qualquer DeepAgent.
- Os subagentes ZeroUm utilizam `ProcessTemplateFiller` (`agents/business/strategies/zeroum/subagents/template_filler.py`) para preencher automaticamente os modelos de `_DATA`, preservando a estrutura original de `process/<Processo>/_DATA/`.
- Sempre construa o LLM via `build_llm()` ou forneça `llm_instance` ao `create_deep_agent` para manter observabilidade e callbacks configurados.

## 📘 Caso de Uso Completo

Exemplo: executar a estratégia ZeroUm no contexto `MEIFinancialHealth`, usando dois subagentes (`ProblemHypothesisExpress` e `ClientDelivery`) e duas ferramentas internas (`internal_base_search` e `markdown_summarizer`).

1. Configure contexto e workspace com `AgentContext` e `WorkspaceManager`.
2. Prepare as ferramentas oficiais do adapter.
3. Instancie cada subagente apontando para o diretório do drive.
4. Opcionalmente, crie um DeepAgent orquestrador para consolidar o status.

```python
from framework.core import AgentContext
from framework.io import WorkspaceManager
from framework.llm import create_deep_agent
from framework.llm.adapters.tools import (
    create_internal_search_tool,
    create_markdown_summary_tool,
)
from business.strategies.zeroum.subagents.problem_hypothesis_express import (
    ProblemHypothesisExpressAgent,
)
from business.strategies.zeroum.subagents.client_delivery import (
    ClientDeliveryAgent,
)

# 1. Contexto e workspace
ctx = AgentContext(
    context_name="MEIFinancialHealth",
    context_description="Mapear dores e entregar o pacote ZeroUm inicial.",
    strategy_name="ZeroUm",
)
workspace = WorkspaceManager(ctx)
workspace.ensure_workspace()

# 2. Ferramentas compartilhadas
deepagent_tools = [
    create_internal_search_tool(base_path=ctx.base_path),
    create_markdown_summary_tool(max_sentences=3),
]

# 3. Execução dos subagentes
phe_agent = ProblemHypothesisExpressAgent(
    workspace_root=ctx.workspace_root,
    idea_context="Plataforma que ajuda MEIs a acompanhar fluxo de caixa semanal.",
    target_audience="MEIs de serviços financeiros digitais",
)
phe_result = phe_agent.execute_express_session()

delivery_agent = ClientDeliveryAgent(
    workspace_root=ctx.workspace_root,
    client_name="FinHealth Studio",
    delivery_scope="Pacote ZeroUm completo (Problem Hypothesis + Client Delivery)",
    deadline="2024-11-30",
)
delivery_result = delivery_agent.execute_full_delivery()

# 4. DeepAgent orquestrador usando as ferramentas internas
orchestrator_prompt = """
Você supervisiona a estratégia ZeroUm. Leia os manifestos em drive/MEIFinancialHealth
e gere próximos passos em português.
"""
orchestrator = create_deep_agent(
    system_prompt=orchestrator_prompt,
    tools=deepagent_tools,
)
status_report = orchestrator.invoke(
    {
        "input": "Resumo executivo dos processos 00 e 10, destacando riscos e próximos passos."
    }
)
print(status_report)
```

O fluxo cria artefatos numerados em `drive/MEIFinancialHealth/00-ProblemHypothesisExpress/` e `drive/MEIFinancialHealth/10-ClientDelivery/`, preenche os templates originais de `_DATA` via `ProcessTemplateFiller` e mantém o DeepAgent oficial com acesso às ferramentas aprovadas.

## 🔌 Extensibilidade

### Criar um ProcessDefinitionLoader Customizado

```python
from framework.core.protocols import ProcessDefinitionLoader
from pathlib import Path
from typing import Dict, Any

class YAMLProcessLoader(ProcessDefinitionLoader):
    def load(self, path: Path) -> Dict[str, Any]:
        import yaml
        return yaml.safe_load(path.read_text())

    def validate(self, definition: Dict[str, Any]) -> bool:
        return "name" in definition and "steps" in definition
```

### Criar um ArtifactWriter Customizado

```python
from framework.core.protocols import ArtifactWriter
from pathlib import Path
from typing import Dict, Any

class S3ArtifactWriter(ArtifactWriter):
    def write(self, content: str, metadata: Dict[str, Any]) -> Path:
        # Upload para S3
        ...

    def read(self, path: Path) -> str:
        # Download do S3
        ...
```

## 📚 API Reference

### BaseAgent

Classe base genérica e reutilizável para criar agentes e subagentes.

**Attributes (classe)**:

- `process_name` - Nome do processo (ex: "05-CheckoutSetup")
- `strategy_name` - Nome da estratégia (ex: "ZeroUm")

**Constructor Parameters**:

- `workspace_root` - Path do workspace (drive/<Contexto>)
- `process_name` - Sobrescreve o nome do processo da classe (opcional)
- `strategy_name` - Sobrescreve o nome da estratégia da classe (opcional)
- `agent_type` - Tipo do agente para permissões de ferramentas (padrão: PROCESS)
- `enable_tools` - Se True, carrega ferramentas do framework (padrão: True)
- `load_knowledge` - Se True, carrega conhecimento do processo (padrão: True)
- `llm_config` - Configuração customizada do LLM (opcional)

**Properties**:

- `workspace_root` - Path do workspace
- `process_dir` - Path do diretório do processo
- `data_dir` - Path do diretório _DATA
- `process_knowledge` - Conhecimento carregado do processo
- `llm` - Instância do LLM configurado com monitoramento
- `tools` - Lista de ferramentas disponíveis

**Methods**:

- `invoke_llm(prompt, enhance_with_knowledge=True)` - Invoca LLM com prompt enriquecido
- `get_enhanced_prompt(base_prompt)` - Adiciona conhecimento do processo ao prompt
- `setup_directories(additional_dirs=None)` - Cria estrutura de diretórios
- `save_document(filename, content, in_data_dir=False)` - Salva documento no processo
- `read_document(path)` - Lê documento com tratamento de erro
- `format_list(items, separator=", ")` - Formata lista para uso em prompts

**Example**:

```python
from framework.agents import BaseAgent
from pathlib import Path

class MyAgent(BaseAgent):
    process_name = "01-Analysis"
    strategy_name = "DataScience"

agent = MyAgent(workspace_root=Path("drive/Project"))
agent.setup_directories(["outputs", "charts"])

result = agent.invoke_llm("Analyze this data...")
agent.save_document("analysis.MD", result)
```

### AgentContext

Contexto imutável de execução de um agente.

**Attributes**:

- `context_name` - Nome normalizado do contexto
- `context_description` - Descrição detalhada
- `strategy_name` - Nome da estratégia
- `process_code` - Código do processo (opcional)
- `base_path` - Caminho base do repositório

**Properties**:

- `workspace_root` - Path para `drive/<context_name>/`
- `strategy_root` - Path para `drive/<context_name>/<strategy_name>/`
- `process_root` - Path para o processo (se definido)

**Methods**:

- `with_process(code)` - Cria novo contexto com process_code diferente
- `with_metadata(**kwargs)` - Cria novo contexto com metadata adicional

### RunConfig

Configuração imutável de execução de um agente.

**Attributes**:

- `model` - Nome do modelo LLM
- `temperature` - Temperatura para geração (0.0 a 1.0)
- `reasoning_mode` - "simple" ou "reflection"
- `tools` - Lista de nomes de ferramentas
- `enable_todos` - Se deve trackear TODOs
- `enable_tracing` - Se deve habilitar tracing

**Properties**:

- `is_reflection_mode` - True se reasoning_mode == "reflection"
- `is_simple_mode` - True se reasoning_mode == "simple"

**Methods**:

- `with_model(model)` - Cria nova config com modelo diferente
- `with_reasoning_mode(mode)` - Cria nova config com modo diferente
- `with_tools(tools)` - Cria nova config com ferramentas diferentes

## 🔄 Migração de Código Antigo

### Antes (código antigo)

```python
from agents.exceptions import AgentError
from agents.decorators import handle_agent_errors
from agents.config.settings import get_settings
from agents.llm_factory import build_llm
from agents.tools.registry import get_tools
```

> O módulo legado que expunha `create_deep_agent` foi descontinuado; utilize `agents.framework.llm` para todas as integrações atuais.

### Depois (código novo)

```python
from framework.core import AgentError, handle_agent_errors
from framework.config import get_settings
from framework.llm import build_llm, create_deep_agent
from framework.tools import get_tools
```

**Nota**: Os imports antigos continuam funcionando com deprecation warnings.

## 🎯 Progresso da Implementação

- ✅ **Fase 1 (20%)**: Core, Config, IO - **COMPLETA**
- ✅ **Fase 2 (45%)**: LLM, Tools - **COMPLETA**
- ✅ **Fase 3 (65%)**: Orchestration - **COMPLETA**
- ✅ **Fase 4 (75%)**: Observability - **COMPLETA**
- ✅ **Fase 5 (100%)**: Business Migration - **COMPLETA**

## 📝 Licença

Este framework é parte do projeto framework-business.
