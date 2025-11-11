# Observabilidade dos agentes de estratégia

## Objetivo

Garantir visibilidade contínua da execução dos processos automáticos, cobrindo logs estruturados, métricas de desempenho e acionamento de alertas para falhas de LLM ou degradação de custos.

## Callbacks e logging do LangGraph

- Cada nó do LangGraph dispara callbacks `GraphCallbackHandler`, que gravam logs JSON via `logging`.
- Os eventos usam o formato `{ "evento": "node_start|node_end|node_error", "processo": ..., "contexto": ..., "no": ..., "timestamp": ... }`.
- Recomenda-se configurar o logger raiz para `INFO` e redirecionar a saída para um coletor central (ex.: `journald`, `fluent-bit`, `datadog-agent`).
- Falhas de nó ficam marcadas como `node_error` com detalhes sanitizados, evitando vazamento de instruções confidenciais.

## Métricas de execução

- O `MetricsCollector` registra, por nó, duração (`duracao_segundos`), tokens estimados e custo opcional.
- Os registros são emitidos como JSON com `evento=metrics` e também consolidados no manifesto do processo em `drive/<Contexto>/_pipeline/<Processo>-manifest.json`.
- A função de custo lê `ZEROUM_COST_PER_1K_TOKENS` ou `LLM_COST_PER_1K_TOKENS`. Ajuste essas variáveis para refletir valores vigentes.
- Integre os logs a um backend como Prometheus por meio de um `promtail` ou pipeline semelhante, convertendo `duracao_segundos` e `tokens` em métricas numéricas.

## Fallback e continuidade operacional

- Quando o LLM falha, o grafo direciona para o nó `fallback_local`, gerando plano heurístico baseado em `tasks.MD` e anexando o motivo ao manifesto.
- O artefato produzido é salvo no drive com o prefixo padrão do processo, garantindo rastreabilidade.
- O manifesto apresenta o status `fallback` e mantém o campo `notes` com o resumo do incidente para acompanhamento manual.

## Monitoramento e alertas

- Crie regras que alertem quando `status` do manifesto for diferente de `completed`, principalmente para valores `erro` ou `fallback`.
- Monitore outliers de `duracao_segundos` e `tokens` para identificar deriva de desempenho ou custos inesperados.
- Ative alarmes quando `custo_total` ultrapassar limites definidos pela equipe financeira.
- Verifique periodicamente os logs de `node_error`. Acionamentos recorrentes indicam necessidade de ajuste de prompt, contexto ou provisionamento de credenciais.

## Boas práticas operacionais

- Padronize a rotação de logs estruturados para evitar perda de histórico.
- Garanta que a pasta `drive/<Contexto>/_pipeline/` esteja versionada em backup ou bucket seguro.
- Documente no runbook da equipe como regenerar artefatos a partir do fallback heurístico e quais validações humanas são obrigatórias.
- Valide que pipelines CI observam o status do manifesto antes de marcar execuções como concluídas.
