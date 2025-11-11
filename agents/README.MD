# agents – Guia Operacional e de Desenvolvimento

## Propósito e Contexto
- Consolidar toda a automação descrita em `LANGCHAIN.MD` dentro de um módulo isolado, versionado e fácil de evoluir.
- Reaproveitar as regras de `/AGENTS.MD` para executar processos com subagentes especializados e orquestradores consistentes.
- Manter em um único arquivo as instruções de uso, setup, padrões de código, troubleshooting e histórico de melhorias do diretório `agents/`.

## Componentes Essenciais
- `base.py`: define `StrategyAgent` e `ProcessAgent`, responsável por bootstrap de diretórios, manifestos e acesso a ferramentas.
- `config/`: expõe `Settings` e `get_settings()`, centralizando variáveis de ambiente, validação e flags (inclui `reload_settings`).
- `deepagents/`: implementação local usada quando o pacote oficial não está disponível; oferece `create_deep_agent` e o modo de reflexão em três estágios.
- `utils/`: dividido em `io/` (drive, manifestos, empacotamento, reporting), `loaders/`, `observability/` (instrumentation, TODOs), `helpers/` (contexto, validação).
- `ZeroUm/`, `generic/` e `orchestrators/`: contêm os orquestradores específicos; `ZeroUm` possui o subagente real `ProblemHypothesisExpress`.
- `tools/`: registry central com `get_tools_for_agent()` e validação de nomes.
- `scripts/`: `run_strategy_agent.py` (CLI oficial) e utilitários como `check_env.py`.
- `tests/`: suíte unitária para IO, loaders, contexto, manifestos, orquestradores.

## Fluxo Operacional
1. O CLI (`agents/scripts/run_strategy_agent.py`) normaliza o contexto (CamelCase) e valida o ambiente via `validate_sensitive_environment()`.
2. O orquestrador (ex.: `ZeroUmOrchestrator`) chama `bootstrap()`, garante `drive/<Contexto>/<Estratégia>` e `_pipeline`, e instancia subagentes.
3. Cada subagente lê `process/<Estratégia>/<NN-Processo>/`, verifica `_SHARED/`, cria TODOs e executa o LangGraph padrão (`prepare → executar_llm → fallback_local → finalizar`).
4. Artefatos numerados são gravados em `drive/<Contexto>/<Processo>/`, todo manifesto JSON vai para `drive/<Contexto>/_pipeline/` e o consolidado em `drive/<Contexto>/<Estratégia>/00-consolidado.MD`.
5. O orquestrador chama `package_artifacts` para gerar `drive/<Contexto>/_pipeline/<Estratégia>-archive.zip`.

## Setup Rápido
1. **Criar ambiente e instalar dependências**
   ```bash
   cd /Users/douglasprado/www/framework-business
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Configurar credenciais**
   ```bash
   cd agents
   cp .env.example .env
   nano .env  # adicione OPENAI_API_KEY=SUA_OPENAI_API_KEY
   ```
3. **Executar uma estratégia (sempre de dentro de `agents/`)**
   ```bash
   cd agents
   ./RUN.sh ZeroUm "MeuProjeto" "Descrição do projeto"
   # ou
   python3 scripts/run_strategy_agent.py ZeroUm "MeuProjeto" -d "Descrição detalhada"
   ```
   - O contexto informado é normalizado automaticamente; use `AGENTS_DISABLE_CONTEXT_AI=1` para forçar o nome fornecido.
   - Para testar sem API real, defina `AGENTS_SKIP_SECRET_CHECK=1` (modo desenvolvimento com fallback local).
4. **(Opcional) Usar o runtime oficial do DeepAgents**
   - O adaptador tenta usar `langchain-ai/deepagents` sempre que o pacote estiver instalado (Python ≥ 3.11 + `langchain-anthropic`).
   - Caso deseje habilitar, instale em um ambiente compatível:
     ```bash
     # Requer Python 3.11+
     python3.11 -m pip install "deepagents @ git+https://github.com/langchain-ai/deepagents.git"
     python3.11 -m pip install langchain-anthropic
     ```
   - Se o pacote não estiver presente ou a importação falhar, o fallback local continuará sendo utilizado automaticamente.

## Execução por Estratégia
- **ZeroUm**: foco em validação de problema/hipótese (`00-ProblemHypothesisExpress`).
- **Branding**, **MVPBuilder** e **Naming**: usam o orquestrador genérico até que subagentes dedicados sejam adicionados.
- Padrão de execução:
  ```bash
  cd agents
  ./RUN.sh <Estrategia> "CamelCaseContext" "Descrição em uma frase"
  ```
- Exemplos úteis:
  - `./RUN.sh ZeroUm "AutomarticlesAutomacaoBlog" "Plataforma SaaS que automatiza blogs para PMEs"`
    - Gera artefatos em `../drive/AutomarticlesAutomacaoBlog/00-ProblemHypothesisExpress/` e consolidado em `../drive/.../ZeroUm/`.
  - `./RUN.sh Branding "MinhaMarca" "Marca de produtos orgânicos para público jovem"`
  - `./RUN.sh MVPBuilder "MeuSaaS" "MVP de gestão de projetos com IA"`
  - `./RUN.sh Naming "AppFinancas" "App mobile de finanças pessoais"`
- Versão direta em Python oferece mais opções (`--context-description`, `--quiet`).

## Modos e Configurações Avançadas
- **Modelos**: ajuste `AGENTS_LLM_MODEL` e `AGENTS_LLM_TEMPERATURE`; use `gpt-4o` para mais qualidade.
- **Reflection/Thinking Mode**:
  ```bash
  export AGENTS_REASONING_MODE="reflection"
  export AGENTS_REASONING_MODEL="gpt-4o"
  ```
  - Pipeline em três estágios (Draft → Reflection → Refinement) com validação automática contra `validator.MD`.
  - Modo simples consome ~480 tokens em ~16s; reflexão sobe para ~1.800 tokens em ~61s, porém entrega contexto mais rico, notas de leitura e evidências específicas.
  - Prefira reflexão para entregáveis críticos ou orientados a cliente; mantenha modo simples em execuções operacionais ou quando o orçamento for restrito.
- **TODOs**:
  ```bash
  export AGENTS_ENABLE_TODOS="true"
  export AGENTS_TODO_VERBOSE="true"
  ```
  - Gera `*-todos.json` no `_pipeline`, exibindo andamento em tempo real via logs.
- **LangSmith / Observabilidade externa**:
  ```bash
  export LANGCHAIN_TRACING_V2="true"
  export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
  export LANGCHAIN_API_KEY="sua-chave"
  export LANGCHAIN_PROJECT="framework-business"
  ```
- **Contexto via IA**: habilitado por padrão. Para garantir nomes manuais, use `AGENTS_DISABLE_CONTEXT_AI=1`.
- **Modo desenvolvimento**: `AGENTS_SKIP_SECRET_CHECK=1` ignora a validação de secrets (útil para ambientes offline).

## Observabilidade, Artefatos e Estrutura de Saída
- Quando `LANGCHAIN_TRACING_V2=true` e as variáveis do LangSmith estão configuradas, o DeepAgent reporta automaticamente cada chamada ao LLM e cada ferramenta para o painel do LangSmith (sem callbacks customizados).
- O manifesto do processo continua com um resumo local – duração total, tokens estimados e custo heurístico (`ZEROUM_COST_PER_1K_TOKENS` ou `LLM_COST_PER_1K_TOKENS`).
- Manifestos ficam em `drive/<Contexto>/_pipeline/<Processo>-manifest.json` com status (`completed`, `fallback`, `erro`), notas e resumo de TODOs.
- `write_consolidated_report()` gera `00-consolidado.MD` com resumo da estratégia; `package_artifacts()` cria `<Estratégia>-archive.zip` no `_pipeline`.

## Comandos Úteis
- **Setup e Diagnóstico**
  ```bash
  python agents/scripts/check_env.py
  python -c "from agents.config import get_settings; print(get_settings(validate=False))"
  python -c "from agents.registry import STRATEGY_REGISTRY; print('\n'.join(STRATEGY_REGISTRY.keys()))"
  ```
- **Execução via Python**
  ```bash
  python3 agents/scripts/run_strategy_agent.py ZeroUm "MeuProjeto" -d "Descrição"
  ```
- **Testes e Qualidade** (executar na raiz)
  ```bash
  pytest
  pytest --cov=agents --cov-report=html
  ruff check agents/ --fix
  ruff format agents/
  mypy agents/
  pre-commit run --all-files
  ```
- **Navegação e inspeção dos outputs**
  ```bash
  ls -lha drive/*/
  ls -lha drive/MeuProjeto/
  tree drive/MeuProjeto/
  cat drive/MeuProjeto/_pipeline/00-ProblemHypothesisExpress-manifest.json | jq
  open drive/MeuProjeto/ZeroUm/00-consolidado.MD  # macOS
  ```
- **Limpeza**
  ```bash
  rm -rf drive/MeuProjeto/
  find . -type d -name "__pycache__" -exec rm -r {} +
  find . -type f -name "*.pyc" -delete
  ```

## Workflows Sugeridos
- **Validar nova ideia**: rodar ZeroUm → revisar `drive/<Contexto>/00-ProblemHypothesisExpress/` → ler `00-consolidado.MD` → decidir próximos passos.
- **Projeto completo**: executar ZeroUm, Branding, MVPBuilder e Naming sequencialmente para o mesmo contexto, consolidando outputs no `drive/` antes de compartilhar com stakeholders.
- **Execução com observabilidade**: habilitar LangSmith + reflection + TODOs, coletar métricas no `_pipeline` e monitorar traces no dashboard externo.

## Troubleshooting e Dicas
- "`OPENAI_API_KEY` não configurada": confirme `.env` dentro de `agents/` ou exporte temporariamente antes da execução.
- "`ModuleNotFoundError: No module named 'agents'`": garanta `pip install -e .` ou inclua o repositório no `PYTHONPATH`.
- Script não executa: `chmod +x agents/RUN.sh` e rode sempre a partir do diretório `agents/`.
- Execução em modo silencioso: adicione `--quiet` ao CLI.
- Dê descrições claras para obter artefatos melhores; revise outputs e ajuste prompts quando necessário.

## Guia de Desenvolvimento
- **Leitura obrigatória**: `/AGENTS.MD` para visão global → este README → `LANGCHAIN.MD` para entender processos → modelos em `models/process/` antes de criar novos artefatos.
- **Princípios**:
  - Use `get_settings()` em vez de `os.getenv` direto.
  - Prefira exceções de `agents.exceptions` (ex.: `ProcessExecutionError`, `MissingConfigError`).
  - Organize imports: `__future__` → stdlib → third-party → locais com caminhos absolutos (`from agents...`).
  - Cubra tudo com type hints e docstrings no formato Google.
  - Use decoradores (`handle_agent_errors`, `log_execution`, `retry_on_failure`) para cross-cutting concerns.
  - Evite duplicação movendo utilitários para `agents/utils/`.
- **Criar um novo ProcessAgent**: derive de `ProcessAgent`, carregue `ProcessDefinition`, inicialize `TodoManager`, implemente `run()` usando LangGraph padrão, salve artefatos numerados e publique manifesto.
- **Criar um novo Orchestrator**: derive de `StrategyAgent`, registre subagentes, use `OrchestrationGraph` (prepare → execute → finalize) e `write_consolidated_report()`.
- **Adicionar configuração**: defina campo em `config/settings.py`, documente em `.env.example`, utilize via `settings.nova_config`.
- **Adicionar tool**: registre no `ToolRegistry`, implemente (se necessário) em `deepagents/tools.py` e exponha via `get_tools_for_agent`.

## Checklist de Qualidade
- **Código**: usa `get_settings()`, exceções customizadas, decorators quando fizer sentido, type hints, docstrings claras, logging informativo.
- **Estrutura**: arquivos no diretório correto, convenções de nome respeitadas (CamelCase para estratégias/processos), `__init__.py` atualizado quando expuser novos símbolos.
- **Testes**: criar/atualizar testes unitários, garantir que passam localmente e cobrem novos caminhos críticos.
- **Documentação**: README atualizado (este arquivo), exemplos de uso revisados, sem tabelas ou emojis, linguagem em pt-BR.
- **Qualidade**: `ruff check`, `ruff format`, `mypy` e hooks de pre-commit executados antes de abrir PR.

## Anti-Padrões a Evitar
- Ler variáveis com `os.getenv` diretamente ou espalhar validação de secrets pelo código.
- Levantar `ValueError`/`RuntimeError` genéricos quando há exceções dedicadas.
- Instanciar listas de ferramentas manualmente (use `get_tools_for_agent`).
- Repetir lógica de IO/consolidado dentro de agentes; mova para `agents/utils/`.
- Escrever novos arquivos sem ler modelos ou verificar `_SHARED/` primeiro.
- Usar imports relativos (`from ..utils import ...`) fora de pacotes locais.

## Histórico de Melhorias (resumo)
- **Fase 1 – Configuração e correções**: criação do módulo `config/`, validação centralizada e correção do cache em `StrategyAgent`.
- **Fase 2 – Reorganização**: `utils/` dividido em subpacotes (`io`, `loaders`, `observability`, `helpers`), introdução de `reporting.py` e renomeação para `ZeroUm/` (CamelCase).
- **Fase 3 – DRY**: `write_consolidated_report()` e helpers compartilhados eliminaram código duplicado entre orquestradores.
- **Fase 4 – Padronização**: hierarquia de exceções dedicadas, decoradores (`handle_agent_errors`, `log_execution`, `retry_on_failure`), configuração de linting (`pyproject.toml`, Ruff, MyPy, pre-commit).

## Próximos Passos Recomendados
- Expandir subagentes da estratégia ZeroUm seguindo o padrão de `subagents/base.py`.
- Criar orquestradores específicos para Branding, Naming e MVPBuilder para substituir o modo genérico.
- Estender o modo de reflexão e o sistema de TODOs para todos os novos processos.
- Manter LangSmith/Tracing habilitado para acompanhar tokens/custos diretamente no runtime oficial.
