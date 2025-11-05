# Estrategias - Guia de Organizacao

## Sobre este diretorio

Este diretorio organiza estrategias de negocio, campanhas e iniciativas estruturadas que orientam acoes taticas em diferentes contextos (validacao de produto, lancamento, crescimento, otimizacao).

Cada estrategia e armazenada em sua propria subpasta com tres arquivos essenciais que se complementam e devem manter coerencia total entre si.

## Estrutura padrao para cada estrategia

Ao criar uma nova estrategia, organize os arquivos seguindo a estrutura:

```
strategies/
  NomeDaEstrategia/
    _DATA/
    knowledge.MD
    process.MD
    tasks.MD
```

## Arquivo 1: knowledge.MD

### Objetivo

Fornecer o conteudo teorico, fundamentos e referencias que suportam a estrategia. Serve como guia conceitual antes da execucao.

### Conteudo obrigatorio

1. **Visao geral**

   - Descricao da estrategia
   - Contexto de aplicacao e principais casos de uso

2. **Objetivo central**

   - Meta principal que a estrategia pretende alcancar
   - Metricas de sucesso esperadas

3. **Principios fundamentais**

   - Lista de principios que orientam decisoes e acoes
   - Valores que devem ser mantidos ao longo da execucao

4. **Metricas de sucesso iniciais**

   - Indicadores quantitativos que validam se a estrategia funciona
   - Benchmarks e referencias de mercado quando aplicavel

5. **Quando aplicar**

   - Situacoes, contextos ou estagios do negocio em que a estrategia e adequada
   - Sinais e gatilhos que indicam a necessidade de aplicar a estrategia

6. **Como aplicar**

   - Visao macro das etapas necessarias para executar a estrategia
   - Prerequisitos e condicoes de entrada

7. **Etapas da estrategia**

   - Divisao conceitual em fases ou etapas
   - Para cada etapa:
     - Objetivo especifico
     - Acoes necessarias
     - Criterios de aceite (o que valida que a etapa foi concluida)
     - Ferramentas ou artefatos sugeridos

8. **Fluxo da estrategia**

   - Diagrama textual ou narrativa do fluxo de etapas
   - Decisoes criticas e pontos de bifurcacao

9. **Lista de tarefas para executar a estrategia**

   - Lista ordenada de entregas tangivel que devem ser produzidas
   - Checklist de alto nivel que conecta ao arquivo tasks.MD

10. **Templates uteis**

    - Modelos de mensagens, roteiros, estruturas de copy, planilhas ou ferramentas prontas
    - Exemplos praticos de cada artefato necessario

11. **Riscos comuns e como evitar**

    - Problemas recorrentes ao aplicar a estrategia
    - Mitigacoes recomendadas

12. **Proximos passos sugeridos**

    - Orientacoes claras para quem terminou de ler e quer comecar a execucao

13. **Referencias internas**
    - Links para process.MD e tasks.MD
    - Links para outras estrategias ou processos relacionados

### Exemplo de estrutura

```markdown
# Base de Conhecimento - Estrategia [Nome]

## Visao geral

[Descricao da estrategia]

## Objetivo central

[Meta principal]

## Principios fundamentais

1. Principio 1
2. Principio 2

## Metricas de sucesso iniciais

- Metrica 1: valor esperado
- Metrica 2: valor esperado

## Quando aplicar

- Situacao 1
- Situacao 2

## Como aplicar

[Visao macro das etapas]

## Etapas da estrategia

### Etapa 1 - Nome da etapa (tempo estimado)

Objetivo: [descricao do objetivo]

Acoes necessarias:

- Acao 1
- Acao 2

Criterio de aceite: [validacao]

### Etapa 2 - Nome da etapa (tempo estimado)

[...]

## Fluxo da estrategia

[Diagrama textual ou narrativa]

## Lista de tarefas para executar a estrategia

- [ ] Tarefa 1
- [ ] Tarefa 2

## Templates uteis

[Modelos prontos]

## Riscos comuns e como evitar

1. Risco X - Mitigacao Y

## Proximos passos sugeridos

A) Opcao 1
B) Opcao 2

## Referencias internas

- process.MD
- tasks.MD
- [Outras referencias]
```

## Arquivo 2: process.MD

### Objetivo

Detalhar o passo a passo operacional de como executar a estrategia na pratica. Especifica responsaveis, entradas, ferramentas, prazos e indicadores.

### Conteudo obrigatorio

1. **Objetivo do processo**
   - Descricao clara do que o processo entrega
   - Alinhamento com o objetivo central da knowledges.MD
   -
2. **Entradas essenciais**

   - Lista de insumos, dados ou condicoes que devem estar disponiveis antes de comecar
   - Exemplos: documentos, acessos, orcamento, tempo disponivel

3. **Ferramentas e artefatos de apoio**

   - Lista de sistemas, plataformas, templates, planilhas ou documentos necessarios
   - Links ou referencias a templates existentes

4. **Requisitos**

   - Prerequisitos tecnicos, operacionais ou de conhecimento
   - Certificacoes, habilitacoes ou permissoes necessarias

5. **Fluxo detalhado por etapa**

   - Para cada etapa listada na knowledges.MD:
     - Tabela com colunas: Atividade | Descricao | Saida esperada
     - Tempo estimado por atividade
     - Criterio de aceite especifico
   - Deve haver correspondencia 1:1 com as etapas da knowledges.MD

6. **Indicadores de sucesso**

   - KPIs e metricas que validam a execucao
   - Metas quantitativas por indicador
   - Alinhamento com as metricas de sucesso definidas na knowledges.MD

7. **Rituais e comunicacao**

   - Frequencia de check-ins, reunioes de acompanhamento e alinhamento
   - Canais de comunicacao utilizados (hub, Slack, e-mail, etc)
   - Momentos de documentacao e reporte

8. **Riscos e mitigacoes**

   - Tabela com: Risco | Probabilidade | Impacto | Mitigacao
   - Correspondencia com os riscos listados na knowledges.MD

9. **Checklist de prontidao para inicio**

   - Checklist que valida se todas as entradas e requisitos estao prontos
   - Garante que a execucao comece apenas quando preparada

10. **Proximos passos apos conclusao**

    - Orientacao sobre o que fazer quando a estrategia for concluida
    - Conexao com outros processos ou estrategias subsequentes

### Exemplo de estrutura

```markdown
# Processo [Nome da Estrategia]

## Objetivo do processo

[Descricao do que o processo entrega]

## Entradas essenciais

- Entrada 1
- Entrada 2

## Ferramentas e artefatos de apoio

- Ferramenta 1
- Ferramenta 2

## Requisitos

- Requisito 1
- Requisito 2

## Fluxo detalhado por etapa

### Etapa 1 - Nome da etapa (tempo)

#### Atividade

Descrição do que precisa ser feito na ativadade

#### Critério de aceite

Validação para identificar que a atividade foi realizada de acordo com o esperado

#### Resultado esperado

Resultado que deverá ser espero para conclusao da atividade

### Etapa 2 - Nome da etapa (tempo)

[...]

## Indicadores de sucesso

- Indicador 1: meta
- Indicador 2: meta

## Rituais e comunicacao

- Ritual 1: frequencia e objetivo
- Ritual 2: frequencia e objetivo

## Riscos e mitigacoes

| Risco   | Probabilidade | Impacto | Mitigacao         |
| ------- | ------------- | ------- | ----------------- |
| Risco 1 | Alta          | Medio   | [acao preventiva] |
| Risco 2 | Baixa         | Alto    | [acao preventiva] |

## Checklist de prontidao para inicio

- [ ] Item 1 pronto
- [ ] Item 2 pronto

## Proximos passos apos conclusao

1. [proxima acao]
2. [proxima acao]
```

## Arquivo 3: tasks.MD

### Objetivo

Fornecer um checklist detalhado e operacional com todas as tarefas necessarias para executar a estrategia. Cada tarefa deve especificar responsavel, tempo estimado e criterio de validacao.

### Conteudo obrigatorio

1. **Como usar este documento**

   - Instrucoes sobre como marcar itens completos
   - Definicoes de Owner (responsavel final) e Responsaveis (executores)
   - Orientacao sobre atualizacao de prazos

2. **Tarefas por etapa**

   - Para cada etapa do process.MD, liste tarefas especificas
   - Cada tarefa deve conter:
     - [ ] Checkbox para marcar conclusao
     - Descricao clara da tarefa
     - Owner: cargo responsavel final pela entrega
     - Responsaveis: cargos que executam (pode ser mais de um)
     - Aceite: criterio mensuravel que valida a tarefa como concluida
     - Prazo sugerido: indicacao de quando a tarefa deve ser concluida (ex: Dia 1, Dias 2-4)

3. **Correspondencia 1:1 com etapas**

   - Cada secao de tarefas deve corresponder exatamente a uma etapa do process.MD
   - A ordem das tarefas deve seguir o fluxo logico de execucao

4. **Checklist Go-Live (se aplicavel)**

   - Lista de pre-requisitos que devem estar concluidos antes de iniciar vendas, lancamento ou ativacao
   - Garante que nenhuma etapa critica seja pulada

5. **KPIs - Acompanhamento periodico**

   - Lista dos indicadores que devem ser monitorados durante a execucao
   - Metas quantitativas para cada KPI
   - Alinhamento com Indicadores de sucesso do process.MD

6. **Observacoes importantes**
   - Notas sobre adaptacoes para contextos diferentes (projetos solo, startups pequenas, etc)
   - Lembretes sobre uso de nomenclatura exata de cargos
   - Orientacoes sobre documentacao continua

### Exemplo de estrutura

```markdown
# Tarefas Operacionais - Estrategia [Nome]

## Como usar este documento

- Marque cada item quando o criterio de aceite for atingido
- Atualize prazos conforme necessario

## Etapa 1 - Nome da etapa (tempo estimado)

- [ ] Tarefa 1

  - Aceite: [criterio mensuravel]
  - Tempo estimado: Dia 1

- [ ] Tarefa 2
  - Aceite: [criterio mensuravel]
  - Tempo estimado: Dias 1-2

## Etapa 2 - Nome da etapa (tempo estimado)

- [ ] Tarefa 3
      [...]

## Checklist Go-Live (pre-requisitos para inicio)

- [ ] Pre-requisito 1
- [ ] Pre-requisito 2

## KPIs - Acompanhamento [periodicidade]

- KPI 1: meta > X%
- KPI 2: meta < Y dias

## Observacoes importantes

1. [Nota 1]
2. [Nota 2]
```

## Coerencia entre os tres arquivos

Para garantir que os tres arquivos estejam alinhados, siga estas regras:

### knowledge.MD → process.MD

- Cada **Etapa** da Base de conhecimento deve ter uma secao correspondente no **Fluxo detalhado por etapa** do process.MD
- As **Metricas de sucesso** da Base de conhecimento devem aparecer como **Indicadores de sucesso** no process.MD
- Os **Riscos comuns** da Base de conhecimento devem estar detalhados em **Riscos e mitigacoes** do process.MD

### process.MD → tasks.MD

- Cada **Etapa** do process.MD deve gerar uma secao de tarefas correspondente no tasks.MD
- As **Atividades** listadas em cada etapa do process.MD devem ser desmembradas em tarefas especificas no tasks.MD
- Os **Indicadores de sucesso** do process.MD devem aparecer na secao **KPIs** do tasks.MD
- Os **Responsaveis e stakeholders** do process.MD devem corresponder aos **Owners e Responsaveis** listados nas tarefas

### knowledges.MD → tasks.MD

- A **Lista de tarefas para executar a estrategia** da Base de conhecimento e a versao resumida do checklist completo do tasks.MD
- Os **Criterios de aceite** de cada etapa da Base de conhecimento devem estar refletidos nos criterios de aceite das tarefas no tasks.MD

## Checklist de validacao ao criar nova estrategia

Ao finalizar a criacao de uma nova estrategia, valide a coerencia usando esta checklist:

- [ ] Todas as etapas da knowledges.MD possuem secao correspondente no process.MD
- [ ] Todas as etapas do process.MD possuem tarefas correspondentes no tasks.MD
- [ ] As metricas de sucesso estao consistentes nos tres arquivos
- [ ] Os riscos listados na knowledges.MD estao detalhados no process.MD
- [ ] Os criterios de aceite sao especificos e mensuraveis em todos os arquivos
- [ ] Os prazos sugeridos no tasks.MD sao realistas e alinhados com o tempo estimado no process.MD
- [ ] Ferramentas e artefatos mencionados estao consistentes entre knowledges.MD e process.MD
- [ ] Templates citados na knowledges.MD sao referenciados no process.MD quando aplicavel
- [ ] Proximos passos estao documentados tanto na knowledges.MD quanto no process.MD

## Estrategias Disponiveis

### MVPBuilder - Construcao de Minimum Viable Product

**Localizacao**: [strategies/MVPBuilder/](MVPBuilder/)

**Objetivo**: Construir e validar um MVP funcional em ate 8 semanas utilizando stack tecnica padronizada (Next.js, Prisma, PostgreSQL, NextAuth, Stripe).

**Quando usar**:
- Voce tem hipotese de produto clara para validar
- Existe documentacao inicial (briefing, pesquisas, personas)
- Objetivo e validacao rapida antes de investir pesado
- Solucao pode ser construida como SaaS/aplicacao web
- Necessidade de testar monetizacao desde cedo

**Entradas principais**:
- Briefing de produto ou documentacao inicial
- Hipotese de valor clara
- Definicao de publico-alvo
- Budget aprovado ($500-2.000/mes)
- Time minimo (1 dev full-stack)

**Saidas principais**:
- MVP funcional em producao
- Sistema de pagamento integrado (Stripe)
- Lista completa de issues para desenvolvimento
- Relatorio de validacao com recomendacao (Pivotar/Perseverar/Expandir)

**Duracao**: 6-8 semanas de desenvolvimento + 2-4 semanas de validacao

**Documentos**:
- [README.MD](MVPBuilder/README.MD) - Guia rapido
- [knowledge.MD](MVPBuilder/knowledge.MD) - Base teorica completa
- [process.MD](MVPBuilder/process.MD) - Processo operacional detalhado
- [tasks.MD](MVPBuilder/tasks.MD) - Checklist de tarefas
- [_DATA/](MVPBuilder/_DATA/) - Templates de artefatos

---

## Referencias de exemplo

Para criar uma nova estrategia, consulte a estrutura ja existente:

- [MVPBuilder/knowledge.MD](MVPBuilder/knowledge.MD) - exemplo completo de base teorica
- [MVPBuilder/process.MD](MVPBuilder/process.MD) - exemplo de processo operacional detalhado
- [MVPBuilder/tasks.MD](MVPBuilder/tasks.MD) - exemplo de checklist operacional

## Atualizacao de estrategias existentes

Ao atualizar uma estrategia ja documentada:

1. Identifique qual dos tres arquivos precisa de ajuste
2. Atualize o arquivo principal
3. Valide se a mudanca impacta os outros dois arquivos
4. Atualize os arquivos relacionados para manter coerencia
5. Execute a checklist de validacao acima

## Integracao com processos organizacionais

- Sempre que uma estrategia mencionar um cargo, valide que ele existe em `README.MD`
- Se a execucao da estrategia gerar novos processos permanentes, adicione-os em `Processos/`
- Estrategias que envolvem multiplas areas devem ser validadas com os coordenadores ou gerentes das areas impactadas antes de ativar
