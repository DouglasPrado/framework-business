# Resumo de Renomeações - Funções e Variáveis em Inglês

## Data: 2025-11-13

Este documento registra todas as alterações feitas para converter nomes de funções, métodos e variáveis de português para inglês no Framework Business.

## Objetivo

Garantir que todo código executável (funções, métodos, classes, variáveis) esteja em inglês, mantendo a documentação e mensagens de log em português conforme a convenção do projeto.

---

## Alterações Realizadas

### 1. business/strategies/zeroum/orchestrator.py

#### Métodos Renomeados

| Antes (Português) | Depois (Inglês) | Descrição |
|-------------------|-----------------|-----------|
| `_coletar_contexto` | `_collect_context` | Prepara workspace para execução |
| `_analisar_contexto` | `_analyze_context` | Analisa contexto e seleciona subagente |
| `_executar_subagente` | `_execute_subagent` | Executa subagente selecionado |
| `_gerar_hipotese` | `_generate_hypothesis` | Gera hipóteses usando LLM |
| `_validar_resultado` | `_validate_result` | Valida resultados e gera consolidado |

#### Variáveis Renomeadas

| Antes (Português) | Depois (Inglês) | Contexto |
|-------------------|-----------------|----------|
| `duracao_total_segundos` | `total_duration_seconds` | Métricas de tempo de execução |
| `custo_total` | `total_cost` | Métricas de custo estimado |

#### Referências no OrchestrationGraph

```python
# ANTES
graph = OrchestrationGraph.from_handlers({
    "coletar_contexto": self._coletar_contexto,
    "analisar_contexto": self._analisar_contexto,
    "executar_subagente": self._executar_subagente,
    "validar_resultado": self._validar_resultado,
})

# DEPOIS
graph = OrchestrationGraph.from_handlers({
    "collect_context": self._collect_context,
    "analyze_context": self._analyze_context,
    "execute_subagent": self._execute_subagent,
    "validate_result": self._validate_result,
})
```

---

### 2. business/strategies/generic/orchestrator.py

#### Métodos Renomeados

| Antes (Português) | Depois (Inglês) | Descrição |
|-------------------|-----------------|-----------|
| `_coletar_contexto` | `_collect_context` | Prepara workspace e estrutura básica |
| `_gerar_hipotese` | `_generate_hypothesis` | Gera manifestos placeholder |
| `_validar_resultado` | `_validate_result` | Valida resultados e gera consolidado |

#### Referências no OrchestrationGraph

```python
# ANTES
graph = OrchestrationGraph.from_handlers({
    "coletar_contexto": self._coletar_contexto,
    "gerar_hipotese": self._gerar_hipotese,
    "validar_resultado": self._validar_resultado,
})

# DEPOIS
graph = OrchestrationGraph.from_handlers({
    "collect_context": self._collect_context,
    "generate_hypothesis": self._generate_hypothesis,
    "validate_result": self._validate_result,
})
```

---

### 3. docs/OBSERVABILITY.MD

#### Variáveis de Métricas

Atualizado a documentação para refletir os novos nomes:

```markdown
# ANTES
- `duracao_total_segundos`: tempo da chamada ao LLM
- `custo_total`: cálculo heurístico

# DEPOIS
- `total_duration_seconds`: tempo da chamada ao LLM
- `total_cost`: cálculo heurístico
```

---

### 4. CLAUDE.MD

Atualizado todos os exemplos de código com os novos nomes:

- Métodos: `_generate_hypothesis`, `_validate_hypothesis`, `_collect_context`, etc.
- Handlers nos exemplos de OrchestrationGraph
- Variáveis de estado: `step_1_complete`, `step_2_result`, etc.
- Agent context: `"subagent": "generate_hypothesis"` ao invés de `"gerar_hipotese"`

---

## Verificações Realizadas

### ✅ Framework Directory

Todos os métodos e funções no diretório `framework/` **já estavam em inglês**:
- `framework/core/` ✅
- `framework/io/` ✅
- `framework/llm/` ✅
- `framework/orchestration/` ✅
- `framework/observability/` ✅
- `framework/tools/` ✅

### ✅ Business Directory

Métodos principais renomeados:
- `business/strategies/zeroum/orchestrator.py` ✅
- `business/strategies/generic/orchestrator.py` ✅
- Subagentes (não alterados - classes com nomes descritivos) ✅

### ✅ Scripts

Scripts de execução mantêm compatibilidade:
- `scripts/run_strategy_agent.py` ✅
- Nenhuma alteração necessária

---

## Padrão de Nomenclatura Estabelecido

### Código (INGLÊS)

```python
# ✅ CORRETO - Inglês
class HypothesisGenerator:
    def generate_statement(self, context_description: str) -> str:
        total_duration_seconds = 0
        total_cost = 0.0
        validation_ok = True
```

```python
# ❌ INCORRETO - Português
class GeradorHipotese:
    def gerar_declaracao(self, descricao_contexto: str) -> str:
        duracao_total_segundos = 0
        custo_total = 0.0
        validacao_ok = True
```

### Documentação e Logs (PORTUGUÊS)

```python
# ✅ CORRETO - Docstrings em português, código em inglês
def generate_hypothesis(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Gera declaração de hipótese de negócio.

    Args:
        state: Estado contendo contexto do projeto

    Returns:
        Estado com hipótese gerada
    """
    logger.info("Gerando declaração de hipótese")
    # Código em inglês
    hypothesis_text = self._build_hypothesis(context)
    return {"hypothesis": hypothesis_text}
```

---

## Arquivos Não Alterados (Intencionalmente)

### Documentação Histórica

Os seguintes arquivos em `docs/` contêm referências aos nomes antigos e **não foram alterados** pois são documentos históricos/logs de execução:

- `docs/ORQUESTRADOR_COMPLETO_IMPLEMENTADO.md`
- `docs/ORQUESTRADOR_DINAMICO_IMPLEMENTADO.md`
- `docs/EXECUCAO_AUTOMARTICLES_COMPLETA.md`
- `docs/LOGS_MELHORADOS.md`
- Outros documentos de histórico

**Justificativa**: Estes são registros de versões anteriores e devem permanecer como estavam para rastreabilidade.

### Arquivo Legacy

- `framework/orchestration/langgraph_adapter.py` - Contém nomes em português mas **não é mais usado** no código (substituído por `OrchestrationGraph`)

---

## Impacto nas Execuções

### Retrocompatibilidade

⚠️ **BREAKING CHANGE**: Código que referencia os métodos antigos precisará ser atualizado:

```python
# QUEBRADO - Não funciona mais
orchestrator._coletar_contexto(state)

# CORRETO - Nova nomenclatura
orchestrator._collect_context(state)
```

### Migração

Para migrar código existente:

1. Substitua nomes de métodos conforme tabela acima
2. Atualize referências em `OrchestrationGraph.from_handlers()`
3. Atualize variáveis de métricas (`duracao_total_segundos` → `total_duration_seconds`)
4. Atualize contextos de agente (`"subagent": "gerar_hipotese"` → `"generate_hypothesis"`)

---

## Benefícios

1. **Padronização Internacional**: Código legível para desenvolvedores de qualquer país
2. **Consistência**: Todo código executável em inglês
3. **Manutenibilidade**: Mais fácil para contribuidores externos
4. **Documentação Dupla**: Código em inglês, explicações em português

---

## Próximos Passos

### Opcional (Futuro)

Se necessário, considerar:

1. Atualizar documentação histórica em `docs/` (baixa prioridade)
2. Remover `langgraph_adapter.py` se confirmado que não é mais usado
3. Criar aliases de compatibilidade se necessário (não recomendado)

---

## Contato

Para dúvidas sobre estas mudanças, consulte:
- [CLAUDE.MD](../CLAUDE.MD) - Guia completo do framework
- [framework/README.md](../framework/README.md) - Arquitetura do framework
- [docs/OBSERVABILITY.MD](OBSERVABILITY.MD) - Sistema de monitoramento

---

**Status**: ✅ Concluído em 2025-11-13
