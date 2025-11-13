# ProcessTemplateFiller - Guia de Uso

## Visão Geral

`ProcessTemplateFiller` é um utilitário que preenche templates de processos usando LLM para interpretar o contexto gerado por subagentes e preencher campos de forma inteligente.

**Localização**: `agents/business/strategies/zeroum/subagents/template_filler.py`

## Quando Usar

✅ **USE quando**:

1. Você tem templates BASE com placeholders/campos vazios em `process/<Strategy>/<Process>/_DATA/`
2. Você executou um subagente que gerou CONTEXTO (análises, dados, insights)
3. Você quer usar o LLM para preencher os templates automaticamente com base no contexto
4. Você precisa gerar múltiplos documentos formatados a partir do mesmo contexto

### Exemplo de Uso Correto

```python
from agents.business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

# Subagente executou e gerou contexto consolidado
context = """
Problema identificado: PMEs gastam 15h/semana criando conteúdo manualmente
Solução proposta: Plataforma de automação com IA
Público-alvo: Donos de e-commerce B2C com 10-50 produtos
"""

# Templates BASE existem em process/ZeroUm/ProblemHypothesisExpress/_DATA/
# Exemplos: 01-problema-hipotese.MD, 02-publico-alvo.MD

# Criar filler
filler = ProcessTemplateFiller(
    process_code="ProblemHypothesisExpress",
    output_dir=Path("drive/MeuContexto/00-ProblemHypothesisExpress"),
    strategy_name="ZeroUm",
)

# Definir tarefas de preenchimento
tasks = [
    TemplateTask(
        template="01-problema-hipotese.MD",
        instructions="Preencha com dados específicos do problema e solução identificados",
        output_name="01-problema-hipotese.MD",
    ),
    TemplateTask(
        template="02-publico-alvo.MD",
        instructions="Descreva o público-alvo com base nos dados coletados",
        output_name="02-publico-alvo.MD",
    ),
]

# Preencher templates
filled_paths = filler.fill_templates(tasks, context)
# Resultado: drive/MeuContexto/00-ProblemHypothesisExpress/01-problema-hipotese.MD (preenchido)
#            drive/MeuContexto/00-ProblemHypothesisExpress/02-publico-alvo.MD (preenchido)
```

## Quando NÃO Usar

❌ **NÃO USE quando**:

1. **Seu subagente já gera documentos completos diretamente**
   - Exemplo: `ClientDelivery` tem 6 estágios que criam documentos finais
   - Usar `ProcessTemplateFiller` após isso seria redundante

2. **Você não tem templates BASE com estrutura definida**
   - O filler precisa de templates para preencher
   - Se não existem templates em `_DATA/`, não há o que preencher

3. **Você precisa de lógica de negócio complexa para gerar conteúdo**
   - O filler é bom para preenchimento "formulário-like"
   - Para lógica complexa (cálculos, validações, formatações especiais), implemente diretamente no subagente

### Exemplo de Uso INCORRETO

```python
# ❌ ERRADO: ClientDelivery já gerou tudo
class ClientDeliveryAgent(ZeroUmSubagent):
    def execute_full_delivery(self, results):
        # Estágio 1-6: Geram documentos completos
        self._research_problem_solution(results)  # Gera 01-pesquisa-problema-solucao.MD
        self._generate_value_proposition(results)  # Gera 02-proposta-valor.MD
        # ... outros estágios ...

        # ❌ REDUNDANTE: Documentos já foram criados acima
        self._fill_data_templates(results)  # Tentaria preencher templates que não existem
```

## Como Funciona Internamente

### 1. Construção do Caminho dos Templates

```python
# template_filler.py linha 48
repo_root = Path(__file__).resolve().parents[5]
self.templates_root = repo_root / "process" / strategy_name / process_code / "_DATA"
```

**Estrutura esperada**:
```
framework-business/
└── process/
    └── ZeroUm/
        └── ProblemHypothesisExpress/
            └── _DATA/
                ├── 01-problema-hipotese.MD  ← Template BASE
                └── 02-publico-alvo.MD       ← Template BASE
```

### 2. Invocação do LLM

```python
# template_filler.py linha 85
response = self.llm.invoke(prompt)
```

O prompt contém:
- **Contexto consolidado**: Saída do subagente
- **Instruções personalizadas**: Como preencher
- **Template base**: Estrutura a ser preenchida
- **Regras**: Preservar estrutura, usar português, não deixar campos vazios

### 3. Salvamento do Resultado

```python
# template_filler.py linha 96-98
output_path = self.output_dir / output_rel
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(filled_text.strip() + "\n", encoding="utf-8")
```

**Estrutura gerada**:
```
framework-business/
└── drive/
    └── MeuContexto/
        └── 00-ProblemHypothesisExpress/
            ├── 01-problema-hipotese.MD  ← Template PREENCHIDO
            └── 02-publico-alvo.MD       ← Template PREENCHIDO
```

## Configuração de LLM

Por padrão, usa `build_llm()` que pode ser customizado:

```python
from agents.framework.llm.factory import build_llm

# LLM customizado
custom_llm = build_llm({"model": "gpt-4", "temperature": 0.5})

filler = ProcessTemplateFiller(
    process_code="MeuProcesso",
    output_dir=output_dir,
    llm=custom_llm,  # LLM customizado
)
```

## Vantagens

1. **Consistência**: Todos os documentos seguem a mesma estrutura dos templates
2. **Eficiência**: LLM preenche automaticamente baseado no contexto
3. **Escalabilidade**: Múltiplos templates preenchidos com uma única chamada
4. **Manutenibilidade**: Templates BASE centralizados em `process/`

## Desvantagens

1. **Dependência de LLM**: Custo de API e possível variação na qualidade
2. **Rigidez**: Templates precisam existir previamente em `_DATA/`
3. **Contexto limitado**: LLM só tem acesso ao contexto fornecido
4. **Sem validação de negócio**: Não executa lógica complexa, apenas preenchimento

## Recomendações

### Para Processos Simples (Formulários, Relatórios Padronizados)

✅ **USE ProcessTemplateFiller**

Crie templates BASE em `process/<Strategy>/<Process>/_DATA/` e use o filler para preencher.

### Para Processos Complexos (Múltiplos Estágios, Lógica de Negócio)

❌ **NÃO USE ProcessTemplateFiller**

Implemente a geração de documentos diretamente no subagente, como faz `ClientDelivery`.

### Arquitetura Híbrida (Recomendada)

Combine ambas as abordagens:

```python
class MeuSubagente(ZeroUmSubagent):
    def execute(self, context):
        # Estágio 1: Pesquisa e análise (lógica complexa)
        research_data = self._complex_research()

        # Estágio 2: Gerar relatório técnico (documento complexo)
        self._generate_technical_report(research_data)

        # Estágio 3: Preencher templates padrão (formulários simples)
        context_text = self._build_context(research_data)
        filler = ProcessTemplateFiller(...)
        filler.fill_templates([
            TemplateTask("01-sumario-executivo.MD", ...),
            TemplateTask("02-recomendacoes.MD", ...),
        ], context_text)
```

## Troubleshooting

### Erro: Template não encontrado

```
FileNotFoundError: Template 'XX.MD' não encontrado em /path/to/_DATA
```

**Solução**: Verifique se o template BASE existe em `process/<Strategy>/<Process>/_DATA/`

### Erro: Output em formato incorreto

**Problema**: LLM retorna JSON, lista ou formato inesperado

**Solução**: Verificar linhas 87-93 de `template_filler.py` - já trata listas e objetos

### Aviso: Contexto muito grande

**Problema**: Contexto excede limite de tokens do LLM

**Solução**:
1. Resuma o contexto antes de passar ao filler
2. Use LLM com janela maior (gpt-4-turbo, claude-3)
3. Divida em múltiplas chamadas com contexto específico por template

## Conclusão

`ProcessTemplateFiller` é uma ferramenta poderosa para **preenchimento automatizado de templates estruturados**.

- ✅ Use para documentos padronizados baseados em templates
- ❌ Não use quando o subagente já gera documentos completos
- 🎯 Combine ambas as abordagens para máxima flexibilidade

## Referências

- **Código fonte**: `agents/business/strategies/zeroum/subagents/template_filler.py`
- **Exemplo de uso**: `agents/tests/test_template_filler.py`
- **Templates BASE**: `process/ZeroUm/<Process>/_DATA/`
- **Documentos gerados**: `drive/<Context>/<Process>/`
