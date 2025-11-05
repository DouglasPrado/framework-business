# Estrategia MVP Builder

## Visao Geral

A estrategia MVP Builder e um processo completo e estruturado para construir Minimum Viable Products (MVPs) de forma rapida e eficiente, desde a analise de documentacao ate o lancamento em producao com validacao de hipoteses.

**Objetivo**: Construir e validar um MVP funcional em ate 8 semanas, utilizando stack tecnica padronizada e gerando aprendizados acionaveis para decisao de pivotar, perseverar ou expandir.

---

## Quando Usar Esta Estrategia

Use esta estrategia quando:

- Voce tem uma hipotese de produto clara que precisa validar com mercado real
- Existe documentacao inicial (briefing, pesquisas, personas, hipoteses)
- O objetivo e validacao rapida ao inves de construcao de produto completo
- Ha orcamento limitado e necessidade de validar antes de investir pesado
- A solucao pode ser construida como SaaS/aplicacao web
- Existe necessidade de testar monetizacao desde cedo

---

## Stack Tecnica Padrao

- **Frontend**: Next.js (latest) + TypeScript + TailwindCSS
- **Backend**: Next.js API Routes
- **Banco de dados**: Prisma + PostgreSQL
- **Autenticacao**: NextAuth.js
- **Pagamento**: Stripe (sempre incluido)
- **Deploy**: Vercel
- **Analytics**: Google Analytics 4 ou Posthog
- **Monitoramento**: Sentry

---

## Estrutura de Arquivos

```
MVPBuilder/
├── README.MD (este arquivo)
├── knowledge.MD (base teorica, principios, etapas)
├── process.MD (fluxo operacional detalhado)
├── tasks.MD (checklist completo de tarefas)
└── _DATA/ (templates e artefatos)
    ├── template-briefing-mvp.md
    ├── template-funcionalidades.md
    ├── template-issue-github.md
    ├── checklist-go-live.md
    └── template-relatorio-validacao.md
```

---

## Como Usar Esta Estrategia

### Passo 1: Leia a Base de Conhecimento

Comece lendo [knowledge.MD](knowledge.MD) para entender:
- Principios fundamentais de MVP
- Etapas da estrategia
- Metricas de sucesso
- Riscos comuns e mitigacoes

**Tempo estimado**: 30-45 minutos de leitura

---

### Passo 2: Prepare as Entradas

Certifique-se de ter:
- [ ] Briefing de produto ou documentacao inicial
- [ ] Hipotese de valor clara
- [ ] Definicao de publico-alvo (persona)
- [ ] Acesso a pasta com documentacao do projeto
- [ ] Budget aprovado ($500-2.000/mes)
- [ ] Time alocado (minimo 1 dev full-stack)

Se faltar algum desses itens, volte e prepare antes de comecar.

---

### Passo 3: Leia o Processo Operacional

Leia [process.MD](process.MD) para entender o fluxo detalhado:
- Entradas essenciais
- Ferramentas necessarias
- Fluxo passo a passo de cada etapa
- Criterios de aceite
- Indicadores de sucesso

**Tempo estimado**: 1-2 horas de leitura

---

### Passo 4: Baixe os Templates

Acesse a pasta [_DATA/](_DATA/) e baixe os templates:

1. **template-briefing-mvp.md**: Use para criar o Briefing do MVP
2. **template-funcionalidades.md**: Use para mapear funcionalidades
3. **template-issue-github.md**: Use para criar issues tecnicas
4. **checklist-go-live.md**: Use antes do lancamento
5. **template-relatorio-validacao.md**: Use apos 2-4 semanas de validacao

---

### Passo 5: Execute as Tarefas

Use [tasks.MD](tasks.MD) como checklist operacional:
- Marque cada tarefa conforme completa
- Siga a ordem sugerida
- Ajuste prazos conforme necessario
- Monitore KPIs semanalmente

**Duracao total**: 6-8 semanas

---

### Passo 6: Lance e Valide

Apos lancamento:
- Monitore metricas diariamente
- Colete feedback qualitativo (entrevistas, surveys)
- Corrija bugs criticos rapidamente
- Prepare relatorio de validacao apos 2-4 semanas

---

### Passo 7: Decida Proximo Passo

Com base no relatorio de validacao, decida:
- **EXPANDIR**: Hipotese validada → Investir em crescimento
- **PERSEVERAR**: Resultados mistos → Ajustar e testar novamente
- **PIVOTAR**: Hipotese nao validada → Mudar direcao

---

## Etapas da Estrategia (Resumo)

### Etapa 1: Analise e Definicao de Escopo (4-5 dias)
- Analise de documentacao existente
- Identificacao de hipotese principal
- Definicao de funcionalidade core e secundarias
- Criacao do Briefing do MVP

### Etapa 2: Mapeamento de Issues (3-4 dias)
- Criacao do repositorio
- Mapeamento de funcionalidades em issues
- Priorizacao e estimativa
- Setup de project management

### Etapa 3: Setup de Infraestrutura (5-7 dias)
- Configuracao Prisma + PostgreSQL
- Implementacao de autenticacao (NextAuth)
- Integracao com Stripe
- Componentes base
- Deploy continuo

### Etapa 4: Desenvolvimento Core (10-14 dias)
- Frontend da funcionalidade principal
- Backend da funcionalidade principal
- Integracao
- Testes e refinamento

### Etapa 5: Desenvolvimento Secundario (7-10 dias)
- Funcionalidades secundarias
- Dashboard e perfil
- Notificacoes
- Refinamento de UX

### Etapa 6: Testes e Pre-Lancamento (5-7 dias)
- Testes completos de qualidade
- Correcao de bugs criticos
- Setup de analytics e monitoramento
- Preparacao de producao
- Checklist de Go-Live

### Etapa 7: Lancamento e Validacao (Continuo)
- Deploy final
- Onboarding de early adopters
- Monitoramento de metricas
- Coleta de feedback
- Relatorio de validacao

---

## Metricas de Sucesso

### Durante Desenvolvimento
- **Timeline**: MVP completo em ate 8 semanas
- **Issues concluidas**: 90%+ das issues planejadas
- **Bugs criticos pre-lancamento**: Zero bugs P0
- **Performance**: < 2s de resposta

### Pos-Lancamento (Validacao)
- **Cadastros**: Minimo 20 usuarios nas primeiras 4 semanas
- **Taxa de ativacao**: Minimo 60% completam funcionalidade core
- **Taxa de conversao**: Minimo 5% dos usuarios pagam
- **NPS**: Minimo 30 pontos
- **Retencao semana 2**: Minimo 40% retornam

---

## Principios Fundamentais

1. **Uma funcionalidade principal**: Foco em resolver UM problema muito bem
2. **Stack padrao para velocidade**: Tecnologias validadas reduzem riscos
3. **Validacao antes de construcao**: Analisar documentacao antes de codar
4. **Issues como contrato**: Tudo mapeado antes de desenvolver
5. **Prototipo funcional**: MVP funciona de verdade, nao e mockup
6. **Pagamento desde o inicio**: Valida disposicao real de pagar
7. **Aprender rapido e barato**: Feedback real > opinioes internas

---

## Documentos Principais

### Para Planejar
- [knowledge.MD](knowledge.MD) - Base teorica completa
- [process.MD](process.MD) - Processo operacional detalhado

### Para Executar
- [tasks.MD](tasks.MD) - Checklist de tarefas
- [template-briefing-mvp.md](_DATA/template-briefing-mvp.md)
- [template-funcionalidades.md](_DATA/template-funcionalidades.md)
- [template-issue-github.md](_DATA/template-issue-github.md)

### Para Lancar
- [checklist-go-live.md](_DATA/checklist-go-live.md)

### Para Validar
- [template-relatorio-validacao.md](_DATA/template-relatorio-validacao.md)

---

## Riscos Comuns e Mitigacoes

### Risco 1: Escopo crescer (scope creep)
**Mitigacao**: Documento "O que NAO entra no MVP" + revisao semanal

### Risco 2: Nao conseguir early adopters
**Mitigacao**: Identificar 20-50 testadores desde Etapa 1 + oferecer incentivos

### Risco 3: Bugs criticos em producao
**Mitigacao**: Testes exaustivos + Sentry + monitoramento ativo primeiras 48h

### Risco 4: Hipotese nao validada mas insistir
**Mitigacao**: Criterios claros de validacao + acordo pre-estabelecido com stakeholders

---

## FAQ

### Quanto tempo leva?
6-8 semanas desde analise ate lancamento, mais 2-4 semanas de validacao.

### Qual o custo?
$500-2.000/mes de infraestrutura + custo de time (se houver).

### Preciso de quantos desenvolvedores?
Minimo: 1 dev full-stack. Ideal: 1 frontend + 1 backend + 1 designer.

### O que acontece se a hipotese nao validar?
Use aprendizados para pivotar (mudar problema, solucao, publico ou modelo).

### Posso usar outras tecnologias que nao a stack padrao?
Pode, mas a estrategia foi otimizada para Next.js + Prisma + Stripe. Outras stacks podem aumentar timeline.

### E se meu MVP precisar de mais que 8 semanas?
Provavelmente o escopo esta grande demais. Revise o Briefing e corte features secundarias.

### Preciso sempre ter sistema de pagamento?
Sim. Validar disposicao real de pagamento e critico. Mesmo que seja $1, teste monetizacao desde o inicio.

---

## Proximos Passos Sugeridos

**Se voce acabou de encontrar esta estrategia**:
1. Leia [knowledge.MD](knowledge.MD) completo
2. Avalie se tem as entradas necessarias
3. Se sim, continue para [process.MD](process.MD)
4. Se nao, volte e prepare documentacao inicial

**Se voce ja leu tudo e esta pronto para comecar**:
1. Baixe [template-briefing-mvp.md](_DATA/template-briefing-mvp.md)
2. Preencha o Briefing do MVP
3. Valide com stakeholders
4. Inicie Etapa 1 seguindo [tasks.MD](tasks.MD)

**Se voce concluiu o MVP e esta validando**:
1. Continue monitoramento de metricas
2. Realize entrevistas com usuarios
3. Colete respostas de survey
4. Apos 2-4 semanas, use [template-relatorio-validacao.md](_DATA/template-relatorio-validacao.md)

---

## Suporte

**Duvidas sobre a estrategia?**
- Consulte [knowledge.MD](knowledge.MD) secao FAQ
- Revise [process.MD](process.MD) para detalhes operacionais

**Duvidas tecnicas (Next.js, Prisma, Stripe)?**
- Consulte documentacao oficial das tecnologias
- Stack escolhida tem ampla documentacao e comunidade

**Precisa de ajuda para definir sua hipotese?**
- Use processo [ProblemHypothesisDefinition](../../process/ProblemHypothesisDefinition/process.MD)
- Use template [Declaracao de Hipotese](../../process/_SHARED/templates/declaracao-hipotese.md)

---

## Integracao com Outros Processos

Esta estrategia pode usar:
- **Antes**: [ProblemHypothesisDefinition](../../process/ProblemHypothesisDefinition/process.MD) - Para definir hipotese
- **Antes**: [TargetUserIdentification](../../process/TargetUserIdentification/process.MD) - Para definir persona
- **Depois**: Estrategia de Growth (se validar e expandir)
- **Depois**: Processo de Roadmap (para planejar proximas features)

---

## Historico de Versoes

**v1.0** - 2025-11-05
- Versao inicial da estrategia MVP Builder
- Baseado em metodologia Lean Startup e best practices de MVP
- Stack padronizada: Next.js + Prisma + PostgreSQL + Stripe
- Templates completos incluidos

---

**Criado em**: 2025-11-05
**Mantido por**: Framework Business Team
**Versao**: 1.0
**Tipo**: Estrategia de Execucao

---

## Checklist Rapido: Estou Pronto para Comecar?

- [ ] Li [knowledge.MD](knowledge.MD) completo
- [ ] Tenho briefing de produto ou documentacao inicial
- [ ] Tenho hipotese de valor clara
- [ ] Tenho publico-alvo definido
- [ ] Tenho budget aprovado ($500-2k/mes)
- [ ] Tenho time alocado (1+ dev)
- [ ] Baixei templates da pasta _DATA/
- [ ] Criei repositorio Git
- [ ] Li [process.MD](process.MD)

Se todos os itens estao marcados, voce esta pronto! Comece pela Etapa 1 em [tasks.MD](tasks.MD).
