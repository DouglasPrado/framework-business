# Guia de Migração - Português para Inglês

## Guia Rápido de Atualização

Este guia ajuda a migrar código existente para usar os novos nomes de métodos em inglês.

---

## 🔄 Find & Replace

Use o comando abaixo para atualizar seu código automaticamente:

### Para Orquestradores

```bash
# Substituir métodos no seu código
sed -i '' 's/_coletar_contexto/_collect_context/g' seu_arquivo.py
sed -i '' 's/_analisar_contexto/_analyze_context/g' seu_arquivo.py
sed -i '' 's/_executar_subagente/_execute_subagent/g' seu_arquivo.py
sed -i '' 's/_gerar_hipotese/_generate_hypothesis/g' seu_arquivo.py
sed -i '' 's/_validar_resultado/_validate_result/g' seu_arquivo.py
```

### Para Variáveis de Métricas

```bash
sed -i '' 's/duracao_total_segundos/total_duration_seconds/g' seu_arquivo.py
sed -i '' 's/custo_total/total_cost/g' seu_arquivo.py
```

---

## 📋 Checklist de Migração

### Passo 1: Métodos do Orquestrador

- [ ] Substituir `_coletar_contexto` por `_collect_context`
- [ ] Substituir `_analisar_contexto` por `_analyze_context`
- [ ] Substituir `_executar_subagente` por `_execute_subagent`
- [ ] Substituir `_gerar_hipotese` por `_generate_hypothesis`
- [ ] Substituir `_validar_resultado` por `_validate_result`

### Passo 2: Handlers do OrchestrationGraph

Atualizar dicionário de handlers:

```python
# ANTES ❌
graph = OrchestrationGraph.from_handlers({
    "coletar_contexto": self._coletar_contexto,
    "gerar_hipotese": self._gerar_hipotese,
    "validar_resultado": self._validar_resultado,
})

# DEPOIS ✅
graph = OrchestrationGraph.from_handlers({
    "collect_context": self._collect_context,
    "generate_hypothesis": self._generate_hypothesis,
    "validate_result": self._validate_result,
})
```

### Passo 3: Variáveis de Métricas

```python
# ANTES ❌
metrics = manifest.get("metrics") or {}
duration = metrics.get("duracao_total_segundos")
cost = metrics.get("custo_total")

# DEPOIS ✅
metrics = manifest.get("metrics") or {}
duration = metrics.get("total_duration_seconds")
cost = metrics.get("total_cost")
```

### Passo 4: Contexto de Agente

```python
# ANTES ❌
llm = build_llm({
    "agent_context": {
        "subagent": "gerar_hipotese"
    }
})

# DEPOIS ✅
llm = build_llm({
    "agent_context": {
        "subagent": "generate_hypothesis"
    }
})
```

---

## 🔍 Exemplos Completos

### Exemplo 1: Orquestrador Simples

#### ANTES ❌

```python
class MeuOrchestrator:
    def run(self):
        graph = OrchestrationGraph.from_handlers({
            "coletar": self._coletar_contexto,
            "gerar": self._gerar_hipotese,
            "validar": self._validar_resultado,
        })
        return graph.execute()

    def _coletar_contexto(self, state):
        # Lógica
        return state

    def _gerar_hipotese(self, state):
        # Lógica
        return state

    def _validar_resultado(self, state):
        duracao = state.get("duracao_total_segundos")
        custo = state.get("custo_total")
        return state
```

#### DEPOIS ✅

```python
class MeuOrchestrator:
    def run(self):
        graph = OrchestrationGraph.from_handlers({
            "collect": self._collect_context,
            "generate": self._generate_hypothesis,
            "validate": self._validate_result,
        })
        return graph.execute()

    def _collect_context(self, state):
        # Lógica
        return state

    def _generate_hypothesis(self, state):
        # Lógica
        return state

    def _validate_result(self, state):
        duration = state.get("total_duration_seconds")
        cost = state.get("total_cost")
        return state
```

### Exemplo 2: Subagente Customizado

#### ANTES ❌

```python
@SubagentRegistry.register("meu_subagente")
class MeuSubagente:
    def executar(self, state):
        llm = build_llm({
            "agent_context": {
                "subagent": "meu_subagente"
            }
        })
        resultado = self._gerar_conteudo(state)
        return {"resultado": resultado}

    def _gerar_conteudo(self, state):
        # Lógica
        pass
```

#### DEPOIS ✅

```python
@SubagentRegistry.register("my_subagent")
class MySubagent:
    def execute(self, state):
        llm = build_llm({
            "agent_context": {
                "subagent": "my_subagent"
            }
        })
        result = self._generate_content(state)
        return {"result": result}

    def _generate_content(self, state):
        # Lógica
        pass
```

---

## ⚠️ Erros Comuns

### Erro 1: AttributeError

```
AttributeError: 'ZeroUmOrchestrator' object has no attribute '_coletar_contexto'
```

**Causa**: Tentando chamar método com nome antigo

**Solução**: Atualizar para `_collect_context`

### Erro 2: KeyError em Metrics

```
KeyError: 'duracao_total_segundos'
```

**Causa**: Tentando acessar métrica com nome antigo

**Solução**: Atualizar para `total_duration_seconds`

### Erro 3: Handler não encontrado

```
KeyError: 'coletar_contexto' not found in graph handlers
```

**Causa**: Handler registrado com nome antigo no OrchestrationGraph

**Solução**: Atualizar chaves do dicionário de handlers

---

## 🧪 Testando as Mudanças

Após migrar, execute:

```bash
# Testar estratégia ZeroUm
python scripts/run_strategy_agent.py zeroum TestMigration \
  -d "Teste de migração"

# Verificar se não há erros de AttributeError ou KeyError
```

---

## 📚 Referências

- [RENAMING_SUMMARY.MD](RENAMING_SUMMARY.MD) - Resumo completo das mudanças
- [CLAUDE.MD](../CLAUDE.MD) - Guia atualizado do framework
- [OBSERVABILITY.MD](OBSERVABILITY.MD) - Documentação de métricas atualizada

---

## ❓ FAQ

**P: Preciso atualizar logs e comentários?**
R: Não, apenas código executável (funções, métodos, variáveis). Logs e comentários podem permanecer em português.

**P: E a documentação em docs/?**
R: Documentos históricos não foram atualizados intencionalmente para preservar rastreabilidade.

**P: Tem retrocompatibilidade?**
R: Não, esta é uma breaking change. Todo código deve ser atualizado.

**P: Posso criar aliases para os nomes antigos?**
R: Tecnicamente sim, mas não é recomendado. Melhor migrar completamente.

---

**Última atualização**: 2025-11-13
