# Base de Conhecimento - Estrategia MVP Builder

## Visao geral

A estrategia MVP Builder e um processo estruturado para construir Minimum Viable Products (Produtos Minimos Viaveis) baseado em analise de hipoteses, definicao de funcionalidades prioritarias e execucao tecnica padronizada.

Esta estrategia guia desde a analise inicial de documentacao de produto ate a entrega de um MVP funcional com stack tecnica padrao, incluindo sistema de pagamentos e infraestrutura completa para validacao rapida no mercado.

**Contexto de aplicacao**: Startups, produtos digitais, validacao de hipoteses de negocio, lancamento de novas funcionalidades core.

**Principio central**: Entregar o minimo necessario para validar a hipotese principal com usuarios reais, evitando desperdicio de recursos em funcionalidades secundarias.

## Objetivo central

Construir um MVP funcional e escalavel que permita validar a principal hipotese de produto com usuarios reais, coletando feedback qualitativo e quantitativo para decisoes de pivotar, perseverar ou expandir.

**Meta principal**: MVP em producao validando hipotese core em ate 8 semanas.

## Principios fundamentais

1. **Uma funcionalidade principal, multiplas secundarias apenas se criticas** - O MVP deve resolver UM problema principal muito bem, nao varios problemas de forma mediocre

2. **Stack padrao para velocidade** - Usar tecnologias validadas (Next.js, Prisma, PostgreSQL, Stripe) para acelerar desenvolvimento e reduzir riscos tecnicos

3. **Validacao antes de construcao** - Analisar documentacao existente (briefing, pesquisas, hipoteses) antes de escrever codigo

4. **Issues como contrato de trabalho** - Toda funcionalidade deve estar mapeada em issues detalhadas antes do desenvolvimento

5. **Prototipo funcional, nao prototipo de aparencia** - O MVP deve funcionar de verdade, nao ser apenas um mockup clicavel

6. **Sistema de pagamento desde o inicio** - Validar disposicao real de pagamento e desde o dia 1

7. **Aprender rapido e barato** - Preferir feedback real de usuarios a opinioes internas

## Metricas de sucesso iniciais

- **Time to MVP**: Lancamento em ate 8 semanas desde kick-off
- **Taxa de conclusao de fluxo principal**: Minimo 60% dos usuarios completam a acao core
- **Taxa de conversao para pagamento**: Minimo 5% dos usuarios cadastrados realizam compra de teste
- **Tempo medio de resposta da aplicacao**: Maximo 2 segundos em todas as telas criticas
- **Net Promoter Score (NPS) inicial**: Benchmark de usuario early adopter acima de 30
- **Custo de validacao**: Maximo $5.000 em infraestrutura e ferramentas ate primeira validacao

## Quando aplicar

Use esta estrategia quando:

- Voce tem uma hipotese de produto clara que precisa validar com mercado real
- Existe documentacao inicial (briefing, pesquisas, personas, hipoteses) pronta para analise
- O objetivo e validacao rapida ao invés de construcao de produto completo
- Ha orcamento limitado e necessidade de validar antes de investir pesado
- A solucao pode ser construida como SaaS/aplicacao web
- Existe necessidade de testar monetizacao desde cedo

Sinais que indicam uso desta estrategia:

- Sua empresa precisa decidir se investe ou nao em uma ideia antes de gastar 6 meses de desenvolvimento
- Voce quer validar disposicao de pagamento real antes de construir features complexas
- Existe risco alto de construir algo que ninguem quer
- Time enxuto (1-3 desenvolvedores) precisa entregar rapido
- Produto digital que pode se beneficiar de iteracao rapida

## Como aplicar

### Visao macro das etapas

**Fase 1 - Analise e Compreensao (Semana 1)**
Analise profunda da documentacao existente, identificacao de hipotese principal, definicao de funcionalidade core e secundarias.

**Fase 2 - Estruturacao Tecnica (Semana 1-2)**
Mapeamento completo de issues, setup de stack tecnica padrao, configuracao de infraestrutura base.

**Fase 3 - Desenvolvimento Core (Semanas 3-5)**
Construcao da funcionalidade principal, integracao com sistema de pagamento, implementacao de autenticacao.

**Fase 4 - Desenvolvimento Secundario (Semanas 6-7)**
Construcao de funcionalidades secundarias criticas identificadas, refinamento de fluxos, ajustes de UX.

**Fase 5 - Validacao e Lancamento (Semana 8)**
Testes com usuarios reais, correcao de bugs criticos, deploy em producao, setup de metricas.

### Prerequisitos

- Briefing de produto documentado
- Hipotese de valor clara
- Definicao de publico-alvo (persona)
- Acesso a pasta com documentacao do projeto (Google Drive ou equivalente)
- Budget aprovado para infraestrutura ($500-$2.000/mes)
- Time minimo: 1 desenvolvedor full-stack ou 2 desenvolvedores (front + back)

## Etapas da estrategia

### Etapa 1 - Analise de Documentacao e Definicao de Escopo (4-5 dias)

**Objetivo**: Compreender profundamente o problema, publico e solucao proposta, identificando a funcionalidade core e funcionalidades secundarias criticas.

**Acoes necessarias**:

- Ler e analisar toda documentacao disponivel na pasta especificada (briefing, pesquisas, hipoteses, personas)
- Identificar e extrair a hipotese principal de valor
- Definir funcionalidade principal (aquela que valida a hipotese core)
- Listar funcionalidades secundarias e priorizar apenas as criticas
- Documentar stack tecnica padrao a ser usada
- Criar documento de escopo de MVP (o que entra, o que fica de fora)

**Criterios de aceite**:

- Documento de Briefing do MVP criado com hipotese principal clara
- Funcionalidade principal definida e documentada
- Lista de funcionalidades secundarias priorizadas (maximo 3)
- Stack tecnica validada e documentada
- Todos os stakeholders alinhados com o escopo

**Ferramentas sugeridas**:

- Template de Briefing de MVP ([ver _DATA/template-briefing-mvp.md](../_DATA/template-briefing-mvp.md))
- Template de Definicao de Funcionalidades ([ver _DATA/template-funcionalidades.md](../_DATA/template-funcionalidades.md))

### Etapa 2 - Mapeamento de Issues e Planejamento Tecnico (3-4 dias)

**Objetivo**: Transformar funcionalidades definidas em issues acionaveis e detalhadas, criando um roadmap tecnico claro.

**Acoes necessarias**:

- Criar repositorio Git do projeto
- Setup inicial do projeto Next.js com estrutura padrao
- Mapear todas as funcionalidades em issues no GitHub/GitLab
- Detalhar cada issue com: descricao, criterios de aceite, estimativa, dependencias
- Criar issues de setup: autenticacao (NextAuth), banco (Prisma + PostgreSQL), pagamento (Stripe)
- Priorizar issues em ordem de dependencia e valor
- Estimar tempo total de desenvolvimento

**Criterios de aceite**:

- Repositorio criado e estrutura Next.js inicializada
- Minimo 15 issues criadas e detalhadas
- Issues de setup tecnico mapeadas (auth, database, payment)
- Timeline estimada de desenvolvimento documentada
- Todas as issues tem criterios de aceite claros

**Ferramentas sugeridas**:

- Template de Issue ([ver _DATA/template-issue-github.md](../_DATA/template-issue-github.md))
- GitHub Projects ou equivalente para kanban
- Miro ou Excalidraw para diagramas de arquitetura

### Etapa 3 - Setup de Infraestrutura e Autenticacao (5-7 dias)

**Objetivo**: Preparar toda a base tecnica necessaria para desenvolvimento agil: banco de dados, autenticacao, estrutura de pastas, integracao com Stripe.

**Acoes necessarias**:

- Configurar Prisma com schema inicial de banco de dados
- Setup de PostgreSQL (local para dev, Supabase/Neon/Railway para prod)
- Implementar autenticacao completa com NextAuth (login, cadastro, recuperacao de senha)
- Configurar Stripe em modo teste
- Criar componentes base (layout, formularios, botoes)
- Setup de variaveis de ambiente (.env)
- Configurar deploy continuo (Vercel recomendado)

**Criterios de aceite**:

- Usuario consegue se cadastrar e fazer login
- Banco de dados criado e migrations funcionando
- Integracao Stripe configurada em modo teste
- Ambiente de desenvolvimento funcionando localmente
- Deploy automatico configurado
- Documentacao de setup para novos desenvolvedores criada

**Ferramentas sugeridas**:

- Vercel para deploy
- Supabase, Neon ou Railway para PostgreSQL
- NextAuth documentation
- Stripe documentation

### Etapa 4 - Desenvolvimento da Funcionalidade Principal (10-14 dias)

**Objetivo**: Construir, testar e validar a funcionalidade core que valida a hipotese principal do produto.

**Acoes necessarias**:

- Desenvolver frontend da funcionalidade principal
- Implementar API routes necessarias
- Criar schema de banco para funcionalidade core
- Implementar logica de negocio principal
- Conectar funcionalidade principal com sistema de pagamento
- Criar testes basicos de fluxo principal
- Validar com stakeholders internos

**Criterios de aceite**:

- Funcionalidade principal 100% funcional
- Usuario consegue completar fluxo principal end-to-end
- Integracao com pagamento funcionando (modo teste)
- Sem bugs criticos identificados
- Performance aceitavel (< 2s de resposta)

**Ferramentas sugeridas**:

- Playwright ou Cypress para testes E2E
- React Hook Form para formularios
- TailwindCSS para estilizacao rapida

### Etapa 5 - Desenvolvimento de Funcionalidades Secundarias (7-10 dias)

**Objetivo**: Implementar funcionalidades secundarias criticas que complementam a experiencia principal.

**Acoes necessarias**:

- Desenvolver funcionalidades secundarias priorizadas
- Implementar dashboard basico de usuario
- Criar paginas de configuracoes/perfil
- Implementar notificacoes basicas (email ou in-app)
- Refinar UX de fluxos secundarios
- Corrigir bugs nao-criticos identificados

**Criterios de aceite**:

- Todas as funcionalidades secundarias criticas implementadas
- Usuario consegue gerenciar conta e configuracoes basicas
- Sistema de notificacoes funcionando
- UX refinada e consistente
- Lista de bugs conhecidos documentada e priorizada

**Ferramentas sugeridas**:

- Resend ou SendGrid para emails transacionais
- shadcn/ui para componentes de UI
- Vercel Analytics para metricas basicas

### Etapa 6 - Testes, Ajustes e Pre-Lancamento (5-7 dias)

**Objetivo**: Validar qualidade, corrigir bugs criticos, preparar lancamento e setup de metricas de validacao.

**Acoes necessarias**:

- Realizar testes completos de todos os fluxos
- Corrigir bugs criticos identificados
- Setup de analytics (Google Analytics, Mixpanel ou Posthog)
- Configurar monitoramento de erros (Sentry)
- Criar documentacao basica para usuarios
- Preparar ambiente de producao
- Testar fluxo completo de pagamento em modo teste
- Migrar Stripe para modo producao (quando aprovado)

**Criterios de aceite**:

- Zero bugs criticos identificados
- Analytics e monitoramento funcionando
- Fluxo de pagamento validado
- Ambiente de producao estavel
- Documentacao de usuario criada
- Checklist de go-live completo

**Ferramentas sugeridas**:

- Sentry para error tracking
- Posthog ou Mixpanel para analytics
- Google Analytics 4
- Checklist de Go-Live ([ver _DATA/checklist-go-live.md](../_DATA/checklist-go-live.md))

### Etapa 7 - Lancamento e Coleta de Feedback (Continuo)

**Objetivo**: Colocar MVP em producao, coletar feedback real de usuarios e preparar decisao de pivotar/perseverar/expandir.

**Acoes necessarias**:

- Deploy final em producao
- Onboarding de primeiros usuarios (early adopters)
- Monitorar metricas definidas diariamente
- Coletar feedback qualitativo (entrevistas, surveys)
- Documentar bugs e melhorias solicitadas
- Realizar retrospectiva semanal do MVP
- Preparar relatorio de validacao apos 2-4 semanas

**Criterios de aceite**:

- MVP disponivel publicamente
- Minimo 20 usuarios reais usando o produto
- Metricas sendo coletadas corretamente
- Feedback qualitativo documentado
- Relatorio de validacao criado com recomendacoes

**Ferramentas sugeridas**:

- Typeform ou Google Forms para surveys
- Calendly para agendar entrevistas
- Notion ou Google Docs para documentacao de feedback
- Template de Relatorio de Validacao ([ver _DATA/template-relatorio-validacao.md](../_DATA/template-relatorio-validacao.md))

## Fluxo da estrategia

```
[Documentacao inicial]
        ↓
[Analise de Documentacao] → Define hipotese principal e funcionalidade core
        ↓
[Mapeamento de Issues] → Transforma em tarefas acionaveis
        ↓
[Setup de Infraestrutura] → Prepara base tecnica (auth, db, payment)
        ↓
[Desenvolvimento Core] → Constroi funcionalidade principal
        ↓
[Desenvolvimento Secundario] → Adiciona features criticas de suporte
        ↓
[Testes e Ajustes] → Valida qualidade e corrige bugs
        ↓
[Lancamento] → Deploy e onboarding de usuarios
        ↓
[Coleta de Feedback] → Mede, aprende, decide proximo passo
        ↓
[DECISAO: Pivotar | Perseverar | Expandir]
```

**Pontos de decisao criticos**:

- **Apos Etapa 1**: O escopo definido e realmente um MVP ou esta grande demais?
- **Apos Etapa 4**: A funcionalidade core esta realmente validando a hipotese principal?
- **Apos Etapa 7 (2-4 semanas)**: Os usuarios estao usando e dispostos a pagar? Pivotar, perseverar ou expandir?

## Lista de tarefas para executar a estrategia

- [ ] Ler documentacao do projeto na pasta especificada
- [ ] Criar Briefing do MVP com hipotese principal
- [ ] Definir funcionalidade principal e secundarias
- [ ] Documentar stack tecnica padrao
- [ ] Criar repositorio e estrutura Next.js
- [ ] Mapear todas as funcionalidades em issues
- [ ] Setup de autenticacao com NextAuth
- [ ] Configurar Prisma + PostgreSQL
- [ ] Integrar Stripe em modo teste
- [ ] Desenvolver funcionalidade principal
- [ ] Desenvolver funcionalidades secundarias criticas
- [ ] Setup de analytics e error tracking
- [ ] Realizar testes completos de qualidade
- [ ] Deploy em producao
- [ ] Onboarding de primeiros usuarios
- [ ] Coletar feedback e metricas
- [ ] Criar relatorio de validacao

## Templates uteis

### 1. Briefing de MVP
Documento estruturado contendo:
- Hipotese principal
- Publico-alvo (persona resumida)
- Problema que resolve
- Solucao proposta (funcionalidade core)
- Metricas de validacao
- O que NAO entra no MVP (scope negativo)

**Localizacao**: [template-briefing-mvp.md](_DATA/template-briefing-mvp.md)

### 2. Template de Funcionalidades
Lista estruturada de funcionalidades com:
- Funcionalidade principal (descrição detalhada)
- Funcionalidades secundarias (priorizadas)
- Justificativa de cada feature
- Criterios de aceite por funcionalidade

**Localizacao**: [template-funcionalidades.md](_DATA/template-funcionalidades.md)

### 3. Template de Issue GitHub
Formato padrao para issues tecnicas:
- Titulo claro e objetivo
- Descricao detalhada
- Criterios de aceite (checklist)
- Estimativa de tempo
- Labels e prioridade
- Dependencias

**Localizacao**: [template-issue-github.md](_DATA/template-issue-github.md)

### 4. Checklist de Go-Live
Lista completa de validacoes antes do lancamento:
- Validacoes tecnicas
- Validacoes de negocio
- Validacoes de legal/compliance
- Setup de monitoramento

**Localizacao**: [checklist-go-live.md](_DATA/checklist-go-live.md)

### 5. Template de Relatorio de Validacao
Estrutura para documentar resultados apos lancamento:
- Metricas coletadas vs. esperadas
- Feedback qualitativo (quotes de usuarios)
- Bugs e melhorias identificadas
- Recomendacao: Pivotar, Perseverar ou Expandir
- Proximos passos

**Localizacao**: [template-relatorio-validacao.md](_DATA/template-relatorio-validacao.md)

## Riscos comuns e como evitar

### Risco 1: Escopo crescer durante desenvolvimento (scope creep)
**Probabilidade**: Alta
**Impacto**: Alto
**Mitigacao**: Criar documento claro de "O que NAO entra no MVP" e revisar semanalmente. Toda nova feature proposta deve ser justificada contra a hipotese principal.

### Risco 2: Funcionalidade principal mal definida
**Probabilidade**: Media
**Impacto**: Critico
**Mitigacao**: Usar a pergunta "Se tivessemos apenas 1 funcionalidade, qual validaria nossa hipotese?" e validar com stakeholders antes de comecar desenvolvimento.

### Risco 3: Problemas tecnicos com stack padrao
**Probabilidade**: Baixa
**Impacto**: Alto
**Mitigacao**: Stack escolhida (Next.js + Prisma + PostgreSQL) e amplamente documentada. Seguir documentacao oficial e usar templates validados.

### Risco 4: Nao conseguir usuarios para testar
**Probabilidade**: Media
**Impacto**: Alto
**Mitigacao**: Identificar e contatar early adopters desde a Etapa 1. Ter lista de 20-50 potenciais testadores antes do lancamento.

### Risco 5: Integracao com Stripe complexa
**Probabilidade**: Media
**Impacto**: Medio
**Mitigacao**: Comecar integracao na Etapa 3 em modo teste. Usar Stripe Checkout (solucao hosted) ao inves de custom flow no primeiro MVP.

### Risco 6: Performance ruim em producao
**Probabilidade**: Baixa
**Impacto**: Medio
**Mitigacao**: Testar com dados reais desde cedo. Usar Vercel Edge Functions e caching. Monitorar performance desde primeiro deploy.

### Risco 7: MVP virar produto completo sem validacao
**Probabilidade**: Alta
**Impacto**: Alto
**Mitigacao**: Definir tempo maximo de desenvolvimento (8 semanas hard stop). Forcar lancamento mesmo com features incompletas se funcionalidade core estiver pronta.

## Proximos passos sugeridos

Apos ler esta base de conhecimento:

**A) Se voce ja tem documentacao pronta**:
1. Va para [process.MD](process.MD) e leia o fluxo detalhado
2. Baixe os templates da pasta [_DATA](_DATA/)
3. Inicie pela Etapa 1: Analise de Documentacao

**B) Se voce ainda nao tem documentacao**:
1. Crie primeiro o briefing inicial de produto
2. Defina claramente sua hipotese de valor
3. Documente sua persona (publico-alvo)
4. Depois volte e siga opcao A

**C) Se voce precisa de ajuda para definir MVP**:
1. Consulte o processo [ProblemHypothesisDefinition](../../process/ZeroUm/01-ProblemHypothesisDefinition/process.MD)
2. Use o template [Declaracao de Hipotese](../../process/_SHARED/templates/declaracao-hipotese.md)
3. Depois volte para esta estrategia

**D) Se voce quer entender melhor o time necessario**:
1. Leia a secao "Requisitos" em [process.MD](process.MD)
2. Avalie se tem as competencias internas ou precisa contratar
3. Ajuste timeline de acordo com disponibilidade do time

## Referencias internas

- [process.MD](process.MD) - Processo operacional detalhado
- [tasks.MD](tasks.MD) - Checklist completo de tarefas
- [Pasta _DATA](_DATA/) - Templates e artefatos

## Referencias externas

- [PM3: O que e MVP](https://pm3.com.br/glossario/mvp-minimo-produto-viavel/)
- [The Lean Startup - Eric Ries](https://theleanstartup.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Prisma Documentation](https://www.prisma.io/docs)
- [Stripe Documentation](https://stripe.com/docs)
- [NextAuth.js Documentation](https://next-auth.js.org/)

---

**Ultima atualizacao**: 2025-11-05
**Versao**: 1.0
**Mantido por**: Framework Business Team
