# Configuração de LLMs

Este repositório utiliza a função `agents.llm_factory.build_llm` para criar instâncias de modelos conversacionais compatíveis com LangChain. A fábrica centraliza ajustes de credenciais, parâmetros de geração e callbacks de observabilidade, garantindo comportamento consistente entre orquestradores e subagentes.

## Perfis de execução

### Produção

- Utilize uma chave válida em `OPENAI_API_KEY` ou defina `api_key` no `llm_config` repassado aos agentes.
- Ajuste o modelo principal com `AGENTS_LLM_MODEL` ou com o campo `model` do `llm_config`, priorizando versões estáveis (ex.: `gpt-4o`).
- Habilite observabilidade contínua configurando `observability.langsmith` com `project_name`, `tags` e metadados relevantes; mantenha as credenciais do LangSmith ativas.
- Para auditoria adicional, ative o `LangChainTracer` informando `observability.langchain_tracer` (por exemplo, `{"project_name": "framework-business-prod"}`).
- Registre políticas de temperatura e limites de tokens explícitos (`temperature`, `max_tokens`) para reprodutibilidade.

### Desenvolvimento

- Priorize modelos de menor custo (ex.: `gpt-4o-mini`) definindo `AGENTS_LLM_MODEL` ou sobrescrevendo o campo `model` no `llm_config`.
- Utilize `AGENTS_LLM_TEMPERATURE` para experimentar diferentes graus de criatividade sem alterar o código.
- Ative a instrumentação somente quando necessário (`observability.langsmith` ou `observability.langchain_tracer`), evitando ruído em ambientes locais.
- Quando não houver credenciais disponíveis, o `create_deep_agent` mantém o fallback manual, permitindo testar fluxos sem chamadas externas.
- Combine com `AGENTS_DISABLE_CONTEXT_AI=1` para impedir que utilidades auxiliares façam chamadas automáticas durante prototipagem.

## Callbacks de observabilidade

- `observability.langchain_tracer`: aceita `True`, um nome de projeto (string) ou um dicionário com `project_name`, `session_name` e `client`. Requer suporte ao LangChain Tracing.
- `observability.langsmith`: aceita `True` ou um dicionário com `project_name`, `tags`, `metadata` e, opcionalmente, um `client` já instanciado. Exige dependência `langsmith` configurada com token válido.
- O campo `callbacks` continua aceitando handlers adicionais definidos manualmente; todos são combinados com os callbacks automáticos.

## Variáveis e campos úteis

- `OPENAI_API_KEY`: chave padrão lida pelo LangChain/OpenAI.
- `AGENTS_LLM_MODEL`: modelo padrão aplicado quando o `llm_config` não define `model`.
- `AGENTS_LLM_TEMPERATURE`: temperatura global aplicada na ausência de configuração explícita.
- `AGENTS_DISABLE_CONTEXT_AI`: impede que a normalização de contexto utilize IA quando definido como `1`, `true` ou `yes`.
- Campos de `llm_config`: `model`, `temperature`, `max_tokens`, `timeout`, `api_key`, `base_url`, `default_headers`, `observability`, `callbacks`.
