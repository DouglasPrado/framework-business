# Plano de Agentes DeepAgents por Estratégia

## Contexto Atual

- O repositório organiza estratégias em `strategies/`, processos em `process/<Processo>/` (com `process.MD`, `knowledge.MD`, `tasks.MD`, `validator.MD` e `_DATA/`) e outputs reais em `drive/`, seguindo as regras descritas em `AGENTS.MD` e `drive/README.MD`.
- Cada processo já possui instruções detalhadas, templates e validadores; o agente precisa apenas interpretá-los e executar as tarefas.
- A integração planejada **não** utilizará `cagent.yaml` ou o modelo de agente genérico anterior. Em vez disso, haverá agentes especializados por estratégia (ex.: ZeroUm) com subagentes responsáveis apenas por uma etapa/processo dessa estratégia.

## Objetivo

- Criar um agente orquestrador por estratégia (ex.: `ZeroUmAgent`) que coordene subagentes dedicados a cada processo/etapa (`ProblemHypothesisExpressAgent`, `ProblemHypothesisDefinitionAgent`, `TargetUserIdentificationAgent`, etc.).
- Cada subagente executa somente o processo correspondente, gera os artefatos exigidos em `drive/<Contexto>/<Processo>/` e retorna um pacote padronizado ao orquestrador.
- O agente da estratégia consolida os artefatos recebidos, produz um relatório final e disponibiliza todos os arquivos para download (ex.: geração de ZIP em `drive/<Contexto>/<Estratégia>/outputs.zip`).

## Arquitetura Proposta

1. **Orquestrador da Estratégia (ex.: ZeroUmAgent)**

   - Responsável por ler `strategies/<Estratégia>/` para entender objetivos, processos e dependências.
   - Mantém o estado global da execução (lista de processos concluídos, artefatos recebidos, bloqueios).
   - Invoca subagentes em sequência ou paralelamente conforme dependências descritas em `strategy/process.MD`.
   - Concatena outputs parciais em um consolidado final (`drive/<Contexto>/<Estratégia>/00-consolidado.MD`) e dispara empacotamento para download.

2. **Subagentes por Processo**

   - Cada subagente possui system prompt específico apontando para `process/<Estratégia>/<NN-Processo>/`.
   - Sequência interna:
     1. Ler `process.MD`, `knowledge.MD`, `tasks.MD`, `validator.MD` e `_DATA/`.
     2. Usar `write_todos` para planejar execução local (sem interferir em outros processos).
     3. Criar artefatos numerados em `drive/<Contexto>/<Processo>/` baseados nos templates e validar com `validator.MD`.
     4. Retornar ao orquestrador um manifesto (`manifest.json`) contendo metadados (arquivos gerados, status do validador, pendências).
   - Subagente não cria novos processos; ele apenas executa a etapa designada.

3. **Canal de Artefatos**

   - Repositório intermediário em `drive/<Contexto>/_pipeline/` onde subagentes salvam manifestos e dados resumidos para o orquestrador consumir.
   - Orquestrador vigia esse diretório para saber quando cada etapa terminou e se precisa reabrir TODOs.

4. **Módulo de Empacotamento**
   - Script utilitário (ex.: `scripts/package_drive_artifacts.py`) que compacta `drive/<Contexto>/<Estratégia>/` (incluindo subpastas de processos) em um único arquivo `.zip` para download.
   - Chamado automaticamente pelo orquestrador após validar que todos os subagentes concluíram suas etapas.

## Ferramentas e Recursos Necessários

- `deepagents` com `create_deep_agent` para montar tanto o orquestrador quanto os subagentes (cada um com prompts próprios).
- Ferramentas de filesystem do pacote (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`).
- Ferramentas customizadas sugeridas:
  - `load_strategy(strategy_name)` → retorna objetivos, processos e ordem.
  - `load_process(process_path)` → agrega dados do processo específico para o subagente.
  - `drive_writer(context_folder, target, artifact_spec)` → garante prefixos numéricos, português e menção a `_SHARED/` quando aplicável.
  - `manifest_handler` → salva/consome arquivos JSON com o status de cada subagente.
  - `package_artifacts(context_folder, strategy_name)` → gera ZIP final.

## Fluxo Operacional

1. **Contexto Inicial**

   - Usuário fornece o contexto da ideia do negocio e o orquestrador define o nome (ex.: `MEIFinancialHealth`). O orquestrador cria/valida `drive/<Contexto>/<Estratégia>/`.
   - Orquestrador registra checklist inicial (inputs disponíveis, restrições).

2. **Planejamento da Estratégia**

   - Orquestrador lê `strategies/<Estratégia>/` e gera TODOs globais (ex.: preparar dados, acionar processos, consolidar).
   - Define ordem dos subagentes conforme dependências (por exemplo, `ProblemHypothesisExpress` antes de `ProblemHypothesisDefinition`).

3. **Execução dos Subagentes**

   - Para cada processo:
     - Instanciar subagente com prompts específicos.
     - Subagente executa tarefas, gera arquivos numerados (ex.: `drive/<Contexto>/<Processo>/01-contexto.MD`).
     - Valida entregas com `validator.MD`.
     - Publica `drive/<Contexto>/_pipeline/<Processo>-manifest.json` contendo referências de arquivos e status `completed/pending`.
   - Orquestrador monitora manifestos; se algum apontar pendências, reexecuta o subagente ou solicita ajustes.

4. **Consolidação**

   - Após manifestos finalizados, orquestrador:
     - Lê outputs chave de cada processo (ex.: `03-recomendacoes.MD`).
     - Produz `drive/<Contexto>/<Estratégia>/00-consolidado.MD` com sumário, links relativos e próximos passos.
     - Atualiza log final (`drive/<Contexto>/<Estratégia>/zz-log.MD`) mencionando os arquivos gerados e status dos validadores.

5. **Disponibilização para Download**
   - Chamar `package_artifacts` para gerar `drive/<Contexto>/<Estratégia>/ZeroUmAgentOutputs.zip`.
   - Registrar no log o caminho do pacote e checksum opcional.

## Implementação Recomendada

1. **Setup**

   - Criar virtualenv, instalar `deepagents`, `langgraph`, `langchain-openai`, `python-dotenv`, `tavily-python` (se buscas externas forem permitidas) e libs auxiliares (`pyyaml`, `rich`).
   - Manter **todo o código, dependências específicas, tests e stubs relacionados aos agentes dentro da pasta `agents/`**, evitando arquivos soltos na raiz do repositório.
   - Documentar variáveis em `.env.example` (chaves de modelo, caminhos, flags de empacotamento).

2. **Prompts**

   - Escrever system prompt específico para cada agente:
     - Orquestrador: orientado pela estratégia (ZeroUm) + regras de governança (AGENTS.MD).
     - Subagentes: prompts enxutos focados no processo, mencionando explicitamente `process/<Estratégia>/<NN-Processo>/`.
   - Todos reforçam: português obrigatório, sem tabelas/emojis, checar `_SHARED/`, atualizar `drive/`.

3. **Código**

   - `agents/zero_um/orchestrator.py`: instancia `create_deep_agent` com ferramentas globais e lógica para acionar subagentes via `task`.
   - `agents/zero_um/subagents/problem_hypothesis_express.py` (e demais) compartilhando utilidades comuns.
   - `agents/utils/drive_writer.py`, `agents/utils/manifest.py`, `agents/utils/package.py`.
   - CLI `scripts/run_strategy_agent.py --strategy ZeroUm --context ZeroUmMEIFinancialHealth`.

4. **Persistência**

   - Usar LangGraph Store ou arquivos em `drive/<Contexto>/_pipeline/state.json` para retomar execuções interrompidas.

5. **Validação**
   - Testes unitários para utilitários (ex.: geração de nomes numerados).
   - Teste integrado executando cadeia curta (ex.: apenas `ProblemHypothesisExpress`) para garantir criação de manifestos e consolidados.

## Artefatos Esperados

- Pastas por processo em `drive/<Contexto>/<Processo>/` com arquivos numerados conforme tarefas.
- Manifestos JSON por processo listando arquivos gerados, indicadores, bloqueios.
- Consolidado da estratégia em `drive/<Contexto>/<Estratégia>/00-consolidado.MD` e log `zz-log.MD`.
- Pacote ZIP final em `drive/<Contexto>/<Estratégia>/ZeroUmAgentOutputs.zip` (ou `<Estratégia>AgentOutputs.zip` para outras estratégias).
- Scripts/CLI e módulos de agentes descritos acima.

## Próximos Passos

1. Definir ordem e dependências dos processos prioritários de ZeroUm para configurar o orquestrador inicial.
2. Implementar utilitários compartilhados (`drive_writer`, `manifest_handler`, `package_artifacts`).
3. Criar prompts e instâncias dos subagentes ZeroUm (ProblemHypothesisExpress, ProblemHypothesisDefinition, TargetUserIdentification, etc.) e validar cada um isoladamente.
4. Integrar os subagentes ao orquestrador ZeroUm e testar o fluxo ponta a ponta, incluindo a geração do ZIP.
5. Replicar o padrão para outras estratégias (MVPBuilder, Branding, Naming) reutilizando os utilitários e ajustando apenas prompts/listas de processos.

---
