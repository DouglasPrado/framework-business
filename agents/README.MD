# agents – Implementação baseada em LANGCHAIN.MD

## Propósito
- Consolidar toda a automação descrita em `LANGCHAIN.MD` dentro de uma camada isolada
- Reutilizar as regras de `AGENTS.MD` para orquestrar processos via subagentes especializados
- Facilitar a evolução incremental (adição de novas estratégias, processos e utilitários)

## Estrutura Atual
- `base.py`: classes genéricas para orquestradores (`StrategyAgent`) e subagentes (`ProcessAgent`)
- `utils/`: helpers para carregar estratégias/processos, escrever em `drive/`, lidar com manifestos e empacotar outputs
- `generic/`: orquestrador padrão para estratégias que ainda não possuem subagentes dedicados
- `zero_um/`: primeira estratégia com subagentes reais em `subagents/`
- `registry.py`: mapeia nomes das estratégias (`ZeroUm`, `Branding`, `MVPBuilder`, `Naming`) para seus orquestradores
- `scripts/run_strategy_agent.py`: CLI que consome o registry (`python agents/scripts/run_strategy_agent.py ZeroUm NomeDoContexto -d "Contexto completo"`)
- `tests/`: cobertura inicial para `drive_writer`, manifestos e empacotamento
- `deepagents/`: stub local utilizado apenas quando o pacote oficial ainda não está disponível

> Convenção: **qualquer arquivo relacionado aos agentes (scripts, utilitários, dependências, testes ou stubs)** deve permanecer dentro desta pasta `agents/`. Evite duplicar lógica em outros diretórios do repositório.

> Integração de IA: `agents/deepagents/` tenta usar `langchain_openai.ChatOpenAI` sempre que `OPENAI_API_KEY` estiver configurada. Caso a chave não exista, gera um resumo sintético a partir das instruções (incluindo o contexto completo passado via `-d`) sem copiar o texto integral dos processos.

## Fluxo Operacional
1. `ZeroUmOrchestrator` lê `strategies/ZeroUm`, prepara `drive/<Contexto>/ZeroUm` e `_pipeline`
2. Cada processo listado ganha um subagente dedicado (por enquanto `ProblemHypothesisExpress`)
3. Subagentes precisam ler `process/<Estratégia>/<NN-Processo>/` antes de produzir artefatos numerados em `drive/<Contexto>/<Processo>/`
4. Manifestos JSON são gravados em `drive/<Contexto>/_pipeline/`, permitindo que o orquestrador acompanhe o status
5. Ao final, o orquestrador gera `00-consolidado.MD` e chama `package_artifacts` para montar o `.zip`

### Contexto detalhado
- Passe a descrição completa do projeto pelo parâmetro `-d/--context-description` do CLI. Esse texto alimenta o orquestrador e todos os subagentes, orientando como aplicar o processo.
- Exemplo: `python agents/scripts/run_strategy_agent.py ZeroUm AutomarticlesAutomacaoBlog -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS."`
- O contexto completo será registrado no consolidado da estratégia e embutido em cada prompt enviado aos subagentes.

## Próximos Passos
- Adicionar os demais subagentes da estratégia ZeroUm seguindo o padrão de `subagents/base.py`
- Validar o fluxo ponta a ponta com `deepagents` instalado, garantindo que os artefatos sejam gerados automaticamente
- Criar orquestradores específicos para Branding, Naming e MVPBuilder para substituir o modo genérico
