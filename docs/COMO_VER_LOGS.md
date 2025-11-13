# Como Ver os Logs Melhorados do Orquestrador

## Problema

O Python bufferiza a saída por padrão, então os logs podem não aparecer em tempo real quando executado em background.

## Solução: Execute Diretamente no Terminal

### Comando Completo

```bash
source agents/.venv/bin/activate && \
python3 agents/scripts/run_strategy_agent.py zeroum "Automarticles" \
  -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS"
```

### O Que Você Verá

```
19:37:30 | INFO     | __main__                                             | ================================================================================
19:37:30 | INFO     | __main__                                             | Framework Business - Executor de Estratégias
19:37:30 | INFO     | __main__                                             | ================================================================================
19:37:30 | INFO     | __main__                                             | Estratégia: zeroum
19:37:30 | INFO     | __main__                                             | Contexto: Automarticles
19:37:30 | INFO     | __main__                                             | Descrição: Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS
19:37:30 | INFO     | __main__                                             | ================================================================================

# REGISTRY DE SUBAGENTES
19:37:30 | INFO     | agents.business.strategies.zeroum.subagents.registry | Subagente registrado: problem_hypothesis_express (00-ProblemHypothesisExpress)
19:37:30 | INFO     | agents.business.strategies.zeroum.subagents.registry | Subagente registrado: client_delivery (10-ClientDelivery)

# INÍCIO DO GRAFO
19:37:30 | INFO     | agents.framework.orchestration.graph                 | Iniciando execução do grafo a partir de 'coletar_contexto'

# PREPARAÇÃO DO WORKSPACE
19:37:30 | INFO     | agents.business.strategies.zeroum.orchestrator       | Preparando workspace para estratégia ZeroUm
19:37:30 | INFO     | agents.business.strategies.zeroum.orchestrator       | Workspace preparado em /Users/douglasprado/www/framework-business/drive/Automarticles

# ANÁLISE DE CONTEXTO (PENSAMENTO DO ORQUESTRADOR)
19:37:30 | INFO     | agents.business.strategies.zeroum.orchestrator       | Analisando contexto para seleção de subagente...
19:37:32 | INFO     | agents.business.strategies.zeroum.orchestrator       | Análise concluída: Uma plataforma de automação de blogs para PMEs requer validação rápida de hipótese para garantir que resolve um problema real antes de desenvolvimento
19:37:32 | INFO     | agents.business.strategies.zeroum.orchestrator       | Complexidade: simple
19:37:32 | INFO     | agents.business.strategies.zeroum.orchestrator       | Subagente recomendado: problem_hypothesis_express

# EXECUÇÃO DO SUBAGENTE
19:37:32 | INFO     | agents.business.strategies.zeroum.orchestrator       | Executando subagente: problem_hypothesis_express
19:37:32 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Iniciando sessão express Problem Hypothesis (30 min)

# ETAPA 1/5
19:37:32 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Etapa 1/5: Preparar foco da sessão (3 min)
19:37:32 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Preparando foco da sessão
19:37:35 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Foco da sessão salvo em /path/to/01-foco-sessao.MD

# ETAPA 2/5
19:37:35 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Etapa 2/5: Mapear usuários-alvo imediatos (5 min)
19:37:35 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Mapeando usuários-alvo imediatos
19:37:40 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Usuários-alvo salvos em /path/to/02-usuarios-alvo.MD

# ETAPA 3/5
19:37:40 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Etapa 3/5: Identificar a dor central (7 min)
19:37:40 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Identificando dor central
19:37:50 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Dor central salva em /path/to/03-dor-central.MD

# ETAPA 4/5
19:37:50 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Etapa 4/5: Redigir e testar variações (10 min)
19:37:50 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Criando variações da frase de proposta de valor
19:38:00 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Variações salvas em /path/to/04-variacoes-proposta.MD

# ETAPA 5/5
19:38:00 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Etapa 5/5: Preparar validação (5 min)
19:38:00 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Preparando materiais de validação
19:38:10 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Guia de validação salvo em /path/to/05-guia-validacao.MD
19:38:10 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Template de log criado em /path/to/06-log-versoes-feedback.MD

# CONSOLIDAÇÃO
19:38:10 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Gerando documento consolidado
19:38:10 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Documento consolidado salvo em /path/to/00-sessao-consolidada.MD
19:38:10 | INFO     | agents.business.strategies.zeroum.subagents.problem_hypothesis_express | Sessão express concluída com sucesso

# FINALIZAÇÃO
19:38:10 | INFO     | agents.business.strategies.zeroum.orchestrator       | Subagente problem_hypothesis_express executado com sucesso
19:38:10 | INFO     | agents.business.strategies.zeroum.orchestrator       | Consolidado salvo em /path/to/00-consolidado.MD
19:38:10 | INFO     | agents.business.strategies.zeroum.orchestrator       | Pacote final gerado em /path/to/Automarticles_ZeroUm_outputs.zip
19:38:10 | INFO     | agents.framework.orchestration.graph                 | Nó final alcançado: validar_resultado
19:38:10 | INFO     | agents.framework.orchestration.graph                 | Execução do grafo concluída. Visitados 4 nós.
19:38:10 | INFO     | agents.business.strategies.zeroum.orchestrator       | Estratégia ZeroUm concluída em 40.25s

# RESUMO FINAL
19:38:10 | INFO     | __main__                                             |
19:38:10 | INFO     | __main__                                             | ================================================================================
19:38:10 | INFO     | __main__                                             | EXECUÇÃO CONCLUÍDA COM SUCESSO
19:38:10 | INFO     | __main__                                             | ================================================================================
19:38:10 | INFO     | __main__                                             |
19:38:10 | INFO     | __main__                                             | DECISÃO DO ORQUESTRADOR:
19:38:10 | INFO     | __main__                                             |   Complexidade detectada: simple
19:38:10 | INFO     | __main__                                             |   Subagente selecionado: problem_hypothesis_express
19:38:10 | INFO     | __main__                                             |
19:38:10 | INFO     | __main__                                             | SUBAGENTES EXECUTADOS:
19:38:10 | INFO     | __main__                                             |   1. problem_hypothesis_express
19:38:10 | INFO     | __main__                                             |      Status: completed
19:38:10 | INFO     | __main__                                             |      Início: 2025-11-12 19:37:30
19:38:10 | INFO     | __main__                                             |      Fim: 2025-11-12 19:38:10
19:38:10 | INFO     | __main__                                             |      Notas: Subagente selecionado automaticamente. Uma plataforma de automação de blogs para PMEs requer validação rápida...
19:38:10 | INFO     | __main__                                             |      Estágios executados: 5
19:38:10 | INFO     | __main__                                             |        ✓ stage_1_define_focus
19:38:10 | INFO     | __main__                                             |        ✓ stage_2_map_users
19:38:10 | INFO     | __main__                                             |        ✓ stage_3_identify_pain
19:38:10 | INFO     | __main__                                             |        ✓ stage_4_create_variations
19:38:10 | INFO     | __main__                                             |        ✓ stage_5_prepare_validation
19:38:10 | INFO     | __main__                                             |      Artefatos gerados: 7 arquivos
19:38:10 | INFO     | __main__                                             |
19:38:10 | INFO     | __main__                                             | ARQUIVOS GERADOS:
19:38:10 | INFO     | __main__                                             |   Consolidado: /path/to/drive/Automarticles/00-consolidado.MD
19:38:10 | INFO     | __main__                                             |   Pacote ZIP: /path/to/drive/Automarticles/Automarticles_ZeroUm_outputs.zip
19:38:10 | INFO     | __main__                                             |
19:38:10 | INFO     | __main__                                             | MÉTRICAS:
19:38:10 | INFO     | __main__                                             |   zeroum_strategy: 40.25
```

## Explicação dos Logs

### 1. Formato do Log

```
HORA     | NÍVEL    | MÓDULO                                               | MENSAGEM
19:37:30 | INFO     | agents.orchestrator                                  | Analisando contexto...
```

**Colunas**:
- **HORA**: Timestamp em HH:MM:SS
- **NÍVEL**: INFO/WARNING/ERROR
- **MÓDULO**: De onde veio o log (orchestrator, subagents, graph, registry)
- **MENSAGEM**: O que aconteceu

### 2. Fluxo do Orquestrador

Os logs mostram exatamente o que o orquestrador está fazendo:

1. **Registry**: Registra subagentes disponíveis
2. **Grafo**: Inicia execução do pipeline
3. **Workspace**: Prepara diretórios
4. **Análise**: LLM analisa contexto e decide complexidade
5. **Seleção**: Escolhe subagente apropriado
6. **Execução**: Roda o subagente escolhido
7. **Consolidação**: Gera relatório final

### 3. Pensamento do Orquestrador

A análise de contexto mostra como o LLM "pensa":

```
Analisando contexto para seleção de subagente...
Análise concluída: Uma plataforma de automação de blogs para PMEs requer
validação rápida de hipótese para garantir que resolve um problema real
Complexidade: simple
Subagente recomendado: problem_hypothesis_express
```

### 4. Progresso do Subagente

Cada etapa é registrada em tempo real:

```
Etapa 1/5: Preparar foco da sessão (3 min)
Etapa 2/5: Mapear usuários-alvo imediatos (5 min)
Etapa 3/5: Identificar a dor central (7 min)
Etapa 4/5: Redigir e testar variações (10 min)
Etapa 5/5: Preparar validação (5 min)
```

### 5. Artefatos Criados

Cada arquivo salvo é registrado:

```
Foco da sessão salvo em .../01-foco-sessao.MD
Usuários-alvo salvos em .../02-usuarios-alvo.MD
Dor central salva em .../03-dor-central.MD
Variações salvas em .../04-variacoes-proposta.MD
Guia de validação salvo em .../05-guia-validacao.MD
Template de log criado em .../06-log-versoes-feedback.MD
Documento consolidado salvo em .../00-sessao-consolidada.MD
```

### 6. Resumo Final

No final, você vê um resumo completo:

- Decisão do orquestrador (complexidade + subagente)
- Subagentes executados (status, início, fim, notas)
- Estágios executados (com ✓ ou ✗)
- Arquivos gerados (consolidado + ZIP)
- Métricas (tempo total)

## Comando Alternativo: Ver Apenas Resumo

Se você quiser ver apenas o resumo final sem todos os logs:

```bash
source agents/.venv/bin/activate && \
python3 agents/scripts/run_strategy_agent.py zeroum "Automarticles" \
  -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS" \
  --quiet
```

Isso exibe apenas o JSON final.

## Comando Alternativo: Salvar em Arquivo

Para salvar o resultado em JSON:

```bash
source agents/.venv/bin/activate && \
python3 agents/scripts/run_strategy_agent.py zeroum "Automarticles" \
  -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS" \
  --output resultado.json
```

Depois você pode ver:

```bash
cat resultado.json | jq '.'
```

## Melhorias Futuras Possíveis

1. **Logs Coloridos**: Usar `colorlog` para diferentes cores por nível
2. **Progress Bar**: Barra de progresso para etapas longas
3. **Verbose Levels**: -v, -vv, -vvv para mais detalhes
4. **Log File Auto**: Salvar automaticamente em `drive/<nome>/_logs/execution.log`
5. **Streaming JSON**: Logs em formato JSON para parsing automatizado

## Conclusão

Os logs agora fornecem **transparência total** sobre:

- ✅ Como o orquestrador pensa e decide
- ✅ Qual subagente foi selecionado e por quê
- ✅ Cada etapa sendo executada em tempo real
- ✅ Todos os artefatos sendo criados
- ✅ Métricas de tempo e performance

Execute o comando no seu terminal para ver em ação!
