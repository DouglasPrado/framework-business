# Framework Business - Guia Completo para Agentes de IA

## Visão Geral

Este documento fornece instruções completas para agentes de IA (como Claude, ChatGPT ou outros LLMs) trabalhando com o **Framework Business**, um sistema para criação de agentes de IA que executam processos de negócio.

## Arquitetura do Projeto

O projeto está organizado em duas camadas principais:

```
framework-business/
├── framework/           # 75% - Infraestrutura reutilizável
│   ├── core/           # Abstrações fundamentais
│   ├── llm/            # Integração com LLMs
│   ├── tools/          # Sistema de ferramentas
│   ├── orchestration/  # Orquestração de execução
│   ├── observability/  # Monitoramento e métricas
│   ├── io/             # Entrada/saída (workspace, arquivos)
│   └── config.py       # Configuração global
│
├── business/           # 25% - Lógica de negócio
│   └── strategies/     # Estratégias específicas
│       ├── zeroum/     # Estratégia ZeroUm (validação de hipóteses)
│       ├── generic/    # Estratégia genérica
│       └── task_execution/ # Execução de tarefas autônomas
│
├── process/            # Processos de negócio (templates)
├── models/             # Modelos de documentos
├── scripts/            # Scripts de execução
└── drive/              # Artefatos gerados
```

### Separação Framework vs Business

- **framework/**: Código reutilizável, genérico, sem conhecimento de negócio
- **business/**: Implementações específicas que usam o framework
- **Importações**: Sempre `from framework.X` e `from business.Y` (nunca `agents.framework`)

---

## Como Usar o Framework

### 1. Conceitos Fundamentais

#### AgentContext

Contexto imutável que carrega informações de execução:

```python
from framework.core.context import AgentContext

context = AgentContext(
    context_name="MeuProjeto",
    context_description="Descrição do projeto",
    strategy_name="ZeroUm",
    base_path=Path("/caminho/do/projeto")
)

# Propriedades principais
context.workspace_root  # drive/MeuProjeto/
context.strategy_path   # business/strategies/zeroum/
context.context_name    # "MeuProjeto"
```

#### RunConfig

Configuração de execução:

```python
from framework.core.context import RunConfig

config = RunConfig(
    dry_run=False,           # Se True, não executa de fato
    max_retries=3,           # Tentativas em caso de erro
    enable_metrics=True,     # Habilitar métricas
    enable_tracing=True      # Habilitar tracing
)
```

### 2. Sistema de Ferramentas (Tools)

O framework possui um sistema hierárquico de permissões:

```python
from framework.tools.permissions import AgentType

# Hierarquia de permissões (do mais restrito ao mais permissivo)
AgentType.PROCESS        # Apenas leitura de arquivos
AgentType.STRATEGY       # + escrita de arquivos
AgentType.ORCHESTRATOR   # + comandos git básicos
AgentType.AUTONOMOUS     # + comandos de sistema e execução de código
```

#### Ferramentas Disponíveis

##### Filesystem (AgentType.PROCESS)

```python
from framework.tools.builtin.filesystem import (
    _ls, _read_file, _write_file, _edit_file, _glob, _grep
)

# Listar diretório
files = _ls("/caminho/diretorio")

# Ler arquivo
content = _read_file("/caminho/arquivo.txt")

# Escrever arquivo
_write_file("/caminho/novo.txt", "conteúdo")

# Editar arquivo
_edit_file("/caminho/arquivo.txt", "texto antigo", "texto novo")

# Buscar arquivos por padrão
matches = _glob("/caminho", "*.py")

# Buscar texto em arquivos
results = _grep("/caminho", "pattern", file_pattern="*.md")
```

##### Execution (AgentType.ORCHESTRATOR para git, AUTONOMOUS para outros)

```python
from framework.tools.builtin.execution import (
    _git_status, _git_diff, _git_add, _git_commit, _git_log,
    _run_command, _mkdir, _rm, _mv, _run_python, _run_tests
)

# Comandos git (ORCHESTRATOR)
status = _git_status("/repo")
diff = _git_diff("/repo", "HEAD~1")
_git_add("/repo", ["arquivo.py"])
_git_commit("/repo", "feat: nova funcionalidade")

# Comandos de sistema (AUTONOMOUS apenas)
output = _run_command(["ls", "-la"], cwd="/caminho")
_mkdir("/novo/diretorio")
_mv("/origem.txt", "/destino.txt")
resultado = _run_python("/script.py", args=["arg1", "arg2"])
test_results = _run_tests("/tests/", pattern="test_*.py")
```

#### Criando Ferramentas Personalizadas

```python
from framework.tools.registry import ToolRegistry
from framework.tools.permissions import AgentType

# Registrar nova ferramenta
@ToolRegistry.register(
    name="minha_ferramenta",
    description="Faz algo específico",
    agent_type=AgentType.STRATEGY
)
def minha_ferramenta(param1: str, param2: int) -> str:
    """Documentação da ferramenta."""
    # Implementação
    return f"Resultado: {param1} x {param2}"

# Obter ferramentas para um tipo de agente
tools = ToolRegistry.get_tools_for_agent(AgentType.STRATEGY)
```

### 3. Integração com LLMs

#### Build LLM com Factory

```python
from framework.llm.factory import build_llm

# Configuração básica (usa variáveis de ambiente)
llm = build_llm()

# Configuração customizada
llm = build_llm({
    "model": "gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 2000,
    "agent_context": {  # Para correlação em logs
        "context_name": "MeuProjeto",
        "strategy_name": "ZeroUm"
    }
})

# Invocar
response = llm.invoke("Qual é a capital do Brasil?")
content = response.content if hasattr(response, 'content') else str(response)
```

#### Monitoramento Automático

O framework monitora automaticamente todas as chamadas LLM:

```python
# Monitoramento é automático quando usa build_llm()
llm = build_llm({"agent_context": {"subagent": "validador"}})
response = llm.invoke("Prompt...")

# Dados capturados automaticamente:
# - Modelo usado
# - Tokens (input/output)
# - Latência
# - Custo estimado
# - Contexto do agente
```

### 4. Orquestração

#### OrchestrationGraph

Sistema declarativo para criar fluxos de execução:

```python
from framework.orchestration.graph import OrchestrationGraph

# Definir handlers (nodes)
def coletar_dados(state):
    state['dados'] = "coletados"
    return state

def processar(state):
    state['resultado'] = f"Processado: {state['dados']}"
    return state

def validar(state):
    state['valido'] = len(state['resultado']) > 0
    return state

# Criar grafo
graph = OrchestrationGraph.from_handlers({
    "coletar": coletar_dados,
    "processar": processar,
    "validar": validar
})

# Executar
final_state = graph.execute(initial_state={})
print(final_state)  # {'dados': 'coletados', 'resultado': '...', 'valido': True}
```

#### Roteamento Condicional

```python
def router(state):
    """Decide qual próximo node executar."""
    if state.get('valido'):
        return "finalizar"
    else:
        return "corrigir"

graph = OrchestrationGraph.from_handlers({
    "validar": validar,
    "router": router,
    "corrigir": corrigir,
    "finalizar": finalizar
})
```

### 5. Observabilidade

#### Sistema de Monitoramento

```python
from framework.observability.monitoring import MonitoringManager

# Verificar se está habilitado
if MonitoringManager.is_enabled():
    # Monitoramento ativo
    pass

# Desabilitar temporariamente
MonitoringManager.set_enabled(False)

# Obter eventos capturados
manager = MonitoringManager.get_instance()
llm_calls = manager.get_llm_calls()
tool_calls = manager.get_tool_calls()
metrics = manager.get_aggregated_metrics()
```

#### Exportar Dados de Monitoramento

```python
from framework.observability.exporters import export_all
from pathlib import Path

# Exportar tudo (JSON, CSV, relatório)
files_created = export_all(
    base_directory=Path("drive/MeuProjeto/_monitoring"),
    formats=['json', 'csv', 'summary']
)

# files_created = {
#   'json': 'monitoring_data.json',
#   'csv': {
#       'llm_calls': 'llm_calls.csv',
#       'tool_calls': 'tool_calls.csv'
#   },
#   'summary': 'monitoring_summary.txt'
# }
```

#### Métricas e Tracing

```python
from framework.observability import MetricsCollector, TracingManager

# Métricas
metrics = MetricsCollector()
metrics.start_timer("operacao")
# ... executar operação
elapsed = metrics.stop_timer("operacao")
metrics.increment("contador_eventos")

# Tracing
tracing = TracingManager()
if tracing.is_enabled:
    tracing.start_trace("minha_operacao")
    # ... executar
    tracing.end_trace()
```

### 6. Workspace e I/O

```python
from framework.io.workspace import WorkspaceManager
from framework.io.package import PackageService

# Gerenciar workspace
workspace = WorkspaceManager(context)
workspace.ensure_workspace()  # Cria drive/MeuProjeto/

# Criar artefato
artifact_path = workspace.workspace_root / "00-ProblemHypothesisExpress" / "hipotese.MD"
artifact_path.parent.mkdir(parents=True, exist_ok=True)
artifact_path.write_text("Conteúdo da hipótese", encoding='utf-8')

# Empacotar resultados
package_service = PackageService(context)
zip_path = package_service.create_package(
    workspace.workspace_root,
    output_name="MeuProjeto_outputs.zip"
)
```

---

## Como Usar o Business (Estratégias)

### Estrutura de uma Estratégia

```
business/strategies/nome_estrategia/
├── __init__.py
├── orchestrator.py      # Orquestrador principal
├── config.py            # Configuração da estratégia
├── subagents/           # Subagentes (opcional)
│   ├── __init__.py
│   ├── registry.py      # Registro de subagentes
│   └── meu_subagente.py
└── README.md
```

### Exemplo: Executar Estratégia ZeroUm

```bash
# Via script
python scripts/run_strategy_agent.py ZeroUm MeuProjeto \
  -d "Validar hipótese de produto para marketplace B2B"

# Programaticamente
from business.strategies.zeroum.orchestrator import ZeroUmOrchestrator

orchestrator = ZeroUmOrchestrator(
    context_name="MeuProjeto",
    context_description="Validar hipótese..."
)

result = orchestrator.run()
print(result['consolidated'])
```

---

## Como Criar Subagentes

### Abordagem 1: Nodes no OrchestrationGraph (Recomendado)

Subagentes são implementados como **métodos** do orquestrador que são registrados como nodes:

```python
# business/strategies/zeroum/orchestrator.py

class ZeroUmOrchestrator:

    def _generate_hypothesis(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Subagente: Gera declaração de hipótese.

        Args:
            state: Estado contendo contexto do projeto

        Returns:
            Estado com hipótese gerada
        """
        logger.info("Gerando hipótese")

        # Obter contexto
        context_desc = state.get('context_description', '')

        # Criar LLM com monitoramento automático
        llm = build_llm({
            "model": "gpt-4o-mini",
            "temperature": 0.4,
            "agent_context": {
                "context_name": self.context.context_name,
                "strategy_name": "ZeroUm",
                "subagent": "generate_hypothesis"
            }
        })

        # Prompt específico
        prompt = f"""
        Você é um especialista em validação de hipóteses de negócio.

        Com base no contexto abaixo, crie uma declaração de hipótese estruturada:

        Contexto: {context_desc}

        A declaração deve conter:
        1. Problema identificado
        2. Perfis de usuários-alvo (mínimo 3)
        3. Dor principal
        4. Solução proposta
        5. Proposta de valor
        6. Canais de aquisição
        7. Experimentos para validação
        """

        # Invocar LLM (monitorado automaticamente)
        response = llm.invoke(prompt)
        hypothesis = response.content if hasattr(response, 'content') else str(response)

        # Salvar artefato
        artifact_path = self.context.workspace_root / "00-ProblemHypothesisExpress"
        artifact_path.mkdir(parents=True, exist_ok=True)

        file_path = artifact_path / "01-declaracao-hipotese.MD"
        file_path.write_text(hypothesis, encoding='utf-8')

        logger.info(f"Hipótese salva em {file_path}")

        # Atualizar estado
        state['hypothesis'] = hypothesis
        state['artifacts'] = state.get('artifacts', []) + [str(file_path)]

        return state

    def _validate_hypothesis(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Subagente: Valida a hipótese gerada."""
        logger.info("Validando hipótese")

        hypothesis = state.get('hypothesis', '')

        llm = build_llm({
            "agent_context": {
                "subagent": "validate_hypothesis"
            }
        })

        prompt = f"""
        Analise a hipótese abaixo e identifique:
        1. Pontos fortes
        2. Pontos fracos
        3. Sugestões de melhoria

        Hipótese:
        {hypothesis}
        """

        response = llm.invoke(prompt)
        validation = response.content if hasattr(response, 'content') else str(response)

        # Salvar validação
        file_path = self.context.workspace_root / "00-ProblemHypothesisExpress" / "02-validacao.MD"
        file_path.write_text(validation, encoding='utf-8')

        state['validation'] = validation
        state['artifacts'] = state.get('artifacts', []) + [str(file_path)]

        return state

    def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
        """Executa a estratégia."""

        # Criar grafo com subagentes como nodes
        graph = OrchestrationGraph.from_handlers({
            "collect_context": self._collect_context,
            "generate_hypothesis": self._generate_hypothesis,
            "validate_hypothesis": self._validate_hypothesis,
            "consolidate": self._consolidate
        })

        # Executar
        final_state = graph.execute(initial_state={
            'context_description': self.context.context_description
        })

        return {
            'hypothesis': final_state.get('hypothesis'),
            'validation': final_state.get('validation'),
            'artifacts': final_state.get('artifacts', [])
        }
```

### Abordagem 2: Classes Dedicadas (Avançado)

Para subagentes muito complexos, crie classes separadas:

```python
# business/strategies/zeroum/subagents/validador_complexo.py

from typing import Dict, Any
from framework.core.context import AgentContext
from framework.llm.factory import build_llm

class ValidadorComplexo:
    """Subagente complexo com múltiplas etapas de validação."""

    def __init__(self, context: AgentContext):
        self.context = context
        self.llm = build_llm({
            "agent_context": {
                "context_name": context.context_name,
                "subagent": "validador_complexo"
            }
        })

    def validar_perfis(self, hypothesis: str) -> Dict[str, Any]:
        """Valida perfis de usuários."""
        # Implementação
        pass

    def validar_canais(self, hypothesis: str) -> Dict[str, Any]:
        """Valida canais de aquisição."""
        # Implementação
        pass

    def executar(self, hypothesis: str) -> Dict[str, Any]:
        """Executa validação completa."""
        perfis = self.validar_perfis(hypothesis)
        canais = self.validar_canais(hypothesis)

        return {
            'perfis_validados': perfis,
            'canais_validados': canais
        }

# Usar no orchestrator:
# business/strategies/zeroum/orchestrator.py

def _validacao_complexa(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """Node que usa subagente complexo."""
    from business.strategies.zeroum.subagents.validador_complexo import ValidadorComplexo

    validador = ValidadorComplexo(self.context)
    resultado = validador.executar(state['hypothesis'])

    state['validacao_complexa'] = resultado
    return state
```

### Registry de Subagentes

Para organizar múltiplos subagentes:

```python
# business/strategies/zeroum/subagents/registry.py

from typing import Dict, Type

class SubagentRegistry:
    """Registry de subagentes disponíveis."""

    _subagents: Dict[str, Type] = {}

    @classmethod
    def register(cls, name: str):
        """Decorator para registrar subagente."""
        def decorator(subagent_class):
            cls._subagents[name] = subagent_class
            return subagent_class
        return decorator

    @classmethod
    def get(cls, name: str):
        """Obtém classe de subagente."""
        return cls._subagents.get(name)

    @classmethod
    def list_all(cls):
        """Lista todos os subagentes registrados."""
        return list(cls._subagents.keys())

# Registrar subagentes
from business.strategies.zeroum.subagents.registry import SubagentRegistry

@SubagentRegistry.register("validador_complexo")
class ValidadorComplexo:
    # Implementação
    pass

@SubagentRegistry.register("hypothesis_generator")
class HypothesisGenerator:
    # Implementação
    pass

# Usar no orchestrator
def _execute_subagent(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """Executa subagente dinamicamente."""
    subagent_name = state.get('next_subagent')
    SubagentClass = SubagentRegistry.get(subagent_name)

    if SubagentClass:
        subagent = SubagentClass(self.context)
        result = subagent.execute(state)
        state.update(result)

    return state
```

---

## Como Criar Orquestradores

### Estrutura Básica

```python
# business/strategies/minha_estrategia/orchestrator.py

from typing import Any, Dict, Optional
from pathlib import Path
import logging

from framework.core.context import AgentContext, RunConfig
from framework.orchestration.graph import OrchestrationGraph
from framework.io.workspace import WorkspaceManager
from framework.io.package import PackageService
from framework.observability import MetricsCollector, TracingManager
from framework.llm.factory import build_llm

logger = logging.getLogger(__name__)

class MinhaEstrategiaOrchestrator:
    """Orquestrador da estratégia MinhaEstrategia."""

    strategy_name = "MinhaEstrategia"

    def __init__(
        self,
        context_name: str,
        context_description: str = "",
        base_path: Optional[Path] = None
    ) -> None:
        """Inicializa o orquestrador."""

        # Criar contexto
        repo_root = base_path or Path(__file__).resolve().parents[3]
        self.context = AgentContext(
            context_name=context_name,
            context_description=context_description,
            strategy_name=self.strategy_name,
            base_path=repo_root
        )

        # Componentes do framework
        self.workspace = WorkspaceManager(self.context)
        self.package_service = PackageService(self.context)
        self.metrics = MetricsCollector()
        self.tracing = TracingManager()

        # LLM compartilhado (opcional)
        self.llm = build_llm({
            "model": "gpt-4o-mini",
            "agent_context": {
                "context_name": context_name,
                "strategy_name": self.strategy_name
            }
        })

    def _step_1(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Primeira etapa da estratégia."""
        logger.info("Executando etapa 1")

        # Sua lógica aqui
        state['step_1_complete'] = True

        return state

    def _step_2(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Segunda etapa da estratégia."""
        logger.info("Executando etapa 2")

        # Usar LLM
        response = self.llm.invoke("Prompt...")
        state['step_2_result'] = response.content

        return state

    def _consolidate(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Consolida resultados finais."""
        logger.info("Consolidando resultados")

        # Criar documento consolidado
        consolidated = f"""
        # Resultados - {self.context.context_name}

        ## Etapa 1
        {state.get('step_1_result', 'N/A')}

        ## Etapa 2
        {state.get('step_2_result', 'N/A')}
        """

        # Salvar
        consolidated_path = self.context.workspace_root / "00-consolidado.MD"
        consolidated_path.write_text(consolidated, encoding='utf-8')

        state['consolidated'] = str(consolidated_path)

        return state

    def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
        """Executa a estratégia completa."""
        if config is None:
            config = RunConfig()

        # Iniciar tracing
        if self.tracing.is_enabled:
            self.tracing.start_trace(f"{self.strategy_name}_{self.context.context_name}")

        self.metrics.start_timer(f"{self.strategy_name}_strategy")

        try:
            # Preparar workspace
            self.workspace.ensure_workspace()

            # Criar grafo de orquestração
            graph = OrchestrationGraph.from_handlers({
                "step_1": self._step_1,
                "step_2": self._step_2,
                "consolidate": self._consolidate
            })

            # Executar
            final_state = graph.execute(initial_state={
                'context_description': self.context.context_description
            })

            # Empacotar resultados
            archive_path = self.package_service.create_package(
                self.workspace.workspace_root,
                output_name=f"{self.context.context_name}_{self.strategy_name}_outputs.zip"
            )

            # Registrar métricas
            elapsed = self.metrics.stop_timer(f"{self.strategy_name}_strategy")
            logger.info(f"Estratégia {self.strategy_name} concluída em {elapsed:.2f}s")

            if self.tracing.is_enabled:
                self.tracing.end_trace()

            return {
                'consolidated': final_state.get('consolidated'),
                'archive': str(archive_path),
                'state': final_state
            }

        except Exception as exc:
            logger.exception(f"Erro ao executar estratégia {self.strategy_name}")
            if self.tracing.is_enabled:
                self.tracing.end_trace()
            raise
```

### Orquestrador com Roteamento Dinâmico

```python
def _router(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """Decide dinamicamente próximo node."""

    # Lógica de decisão
    if state.get('validation_ok'):
        state['next_node'] = 'finalize'
    elif state.get('attempts', 0) < 3:
        state['next_node'] = 'refine'
        state['attempts'] = state.get('attempts', 0) + 1
    else:
        state['next_node'] = 'error'

    return state

def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
    """Executa com roteamento dinâmico."""

    graph = OrchestrationGraph.from_handlers({
        "collect": self._collect,
        "validate": self._validate,
        "router": self._router,
        "refine": self._refine,
        "finalize": self._finalize,
        "error": self._handle_error
    })

    final_state = graph.execute(initial_state={})
    return final_state
```

---

## Como Criar Estratégias

### Passo 1: Estrutura de Diretórios

```bash
mkdir -p business/strategies/nome_estrategia/subagents
touch business/strategies/nome_estrategia/__init__.py
touch business/strategies/nome_estrategia/orchestrator.py
touch business/strategies/nome_estrategia/config.py
touch business/strategies/nome_estrategia/README.md
touch business/strategies/nome_estrategia/subagents/__init__.py
touch business/strategies/nome_estrategia/subagents/registry.py
```

### Passo 2: Implementar Orquestrador

Veja seção "Como Criar Orquestradores" acima.

### Passo 3: Configuração (Opcional)

```python
# business/strategies/nome_estrategia/config.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class MinhaEstrategiaConfig:
    """Configuração específica da estratégia."""

    modelo_llm: str = "gpt-4o-mini"
    temperatura: float = 0.4
    max_tokens: int = 2000
    processos_obrigatorios: list[str] = None

    def __post_init__(self):
        if self.processos_obrigatorios is None:
            self.processos_obrigatorios = [
                "ProblemHypothesisExpress",
                "SolutionDesign"
            ]
```

### Passo 4: README da Estratégia

```markdown
# MinhaEstrategia

## Objetivo

[Descrever objetivo da estratégia]

## Processos Incluídos

1. **Processo1**: [Descrição]
2. **Processo2**: [Descrição]

## Como Usar

```bash
python scripts/run_strategy_agent.py MinhaEstrategia NomeContexto \
  -d "Descrição do contexto"
```

## Artefatos Gerados

- `drive/NomeContexto/00-Processo1/`: [Descrição]
- `drive/NomeContexto/01-Processo2/`: [Descrição]
- `drive/NomeContexto/00-consolidado.MD`: Documento consolidado
- `drive/NomeContexto/NomeContexto_MinhaEstrategia_outputs.zip`: Pacote final

## Configuração

Variáveis de ambiente opcionais:
- `AGENTS_LLM_MODEL`: Modelo LLM (padrão: gpt-4o-mini)
- `AGENTS_MONITORING_ENABLED`: Monitoramento (padrão: true)
```

### Passo 5: Registrar Estratégia

```python
# scripts/run_strategy_agent.py (adicionar import)

from business.strategies.nome_estrategia.orchestrator import MinhaEstrategiaOrchestrator

STRATEGIES = {
    'zeroum': ('business.strategies.zeroum.orchestrator', 'ZeroUmOrchestrator'),
    'generic': ('business.strategies.generic.orchestrator', 'GenericOrchestrator'),
    'minhaestrategia': ('business.strategies.nome_estrategia.orchestrator', 'MinhaEstrategiaOrchestrator'),
}
```

### Passo 6: Testar

```bash
# Executar estratégia
python scripts/run_strategy_agent.py MinhaEstrategia TesteProjeto \
  -d "Teste da nova estratégia"

# Verificar artefatos
ls -la drive/TesteProjeto/

# Verificar monitoramento
ls -la drive/TesteProjeto/_monitoring/
```

---

## Sistema de Monitoramento

### Configuração

```bash
# .env (já configurado automaticamente)
AGENTS_MONITORING_ENABLED=true
AGENTS_MONITORING_LEVEL=detailed
AGENTS_MONITORING_EXPORT_PATH=  # Opcional, padrão: drive/{context}/_monitoring/
```

### Dados Capturados

#### Chamadas LLM
- Modelo usado
- Tokens de entrada/saída
- Latência (ms)
- Custo estimado (USD)
- Contexto do agente (strategy, subagent, context_name)
- Ferramentas fornecidas ao modelo

#### Execuções de Ferramentas
- Nome da ferramenta
- Argumentos
- Resultado
- Duração (ms)
- Sucesso/erro

#### Métricas Agregadas
- Total de tokens
- Custo total
- Número de chamadas
- Latência média/mínima/máxima
- Ferramentas mais usadas

### Exportação

```python
from framework.observability.exporters import export_all
from pathlib import Path

# Exportar ao final da execução
files = export_all(
    base_directory=Path(f"drive/{context_name}/_monitoring"),
    formats=['json', 'csv', 'summary']
)

# Arquivos criados:
# - monitoring_data.json (dados completos)
# - llm_calls.csv (chamadas LLM em tabela)
# - tool_calls.csv (chamadas de ferramentas em tabela)
# - monitoring_summary.txt (relatório legível)
```

### Exemplo de Relatório

```
================================================================================
RESUMO DE MONITORAMENTO - MeuProjeto
================================================================================
Período: 2025-11-13 14:30:00 - 2025-11-13 14:32:15

CHAMADAS LLM
Modelos usados: gpt-4o-mini (5 chamadas)
Tokens totais: 12,450 (input: 8,200 | output: 4,250)
Custo total estimado: $0.0187
Latência média: 1,245ms (min: 890ms | max: 2,100ms)

FERRAMENTAS
Total de execuções: 23
Ferramentas mais usadas:
  - _write_file: 8 chamadas
  - _read_file: 6 chamadas
  - _grep: 5 chamadas
  - _glob: 4 chamadas

AGENTES
Subagentes executados: gerar_hipotese, validar_hipotese, consolidar
Duração total: 2m 15s
```

---

## Boas Práticas

### Para Agentes de IA

1. **Sempre use o framework**: Não reimplemente funcionalidades já existentes
2. **Siga a hierarquia de permissões**: Respeite AgentType ao usar ferramentas
3. **Use monitoramento**: Sempre forneça `agent_context` ao criar LLMs
4. **Documente bem**: Mantenha docstrings e comentários claros
5. **Teste isoladamente**: Crie testes para cada subagente/node
6. **Gerencie erros**: Use try/except e log adequadamente
7. **Preserve estado**: Sempre retorne `state` atualizado nos nodes
8. **Não bloqueie**: Evite operações síncronas longas

### Para Desenvolvimento

1. **Separação de responsabilidades**: Framework genérico, business específico
2. **Imutabilidade**: AgentContext é imutável, não tente modificá-lo
3. **Logs estruturados**: Use logger do Python, não print()
4. **Artefatos organizados**: Siga estrutura `drive/{context}/{processo}/`
5. **Versionamento**: Mantenha logs de versões em `_pipeline/`

### Para Processos de Negócio

1. **Templates em process/**: Processos reutilizáveis vão em `process/`
2. **Artefatos em \_DATA/**: Todos os templates/exemplos em `_DATA/`
3. **Shared artifacts**: Use `process/_SHARED/` para templates comuns
4. **Documentação em PT-BR**: Processos e artefatos em português
5. **Nomes em CamelCase**: Pastas de processos em CamelCase

---

## Recursos Adicionais

### Documentação Técnica

- [framework/README.md](framework/README.md): Arquitetura do framework
- [framework/observability/README.md](framework/observability/README.md): Sistema de monitoramento
- [docs/GUIA_CRIAR_SUBAGENTES.md](docs/GUIA_CRIAR_SUBAGENTES.md): Guia completo de subagentes
- [docs/QUICK_SETUP.md](docs/QUICK_SETUP.md): Setup rápido
- [docs/OBSERVABILITY.MD](docs/OBSERVABILITY.MD): Observabilidade e métricas
- [docs/LANGCHAIN.MD](docs/LANGCHAIN.MD): Integração com LangChain

### Exemplos Reais

- [business/strategies/zeroum/](business/strategies/zeroum/): Estratégia completa de validação de hipóteses
- [business/strategies/generic/](business/strategies/generic/): Estratégia genérica base
- [business/strategies/task_execution/](business/strategies/task_execution/): Execução autônoma de tarefas

### Scripts de Execução

```bash
# Executar estratégia
python scripts/run_strategy_agent.py <estrategia> <contexto> -d "descrição"

# Executar tarefa autônoma
python scripts/run_autonomous_task.py "tarefa a executar"

# Testar monitoramento
python scripts/test_monitoring.py
```

---

## Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'business'"

**Causa**: PYTHONPATH não configurado ou virtual environment não ativado

**Solução**:
```bash
# Ativar venv
source .venv/bin/activate

# Ou executar com PYTHONPATH
PYTHONPATH=/caminho/do/projeto python scripts/run_strategy_agent.py ...
```

### Erro: "deepagents not installed"

**Causa**: Dependência opcional não instalada

**Solução**:
```bash
# Instalar deepagents (opcional)
pip install "deepagents @ git+https://github.com/langchain-ai/deepagents.git"

# Ou ignorar - framework funciona sem deepagents
```

### Erro: "OPENAI_API_KEY not set"

**Causa**: Variável de ambiente não configurada

**Solução**:
```bash
# Criar/editar .env na raiz
echo "OPENAI_API_KEY=sk-sua-chave-aqui" > .env

# Ou exportar
export OPENAI_API_KEY="sk-sua-chave-aqui"
```

### Monitoramento não funciona

**Causa**: Pode estar desabilitado ou callbacks não adicionados

**Solução**:
```bash
# Verificar .env
echo "AGENTS_MONITORING_ENABLED=true" >> .env

# Verificar programaticamente
python -c "from framework.observability.monitoring import MonitoringManager; print(MonitoringManager.is_enabled())"

# Sempre use build_llm() para obter callbacks automaticamente
```

### Imports quebrados após reestruturação

**Causa**: Migração de `agents/framework` para `framework/`

**Solução**: Todos os imports devem ser:
```python
# CORRETO
from framework.core.context import AgentContext
from business.strategies.zeroum.orchestrator import ZeroUmOrchestrator

# ERRADO
from agents.framework.core.context import AgentContext
from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator
```

---

## Conformidade com Processos de Negócio

Este framework também suporta **processos de negócio documentados** que seguem templates específicos. Quando trabalhando com processos:

### Estrutura de Processos

```
process/
├── _SHARED/              # Templates e referências compartilhadas
├── ProcessoExemplo/
│   ├── process.MD        # Definição do processo
│   ├── knowledge.MD      # Conhecimento e referências
│   ├── tasks.MD          # Tarefas operacionais
│   ├── validator.MD      # Critérios de validação
│   └── _DATA/            # Templates, exemplos, outputs
└── README.MD
```

### Executando Processos

1. **Processos são executados via estratégias**: Estratégias combinam múltiplos processos
2. **Artefatos vão para drive/**: Resultados da execução ficam em `drive/{context}/{processo}/`
3. **Seguir templates**: Sempre use templates de `process/_SHARED/` ou `_DATA/`

### Convenções para Processos

- **Nomes de pastas**: CamelCase (ex: `ProblemHypothesisExpress`)
- **Nomes de arquivos**: lowercase.MD (ex: `process.MD`, `knowledge.MD`)
- **Linguagem**: Documentação em português (pt-BR)
- **Formato**: Markdown puro, sem tabelas, sem emojis
- **Referências**: Sempre relativas ao repositório

Para detalhes completos sobre processos de negócio, consulte os arquivos originais preservados na primeira seção deste documento.

---

**Lembre-se**: Este framework existe para habilitar operações de negócio escaláveis e consistentes. Seu papel como agente é manter essa consistência sendo flexível o suficiente para lidar com requisitos únicos de processos. Em caso de dúvida, leia os modelos e faça perguntas.
