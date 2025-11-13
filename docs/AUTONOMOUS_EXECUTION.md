# Autonomous Execution - Guia Completo

## Visão Geral

O sistema de execução autônoma permite que o framework execute tarefas complexas de forma autônoma usando LLM para planejamento e execução. O LLM:

1. Analisa a tarefa e cria um plano de execução
2. Executa cada etapa usando todas as tools disponíveis
3. Valida resultados após cada etapa
4. Recupera automaticamente de erros
5. Gera relatório consolidado com resultados

## Arquitetura

### Componentes Principais

```
AutonomousAgent
  ├─ Analisa tarefa e cria plano (LLM)
  ├─ Executa plano step-by-step
  ├─ Valida resultados
  └─ Recupera de erros (opcional)

TaskExecutionOrchestrator
  ├─ Orquestra execução completa
  ├─ Gerencia workspace
  ├─ Empacota resultados
  └─ Coleta métricas

Security Controls
  ├─ CommandValidator: valida comandos shell
  ├─ PathValidator: valida acessos a arquivos
  └─ RateLimiter: limita taxa de operações
```

### Tools Disponíveis

O agente autônomo (`AgentType.AUTONOMOUS`) tem acesso a **todas as tools**:

#### FILE_SYSTEM (6 tools)
- `ls` - Listar diretórios
- `read_file` - Ler arquivos
- `write_file` - Escrever arquivos
- `edit_file` - Editar arquivos (regex)
- `glob` - Buscar arquivos por padrão
- `grep` - Buscar conteúdo em arquivos

#### SEARCH (1 tool)
- `grep` - Busca avançada com contexto

#### CONTENT (1 tool)
- `markdown_summarizer` - Resumir markdown com LLM

#### EXECUTION (11 tools) ✨ NOVO
- `run_command` - Executar comandos shell (whitelist)
- `git_status` - Status do repositório
- `git_diff` - Ver diferenças
- `git_add` - Adicionar arquivos ao stage
- `git_commit` - Criar commit
- `git_log` - Ver histórico
- `mkdir` - Criar diretórios
- `rm` - Remover arquivos/diretórios
- `mv` - Mover/renomear
- `run_python` - Executar scripts Python
- `run_tests` - Executar pytest

**Total: 20 tools disponíveis**

## Uso Básico

### 1. Via CLI (Recomendado)

```bash
python agents/scripts/run_autonomous_task.py \
  --task "Analyze all Python files in agents/business and create complexity report" \
  --context "CodeAnalysis"
```

#### Opções do CLI

```bash
--task, -t          Descrição da tarefa em linguagem natural (obrigatório)
--context, -c       Nome do contexto/workspace (CamelCase, obrigatório)
--max-iterations, -m  Máximo de iterações (default: 20)
--no-recovery       Desabilitar recuperação automática de erros
--verbose, -v       Habilitar logging detalhado
--base-path, -b     Caminho base para workspace (default: drive/)
```

#### Exemplos de Uso

**Análise de código:**
```bash
python agents/scripts/run_autonomous_task.py \
  --task "List all functions in agents/framework/tools and describe what each does" \
  --context "ToolsDocumentation"
```

**Operações Git:**
```bash
python agents/scripts/run_autonomous_task.py \
  --task "Check git status, show last 5 commits, and summarize recent changes" \
  --context "GitSummary"
```

**Geração de documentação:**
```bash
python agents/scripts/run_autonomous_task.py \
  --task "Read all markdown files in docs/ and create a table of contents" \
  --context "DocsTOC" \
  --max-iterations 30
```

**Análise de testes:**
```bash
python agents/scripts/run_autonomous_task.py \
  --task "Run pytest on agents/tests and summarize test results" \
  --context "TestAnalysis"
```

### 2. Via API Python

```python
from agents.business.strategies.task_execution.orchestrator import TaskExecutionOrchestrator

# Criar orchestrator
orchestrator = TaskExecutionOrchestrator(
    context_name="MyTask",
    task_description="Your task description here",
    max_iterations=20,
    enable_recovery=True,
)

# Executar
result = orchestrator.run()

# Verificar resultado
if result['success']:
    print(f"Task completed successfully!")
    print(f"Report: {result['consolidated']}")
    print(f"Archive: {result['archive']}")
else:
    print(f"Task failed: {result.get('errors')}")
```

### 3. Usando AutonomousAgent Diretamente

```python
from pathlib import Path
from agents.framework.core.context import AgentContext
from agents.framework.orchestration.autonomous import AutonomousAgent

# Criar contexto
context = AgentContext(
    context_name="DirectTask",
    strategy_name="TaskExecution",
    process_code=None,
    base_path=Path("drive"),
)

# Criar agente
agent = AutonomousAgent(
    context=context,
    task_description="Analyze Python files in agents/framework",
    max_iterations=15,
    enable_recovery=True,
)

# Executar
result = agent.execute()

# Acessar resultados
print(f"Success: {result.success}")
print(f"Complexity: {result.plan.complexity}")
print(f"Steps executed: {len(result.plan.steps)}")

for step in result.plan.steps:
    print(f"{step.number}. [{step.status}] {step.description}")
```

## Fluxo de Execução

### 1. Análise e Planejamento

O LLM analisa a tarefa e cria um plano estruturado:

```json
{
  "complexity": "moderate",
  "estimated_steps": 5,
  "steps": [
    {
      "number": 1,
      "description": "List all Python files in target directory",
      "tools_needed": ["glob", "ls"],
      "expected_outcome": "List of .py files"
    },
    {
      "number": 2,
      "description": "Read each file and extract functions",
      "tools_needed": ["read_file"],
      "expected_outcome": "Dictionary of files and their functions"
    }
  ]
}
```

### 2. Execução Step-by-Step

Para cada step:

1. **Preparação**: Contexto dos steps anteriores é passado ao LLM
2. **Execução**: LLM invoca as tools necessárias
3. **Validação**: Resultado é verificado
4. **Logging**: Progresso é registrado

```
[16:30:15] Step 1/5: List all Python files in target directory
[16:30:16]   Tools called: ['glob', 'ls']
[16:30:17]   ✓ Step 1 completed
[16:30:17] Step 2/5: Read each file and extract functions
[16:30:20]   Tools called: ['read_file']
[16:30:21]   ✓ Step 2 completed
```

### 3. Recuperação de Erros

Se um step falhar e `enable_recovery=True`:

1. LLM analisa o erro
2. Decide estratégia de recuperação:
   - **retry**: Tentar novamente com parâmetros diferentes
   - **skip**: Pular step se não for crítico
   - **alternative**: Usar abordagem alternativa
3. Executa recuperação
4. Continua execução ou falha

```
[16:30:25] Step 3/5: Parse Python AST
[16:30:26]   ✗ Step 3 failed: SyntaxError in file
[16:30:26]   Attempting recovery...
[16:30:27]   Recovery action: skip - File has syntax error, skip and continue
[16:30:27]   Recovery successful!
[16:30:27] Step 4/5: Generate report
```

### 4. Resultados e Empacotamento

Ao final:

1. **Relatório consolidado**: `drive/<Context>/00-execution-report.MD`
2. **Logs de execução**: Lista completa de operações
3. **Artefatos criados**: Arquivos gerados durante execução
4. **Archive ZIP**: Pacote com todos os resultados
5. **Métricas**: Tempo, tokens, custos

## Segurança

### CommandValidator

Valida comandos shell antes de executar:

**Whitelist de comandos permitidos:**
```
git, ls, cat, head, tail, wc, find, grep,
python, python3, pip, pytest, npm, node, make, docker
```

**Blacklist de padrões perigosos:**
```
rm -rf /, rm -rf *, fork bombs, dd, mkfs, format,
> /dev/, wget, curl, chmod 777, sudo
```

**Uso:**
```python
from agents.framework.security.controls import CommandValidator

validator = CommandValidator()
is_safe, reason = validator.validate("git status")

if is_safe:
    execute_command()
else:
    print(f"Blocked: {reason}")
```

### PathValidator

Valida acessos a arquivos:

**Paths bloqueados:**
```
/, /etc, /usr, /bin, /sbin, /var, /boot,
/sys, /proc, /dev, /root
```

**Uso:**
```python
from agents.framework.security.controls import PathValidator

validator = PathValidator()

# Validar leitura
is_safe, reason = validator.validate("/home/user/file.txt")

# Validar escrita (mais restritivo)
is_safe, reason = validator.validate_write("/home/user/output.txt")

# Validar deleção (mais restritivo ainda)
is_safe, reason = validator.validate_delete("/tmp/dir", recursive=True)
```

### RateLimiter

Limita taxa de operações:

**Default: 30 operações/minuto**

**Uso:**
```python
from agents.framework.security.controls import RateLimiter

limiter = RateLimiter(max_per_minute=30)

if limiter.check_and_record("command_execution"):
    execute_command()
else:
    print("Rate limit exceeded, wait a moment")
```

### Audit Logging

Todas as operações são auditadas:

```python
from agents.framework.security.controls import SecurityConfig, CommandValidator

config = SecurityConfig(
    enable_audit_log=True,
    audit_log_path=Path("audit.log")
)

validator = CommandValidator(config)
validator.validate("git status")

# Audit log entry:
# 2025-01-15 16:30:15 | ALLOWED | git status | Command in whitelist
```

## Estrutura de Resultados

### Workspace

```
drive/<ContextName>/
├── 00-execution-report.MD      # Relatório consolidado
├── TaskExecution/              # Artefatos da estratégia
│   └── artifacts/              # Arquivos gerados
└── <ContextName>_TaskExecution_YYYYMMDD_HHMMSS.zip  # Archive
```

### Relatório Consolidado

```markdown
# Task Execution Report - CodeAnalysis

**Task:** Analyze all Python files in agents/business and create complexity report
**Status:** ✓ Success
**Started:** 2025-01-15 16:30:00
**Completed:** 2025-01-15 16:32:45
**Duration:** 165.3 seconds

## Execution Plan

**Complexity:** moderate
**Total Steps:** 5
**Completed:** 5
**Failed:** 0

### Steps

1. [✓] List all Python files in agents/business
   Tools: glob, ls

2. [✓] Read each file and count lines
   Tools: read_file

3. [✓] Calculate cyclomatic complexity
   Tools: run_python

4. [✓] Generate complexity report
   Tools: write_file

5. [✓] Create summary visualization
   Tools: write_file

## Execution Log

```
[16:30:00] Analyzing task...
[16:30:01] Plan created with 5 steps
[16:30:01] Executing plan...
[16:30:02] Step 1/5: List all Python files in agents/business
[16:30:03]   ✓ Step 1 completed
...
```

## Artifacts Created

- drive/CodeAnalysis/complexity_report.MD
- drive/CodeAnalysis/complexity_data.json

## Errors

(none)
```

### Dicionário de Resultado

```python
{
    "success": True,
    "task_description": "Analyze all Python files...",
    "complexity": "moderate",
    "plan_summary": {
        "total_steps": 5,
        "completed": 5,
        "failed": 0,
        "skipped": 0
    },
    "execution_log": [
        "[16:30:00] Analyzing task...",
        "[16:30:01] Plan created with 5 steps",
        ...
    ],
    "artifacts": [
        "drive/CodeAnalysis/complexity_report.MD",
        "drive/CodeAnalysis/complexity_data.json"
    ],
    "consolidated": "drive/CodeAnalysis/00-execution-report.MD",
    "archive": "drive/CodeAnalysis/CodeAnalysis_TaskExecution_20250115_163245.zip",
    "metrics": {
        "total_execution": {
            "total": 165.3,
            "count": 1
        },
        "task_analysis": {
            "total": 1.2,
            "count": 1
        },
        "task_execution": {
            "total": 160.1,
            "count": 1
        }
    },
    "errors": []
}
```

## Casos de Uso

### 1. Análise de Código

**Tarefa:** Analisar complexidade de código

```bash
python agents/scripts/run_autonomous_task.py \
  --task "Analyze Python files in agents/framework and report: number of files, total lines, average complexity, and list of most complex functions" \
  --context "CodeComplexityAnalysis"
```

**O que o LLM fará:**
1. Usar `glob` para encontrar todos os arquivos `.py`
2. Usar `read_file` para ler cada arquivo
3. Analisar código e contar linhas
4. Calcular métricas de complexidade
5. Usar `write_file` para criar relatório

### 2. Operações Git

**Tarefa:** Resumo de mudanças

```bash
python agents/scripts/run_autonomous_task.py \
  --task "Check git status, show last 10 commits, and create a summary of recent development activity" \
  --context "GitActivitySummary"
```

**O que o LLM fará:**
1. Usar `git_status` para ver mudanças atuais
2. Usar `git_log` para ver últimos commits
3. Usar `git_diff` para ver mudanças em arquivos
4. Analisar padrões e atividades
5. Usar `write_file` para criar resumo

### 3. Geração de Documentação

**Tarefa:** Criar índice de documentação

```bash
python agents/scripts/run_autonomous_task.py \
  --task "Read all markdown files in docs/, extract headers, and create a comprehensive table of contents with links" \
  --context "DocumentationIndex"
```

**O que o LLM fará:**
1. Usar `glob` para encontrar todos os `.md` em `docs/`
2. Usar `read_file` para ler cada arquivo
3. Extrair headers (# ## ###)
4. Organizar hierarquicamente
5. Usar `write_file` para criar `docs/TABLE_OF_CONTENTS.md`

### 4. Testes e Validação

**Tarefa:** Executar e analisar testes

```bash
python agents/scripts/run_autonomous_task.py \
  --task "Run pytest on agents/tests/, summarize results, and list failed tests with error messages" \
  --context "TestResults"
```

**O que o LLM fará:**
1. Usar `run_tests` para executar pytest
2. Parsear output dos testes
3. Identificar testes falhados
4. Extrair mensagens de erro
5. Usar `write_file` para criar relatório

### 5. Exploração de Projeto

**Tarefa:** Mapear arquitetura

```bash
python agents/scripts/run_autonomous_task.py \
  --task "Explore agents/ directory, identify all modules, map dependencies, and create architecture diagram in markdown" \
  --context "ArchitectureMapping" \
  --max-iterations 30
```

**O que o LLM fará:**
1. Usar `ls` recursivamente para mapear estrutura
2. Usar `read_file` para ler `__init__.py` e identificar exports
3. Usar `grep` para encontrar imports entre módulos
4. Construir grafo de dependências
5. Usar `write_file` para criar diagrama Mermaid

## Limitações e Considerações

### Limitações Atuais

1. **Comandos Shell**: Apenas comandos na whitelist são permitidos
2. **Paths de Sistema**: Acesso a paths de sistema é bloqueado
3. **Iterações**: Limitado a `max_iterations` (default: 20)
4. **Timeout**: Commands têm timeout de 30-120 segundos
5. **LLM Context**: Plano e resultados devem caber no contexto do LLM

### Considerações de Segurança

1. **Sandbox**: Execute em ambiente sandboxed se possível
2. **Whitelist**: Não adicione comandos perigosos à whitelist
3. **Audit Log**: Sempre habilite audit logging em produção
4. **Rate Limiting**: Ajuste limites conforme necessidade
5. **Confirmação**: Para operações críticas, adicione confirmação manual

### Performance

1. **Custo de LLM**: Tarefas complexas podem gerar muitos tokens
2. **Tempo de Execução**: Depende da complexidade e número de steps
3. **Tools IO-bound**: Operações de arquivo podem ser lentas
4. **Recovery**: Habilitado por padrão, pode aumentar tempo

**Otimizações:**
- Use `max_iterations` adequado
- Desabilite recovery se não necessário (`--no-recovery`)
- Use `gpt-4o-mini` para planejamento (default)
- Tarefas simples são mais rápidas e baratas

### Debugging

**Habilitar logging verbose:**
```bash
python agents/scripts/run_autonomous_task.py \
  --task "..." \
  --context "..." \
  --verbose
```

**Inspecionar execution log:**
```python
result = orchestrator.run()

for log_entry in result['execution_log']:
    print(log_entry)
```

**Verificar audit log:**
```python
from agents.framework.security.controls import get_command_validator

validator = get_command_validator()
audit = validator.get_audit_log()

for entry in audit:
    print(f"{entry['timestamp']} | {entry['action']} | {entry['command']}")
```

## Próximos Passos

1. **Teste com tarefas simples** primeiro
2. **Aumente complexidade** gradualmente
3. **Monitore logs** para entender comportamento do LLM
4. **Ajuste max_iterations** conforme necessário
5. **Customize SecurityConfig** para suas necessidades

## Referências

- [EXECUTION_TOOLS.md](EXECUTION_TOOLS.md) - Documentação detalhada das tools
- [SECURITY_CONTROLS.md](SECURITY_CONTROLS.md) - Controles de segurança
- [agents/business/examples/autonomous_task_example.py](../agents/business/examples/autonomous_task_example.py) - Exemplos de código
- [agents/tests/test_autonomous_execution.py](../agents/tests/test_autonomous_execution.py) - Testes
