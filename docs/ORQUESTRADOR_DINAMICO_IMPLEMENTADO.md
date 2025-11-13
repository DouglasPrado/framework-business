# Orquestrador Dinâmico ZeroUm - Implementado

## Resumo

O orquestrador ZeroUm agora possui capacidade de seleção dinâmica de subagentes baseada em análise de contexto usando LLM.

## Arquitetura Implementada

### Fluxo de Execução

```
1. coletar_contexto
   - Prepara workspace
   - Garante estrutura de diretórios

2. analisar_contexto (NOVO)
   - Usa LLM para analisar descrição do contexto
   - Classifica complexidade (simple/moderate/complex)
   - Recomenda subagente mais apropriado
   - Justifica escolha

3. executar_subagente (NOVO)
   - Obtém classe do SubagentRegistry
   - Instancia subagente com parâmetros corretos
   - Executa método apropriado
   - Captura resultados e erros

4. validar_resultado
   - Gera consolidado
   - Empacota artefatos
   - Retorna manifests
```

### Componentes Principais

#### 1. SubagentRegistry

**Arquivo**: `agents/business/strategies/zeroum/subagents/registry.py`

**Responsabilidades**:
- Registro centralizado de subagentes disponíveis
- Descoberta por nome, complexidade ou process_code
- Metadados de cada subagente (descrição, duração, complexidade)

**Subagentes Registrados**:
- `problem_hypothesis_express`: Processo 00-ProblemHypothesisExpress (simple, 30 min)
- `client_delivery`: Processo 10-ClientDelivery (complex, variável)

#### 2. Método _analisar_contexto()

**Arquivo**: `agents/business/strategies/zeroum/orchestrator.py:134-223`

**Funcionamento**:
1. Constrói prompt com contexto do usuário
2. Lista todos os subagentes disponíveis do registry
3. Solicita ao LLM análise e recomendação em formato JSON
4. Parse da resposta (com fallback robusto)
5. Atualiza estado com: complexity, selected_subagent, analysis_reasoning

**Prompt enviado ao LLM**:
```
Você é um especialista em metodologia ZeroUm...

Contexto:
- Nome: [context_name]
- Descrição: [context_description]

Subagentes disponíveis:
- problem_hypothesis_express: ...
- client_delivery: ...

Responda com JSON:
{
  "complexity": "simple|moderate|complex",
  "recommended_subagent": "nome_do_subagente",
  "reasoning": "Justificativa..."
}
```

#### 3. Método _executar_subagente()

**Arquivo**: `agents/business/strategies/zeroum/orchestrator.py:225-296`

**Funcionamento**:
1. Obtém nome do subagente selecionado do estado
2. Recupera classe do SubagentRegistry
3. Instancia com parâmetros corretos baseado no tipo:
   - `problem_hypothesis_express`: workspace_root, idea_context, target_audience, enable_tools
   - `client_delivery`: workspace_root, client_name, delivery_scope, deadline, enable_tools
4. Executa método apropriado (execute_express_session ou execute_full_delivery)
5. Cria manifest com resultados
6. Tratamento de erros com manifest de falha

#### 4. Modificações no run()

**Arquivo**: `agents/business/strategies/zeroum/orchestrator.py:62-108`

**Mudanças**:
- Pipeline antigo: coletar_contexto → gerar_hipotese → validar_resultado
- Pipeline novo: coletar_contexto → analisar_contexto → executar_subagente → validar_resultado
- Retorno adicional: selected_subagent, complexity

### Integração de Tools

Ambos os subagentes agora suportam tools do framework:

**Subagentes modificados**:
- `ProblemHypothesisExpressAgent` (agents/business/strategies/zeroum/subagents/problem_hypothesis_express.py)
- `ClientDeliveryAgent` (agents/business/strategies/zeroum/subagents/client_delivery.py)

**Tools disponíveis** (via `get_tools(AgentType.PROCESS)`):
- FILE_SYSTEM: ls, read_file, write_file, edit_file
- SEARCH: grep_search (busca em arquivos)
- CONTENT: generate_content (geração via LLM)

**Parâmetro**: `enable_tools=True` (padrão em ambos)

## Testes

### Script de Teste

**Arquivo**: `agents/business/examples/dynamic_orchestrator_example.py`

**Cenários de teste**:

1. **Contexto Simples** (ValidacaoIdeiaRapida)
   - Descrição: Validar ideia de plataforma
   - Expectativa: Selecionar `problem_hypothesis_express`
   - Resultado: 7 documentos gerados em 30 minutos simulados

2. **Contexto Complexo** (EntregaProjetoCompleto)
   - Descrição: Entrega completa com handoff, onboarding, planejamento, produção, entrega, pós-entrega
   - Expectativa: Selecionar `client_delivery`
   - Resultado: 11 documentos gerados em 6 etapas

### Executar Testes

```bash
# Ativar ambiente virtual
source agents/.venv/bin/activate

# Executar teste do orquestrador dinâmico
python3 agents/business/examples/dynamic_orchestrator_example.py
```

### Saída Esperada

```
================================================================================
TESTES DO ORQUESTRADOR DINÂMICO ZEROUM
================================================================================

Teste 1: Contexto Simples - Validação de Ideia
Executando orquestrador com análise automática de contexto...

Complexidade detectada: simple
Subagente selecionado: problem_hypothesis_express
Status: completed

Teste 2: Contexto Complexo - Entrega ao Cliente
Executando orquestrador com análise automática de contexto...

Complexidade detectada: complex
Subagente selecionado: client_delivery
Status: completed

Todos os testes passaram!
```

## Benefícios da Implementação

### 1. Roteamento Inteligente
- LLM analisa contexto e seleciona processo mais adequado
- Não precisa especificar manualmente qual subagente usar
- Adaptação automática à complexidade do problema

### 2. Extensibilidade
- Novos subagentes podem ser registrados facilmente
- Registry centralizado facilita descoberta
- Metadados permitem filtragem por complexidade/duração

### 3. Observabilidade
- Justificativa da escolha registrada no manifest
- Métricas de execução capturadas
- Logs detalhados em cada etapa

### 4. Resiliência
- Fallback robusto em caso de erro no parsing
- Manifests de erro quando subagente falha
- Tratamento de exceções em cada etapa

## Próximos Passos

### Melhorias Sugeridas

1. **Roteamento Condicional no Grafo**
   - Usar `add_edge(condition=...)` do OrchestrationGraph
   - Permitir múltiplos caminhos baseados em complexity
   - Suportar combinação de subagentes

2. **Cache de Análises**
   - Evitar re-análise para contextos similares
   - Acelerar execução para casos conhecidos

3. **Métricas de Precisão**
   - Rastrear se seleção foi apropriada
   - Feedback humano para treinar escolhas futuras

4. **Subagentes Adicionais**
   - Implementar todos os 12 processos do ZeroUm
   - Registrar no SubagentRegistry
   - Adicionar handlers em _executar_subagente

5. **Modo Interativo**
   - Perguntar ao usuário se deseja confirmar escolha
   - Permitir override manual do subagente
   - Mostrar raciocínio antes de executar

## Estrutura de Arquivos

```
agents/business/strategies/zeroum/
├── orchestrator.py (MODIFICADO)
│   ├── run() - Pipeline dinâmico
│   ├── _analisar_contexto() - Análise com LLM (NOVO)
│   └── _executar_subagente() - Execução dinâmica (NOVO)
├── subagents/
│   ├── __init__.py (MODIFICADO - exporta SubagentRegistry)
│   ├── registry.py (NOVO)
│   │   ├── SubagentRegistry.register()
│   │   ├── SubagentRegistry.get()
│   │   ├── SubagentRegistry.list_available()
│   │   └── SubagentRegistry.find_by_complexity()
│   ├── problem_hypothesis_express.py (MODIFICADO - tools)
│   └── client_delivery.py (MODIFICADO - tools)
└── examples/
    └── dynamic_orchestrator_example.py (NOVO)
```

## Código Exemplo de Uso

```python
from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator

# Criar orquestrador
orchestrator = ZeroUmOrchestrator(
    context_name="MinhaIdeia",
    context_description="""
    Quero criar uma plataforma de automação de marketing
    para pequenas empresas. Preciso validar se isso resolve
    um problema real antes de investir no desenvolvimento.
    """
)

# Executar (análise e seleção automática)
results = orchestrator.run()

# Verificar resultados
print(f"Subagente selecionado: {results['selected_subagent']}")
print(f"Complexidade: {results['complexity']}")
print(f"Consolidado: {results['consolidated']}")
print(f"Pacote: {results['archive']}")
```

## Logs de Execução

Exemplo de logs durante execução:

```
INFO: Preparando workspace para estratégia ZeroUm
INFO: Workspace preparado em /path/to/drive/MinhaIdeia
INFO: Analisando contexto para seleção de subagente...
INFO: Análise concluída: Contexto indica necessidade de validação rápida de hipótese
INFO: Complexidade: simple
INFO: Subagente recomendado: problem_hypothesis_express
INFO: Executando subagente: problem_hypothesis_express
INFO: Iniciando Problem Hypothesis Express Agent
INFO: Etapa 1/5: Definindo foco da sessão (6 min)...
...
INFO: Subagente problem_hypothesis_express executado com sucesso
INFO: Consolidado salvo em /path/to/drive/MinhaIdeia/00-consolidado.MD
INFO: Pacote final gerado em /path/to/drive/MinhaIdeia/MinhaIdeia_ZeroUm_outputs.zip
INFO: Estratégia ZeroUm concluída em 45.32s
```

## Resumo de Alterações

### Arquivos Criados (3)
1. `agents/business/strategies/zeroum/subagents/registry.py` - Registry de subagentes
2. `agents/business/examples/dynamic_orchestrator_example.py` - Testes
3. `ORQUESTRADOR_DINAMICO_IMPLEMENTADO.md` - Esta documentação

### Arquivos Modificados (4)
1. `agents/business/strategies/zeroum/orchestrator.py` - Análise e roteamento dinâmico
2. `agents/business/strategies/zeroum/subagents/__init__.py` - Export do registry
3. `agents/business/strategies/zeroum/subagents/problem_hypothesis_express.py` - Tools
4. `agents/business/strategies/zeroum/subagents/client_delivery.py` - Tools

### Linhas Adicionadas
- orchestrator.py: +170 linhas (métodos novos)
- registry.py: +198 linhas (novo arquivo)
- dynamic_orchestrator_example.py: +180 linhas (novo arquivo)
- Total: ~550 linhas de código novo

## Conclusão

O orquestrador ZeroUm agora é totalmente dinâmico e capaz de:

1. Analisar contexto automaticamente usando LLM
2. Classificar complexidade (simple/moderate/complex)
3. Selecionar subagente mais apropriado do registry
4. Executar subagente dinamicamente com parâmetros corretos
5. Capturar resultados e gerar consolidado
6. Tratar erros com fallbacks robustos

A implementação está completa, testada e documentada.
