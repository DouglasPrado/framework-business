# Diretrizes Globais para Agentes de Orquestração

## Propósito

Este documento consolida as diretrizes globais que TODOS os agentes do sistema de orquestração devem seguir. Estas regras são referenciadas por múltiplos agentes para evitar redundância e garantir consistência.

## Quando Usar Este Documento

- **Agentes de orquestração**: Leia este documento ANTES de iniciar qualquer operação
- **Desenvolvimento**: Ao adicionar novas regras aplicáveis a múltiplos agentes, adicione AQUI primeiro
- **Manutenção**: Alterações nestas diretrizes propagam automaticamente para todos os agentes

## 1. REGRAS DE AUTONOMIA E PREENCHIMENTO DE ARTEFATOS

### 1.1 Execução Autônoma Obrigatória

**CRÍTICO**: Agentes NUNCA devem parar e pedir informações ao usuário durante a execução.

#### Análise Prévia dos Processos
- ANTES de iniciar execução, leia TODOS os process.MD dos processos da estratégia
- Identifique TODAS as informações que serão necessárias
- Liste TODOS os inputs/requisitos de cada processo
- Planeje como obter cada informação (web_search, assumptions, dados públicos)

#### Coleta Autônoma de Dados
- Delegue para web_search_agent: competidores, tecnologias, mercado, tendências
- Use dados públicos disponíveis na internet
- Faça assumptions razoáveis quando dados não estiverem disponíveis (documente no artefato)
- NUNCA pare execução esperando dados do usuário

#### Preenchimento Completo de Artefatos
- TODOS os artefatos devem ser criados 100% preenchidos
- NENHUM campo deve ficar vazio ou com placeholders como [INSERIR AQUI], [TODO], [PREENCHER]
- Se informação não disponível: use "Assumido: [valor razoável baseado em pesquisa/mercado]"
- Documente fonte de cada informação (web_search_agent, assumption, dado público)

#### Quando Pedir Input do Usuário
- SOMENTE peça: nome do projeto, escolha entre opções (se houver)
- NUNCA peça: objetivos (deduza da estratégia), público-alvo (pesquise), tecnologias (pesquise)
- Se precisar confirmar algo: execute com assumption e documente, não pare a execução

#### Exemplo de Autonomia
- Processo precisa de "público-alvo": delegue para web_search_agent, analise mercado, defina persona
- Processo precisa de "tecnologias": delegue para web_search_agent buscando stack moderna, tendências
- Processo precisa de "competidores": delegue para web_search_agent para encontrar players do mercado
- Processo precisa de "preços": delegue para web_search_agent para pesquisar pricing de competidores

### 1.2 Documentação de Assumptions

Quando usar assumptions (informação não disponível):

```
**Campo**: [Nome do campo]
**Valor**: [Valor assumido]
**Assumido**: Sim
**Base**: [Análise de mercado / Boas práticas / Pesquisa de competidores / Dados públicos]
**Fonte**: [Descrever raciocínio ou referências usadas]
```

Exemplo:
```
**Público-Alvo**: Desenvolvedores Python de empresas médias (50-500 funcionários)
**Assumido**: Sim
**Base**: Análise de mercado de ferramentas similares (Datadog, New Relic)
**Fonte**: web_search sobre "python monitoring tools target audience"
```

## 2. REGRAS DE EXECUÇÃO COMPLETA (NUNCA PARAR NO MEIO)

### 2.1 Completude Obrigatória

**REGRA CRÍTICA**: Agentes executores DEVEM completar 100% dos TODOs antes de reportar conclusão.

#### Nunca Pare no Meio
- Você DEVE executar TODOS os TODOs da lista
- Se cansar ou atingir limite: pause, mas RETOME do ponto exato
- Mantenha contador: "Executando TODO X de Y"
- NUNCA reporte conclusão se X < Y

#### Tratamento de Erros
- Se encontrar erro em um TODO: documente, crie TODO de correção, CONTINUE
- Não deixe erro bloquear execução dos outros TODOs
- Erros não são desculpa para parar no meio
- Colete TODOS os erros e reporte no final

#### Persistência
- Antes de cada TODO: verifique qual é o próximo pending
- Após cada TODO: atualize status imediatamente
- A cada 5 TODOs: faça checkpoint (salve progresso)
- Se precisar pausar: documente TODO atual, retome exatamente dali

#### Métricas de Completude
- 100% dos TODOs devem ser marcados (completed ou failed, nunca pending)
- 100% dos artefatos esperados devem ser criados
- 0% de trabalho incompleto aceitável
- Se não completar tudo: você FALHOU

### 2.2 Auto-Verificação Antes de Reportar

SEMPRE execute antes de reportar conclusão:

1. Conte quantos TODOs foram marcados como completed
2. Conte quantos TODOs existem no total
3. Se completed < total: VOLTE e execute os TODOs pendentes
4. Verifique se TODOS os artefatos esperados foram criados
5. Se algum artefato está faltando: VOLTE e crie
6. SOMENTE reporte quando 100% dos TODOs estiverem completed

Template de verificação:
```
## AUTO-VERIFICAÇÃO DE COMPLETUDE:
- Total de TODOs: [X]
- TODOs completed: [Y]
- TODOs failed: [Z]
- TODOs pending: [W]
- Status: [Y + Z = X? SIM/NÃO]
- Artefatos esperados: [lista]
- Artefatos criados: [lista]
- Completude: [100%/INCOMPLETO]
```

### 2.3 Monitoramento e Recuperação

#### A Cada TODO Executado
```
Log: "✓ TODO X/Y completed: [descrição]"
Se falhou: "✗ TODO X/Y failed: [razão] - documentando e continuando"
Atualizar imediatamente via TodoWrite
```

#### A Cada 5 TODOs (Checkpoint)
- Verificar: quantos pending, quantos in_progress, quantos completed
- Se houver in_progress antigo: marcar como failed e criar novo
- Salvar progresso em 00-process-context.md

#### Se Execução Interrompida
- Ao retomar: ler 00-process-context.md
- Identificar último TODO completed
- Retomar do próximo pending
- NUNCA recomeçar do zero

#### Antes de Reportar Conclusão
- Contar: completed + failed = total?
- Se NÃO: identificar pending e executar
- Se SIM: verificar artefatos criados
- Reportar apenas quando tudo 100%

## 3. CRIAÇÃO DE TODOS DETALHADOS (ANTI-VAGO)

### 3.1 Padrão de Qualidade

TODOs DEVEM ser:
- **Específicos**: Ação clara, sem ambiguidade
- **Mensuráveis**: Critério de aceite verificável
- **Executáveis**: Passos concretos, não abstratos
- **Completos**: Incluir onde buscar informação (ferramenta, fonte)

### 3.2 Exemplos VAGO vs DETALHADO

#### ❌ VAGO (NUNCA fazer assim):
```
- Pesquisar sobre o mercado
- Validar tecnologia
- Criar documento de escopo
- Analisar competidores
```

#### ✅ DETALHADO (SEMPRE fazer assim):
```
- Delegar para web_search_agent: pesquisar "mercado de [produto] Brasil 2024" e coletar: tamanho, crescimento, principais players
- Ler process/[ProcessName]/knowledge.MD seção "Tecnologias Recomendadas" e validar stack contra requisitos do projeto
- Criar 01-escopo.md em drive/[Project]/[Process]/ seguindo template de _DATA/templates/escopo-template.md, preenchendo 100% dos campos
- Delegar para web_search_agent: encontrar 5 competidores de [produto] incluindo features, pricing, público-alvo
```

### 3.3 Estrutura de TODO Completo

```
**TODO [N]**: [Ação específica]
**Ferramenta**: [filesystem/web_search_agent/screenshot_agent/sub_agent]
**Input**: [O que precisa para executar]
**Output**: [O que deve gerar]
**Critério de aceite**: [Como validar que está completo]
**Estimativa**: [Complexidade: simples/média/complexa]
```

Exemplo:
```
**TODO 3**: Pesquisar 5 competidores do mercado de validação Pix
**Ferramenta**: web_search_agent (via delegação)
**Input**: Nome do produto/mercado
**Output**: Lista com 5 competidores contendo: nome, site, features principais, pricing (se disponível)
**Critério de aceite**: Arquivo competitors.md criado com 5 entradas completas, cada uma com mínimo 3 features listadas
**Estimativa**: Média (15-20 min)
```

### 3.4 Quantidade Mínima de TODOs

Para processos completos:
- **Mínimo**: 10 TODOs detalhados
- **Recomendado**: 15-20 TODOs
- **Complexos**: 20-30 TODOs

Breakdown sugerido:
1. **Setup e preparação** (2-3 TODOs): Ler documentação, mapear templates, preparar ambiente
2. **Coleta de dados** (4-6 TODOs): Pesquisas, scraping, análises
3. **Construção de artefatos** (3-5 TODOs): Criar cada artefato separadamente
4. **Validação** (2-3 TODOs): Validar cada artefato contra critérios
5. **Finalização** (1-2 TODOs): Relatório, verificação de completude

### 3.5 TODOs Autônomos (Anti-Dependência de Usuário)

Ao criar TODOs, SEMPRE inclua tasks de coleta autônoma:

❌ **ERRADO** (cria dependência do usuário):
```
- Perguntar ao usuário qual o público-alvo
- Aguardar informação sobre tecnologias preferidas
- Solicitar lista de competidores
```

✅ **CORRETO** (totalmente autônomo):
```
- Delegar para web_search_agent: pesquisar "público-alvo de [tipo de produto] no Brasil" e definir persona baseado em dados de mercado
- Delegar para web_search_agent: pesquisar "melhores práticas stack [tipo de aplicação] 2025" e selecionar tecnologias modernas e populares
- Delegar para web_search_agent: encontrar "competidores de [produto]" e criar lista com top 5 players do mercado
```

## 4. DIRETRIZES DO AGENTS.MD

### 4.1 Leitura Obrigatória de Models

Referência: AGENTS.MD linha 9-10

- SEMPRE leia models antes de criar artefatos
- Use models/ como fonte de verdade para templates
- Mantenha consistência com estrutura definida em models/

### 4.2 Uso de Artifacts Compartilhados (_SHARED/)

Referência: AGENTS.MD linha 134, 183-186, 244

- **ANTES** de criar qualquer template, verifique `process/_SHARED/`
- Se template já existe em _SHARED/: REFERENCIE, não duplique
- Se criar template usado por 2+ processos: mova para _SHARED/ e atualize README
- Consulte process/_SHARED/README.MD para guidelines completas

### 4.3 Consistência Process ↔ Tasks ↔ Validator

Referência: AGENTS.MD linha 47

Sempre verifique alinhamento:
- **process.MD**: Define ETAPAS e OUTPUTS esperados
- **tasks.MD**: Desdobra etapas em TODOs executáveis
- **validator.MD**: Define critérios para validar OUTPUTS

Fluxo de validação:
1. Cada OUTPUT de process.MD deve ter critérios em validator.MD
2. Cada etapa de process.MD deve ter TODOs correspondentes em tasks.MD
3. Cada TODO deve ter critério de aceite alinhado com validator.MD

### 4.4 Idioma e Formatação

Referência: AGENTS.MD linha 115-117

- **Conteúdo markdown**: SEMPRE em Português (pt-BR)
- **Nomes de arquivo**: SEMPRE em inglês CamelCase
- **Sem markdown tables**: Use bullet lists, numbered lists ou plain text
- **Sem emojis**: Mantenha documentação profissional e text-only

## 5. USO DE FERRAMENTAS

### 5.1 Web Search Agent

**IMPORTANTE**: Não existe toolset `web_search` ou `web_scraping`. Use delegação ao `web_search_agent`.

Use web_search_agent (via delegação de subagente) para:
- Consultar informações sobre tecnologias, mercado, concorrentes, tendências
- Buscar informações atualizadas e contexto externo
- Pesquisar referências, URLs, documentação
- Descobrir melhores práticas, padrões de mercado

Como usar:
1. **Delegação**: Quando precisar de pesquisa web, delegue para 'web_search_agent'
2. **Query específica**: Passe query clara e específica
   - Exemplo: "Pesquisar frameworks Node.js modernos para APIs REST 2025"
   - Exemplo: "Encontrar 5 competidores de [produto] no Brasil"
3. **Aguarde resultado**: web_search_agent retornará informações encontradas
4. **Documente**: Sempre documente fontes e data nos artefatos

Sempre documente nos artefatos:
- Query usada
- Data da pesquisa (YYYY-MM-DD)
- Principais achados
- Fontes retornadas pelo web_search_agent

Exemplo de uso:
```
TODO: "Pesquisar tecnologias modernas para autenticação de APIs"
Execução:
1. Delegar para web_search_agent: "modern API authentication technologies 2025 OAuth JWT"
2. Aguardar resultado
3. Documentar: "Pesquisa realizada em 2025-01-07 via web_search_agent. Tecnologias encontradas: OAuth 2.0, JWT, API Keys, mTLS. Fontes: [lista de URLs]"
```

### 5.2 Screenshot Agent

Use screenshot_agent quando:
- Processo requerer evidências visuais
- Reverse Engineering de SaaS
- Validação de interfaces
- Documentação visual de fluxos

Organização:
- Screenshots salvos em `drive/<ProjectName>/_screenshots/`
- Nomeação: `screenshot-YYYY-MM-DD-HH-MM-descrição.png`
- Referência em artefatos: `![Descrição](../_screenshots/screenshot-file.png)`
- Log em `screenshots-log.md`

**Nota**: Screenshots são opcionais - use apenas quando agregar valor à documentação.

### 5.3 Filesystem

Operações de arquivo:
- **Leitura**: Sempre leia process.MD, knowledge.MD, tasks.MD, validator.MD antes de executar
- **Escrita**: Crie artefatos em `drive/<ProjectName>/<ProcessName>/` seguindo nomenclatura numérica (01-, 02-, etc.)
- **Templates**: Copie de `process/<ProcessName>/_DATA/` ou `process/_SHARED/templates/`

### 5.4 TODO (TodoWrite)

Gerenciamento de tarefas:
- **Criar**: Ao iniciar processo, crie lista completa de TODOs (10-20 mínimo)
- **Atualizar**: Marque in_progress ANTES de iniciar, completed APÓS terminar
- **Monitorar**: Mantenha contador "TODO X de Y"
- **Checkpoint**: A cada 5 TODOs, salve estado em 00-process-context.md

Estados possíveis:
- `pending`: Não iniciado
- `in_progress`: Em execução (máximo 1 por vez)
- `completed`: Concluído com sucesso
- `failed`: Falhou (documente razão)

## 6. ESTRUTURA DE ARQUIVOS

### 6.1 Nomenclatura

- **Pastas**: CamelCase (ex: `MVPScopeDefinition`, `LeadQualification`)
- **Arquivos de processo**: lowercase.MD (ex: `process.MD`, `knowledge.MD`)
- **Artefatos em drive/**: Numeração sequencial (ex: `01-escopo.md`, `02-requisitos.md`)
- **Data folder**: `_DATA` (uppercase com underscore)
- **Shared folder**: `_SHARED` (uppercase com underscore)

### 6.2 Hierarquia Padrão

```
process/
  <ProcessName>/
    process.MD           # Definição do processo
    knowledge.MD         # Base de conhecimento
    tasks.MD             # Sequência operacional
    validator.MD         # Critérios de qualidade
    _DATA/               # Artifacts do processo
      templates/         # Templates de artefatos
      examples/          # Exemplos de saída
      references/        # Materiais de apoio
  _SHARED/               # Artifacts compartilhados
    templates/           # Templates globais
    references/          # Referências globais

drive/
  <ProjectName>/         # CamelCase do contexto
    00-context.md        # Contexto do projeto
    <ProcessName>/       # Nome exato do processo
      00-process-context.md   # Contexto + TODOs
      01-artifact.md     # Primeiro artefato
      02-artifact.md     # Segundo artefato
    _screenshots/        # Screenshots (se houver)
      screenshot-*.png
      screenshots-log.md
```

### 6.3 Arquivo 00-process-context.md

Criado por process_memory_manager, contém:

```markdown
# Contexto de Execução: [ProcessName]

## Informações do Projeto
- Nome: [ProjectName]
- Estratégia: [StrategyName]
- Data: [YYYY-MM-DD]
- Executor: process_executor

## Documentação Consolidada

### Process.MD
[Conteúdo completo do process.MD]

### Knowledge.MD
[Conteúdo completo do knowledge.MD]

### Tasks.MD
[Conteúdo completo do tasks.MD]

### Validator.MD
[Conteúdo completo do validator.MD]

## Templates Mapeados

### Templates Locais (_DATA/)
- [Lista de templates em process/<ProcessName>/_DATA/]

### Templates Compartilhados (_SHARED/)
- [Lista de templates em process/_SHARED/templates/]

## TODOs Detalhados

[Lista completa de 10-20 TODOs criados pelo memory_manager]

## Requisitos e Informações Necessárias

[Lista de dados que precisam ser coletados autonomamente]

## Plano de Coleta Autônoma

[Como cada informação será obtida: web_search, web_scraping, assumption]
```

## 7. VALIDAÇÃO E QUALIDADE

### 7.1 Checklist Pré-Execução

Antes de iniciar qualquer processo, valide:

- [ ] Estratégia existe em `strategies/`
- [ ] Processo existe em `process/`
- [ ] process.MD foi lido completamente
- [ ] knowledge.MD foi lido completamente
- [ ] tasks.MD foi lido completamente
- [ ] validator.MD foi lido completamente
- [ ] _SHARED/ foi verificado para templates compartilhados
- [ ] Pasta `drive/<ProjectName>/` será criada com nome CamelCase
- [ ] Lista de requisitos/informações necessárias foi criada
- [ ] Plano de coleta autônoma de dados está definido

### 7.2 Checklist Pós-Execução

Após completar processo, valide:

- [ ] 100% dos TODOs marcados como completed ou failed (nenhum pending)
- [ ] Todos os artefatos esperados foram criados
- [ ] Todos os artefatos estão 100% preenchidos (sem placeholders)
- [ ] Assumptions documentadas com fonte/base clara
- [ ] Artefatos seguem templates de models/ ou _DATA/
- [ ] Nomenclatura de arquivos segue padrão (01-, 02-, etc.)
- [ ] Português correto em todo conteúdo markdown
- [ ] Critérios de validator.MD foram atendidos
- [ ] 00-process-context.md atualizado com resultado final

### 7.3 Critérios de Falha

Processo é considerado FALHO se:

- ❌ Qualquer TODO ficou pending sem justificativa
- ❌ Qualquer artefato ficou incompleto ou com placeholders
- ❌ Execução parou no meio sem checkpoint/recuperação
- ❌ Assumptions feitas sem documentação de base
- ❌ Templates de _SHARED/ foram duplicados em vez de referenciados
- ❌ Nomenclatura de arquivos não segue padrão
- ❌ Conteúdo markdown em inglês em vez de português
- ❌ Critérios de validator.MD não foram atendidos

## 8. TRATAMENTO DE ERROS E EXCEÇÕES

### 8.1 Erros Recuperáveis

Se encontrar erro que não impede continuação:

1. **Documente o erro**:
   ```
   ⚠️ ERRO em TODO [N]: [Descrição do erro]
   Ação tomada: [Como contornou]
   Impacto: [Mínimo/Moderado/Alto]
   ```

2. **Tente alternativa**:
   - web_search falhou → tente web_scraping
   - web_scraping falhou → use assumption baseado em pesquisa
   - Template não encontrado → use template genérico de _SHARED/

3. **Continue execução**: Marque TODO como completed com ressalva

4. **Reporte no final**: Liste todos os erros encontrados no relatório

### 8.2 Erros Bloqueantes

Se encontrar erro que impede continuação:

1. **Documente claramente**:
   ```
   ❌ ERRO BLOQUEANTE em TODO [N]: [Descrição]
   Razão: [Por que impede continuação]
   Tentativas: [O que foi tentado]
   Necessário: [O que precisa para resolver]
   ```

2. **Marque TODO como failed**

3. **Crie TODO de resolução**:
   ```
   TODO [N+1]: Resolver bloqueio do TODO [N]
   Ação: [Passos específicos para resolver]
   Responsável: [Agente/Usuário]
   ```

4. **Continue com próximos TODOs**: Não deixe um bloqueio parar tudo

5. **Reporte ao final**: Liste bloqueios e TODOs que falharam

### 8.3 Limites e Pausas

Se atingir limite de tokens/tempo:

1. **Salve estado atual**:
   - Atualize 00-process-context.md com progresso
   - Marque TODO atual como in_progress
   - Documente último passo executado

2. **Crie ponto de retomada**:
   ```
   ## CHECKPOINT [YYYY-MM-DD HH:MM]
   - TODOs completed: [X]
   - TODO in_progress: [N] - [Descrição]
   - Último passo: [Detalhe]
   - Próximo passo: [O que fazer ao retomar]
   ```

3. **Notifique pausa**: Informe root/usuário que execução será retomada

4. **Ao retomar**: Leia checkpoint, retome do ponto exato

---

## INSTRUÇÕES FINAIS

**Para desenvolvedores de agentes**:
- Ao criar novo agente, referencie este documento para regras globais
- Adicione apenas instruções ESPECÍFICAS do agente no prompt
- Se regra se aplica a 3+ agentes, mova para este arquivo

**Para agentes em execução**:
- Leia este documento COMPLETAMENTE antes de iniciar operações
- Em caso de dúvida, consulte a seção relevante aqui
- Se regra não estiver clara, documente e prossiga com melhor prática

**Hierarquia de prioridade**:
1. Instruções específicas do agente (no orchestrator)
2. Diretrizes deste documento (global-directives.MD)
3. AGENTS.MD (guidelines gerais do framework)
4. Models (templates e estruturas)

**Manutenção**:
- Versão: 1.0
- Última atualização: 2025-01-07
- Responsável: Orquestração CA Agent SDK

---

**Este documento é a fonte única de verdade para diretrizes globais de agentes. Alterações aqui propagam automaticamente para todos os agentes que o referenciam.**
