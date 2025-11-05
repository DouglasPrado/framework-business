# Processo: Definição de Escopo de MVP

## Visão Geral

O processo de Definição de Escopo de MVP transforma documentação dispersa (briefings, pesquisas, entrevistas) em um Briefing de MVP estruturado e aprovado que serve como contrato e referência única para todo o desenvolvimento de um Minimum Viable Product.

**Objetivo:** Criar Briefing de MVP completo com hipótese clara, funcionalidades priorizadas, métricas de validação e aprovação formal de stakeholders.

**Duração:** 4-5 dias

**Responsável típico:** Product Owner, Product Manager ou Fundador

---

## Quando Usar Este Processo

Use este processo quando:
- Você tem materiais de descoberta (briefing, pesquisas, entrevistas) mas precisa estruturar em escopo executável
- Existe decisão de construir um MVP mas escopo não está claro
- Múltiplas funcionalidades foram sugeridas e precisa priorizar
- Stakeholders precisam alinhar expectativas sobre o que entra (e não entra) no MVP
- Você precisa de documento consolidado para guiar desenvolvimento técnico

Não use este processo quando:
- Ainda não há problema/solução definidos (use ProblemHypothesisDefinition primeiro)
- Não há público-alvo claro (use TargetUserIdentification primeiro)
- O escopo já está 100% claro e aprovado (vá direto para MVPIssuesMapping)

---

## Estrutura de Arquivos

```
MVPScopeDefinition/
├── README.MD (este arquivo - visão geral)
├── process.MD (fluxo detalhado de etapas)
├── tasks.MD (checklist operacional de 20 tarefas)
├── knowledge.MD (base teórica, boas práticas, FAQ)
├── validator.MD (critérios de validação de qualidade)
└── _DATA/ (templates e artefatos)
    ├── template-briefing-mvp.md
    └── template-funcionalidades.md
```

---

## Como Executar Este Processo

### Passo 1: Prepare as Entradas
Certifique-se de ter:
- [ ] Pasta com documentação do projeto (Google Drive, Notion)
- [ ] Acesso a stakeholders (disponibilidade de resposta em 48h)
- [ ] Materiais: briefing inicial, pesquisas, entrevistas, personas (se disponíveis)
- [ ] Orçamento pré-aprovado ($500-2.000/mês)
- [ ] Definição de time disponível (mínimo 1 dev full-stack)

**Tempo:** 15 minutos para verificação

### Passo 2: Leia os Documentos Orientadores
Leia nesta ordem:
1. [process.MD](process.MD) - Entenda o fluxo completo de 5 etapas
2. [tasks.MD](tasks.MD) - Familiarize-se com as 20 tarefas operacionais
3. [knowledge.MD](knowledge.MD) - Consulte conceitos fundamentais

**Tempo:** 1-2 horas de leitura

### Passo 3: Execute as Tarefas
Siga o [tasks.MD](tasks.MD) sequencialmente:
- Etapa 1: Análise de Documentação (Tarefas 1-4)
- Etapa 2: Definição de Hipótese (Tarefas 5-6)
- Etapa 3: Definição de Funcionalidades (Tarefas 7-10)
- Etapa 4: Criação do Briefing (Tarefas 11-17)
- Etapa 5: Revisão e Aprovação (Tarefas 18-20)

**Tempo:** 4-5 dias de execução

### Passo 4: Valide a Qualidade
Use o [validator.MD](validator.MD) para garantir:
- [ ] Todos os critérios de completude atendidos
- [ ] Qualidade da hipótese validada
- [ ] Escopo é realista (6-8 semanas)
- [ ] Aprovação formal documentada

**Tempo:** 1 hora de validação

### Passo 5: Compartilhe e Avance
- [ ] Compartilhe Briefing final com todo o time
- [ ] Comunique conclusão a stakeholders
- [ ] Inicie próximo processo: MVPIssuesMapping

---

## Principais Entregas

Ao final deste processo, você terá:

### 1. Briefing de MVP (Documento Principal)
Documento completo com 16 seções incluindo:
- Hipótese principal no formato padrão
- Funcionalidade core detalhada
- Funcionalidades secundárias (máximo 3)
- Scope negativo documentado
- Métricas de validação quantitativas
- Stack técnica validada
- Timeline de 6-8 semanas
- Orçamento estimado
- Riscos e mitigações
- Aprovação formal

**Localização:** _DATA/template-briefing-mvp.md (preencher durante execução)

### 2. Template de Funcionalidades
Detalhamento técnico de funcionalidades com:
- Fluxo de usuário completo da funcionalidade core
- Requisitos funcionais (frontend, backend, banco)
- Casos de uso
- Critérios de aceite
- Features excluídas com justificativas

**Localização:** _DATA/template-funcionalidades.md (preencher durante execução)

### 3. Aprovação Formal
- Ata de reunião de aprovação
- Email ou documento de aprovação de stakeholders
- Registro de versão final aprovada

---

## Métricas de Sucesso

O processo foi bem executado se:
- Tempo total: 4-5 dias (máximo 7)
- Aprovação na primeira ou segunda revisão com stakeholders
- Hipótese é clara e testável por alguém externo
- Funcionalidades cabem em timeline de 6-8 semanas
- 100% dos stakeholders aprovam o Briefing
- Nenhum sinal de alerta no validator.MD

---

## Integrações com Outros Processos

### Processos Anteriores (Opcionais)
- **ProblemHypothesisDefinition:** Se hipótese não existe, execute antes
- **TargetUserIdentification:** Se público-alvo não está claro, execute antes

### Próximo Processo (Obrigatório)
- **MVPIssuesMapping:** Mapeamento técnico de funcionalidades em issues de desenvolvimento

### Processos da Estratégia MVPBuilder
Este processo é a **Etapa 1** da estratégia completa MVPBuilder:
1. **MVPScopeDefinition** (você está aqui)
2. MVPIssuesMapping
3. MVPInfrastructureSetup
4. MVPCoreDevelopment
5. MVPSecondaryDevelopment
6. MVPPreLaunchValidation
7. MVPLaunchMonitoring

---

## Riscos Comuns e Como Evitar

### Risco: Escopo muito grande
**Sinal:** Timeline estimada acima de 8 semanas, mais de 3 funcionalidades secundárias
**Mitigação:** Aplicar rigorosamente critério "MVP funciona sem isso?". Documentar scope negativo.

### Risco: Falta de alinhamento com stakeholders
**Sinal:** Múltiplas rodadas de revisão, feedback contraditório
**Mitigação:** Workshop de alinhamento facilitado. Uso de técnicas de priorização objetiva.

### Risco: Hipótese vaga ou não testável
**Sinal:** QUEM genérico, RESULTADO vago, DOR não validada
**Mitigação:** Consultar knowledge.MD seção "Framework de Hipótese". Validar com usuários.

### Risco: Documentação insuficiente
**Sinal:** Muitas perguntas sem resposta, público-alvo não claro
**Mitigação:** Pausar processo. Executar discovery adicional (entrevistas, pesquisas).

---

## FAQ Rápido

**P: Quanto tempo leva?**
R: 4-5 dias em média. Máximo 7 dias.

**P: Preciso de time técnico envolvido?**
R: Recomendado envolver Tech Lead na validação de stack técnica e timeline (Tarefa 13-14).

**P: E se não houver documentação para analisar?**
R: Execute processos de discovery primeiro (ProblemHypothesisDefinition, TargetUserIdentification) ou realize discovery rápido com stakeholders.

**P: Posso pular a aprovação formal?**
R: Não recomendado. Aprovação documentada evita mal-entendidos e serve como contrato de escopo.

**P: E se stakeholders quiserem mais de 3 funcionalidades secundárias?**
R: Use scope negativo: documente as excluídas, justifique, prometa considerar pós-validação. Se impasse, escalone para decisor final.

**P: As 6-8 semanas incluem este processo de definição?**
R: Não. A timeline de 6-8 semanas é para desenvolvimento técnico (processos 2-7). Este processo de definição leva 4-5 dias adicionais.

---

## Templates Disponíveis

### Template 1: Briefing de MVP
**Arquivo:** _DATA/template-briefing-mvp.md
**Quando usar:** Durante Etapa 4 (Tarefas 11-17)
**O que contém:** Estrutura completa com 16 seções para documentar todo o escopo do MVP

### Template 2: Funcionalidades
**Arquivo:** _DATA/template-funcionalidades.md
**Quando usar:** Durante Etapa 3 (Tarefas 7-9)
**O que contém:** Detalhamento técnico de funcionalidades, fluxos de usuário, requisitos

### Template 3: Declaração de Hipótese (Compartilhado)
**Arquivo:** ../../_SHARED/templates/declaracao-hipotese.md
**Quando usar:** Durante Etapa 2 (Tarefa 5)
**O que contém:** Formato padrão e exemplos de declaração de hipótese

---

## Checklist Rápido: Estou Pronto para Começar?

- [ ] Tenho acesso à pasta com documentação do projeto
- [ ] Stakeholders estão disponíveis para validações
- [ ] Sei quem é o decisor final em caso de impasse
- [ ] Tenho entre 4-6 horas/dia para dedicar ao processo
- [ ] Li process.MD, tasks.MD e knowledge.MD
- [ ] Baixei templates de _DATA/
- [ ] Orçamento de infraestrutura está pré-aprovado

Se todos os itens estão marcados, você está pronto! Comece pela [Tarefa 1 do tasks.MD](tasks.MD).

---

## Suporte

**Dúvidas sobre conceitos?**
Consulte [knowledge.MD](knowledge.MD) - Especialmente seções:
- Fundamentos Teóricos (O que é MVP, Framework de Hipótese)
- Boas Práticas
- Perguntas Frequentes

**Dúvidas sobre qualidade?**
Consulte [validator.MD](validator.MD) - Especialmente seções:
- Critérios de Qualidade
- Sinais de Alerta
- Ações Corretivas

**Dúvidas sobre execução?**
Consulte [tasks.MD](tasks.MD) - Cada tarefa tem:
- Objetivo claro
- Passos detalhados
- Critérios de conclusão
- Output esperado

---

**Criado em:** 2025-11-05
**Mantido por:** Framework Business Team
**Versão:** 1.0
**Parte da estratégia:** MVPBuilder (Etapa 1 de 7)
