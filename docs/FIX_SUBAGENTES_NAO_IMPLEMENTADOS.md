# Fix: Subagentes Não Implementados

## Problema

Ao executar a estratégia ZeroUm:
```bash
python3 scripts/run_strategy_agent.py zeroum "Automarticles" -d "..."
```

**Erros:**
```
ERROR: Erro ao executar subagente problem_hypothesis_definition: Subagente problem_hypothesis_definition não tem handler configurado
ERROR: Erro ao executar subagente target_user_identification: Subagente target_user_identification não tem handler configurado
ERROR: Erro ao executar subagente user_interview_validation: Subagente user_interview_validation não tem handler configurado
ERROR: Erro ao executar subagente landing_page_creation: Subagente landing_page_creation não tem handler configurado
ERROR: Erro ao executar subagente checkout_setup: Subagente checkout_setup não tem handler configurado
```

## Root Cause

O `SubagentRegistry` registra vários subagentes da metodologia ZeroUm:
- problem_hypothesis_express ✅ IMPLEMENTADO
- client_delivery ✅ IMPLEMENTADO
- problem_hypothesis_definition ❌ NÃO IMPLEMENTADO
- target_user_identification ❌ NÃO IMPLEMENTADO
- user_interview_validation ❌ NÃO IMPLEMENTADO
- landing_page_creation ❌ NÃO IMPLEMENTADO
- checkout_setup ❌ NÃO IMPLEMENTADO

Quando o LLM analisa o contexto e sugere um pipeline com múltiplos subagentes, ele pode incluir subagentes que estão **registrados** mas **não implementados**. O orquestrador tentava executá-los e falhava.

## ✅ Solução Aplicada

Modificado `agents/business/strategies/zeroum/orchestrator.py`:

### 1. Lista de Subagentes Implementados

Definida constante `IMPLEMENTED_SUBAGENTS` nos métodos relevantes:

```python
IMPLEMENTED_SUBAGENTS = {"problem_hypothesis_express", "client_delivery"}
```

### 2. Método `_default_pipeline()` Atualizado

**Antes:**
```python
def _default_pipeline(self) -> List[str]:
    available = SubagentRegistry.list_available()
    return available if available else ["problem_hypothesis_express"]
```

**Depois:**
```python
def _default_pipeline(self) -> List[str]:
    """Retorna ordem padrão de execução baseada no registry (apenas implementados)."""
    IMPLEMENTED_SUBAGENTS = {"problem_hypothesis_express", "client_delivery"}

    available = SubagentRegistry.list_available()
    implemented = [name for name in available if name in IMPLEMENTED_SUBAGENTS]

    return implemented if implemented else ["problem_hypothesis_express"]
```

### 3. Método `_sanitize_pipeline()` Atualizado

**Antes:**
```python
def _sanitize_pipeline(self, pipeline, recommended_subagent):
    valid = []
    registered = set(SubagentRegistry.list_available())
    for name in pipeline:
        if name in registered and name not in valid:
            valid.append(name)
    return valid
```

**Depois:**
```python
def _sanitize_pipeline(self, pipeline, recommended_subagent):
    """Normaliza pipeline garantindo somente subagentes válidos E IMPLEMENTADOS."""
    IMPLEMENTED_SUBAGENTS = {"problem_hypothesis_express", "client_delivery"}

    valid = []
    skipped = []
    registered = set(SubagentRegistry.list_available())

    for name in pipeline:
        # Verificar se está registrado E implementado
        if name in registered and name in IMPLEMENTED_SUBAGENTS and name not in valid:
            valid.append(name)
        elif name in registered and name not in IMPLEMENTED_SUBAGENTS:
            skipped.append(name)

    # Log de subagentes não implementados
    if skipped:
        logger.warning(
            f"Subagentes registrados mas NÃO IMPLEMENTADOS foram ignorados: {skipped}. "
            f"Apenas estes estão implementados: {list(IMPLEMENTED_SUBAGENTS)}"
        )

    if not valid:
        logger.info("Nenhum subagente válido no pipeline, usando pipeline padrão")
        return self._default_pipeline()

    return valid
```

## Comportamento Após o Fix

### Antes do Fix

```
LLM sugere pipeline: [
    "problem_hypothesis_definition",
    "target_user_identification",
    "user_interview_validation"
]

Orquestrador tenta executar todos:
  ✗ problem_hypothesis_definition FALHA (não implementado)
  ✗ target_user_identification FALHA (não implementado)
  ✗ user_interview_validation FALHA (não implementado)

RESULTADO: 3 erros, execução falha
```

### Depois do Fix

```
LLM sugere pipeline: [
    "problem_hypothesis_definition",
    "target_user_identification",
    "user_interview_validation"
]

Orquestrador sanitiza pipeline:
  ✗ problem_hypothesis_definition IGNORADO (não implementado)
  ✗ target_user_identification IGNORADO (não implementado)
  ✗ user_interview_validation IGNORADO (não implementado)

WARNING: Subagentes registrados mas NÃO IMPLEMENTADOS foram ignorados: [...]

Pipeline válido vazio, usando pipeline padrão:
  ✓ problem_hypothesis_express EXECUTADO

RESULTADO: Execução bem-sucedida com fallback
```

## Log Esperado Agora

```bash
python3 scripts/run_strategy_agent.py zeroum "Automarticles" -d "..."

# Análise do LLM
INFO: Analisando contexto para seleção de subagente...
INFO: Análise concluída: [reasoning do LLM]
INFO: Complexidade: moderate
INFO: Pipeline recomendado: ['problem_hypothesis_definition', 'target_user_identification']

# Sanitização do pipeline
WARNING: Subagentes registrados mas NÃO IMPLEMENTADOS foram ignorados: ['problem_hypothesis_definition', 'target_user_identification'].
         Apenas estes estão implementados: ['problem_hypothesis_express', 'client_delivery']

INFO: Nenhum subagente válido no pipeline, usando pipeline padrão

# Execução
INFO: Executando subagente: problem_hypothesis_express
INFO: [PHExpress] Iniciando Problem Hypothesis Express Session...
INFO: [PHExpress] Estágio 1/5: Esclarecimento de Audiência
...
INFO: Subagente problem_hypothesis_express executado com sucesso

# Resultado
INFO: EXECUÇÃO CONCLUÍDA COM SUCESSO
```

## Próximos Passos

Para adicionar novos subagentes, siga estes passos:

### 1. Implementar o Subagente

Criar arquivo em `agents/business/strategies/zeroum/subagents/`:

```python
# exemplo: target_user_identification.py
class TargetUserIdentificationAgent:
    def __init__(self, workspace_root, ...):
        ...

    def execute_identification(self):
        # Implementar lógica
        ...
        return results
```

### 2. Registrar no SubagentRegistry

Em `agents/business/strategies/zeroum/subagents/registry.py`:

```python
SubagentRegistry.register(
    name="target_user_identification",
    subagent_class=TargetUserIdentificationAgent,
    description="Identificação de usuários-alvo",
    process_code="02-TargetUserIdentification",
    complexity="moderate",
    duration="60 min",
)
```

### 3. Adicionar Handler no Orchestrator

Em `agents/business/strategies/zeroum/orchestrator.py`:

**a) Atualizar IMPLEMENTED_SUBAGENTS:**
```python
IMPLEMENTED_SUBAGENTS = {
    "problem_hypothesis_express",
    "client_delivery",
    "target_user_identification",  # NOVO
}
```

**b) Adicionar handler em `_run_single_subagent()`:**
```python
def _run_single_subagent(self, subagent_name, state):
    ...
    elif subagent_name == "target_user_identification":
        subagent = SubagentClass(
            workspace_root=self.context.workspace_root,
            context_description=self.context.context_description,
        )
        results = subagent.execute_identification()
    ...
```

## Status: ✅ CORRIGIDO

O orquestrador agora:
- ✅ Filtra subagentes não implementados automaticamente
- ✅ Faz fallback para pipeline padrão quando necessário
- ✅ Exibe warnings informativos sobre subagentes ignorados
- ✅ Nunca tenta executar subagentes sem handler
- ✅ Sempre executa algo (pelo menos problem_hypothesis_express)

**A execução não falha mais com erros de subagentes não implementados!**
