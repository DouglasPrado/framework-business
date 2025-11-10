# Plano de Integração DeepAgents

## Contexto da Estrutura
- Repositório organiza estratégias em `strategies/`, processos detalhados em `process/<Processo>/` com `process.MD`, `knowledge.MD`, `tasks.MD`, `validator.MD` e `_DATA/`, além do diretório `drive/` para outputs executados.
- `AGENTS.MD` define regras obrigatórias: ler antes de escrever, usar modelos de `models/`, manter vocabulário coerente, usar pastas CamelCase, arquivos lowercase.MD, conteúdo em português, sem tabelas ou emojis, referenciar `_SHARED/` quando existir artefato reutilizável e garantir que `process ↔ tasks ↔ validator` estejam alinhados.
- `drive/README.MD` determina que cada execução recebe pasta CamelCase, arquivos numerados (`01-`, `02-`), e que os artefatos copiados dos processos devem ser atualizados com resultados reais sem recriar `_DATA/`.
- `cagent.yaml` já descreve papéis (root, process_memory_manager, process_executor, artifact_builder). O novo deep agent deve replicar essas responsabilidades em um fluxo LangGraph/DeepAgents.

## Objetivo do Agente DeepAgents
- Receber contexto (estratégia/processo e objetivo específico), planejar tarefas usando o `write_todos` nativo do deepagents e executar processos sem dependência manual.
- Ler automaticamente os arquivos de estratégia e processo relevantes, interpretar instruções, identificar inputs que precisam ser coletados e preparar subagentes ou ferramentas para obtê-los.
- Operar ferramentas de sistema de arquivos (ler/copiar/editar) para produzir artefatos em `drive/<Contexto>/<Processo>/`, respeitando convenções (prefixos numéricos, português, sem tabelas, referências a `_SHARED/`).
- Registrar logs e checkpoints que permitam auditoria (quais processos rodaram, quais arquivos foram criados/atualizados, se validadores foram atendidos).

## Arquitetura Proposta
- **Grafo principal (`create_deep_agent`)**: instância `deepagents` com modelo configurado via `langchain.chat_models.init_chat_model` (ex.: `openai:gpt-4o` ou `gpt-5`) e system prompt que incorpora AGENTS.MD + instruções específicas do fluxo Framework Business.
- **Ferramentas base**: `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep` disponibilizadas pelo pacote. Acrescentar ferramentas customizadas:
  - `load_strategy(strategy_name)` para consolidar objetivos, processos e dependências a partir de `strategies/<Nome>/`.
  - `load_process(process_path)` para trazer objetivo, entradas, saídas, tarefas e validadores num único payload.
  - `drive_writer(context_folder, process_name, artefact_spec)` que cria pastas CamelCase, aplica prefixos `01-`, mantém texto em português e registra fontes.
  - `shared_artifact_resolver` que consulta `process/_SHARED` para evitar duplicações.
- **Subagentes** (via tool `task`):
  - `MemoryPlanner`: replica `process_memory_manager` lendo documentação completa e gravando plano estruturado (pode salvar como arquivo temporário em `drive/<Contexto>/<Processo>/00-plano.MD`).
  - `ProcessExecutor`: segue plano, chama ferramentas de escrita, coleta dados externos (via ferramentas adicionais como `web_search` se aprovado) e monitora progresso dos TODOs.
  - `ArtifactBuilder`: transforma outputs em arquivos finais numerados e verifica contra `validator.MD`.
- **Persistência / Store**: usar LangGraph Store para lembrar contextos já executados (nome da pasta em `drive`, decisões tomadas, checagens pendentes).

## Fluxo Operacional
1. **Coleta de contexto**: agente pergunta somente informações mínimas (nome CamelCase para pasta em `drive/`, estratégia/processo alvo, restrições). Valida se pasta já existe para decidir se continua execução anterior ou abre nova.
2. **Leitura obrigatória**: antes de planejar, o agente chama `load_strategy` e `load_process` para cada processo identificado. Caso documentos de modelo estejam ausentes, o agente registra bloqueio.
3. **Planejamento com TODOs**: usar `write_todos` para quebrar execução em blocos (análise, coleta, produção, validação, cópia para `drive`). Cada TODO referencia arquivos específicos e ferramentas necessárias.
4. **Execução iterativa**:
   - `ProcessExecutor` segue TODOs, escreve artefatos temporários em `_DATA/` quando necessário e sincroniza outputs finais com `drive_writer`.
   - A cada arquivo escrito, rodar `validator_check` (trecho do `validator.MD`) para confirmar critérios.
5. **Geração de resultados no drive**:
   - Criar pasta `drive/<ContextoCamelCase>/<Processo>/`.
   - Copiar templates relevantes de `process/<Processo>/_DATA/` ou `process/_SHARED/templates/` para arquivos numerados (`01-contexto.MD`, `02-execucao.MD`, etc.), preenchendo com dados coletados pelo agente.
   - Atualizar metadados (data, responsável, links) e referenciar fontes usadas.
6. **Encerramento**:
   - Atualizar TODOs para `X/X completed`.
   - Registrar relatório em `drive/<Contexto>/<Processo>/zz-log.MD` com resumo, bloqueios, próximos passos.
   - Se faltarem artefatos exigidos pelo `validator.MD`, impedir encerramento automático.

## Passo a Passo de Implementação
1. **Preparação de ambiente**:
   - Criar virtualenv e instalar `deepagents`, `langchain-openai`, `langgraph`, `python-dotenv`, `tavily-python` (se busca web for necessária) e quaisquer SDKs internos já usados.
   - Configurar variáveis `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` ou outro provider aceito.
2. **Modelagem do system prompt**:
   - Basear-se em AGENTS.MD, README.MD e drive/README.MD.
   - Incluir regras explícitas: português obrigatório, sem tabelas/emojis, checar `_SHARED/`, replicar estrutura `process/` → `drive/`.
3. **Construção das ferramentas customizadas**:
   - Implementar `load_strategy` e `load_process` lendo markdown, parseando cabeçalhos e retornando JSON (usar regex simples ou `markdown-it`).
   - `drive_writer`: funções auxiliares para criar pasta CamelCase, gerar nomes `NN-descricao.MD`, copiar templates e preencher placeholders.
   - `validator_runner`: interpreta checklists em `validator.MD` e confirma se arquivos gerados atendem critérios básicos (ex.: presença de seções, menção a KPIs).
4. **Configuração do grafo deep agent**:
   - Invocar `create_deep_agent` com parâmetros:
     - `model=init_chat_model("openai:gpt-5")` (ou outro).
     - `tools=[ls, read_file, write_file, edit_file, glob, grep, load_strategy, load_process, drive_writer, shared_artifact_resolver, validator_runner]`.
     - `max_subtasks` ajustado ao número de processos simultâneos (ex.: 5).
     - `planner_model` opcional para delegar `write_todos` a modelo mais barato.
   - Definir callback que, ao concluir TODOs de um processo, chama `drive_writer` para consolidar arquivos e atualiza store com status.
5. **Subagentes especializados**:
   - Configurar `task` tool com descrições específicas (por exemplo, `"role": "ProcessMemoryManager"` com instruções para ler todos os arquivos antes de sugerir plano).
   - Criar funções Python que instanciam `create_deep_agent` novamente com prompts diferentes caso seja necessário isolamento (ex.: `artifact_builder_agent` focado em formatar texto).
6. **Integração com `cagent.yaml` (opcional)**:
   - Mapear cada agente definido no YAML para uma chamada `task` dentro do deep agent, permitindo manter consistência de papéis.
   - Registrar no YAML que o executor padrão agora é o deep agent e documentar fallback manual.
7. **Rotina de execução completa**:
   - Script `scripts/run_deep_agent.py` que recebe parâmetros (`--strategy`, `--process`, `--context`), inicializa o agente, injeta contexto inicial (objetivos, deadlines) e acompanha o streaming do LangGraph.
   - Opção de continuar execução lendo o Store (para retomar TODOs pendentes).
8. **Observabilidade e segurança**:
   - Habilitar logging estruturado (JSON) das ações do agente (arquivo manipulado, ferramenta usada, tempo).
   - Implementar limites de escrita (whitelist de diretórios: `process/`, `drive/`, `notes/`).
   - Validar que nenhum arquivo fora do workspace é alterado.
9. **Testes e validação**:
   - Criar cenários de teste: execução de processo curto (ex.: `ZeroUm/01-ProblemHypothesisDefinition`) com dados fictícios.
   - Verificar se TODOs são concluídos, se arquivos em `drive/` seguem convenções e se `validator_runner` aprova.
   - Adicionar testes unitários para ferramentas customizadas (ex.: parse correto de cabeçalhos).

## Entregáveis Esperados
- `scripts/run_deep_agent.py` ou CLI equivalente.
- Definição do agent graph (ex.: `agents/deep_agent.py`) com prompts e ferramentas.
- Biblioteca de ferramentas (`agents/tools/process_loader.py`, `agents/tools/drive_writer.py`, etc.).
- Configuração de variáveis em `.env.example`.
- Documentação de uso (incluir seção no README ou na própria `LANGCHAIN.MD` com comandos de execução).
- Exemplos de execuções registradas em `drive/` demonstrando que o agente copia templates e produz arquivos numerados.

## Próximos Passos e Backlog
- Validar com stakeholders se todos os processos prioritários devem ser suportados desde o início ou se haverá rollout gradual.
- Catalogar ferramentas externas aprovadas em `tools/` (ex.: Tavily, GitHub, Figma) e criar wrappers compatíveis com deepagents.
- Investigar integração com LangGraph Studio para observabilidade e depuração visual do grafo.
- Criar mecanismo de aprovação humana opcional antes de escrever em `drive/`, caso seja requisito de governança.
- Documentar procedimentos de recuperação caso o agente interrompa a execução (como reiniciar TODOs a partir do store).

---

Este plano garante aderência às instruções do repositório, utiliza as capacidades nativas do `deepagents` (planejamento, subagentes, ferramentas de filesystem) e descreve como automatizar a execução dos processos até a geração dos artefatos finais no `drive/`.
