# Observabilidade dos agents

## Visão Geral

Os subagentes utilizam o runtime oficial do LangChain DeepAgents. Toda a instrumentação detalhada (ações, ferramentas invocadas, custo real de tokens) pode ser encaminhada automaticamente para o LangSmith/LangChain Tracing, de forma que não precisamos manter callbacks customizados.

## Como habilitar LangSmith / Tracing

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
export LANGCHAIN_API_KEY="sua-chave"
export LANGCHAIN_PROJECT="framework-business"
```

Com essas variáveis configuradas, o `StrategyAgent` e cada `ProcessAgent` geram um `llm_config` com `observability` preenchido. O `build_llm()` adiciona automaticamente `LangChainTracer` e `LangSmithCallbackHandler`, fazendo com que todo o fluxo apareça no painel do LangSmith (incluindo chamadas reflexivas, ferramentas e custo).

## Métricas locais

Mesmo usando LangSmith, o manifesto do processo continua registrando:

- `duracao_total_segundos`: tempo da chamada ao LLM
- `total_tokens`: valor retornado pelo agente (ou estimado)
- `custo_total`: cálculo heurístico usando `ZEROUM_COST_PER_1K_TOKENS` / `LLM_COST_PER_1K_TOKENS`

Essas informações ficam em `drive/<Contexto>/_pipeline/<Processo>-manifest.json`, permitindo auditoria rápida mesmo offline.

## Boas práticas

- Utilize Python 3.11+, `deepagents` (GitHub) e `langchain-anthropic` para obter todo o middleware padrão (Filesystem, TODOs, Summarization e tracing).
- Redirecione os logs locais (`logging.INFO`) para o coletor de sua preferência apenas para auditoria rápida; os detalhes finos ficam no LangSmith.
- Trate alertas monitorando o campo `status` do manifesto e, em seguida, investigue o trace correspondente no LangSmith para descobrir o passo exato que falhou.
