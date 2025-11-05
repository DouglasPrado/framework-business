# Processo MVP Builder

## Objetivo do processo

Executar a construcao de um Minimum Viable Product (MVP) de forma estruturada, desde analise de documentacao ate lancamento em producao, utilizando stack tecnica padronizada (Next.js, Prisma, PostgreSQL, NextAuth, Stripe) e gerando lista completa de issues para desenvolvimento.

**Entrega final**: MVP funcional em producao, com sistema de pagamento integrado, metricas configuradas e primeiros usuarios validando a hipotese principal.

## Entradas essenciais

- **Documentacao de produto**: Briefing, pesquisas de mercado, definicao de problema
- **Hipotese de valor**: Declaracao clara da hipotese principal a ser validada
- **Definicao de publico-alvo**: Persona ou descricao de usuario-alvo
- **Acesso a pasta de documentacao**: Google Drive, Notion ou repositorio com materiais
- **Budget aprovado**: Minimo $500/mes para infraestrutura (hosting, banco, ferramentas)
- **Conta Stripe**: Conta criada e verificada (pode ser iniciada em modo teste)
- **Repositorio Git**: GitHub, GitLab ou Bitbucket configurado

## Ferramentas e artefatos de apoio

### Ferramentas de desenvolvimento
- **Next.js** (latest): Framework React para frontend e API
- **Prisma**: ORM para banco de dados
- **PostgreSQL**: Banco de dados relacional
- **NextAuth.js**: Autenticacao
- **Stripe**: Sistema de pagamentos
- **TypeScript**: Linguagem (recomendado)
- **TailwindCSS**: Estilizacao
- **Vercel**: Deploy e hosting

### Ferramentas de gestao
- **GitHub Projects** ou **Linear**: Gerenciamento de issues
- **Figma** ou **Excalidraw**: Diagramas e wireframes
- **Google Analytics** ou **Posthog**: Analytics
- **Sentry**: Monitoramento de erros
- **Notion** ou **Google Docs**: Documentacao

### Templates necessarios
- [Template de Briefing de MVP](_DATA/template-briefing-mvp.md)
- [Template de Funcionalidades](_DATA/template-funcionalidades.md)
- [Template de Issue GitHub](_DATA/template-issue-github.md)
- [Checklist de Go-Live](_DATA/checklist-go-live.md)
- [Template de Relatorio de Validacao](_DATA/template-relatorio-validacao.md)

## Requisitos

### Competencias tecnicas necessarias
- Desenvolvimento full-stack com JavaScript/TypeScript
- Experiencia com React e Next.js
- Conhecimento de SQL e ORMs
- Experiencia com APIs REST
- Git e versionamento de codigo

### Time minimo
- **Cenario ideal**: 1 desenvolvedor full-stack senior + 1 designer (part-time)
- **Cenario viavel**: 1 desenvolvedor full-stack com nocoes de design
- **Cenario escalavel**: 1 desenvolvedor frontend + 1 desenvolvedor backend + 1 designer

### Prerequisitos operacionais
- Disponibilidade de 30-40 horas/semana para desenvolvimento
- Acesso a stakeholders para validacao (maximo 48h de resposta)
- Ambiente de desenvolvimento configurado (Node.js, Git, editor)

### Conhecimentos desejáveis
- Design Sprint ou Lean Startup (conceitos)
- UX/UI basico
- Testes automatizados (Jest, Playwright)
- DevOps basico (CI/CD, deploy)

## Fluxo detalhado por etapa

### Etapa 1 - Analise de Documentacao e Definicao de Escopo (4-5 dias)

#### Atividade 1.1: Leitura e analise de documentacao existente

**Descricao**: Acessar pasta especificada (Google Drive ou equivalente) e ler todos os documentos disponíveis sobre o projeto: briefing, pesquisas de mercado, entrevistas com usuarios, personas, hipoteses ja validadas, analises de competidores.

**Execucao**:
1. Listar todos os documentos disponiveis na pasta
2. Criar estrutura de anotacoes para consolidar informacoes
3. Ler cada documento identificando:
   - Problema principal mencionado
   - Solucao proposta
   - Publico-alvo descrito
   - Hipoteses explicitas ou implicitas
   - Funcionalidades mencionadas
4. Destacar contradicoes ou gaps de informacao
5. Preparar perguntas para stakeholders

**Criterio de aceite**:
- Todos os documentos listados e lidos
- Anotacoes consolidadas criadas
- Lista de perguntas/duvidas documentada

**Resultado esperado**: Documento de sintese com principais insights, problemas identificados, publico-alvo, e hipoteses encontradas na documentacao.

**Tempo estimado**: 1-2 dias

---

#### Atividade 1.2: Identificacao e documentacao da hipotese principal

**Descricao**: Extrair ou formular a hipotese principal de valor que o MVP deve validar, usando formato estruturado "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]".

**Execucao**:
1. Revisar anotacoes da atividade anterior
2. Identificar a hipotese mais critica a validar
3. Reformular no formato padrao se necessario
4. Validar com stakeholders se a hipotese esta correta
5. Documentar hipoteses secundarias para contexto

**Criterio de aceite**:
- Hipotese principal documentada no formato padrao
- Validacao com stakeholders obtida
- Hipotese e mensuravel (pode ser validada com metricas)

**Resultado esperado**: Hipotese principal clara, validada e documentada que guiara todo o desenvolvimento do MVP.

**Tempo estimado**: 0.5 dia

---

#### Atividade 1.3: Definicao de funcionalidade principal e secundarias

**Descricao**: Identificar qual e a funcionalidade core que valida a hipotese principal e quais funcionalidades secundarias sao absolutamente criticas para o MVP funcionar.

**Execucao**:
1. Fazer a pergunta: "Se tivessemos apenas 1 funcionalidade, qual validaria nossa hipotese?"
2. Descrever detalhadamente a funcionalidade principal
3. Listar todas as funcionalidades secundarias mencionadas na documentacao
4. Priorizar funcionalidades secundarias usando criterio: "O MVP funciona sem isso?"
5. Selecionar no maximo 3 funcionalidades secundarias criticas
6. Documentar o que NAO entra no MVP (scope negativo)
7. Validar com stakeholders

**Criterio de aceite**:
- Funcionalidade principal definida e descrita em detalhes
- Lista de funcionalidades secundarias priorizadas (max 3)
- Documento "O que NAO entra no MVP" criado
- Validacao com stakeholders concluida

**Resultado esperado**: Documento de Funcionalidades preenchido com funcionalidade principal, secundarias criticas, e scope negativo claro.

**Tempo estimado**: 1 dia

---

#### Atividade 1.4: Criacao do Briefing do MVP

**Descricao**: Consolidar toda analise em documento estruturado de Briefing do MVP que sera a referencia principal para todo o desenvolvimento.

**Execucao**:
1. Usar [Template de Briefing MVP](_DATA/template-briefing-mvp.md)
2. Preencher todas as secoes:
   - Hipotese principal
   - Publico-alvo (resumo da persona)
   - Problema que resolve
   - Solucao proposta (funcionalidade core)
   - Funcionalidades secundarias
   - Metricas de validacao
   - O que NAO entra no MVP
   - Stack tecnica
   - Timeline estimada
3. Revisar com stakeholders
4. Obter aprovacao formal para prosseguir

**Criterio de aceite**:
- Briefing completo preenchido
- Aprovacao formal de stakeholders obtida
- Documento compartilhado e acessivel ao time

**Resultado esperado**: Briefing do MVP aprovado servindo como contrato de escopo entre time tecnico e stakeholders.

**Tempo estimado**: 1 dia

---

#### Atividade 1.5: Documentacao da stack tecnica padrao

**Descricao**: Documentar stack tecnica a ser usada, versoes, e justificativas, garantindo alinhamento do time.

**Execucao**:
1. Confirmar stack padrao:
   - Next.js (latest stable)
   - TypeScript
   - Prisma ORM
   - PostgreSQL
   - NextAuth.js
   - Stripe
   - TailwindCSS
   - Vercel (deploy)
2. Documentar alternativas para cada componente (se aplicavel)
3. Listar bibliotecas complementares necessarias
4. Criar documento de decisoes arquiteturais

**Criterio de aceite**:
- Stack completa documentada
- Versoes especificadas
- Time tecnico alinhado

**Resultado esperado**: Documento de Stack Tecnica servindo como referencia para todo desenvolvimento.

**Tempo estimado**: 0.5 dia

---

### Etapa 2 - Mapeamento de Issues e Planejamento Tecnico (3-4 dias)

#### Atividade 2.1: Criacao do repositorio e estrutura inicial

**Descricao**: Criar repositorio Git, inicializar projeto Next.js com TypeScript e estrutura de pastas padrao.

**Execucao**:
1. Criar repositorio no GitHub/GitLab
2. Inicializar projeto Next.js: `npx create-next-app@latest`
3. Configurar TypeScript
4. Criar estrutura de pastas:
   - `/src/app` - App Router do Next.js
   - `/src/components` - Componentes reutilizaveis
   - `/src/lib` - Utilities e helpers
   - `/prisma` - Schema e migrations
   - `/public` - Assets estaticos
5. Configurar ESLint e Prettier
6. Criar README.md com instrucoes de setup
7. Commit inicial e push

**Criterio de aceite**:
- Repositorio criado e acessivel ao time
- Projeto Next.js rodando localmente
- Estrutura de pastas padrao criada
- README com instrucoes de setup

**Resultado esperado**: Repositorio configurado e time capaz de rodar projeto localmente.

**Tempo estimado**: 0.5 dia

---

#### Atividade 2.2: Mapeamento de funcionalidades em issues

**Descricao**: Criar issues detalhadas para cada funcionalidade identificada, seguindo template padrao.

**Execucao**:
1. Para funcionalidade principal, criar 3-5 issues tecnicas:
   - Frontend da funcionalidade
   - API/Backend da funcionalidade
   - Integracao com banco de dados
   - Testes
   - Refinamentos de UX
2. Para cada funcionalidade secundaria, criar 2-3 issues
3. Usar [Template de Issue](_DATA/template-issue-github.md) para cada uma
4. Cada issue deve conter:
   - Titulo claro
   - Descricao detalhada
   - Criterios de aceite (checklist)
   - Estimativa de tempo
   - Labels (frontend, backend, feature, bug, etc)
   - Prioridade (P0, P1, P2)
5. Linkar issues relacionadas (dependencias)

**Criterio de aceite**:
- Minimo 10 issues de features criadas
- Todas as issues seguem template padrao
- Criterios de aceite claros em cada issue
- Dependencias mapeadas

**Resultado esperado**: Backlog estruturado de issues representando todas as funcionalidades do MVP.

**Tempo estimado**: 1.5 dias

---

#### Atividade 2.3: Criacao de issues de setup tecnico

**Descricao**: Criar issues para tarefas de infraestrutura e setup: autenticacao, banco de dados, pagamento, deploy.

**Execucao**:
1. Criar issue: Setup Prisma + PostgreSQL
2. Criar issue: Implementar NextAuth (login, cadastro, recuperacao)
3. Criar issue: Integrar Stripe em modo teste
4. Criar issue: Configurar variaveis de ambiente
5. Criar issue: Setup deploy continuo na Vercel
6. Criar issue: Configurar componentes base (layout, form, button)
7. Criar issue: Setup de testes (opcional para MVP)
8. Marcar todas como P0 (prioridade critica)

**Criterio de aceite**:
- Todas as issues de setup criadas
- Issues marcadas com label "setup" e P0
- Ordem de execucao definida

**Resultado esperado**: Issues de infraestrutura priorizadas e prontas para desenvolvimento.

**Tempo estimado**: 0.5 dia

---

#### Atividade 2.4: Priorizacao e estimativa de issues

**Descricao**: Ordenar todas as issues por prioridade e dependencia, estimar tempo de cada uma.

**Execucao**:
1. Revisar todas as issues criadas
2. Classificar em:
   - P0 (Bloqueante/Setup): deve ser feito primeiro
   - P1 (Core): funcionalidade principal
   - P2 (Secundario): funcionalidades secundarias
   - P3 (Nice to have): pode ser cortado
3. Estimar cada issue em horas ou pontos
4. Calcular tempo total estimado
5. Criar milestones:
   - Milestone 1: Setup completo
   - Milestone 2: Funcionalidade core
   - Milestone 3: Features secundarias
   - Milestone 4: Launch
6. Atribuir issues aos milestones

**Criterio de aceite**:
- Todas as issues priorizadas e estimadas
- Milestones criados e issues atribuidas
- Timeline realista documentada

**Resultado esperado**: Roadmap tecnico com timeline estimada de 6-8 semanas.

**Tempo estimado**: 1 dia

---

#### Atividade 2.5: Setup de projeto management

**Descricao**: Configurar ferramenta de gestao de issues (GitHub Projects, Linear, ou equivalente) com board kanban.

**Execucao**:
1. Criar projeto/board no GitHub Projects
2. Configurar colunas: Backlog | To Do | In Progress | Review | Done
3. Adicionar todas as issues ao board
4. Configurar automacoes basicas (ex: issue fechada → move para Done)
5. Criar view por milestone
6. Definir rituais de atualizacao (diario ou 2x semana)

**Criterio de aceite**:
- Board kanban configurado
- Todas as issues visiveis no board
- Time tem acesso e sabe usar

**Resultado esperado**: Ferramenta de gestao configurada e time alinhado em como usar.

**Tempo estimado**: 0.5 dia

---

### Etapa 3 - Setup de Infraestrutura e Autenticacao (5-7 dias)

#### Atividade 3.1: Configuracao do Prisma e PostgreSQL

**Descricao**: Instalar Prisma, conectar com banco PostgreSQL e criar schema inicial.

**Execucao**:
1. Instalar Prisma: `npm install prisma @prisma/client`
2. Inicializar Prisma: `npx prisma init`
3. Criar banco PostgreSQL:
   - Opcao 1: Local com Docker
   - Opcao 2: Supabase (free tier)
   - Opcao 3: Neon (free tier)
   - Opcao 4: Railway
4. Configurar DATABASE_URL no .env
5. Criar schema inicial com modelo User
6. Rodar primeira migration: `npx prisma migrate dev`
7. Testar conexao com Prisma Studio: `npx prisma studio`

**Criterio de aceite**:
- Prisma instalado e configurado
- Banco PostgreSQL criado e conectado
- Schema inicial criado
- Migration aplicada com sucesso
- Prisma Studio funcionando

**Resultado esperado**: Banco de dados funcional e ORM configurado para uso.

**Tempo estimado**: 1 dia

---

#### Atividade 3.2: Implementacao de autenticacao com NextAuth

**Descricao**: Configurar NextAuth.js com login via email/senha, Google OAuth (opcional) e fluxos de cadastro e recuperacao.

**Execucao**:
1. Instalar NextAuth: `npm install next-auth`
2. Criar `/app/api/auth/[...nextauth]/route.ts`
3. Configurar providers:
   - Credentials (email/senha)
   - Google OAuth (opcional)
4. Criar adapter do Prisma para NextAuth
5. Atualizar schema do Prisma com modelos NextAuth (Account, Session, VerificationToken)
6. Criar paginas:
   - `/app/auth/signin` - Login
   - `/app/auth/signup` - Cadastro
   - `/app/auth/reset-password` - Recuperacao de senha
7. Implementar protecao de rotas (middleware)
8. Criar hook `useSession` para components
9. Testar fluxo completo

**Criterio de aceite**:
- Usuario consegue se cadastrar
- Usuario consegue fazer login
- Sessao persiste entre reloads
- Rotas protegidas funcionando
- Logout funciona corretamente

**Resultado esperado**: Sistema de autenticacao completo e funcional.

**Tempo estimado**: 2-3 dias

---

#### Atividade 3.3: Integracao com Stripe (modo teste)

**Descricao**: Configurar Stripe SDK, criar produtos de teste e implementar fluxo basico de checkout.

**Execucao**:
1. Criar conta Stripe (se nao existir)
2. Obter chaves API (modo teste)
3. Instalar Stripe SDK: `npm install stripe @stripe/stripe-js`
4. Configurar Stripe no backend (`/lib/stripe.ts`)
5. Criar produtos de teste no dashboard Stripe
6. Implementar API route para criar checkout session:
   - `/app/api/checkout/route.ts`
7. Criar pagina de pricing com botoes de compra
8. Implementar Stripe Checkout (hosted)
9. Criar webhooks para eventos Stripe:
   - `/app/api/webhooks/stripe/route.ts`
10. Testar com cartoes de teste do Stripe

**Criterio de aceite**:
- Stripe configurado em modo teste
- Usuario consegue iniciar checkout
- Pagamento de teste funciona
- Webhook recebe eventos
- Status de pagamento atualiza no banco

**Resultado esperado**: Sistema de pagamento funcional em modo teste.

**Tempo estimado**: 2 dias

---

#### Atividade 3.4: Criacao de componentes base

**Descricao**: Criar componentes reutilizaveis que serao usados em todo MVP (layout, forms, buttons, cards).

**Execucao**:
1. Instalar shadcn/ui (opcional mas recomendado):
   - `npx shadcn-ui@latest init`
2. Criar componentes base:
   - `Layout.tsx` - Layout principal com header/footer
   - `Button.tsx` - Botao reutilizavel
   - `Input.tsx` - Input de formulario
   - `Card.tsx` - Container de conteudo
   - `Modal.tsx` - Modal/dialog
   - `Loading.tsx` - Estado de loading
3. Configurar TailwindCSS com tema customizado
4. Criar guia de estilo basico (cores, tipografia, espacamentos)
5. Documentar uso de cada componente

**Criterio de aceite**:
- Componentes base criados e funcionais
- TailwindCSS configurado
- Componentes documentados com exemplos
- Design consistente aplicado

**Resultado esperado**: Biblioteca de componentes base pronta para uso no desenvolvimento de features.

**Tempo estimado**: 1-2 dias

---

#### Atividade 3.5: Configuracao de deploy continuo

**Descricao**: Configurar deploy automatico na Vercel conectado ao repositorio Git.

**Execucao**:
1. Criar conta Vercel (se nao existir)
2. Conectar repositorio GitHub/GitLab ao Vercel
3. Configurar variaveis de ambiente no Vercel:
   - DATABASE_URL
   - NEXTAUTH_SECRET
   - NEXTAUTH_URL
   - STRIPE_SECRET_KEY
   - Outras necessarias
4. Configurar build settings (Next.js detectado automaticamente)
5. Deploy inicial
6. Configurar dominios:
   - Preview: automatico para cada PR
   - Production: branch main
7. Testar deploy funcionando
8. Configurar webhook para notificacoes de deploy (opcional)

**Criterio de aceite**:
- Deploy automatico funcionando
- Variaveis de ambiente configuradas
- Aplicacao acessivel via URL
- Preview deploys funcionando para PRs

**Resultado esperado**: Pipeline de CI/CD funcional com deploys automaticos.

**Tempo estimado**: 0.5 dia

---

### Etapa 4 - Desenvolvimento da Funcionalidade Principal (10-14 dias)

#### Atividade 4.1: Desenvolvimento do frontend da funcionalidade core

**Descricao**: Construir interface de usuario completa para funcionalidade principal, incluindo forms, visualizacoes e interacoes.

**Execucao**:
1. Criar estrutura de rotas para funcionalidade core
2. Desenvolver componentes especificos da feature
3. Implementar formularios com validacao (React Hook Form)
4. Criar estados de loading e erro
5. Implementar feedback visual para acoes do usuario
6. Garantir responsividade mobile
7. Aplicar design consistente com componentes base
8. Adicionar acessibilidade basica (ARIA labels)

**Criterio de aceite**:
- Todas as telas da funcionalidade core criadas
- Formularios com validacao funcionando
- Interface responsiva (desktop e mobile)
- Estados de loading e erro implementados
- Design consistente aplicado

**Resultado esperado**: Interface completa da funcionalidade principal pronta para integrar com backend.

**Tempo estimado**: 4-5 dias

---

#### Atividade 4.2: Desenvolvimento do backend da funcionalidade core

**Descricao**: Implementar API routes, logica de negocio e integracao com banco de dados para funcionalidade principal.

**Execucao**:
1. Atualizar schema do Prisma com modelos necessarios
2. Criar migrations
3. Implementar API routes necessarias:
   - GET para leitura
   - POST para criacao
   - PUT/PATCH para atualizacao
   - DELETE (se aplicavel)
4. Implementar logica de negocio
5. Adicionar validacao de dados no backend
6. Implementar autorizacao (usuarios so acessam seus proprios dados)
7. Adicionar error handling
8. Testar endpoints com Postman/Insomnia

**Criterio de aceite**:
- Todos os endpoints da funcionalidade criados
- Dados salvos e recuperados do banco corretamente
- Validacao de dados funcionando
- Autorizacao implementada
- Error handling adequado

**Resultado esperado**: API completa da funcionalidade principal funcionando e testada.

**Tempo estimado**: 4-5 dias

---

#### Atividade 4.3: Integracao frontend + backend + pagamento

**Descricao**: Conectar frontend com backend, integrar fluxo de pagamento na funcionalidade core se necessario.

**Execucao**:
1. Integrar chamadas de API no frontend
2. Implementar estados de loading durante requests
3. Adicionar tratamento de erros (toast, alerts)
4. Se funcionalidade core envolve pagamento:
   - Integrar Stripe Checkout no fluxo
   - Garantir que acesso so e liberado apos pagamento
5. Testar fluxo completo end-to-end
6. Validar que dados aparecem corretamente apos criacao/edicao
7. Testar cenarios de erro (falha de rede, erro de validacao, etc)

**Criterio de aceite**:
- Frontend e backend integrados
- Usuario consegue completar fluxo principal sem erros
- Pagamento integrado (se aplicavel)
- Tratamento de erros funcionando
- Fluxo end-to-end testado

**Resultado esperado**: Funcionalidade principal 100% funcional e integrada.

**Tempo estimado**: 2-3 dias

---

#### Atividade 4.4: Testes e refinamento da funcionalidade core

**Descricao**: Testar exaustivamente funcionalidade principal, corrigir bugs, refinar UX.

**Execucao**:
1. Criar checklist de casos de teste:
   - Happy path (tudo funciona)
   - Casos de erro (validacao, falhas)
   - Edge cases (valores extremos, dados vazios)
2. Testar em diferentes navegadores (Chrome, Safari, Firefox)
3. Testar em mobile (iOS e Android)
4. Identificar e documentar bugs
5. Corrigir bugs criticos (P0)
6. Refinar UX com base em testes internos:
   - Melhorar mensagens de erro
   - Adicionar hints/tooltips
   - Ajustar fluxos confusos
7. Validar performance (tempo de resposta < 2s)
8. Fazer smoke test completo

**Criterio de aceite**:
- Todos os casos de teste executados
- Bugs criticos corrigidos
- Funciona em Chrome, Safari, Firefox
- Responsivo em mobile
- Performance aceitavel

**Resultado esperado**: Funcionalidade core estavel, testada e refinada.

**Tempo estimado**: 2-3 dias

---

### Etapa 5 - Desenvolvimento de Funcionalidades Secundarias (7-10 dias)

#### Atividade 5.1: Implementacao de funcionalidades secundarias priorizadas

**Descricao**: Desenvolver funcionalidades secundarias criticas identificadas no Briefing (maximo 3).

**Execucao**:
1. Para cada funcionalidade secundaria:
   - Revisar issues criadas
   - Desenvolver frontend
   - Desenvolver backend
   - Integrar
   - Testar
2. Seguir mesmo processo da funcionalidade core (mas mais rapido)
3. Reutilizar componentes base criados
4. Manter consistencia de design e UX
5. Priorizar velocidade sobre perfeicao

**Criterio de aceite**:
- Todas as funcionalidades secundarias priorizadas implementadas
- Funcionalidades integradas com funcionalidade core
- Testes basicos realizados
- Sem bugs criticos

**Resultado esperado**: Funcionalidades secundarias funcionais complementando a experiencia core.

**Tempo estimado**: 5-7 dias (depende da complexidade)

---

#### Atividade 5.2: Implementacao de dashboard e perfil de usuario

**Descricao**: Criar area logada basica com dashboard, configuracoes de perfil e gerenciamento de conta.

**Execucao**:
1. Criar layout de dashboard (sidebar ou top nav)
2. Implementar pagina de perfil:
   - Visualizar dados do usuario
   - Editar nome, email
   - Alterar senha
   - Deletar conta (opcional)
3. Criar dashboard home com:
   - Overview de uso da funcionalidade core
   - Acoes rapidas
   - Status de assinatura/pagamento
4. Adicionar navegacao entre areas
5. Implementar breadcrumbs (opcional)

**Criterio de aceite**:
- Usuario consegue acessar dashboard
- Perfil editavel funcionando
- Dashboard home com informacoes relevantes
- Navegacao clara entre secoes

**Resultado esperado**: Area logada completa com dashboard e gestao de perfil.

**Tempo estimado**: 2-3 dias

---

#### Atividade 5.3: Sistema de notificacoes basico

**Descricao**: Implementar envio de emails transacionais e/ou notificacoes in-app basicas.

**Execucao**:
1. Escolher servico de email:
   - Resend (recomendado)
   - SendGrid
   - Postmark
2. Configurar servico escolhido
3. Criar templates de email:
   - Email de boas-vindas
   - Confirmacao de cadastro (se necessario)
   - Recuperacao de senha
   - Confirmacao de pagamento
   - Notificacoes da funcionalidade core (se aplicavel)
4. Implementar funcoes de envio de email
5. Testar envios
6. (Opcional) Criar notificacoes in-app basicas

**Criterio de aceite**:
- Servico de email configurado
- Templates criados e funcionando
- Emails sendo enviados corretamente
- Emails tem design basico e sao responsivos

**Resultado esperado**: Sistema de notificacoes funcionando para eventos criticos.

**Tempo estimado**: 1-2 dias

---

#### Atividade 5.4: Refinamento geral de UX

**Descricao**: Revisar toda experiencia do usuario, ajustar fluxos confusos, melhorar mensagens, adicionar microcopy.

**Execucao**:
1. Fazer walkthrough completo como usuario novo
2. Identificar pontos de friccao:
   - Formularios confusos
   - Mensagens de erro pouco claras
   - Falta de feedback visual
   - Fluxos longos demais
3. Fazer ajustes de UX:
   - Melhorar labels e placeholders
   - Adicionar tooltips onde necessario
   - Simplificar formularios
   - Adicionar empty states
   - Melhorar mensagens de sucesso/erro
4. Garantir consistencia visual em todas as telas
5. Testar novamente fluxo completo

**Criterio de aceite**:
- Walkthrough completo realizado
- Pontos de friccao identificados e corrigidos
- Mensagens claras e amigaveis
- Empty states implementados
- Experiencia consistente

**Resultado esperado**: UX refinada e experiencia coesa em todo MVP.

**Tempo estimado**: 2 dias

---

### Etapa 6 - Testes, Ajustes e Pre-Lancamento (5-7 dias)

#### Atividade 6.1: Testes completos de qualidade

**Descricao**: Realizar bateria completa de testes em todos os fluxos, navegadores, dispositivos.

**Execucao**:
1. Criar documento de casos de teste cobrindo:
   - Cadastro e login
   - Fluxo completo da funcionalidade core
   - Fluxo de pagamento
   - Funcionalidades secundarias
   - Perfil e configuracoes
   - Recuperacao de senha
   - Cenarios de erro
2. Testar em:
   - Chrome (desktop)
   - Safari (desktop e iOS)
   - Firefox (desktop)
   - Chrome mobile (Android)
3. Testar diferentes tamanhos de tela
4. Validar acessibilidade basica (navegacao por teclado, screen reader)
5. Documentar todos os bugs encontrados em issues
6. Categorizar bugs por severidade (Critico, Alto, Medio, Baixo)

**Criterio de aceite**:
- Todos os casos de teste executados
- Bugs documentados e priorizados
- Funciona nos navegadores principais
- Responsivo em mobile

**Resultado esperado**: Lista completa de bugs priorizados pronta para correcao.

**Tempo estimado**: 2 dias

---

#### Atividade 6.2: Correcao de bugs criticos

**Descricao**: Corrigir todos os bugs criticos e de alta prioridade identificados nos testes.

**Execucao**:
1. Filtrar issues por label "bug" e prioridade "P0" ou "P1"
2. Corrigir bugs na ordem de prioridade
3. Testar correcao de cada bug
4. Marcar issue como resolvida
5. Re-testar fluxos afetados
6. Decidir se bugs de media/baixa prioridade serao corrigidos pre-lancamento ou pos-lancamento

**Criterio de aceite**:
- Todos os bugs criticos (P0) corrigidos
- Todos os bugs altos (P1) corrigidos ou aceitos como riscos
- Bugs corrigidos testados e validados
- Lista de bugs conhecidos (P2/P3) documentada

**Resultado esperado**: MVP estavel sem bugs criticos conhecidos.

**Tempo estimado**: 2-3 dias

---

#### Atividade 6.3: Setup de analytics e monitoramento

**Descricao**: Configurar ferramentas de analytics e monitoramento de erros para coletar metricas apos lancamento.

**Execucao**:
1. Configurar Google Analytics 4 ou Posthog:
   - Criar conta/projeto
   - Adicionar tracking code
   - Configurar eventos customizados:
     - Cadastro concluido
     - Login
     - Funcionalidade core usada
     - Pagamento iniciado
     - Pagamento concluido
   - Testar que eventos estao sendo enviados
2. Configurar Sentry para error tracking:
   - Criar projeto Sentry
   - Instalar SDK: `npm install @sentry/nextjs`
   - Configurar Sentry
   - Testar que erros estao sendo capturados
3. Configurar alertas:
   - Sentry: email para erros criticos
   - Vercel: alertas de downtime
4. Criar dashboard basico de metricas principais

**Criterio de aceite**:
- Analytics configurado e eventos sendo enviados
- Error tracking configurado e erros sendo capturados
- Alertas configurados
- Dashboard de metricas acessivel

**Resultado esperado**: Ferramentas de observabilidade prontas para coletar dados em producao.

**Tempo estimado**: 1 dia

---

#### Atividade 6.4: Preparacao do ambiente de producao

**Descricao**: Validar configuracoes de producao, migrar Stripe para modo live, configurar DNS se necessario.

**Execucao**:
1. Revisar variaveis de ambiente de producao no Vercel
2. Validar DATABASE_URL aponta para banco de producao
3. Migrar Stripe de modo teste para modo live:
   - Preencher informacoes de negocio no Stripe
   - Obter aprovacao da conta (se necessario)
   - Atualizar STRIPE_SECRET_KEY para chave live
   - Configurar webhooks para URL de producao
   - Criar produtos reais no Stripe
4. Se usando dominio customizado:
   - Configurar DNS
   - Validar HTTPS funcionando
5. Executar migration final no banco de producao
6. Fazer smoke test em producao
7. Preparar rollback plan (como reverter se der problema)

**Criterio de aceite**:
- Variaveis de ambiente de producao validadas
- Stripe em modo live configurado
- Dominio customizado funcionando (se aplicavel)
- Banco de producao com schema atualizado
- Smoke test em producao passou

**Resultado esperado**: Ambiente de producao pronto para receber usuarios reais.

**Tempo estimado**: 1 dia

---

#### Atividade 6.5: Criacao de documentacao de usuario

**Descricao**: Criar documentacao basica, FAQ e materiais de suporte para usuarios.

**Execucao**:
1. Criar pagina "Como usar" ou "Getting Started"
2. Documentar passo a passo da funcionalidade principal
3. Criar FAQ com perguntas comuns:
   - Como criar conta?
   - Como funciona o pagamento?
   - Como cancelar assinatura?
   - Politica de reembolso (se aplicavel)
4. Criar pagina de contato/suporte
5. (Opcional) Gravar video tutorial rapido (2-3 min)
6. Preparar email de onboarding com links para docs

**Criterio de aceite**:
- Documentacao basica criada e acessivel
- FAQ com perguntas principais
- Pagina de contato/suporte funcionando
- Email de onboarding preparado

**Resultado esperado**: Materiais de suporte prontos para ajudar primeiros usuarios.

**Tempo estimado**: 1 dia

---

#### Atividade 6.6: Checklist de Go-Live

**Descricao**: Executar checklist completo de validacoes pre-lancamento.

**Execucao**:
1. Usar [Checklist de Go-Live](_DATA/checklist-go-live.md)
2. Validar item por item:
   - Tecnicos (deploy, banco, variaveis ambiente)
   - Funcionais (todos os fluxos funcionando)
   - Negocio (pagamento, termos de uso, privacidade)
   - Legal/Compliance (LGPD basico, cookies)
   - Monitoramento (analytics, error tracking)
3. Corrigir qualquer item nao conforme
4. Obter aprovacao final de stakeholders
5. Agendar data/hora de lancamento

**Criterio de aceite**:
- Todos os itens do checklist validados
- Nao-conformidades corrigidas ou aceitas como riscos
- Aprovacao de stakeholders obtida
- Data de lancamento definida

**Resultado esperado**: MVP aprovado e pronto para lancamento.

**Tempo estimado**: 1 dia

---

### Etapa 7 - Lancamento e Coleta de Feedback (Continuo - primeiras 2-4 semanas)

#### Atividade 7.1: Deploy final e lancamento

**Descricao**: Executar deploy final, validar que tudo esta funcionando e anunciar lancamento.

**Execucao**:
1. Fazer deploy final para producao
2. Executar smoke test pos-deploy:
   - Cadastro funciona
   - Login funciona
   - Funcionalidade core funciona
   - Pagamento funciona
   - Analytics enviando eventos
3. Monitorar logs e Sentry nos primeiros minutos
4. Se tudo OK, considerar lancado
5. Se houver problema critico, executar rollback
6. Anunciar lancamento:
   - Email para lista de espera (se houver)
   - Post em redes sociais
   - Comunicacao interna

**Criterio de aceite**:
- Deploy finalizado
- Smoke test passou
- Sem erros criticos nos primeiros 30 minutos
- Lancamento anunciado

**Resultado esperado**: MVP oficialmente em producao e disponivel.

**Tempo estimado**: 0.5 dia

---

#### Atividade 7.2: Onboarding de early adopters

**Descricao**: Convidar e fazer onboarding manual dos primeiros usuarios (early adopters).

**Execucao**:
1. Identificar lista de early adopters (20-50 pessoas):
   - Usuarios de lista de espera
   - Contatos pessoais
   - Comunidades relevantes
   - Usuarios que participaram de pesquisas
2. Enviar convite personalizado
3. Oferecer incentivo (desconto, acesso vip, suporte direto)
4. Fazer onboarding 1:1 ou em pequenos grupos:
   - Explicar proposta de valor
   - Demonstrar funcionalidade core
   - Ajudar a completar primeiro uso
5. Pedir feedback inicial
6. Criar canal de comunicacao direta (Slack, WhatsApp group, etc)

**Criterio de aceite**:
- Lista de early adopters identificada
- Minimo 20 convites enviados
- Minimo 10 usuarios fizeram onboarding
- Canal de comunicacao criado

**Resultado esperado**: Grupo inicial de usuarios ativos usando o MVP.

**Tempo estimado**: 2-3 dias (primeira semana)

---

#### Atividade 7.3: Monitoramento de metricas

**Descricao**: Acompanhar metricas diariamente, identificar problemas, ajustar rapidamente.

**Execucao**:
1. Checar metricas diariamente:
   - Cadastros
   - Usuarios ativos
   - Taxa de conclusao de fluxo core
   - Taxa de conversao para pagamento
   - Erros no Sentry
   - Performance (Vercel Analytics)
2. Criar documento de acompanhamento semanal
3. Identificar gargalos ou problemas:
   - Usuarios abandonando em qual etapa?
   - Erros recorrentes?
   - Performance ruim em qual pagina?
4. Priorizar correcoes ou melhorias
5. Fazer deploys rapidos para corrigir problemas criticos

**Criterio de aceite**:
- Metricas sendo checadas diariamente
- Documento de acompanhamento criado
- Problemas criticos identificados e corrigidos em ate 48h

**Resultado esperado**: Monitoramento ativo garantindo qualidade da experiencia.

**Tempo estimado**: 1h/dia continuo

---

#### Atividade 7.4: Coleta de feedback qualitativo

**Descricao**: Realizar entrevistas, surveys e coletar feedback detalhado dos early adopters.

**Execucao**:
1. Criar survey curto (5-7 perguntas):
   - O que voce achou do produto?
   - Conseguiu realizar o que queria?
   - O que falta?
   - Voce pagaria por isso?
   - NPS: Recomendaria para um amigo? (0-10)
2. Enviar survey apos 3-5 dias de uso
3. Agendar entrevistas 1:1 com usuarios mais engajados:
   - 5-10 entrevistas de 30 minutos
   - Perguntas abertas sobre experiencia
   - Observar uso ao vivo (session recording ou compartilhamento de tela)
4. Documentar feedback em documento estruturado:
   - Quotes de usuarios
   - Problemas recorrentes
   - Features mais solicitadas
   - Surpresas (positivas e negativas)
5. Categorizar feedback em temas

**Criterio de aceite**:
- Survey criado e enviado
- Minimo 10 respostas ao survey
- Minimo 5 entrevistas realizadas
- Feedback documentado e categorizado

**Resultado esperado**: Insights qualitativos profundos sobre experiencia de usuario.

**Tempo estimado**: 3-5 dias (ao longo de 2 semanas)

---

#### Atividade 7.5: Correcao de bugs e melhorias rapidas

**Descricao**: Corrigir bugs reportados por usuarios e implementar melhorias rapidas que aumentem satisfacao.

**Execucao**:
1. Criar issues para todos os bugs reportados
2. Priorizar:
   - P0: Impede uso - corrigir em 24h
   - P1: Degrada experiencia - corrigir em 1 semana
   - P2: Incomodo menor - corrigir em 2-4 semanas
3. Implementar quick wins:
   - Melhorias de UX simples
   - Ajustes de copy
   - Adicionar hints/tooltips solicitados
4. Comunicar correcoes aos usuarios:
   - Email semanal de updates
   - In-app notifications
5. Agradecer usuarios que reportaram problemas

**Criterio de aceite**:
- Todos os bugs reportados documentados em issues
- Bugs P0 corrigidos em 24h
- Bugs P1 corrigidos em 1 semana
- Quick wins implementados
- Usuarios notificados de correcoes

**Resultado esperado**: MVP cada vez mais estavel e alinhado com expectativas de usuarios.

**Tempo estimado**: 2-3 dias/semana (continuo)

---

#### Atividade 7.6: Preparacao do relatorio de validacao

**Descricao**: Apos 2-4 semanas de MVP em producao, consolidar aprendizados e preparar relatorio de validacao.

**Execucao**:
1. Consolidar metricas coletadas:
   - Cadastros totais
   - Usuarios ativos
   - Taxa de retencao (usuarios que voltam)
   - Taxa de conclusao de fluxo core
   - Taxa de conversao para pagamento
   - Revenue total (se aplicavel)
   - NPS medio
2. Analisar vs. metas definidas no Briefing
3. Resumir feedback qualitativo:
   - Principais temas
   - Quotes mais relevantes
   - Features mais solicitadas
4. Listar bugs conhecidos e melhorias planejadas
5. Fazer recomendacao: **Pivotar | Perseverar | Expandir**
   - **Pivotar**: Hipotese nao validada, mudar direcao
   - **Perseverar**: Resultados mistos, continuar testando
   - **Expandir**: Hipotese validada, investir mais
6. Definir proximos passos claros
7. Usar [Template de Relatorio de Validacao](_DATA/template-relatorio-validacao.md)

**Criterio de aceite**:
- Todas as metricas consolidadas
- Feedback qualitativo resumido
- Recomendacao clara (Pivotar/Perseverar/Expandir)
- Proximos passos definidos
- Relatorio compartilhado com stakeholders

**Resultado esperado**: Decisao informada sobre futuro do produto baseada em dados reais.

**Tempo estimado**: 2 dias

---

## Indicadores de sucesso

### Durante desenvolvimento (Etapas 1-6)

- **Timeline**: MVP completo em ate 8 semanas
- **Issues concluidas**: 90%+ das issues planejadas entregues
- **Bugs criticos pre-lancamento**: Zero bugs P0 conhecidos no go-live
- **Test coverage**: Todos os fluxos principais testados manualmente
- **Performance**: Tempo de resposta < 2s em 95% das requisicoes

### Pos-lancamento (Etapa 7)

- **Time to first user**: Primeiro usuario real em ate 48h pos-lancamento
- **Early adopters onboarding**: Minimo 20 usuarios nos primeiros 7 dias
- **Taxa de conclusao de fluxo core**: Minimo 60% dos usuarios completam acao principal
- **Taxa de conversao para pagamento**: Minimo 5% dos usuarios cadastrados pagam
- **NPS inicial**: Score acima de 30 (indicador de early adopters satisfeitos)
- **Revenue inicial**: Qualquer valor > $0 (valida disposicao de pagamento)
- **Feedback collection**: Minimo 10 respostas de survey + 5 entrevistas
- **Uptime**: 99%+ de disponibilidade

### Criterios de validacao de hipotese

A hipotese e considerada **validada** se:
- Taxa de conclusao de fluxo core > 60%
- Taxa de conversao para pagamento > 5%
- NPS > 30
- Usuarios retornam ao produto (retencao semana 2 > 40%)
- Feedback qualitativo e majoritariamente positivo

A hipotese e considerada **nao validada** se:
- Taxa de conclusao de fluxo core < 40%
- Taxa de conversao para pagamento < 2%
- NPS < 10
- Usuarios nao retornam (retencao semana 2 < 20%)
- Feedback qualitativo identifica problema fundamental com proposta

Resultados entre esses valores indicam necessidade de **perseverar** (continuar testando e ajustando).

## Rituais e comunicacao

### Durante desenvolvimento

**Daily standup** (5-10 min, diario):
- O que fiz ontem?
- O que farei hoje?
- Estou bloqueado em algo?
- Issues movidas no board kanban

**Weekly sync** (30-45 min, toda segunda):
- Review de progresso vs. timeline
- Ajuste de prioridades se necessario
- Decisoes de escopo (adicionar/remover features)
- Demo interno de features prontas

**Demo para stakeholders** (30 min, a cada 2 semanas):
- Demonstracao de features concluidas
- Coleta de feedback
- Validacao de direcao

### Pos-lancamento

**Monitoramento diario** (15 min/dia):
- Check de metricas
- Review de Sentry errors
- Resposta a feedback de usuarios

**Retrospectiva semanal** (1h, toda sexta):
- O que funcionou bem?
- O que precisa melhorar?
- Decisoes para proxima semana
- Atualizacao de roadmap

**Relatorio semanal** (escrito):
- Metricas da semana
- Principais feedbacks
- Bugs corrigidos
- Proximos passos

## Riscos e mitigacoes

### Risco 1: Escopo crescer durante desenvolvimento
**Probabilidade**: Alta
**Impacto**: Alto - Atrasa lancamento, aumenta custo
**Mitigacao**:
- Criar documento "O que NAO entra no MVP" no Briefing
- Revisao semanal de escopo com stakeholders
- Toda nova feature deve ser justificada contra hipotese principal
- Usar regra "3 strikes": Se 3 usuarios diferentes pedirem mesma feature pos-lancamento, adicionar no roadmap (mas nao no MVP inicial)

---

### Risco 2: Time subestimar complexidade tecnica
**Probabilidade**: Media
**Impacto**: Alto - Atraso no cronograma
**Mitigacao**:
- Adicionar buffer de 20% em todas as estimativas
- Fazer spike tecnico nas Etapas 2-3 para validar viabilidade
- Ter plano B para features complexas (versao simplificada)
- Revisao semanal de timeline e ajuste de escopo se necessario

---

### Risco 3: Problemas com integracao Stripe
**Probabilidade**: Media
**Impacto**: Medio - Atrasa teste de monetizacao
**Mitigacao**:
- Comecar integracao cedo (Etapa 3)
- Usar Stripe Checkout (hosted) ao inves de custom payment flow
- Seguir documentacao oficial e usar SDK oficial
- Testar exaustivamente em modo teste antes de ir para live
- Ter suporte Stripe disponivel (documentacao + forum)

---

### Risco 4: Nao conseguir early adopters para testar
**Probabilidade**: Media
**Impacto**: Alto - Nao consegue validar hipotese
**Mitigacao**:
- Identificar potenciais early adopters desde Etapa 1
- Construir lista de espera durante desenvolvimento
- Oferecer incentivos (desconto, acesso vip, lifetime deal)
- Ativar rede pessoal de founders/time
- Usar comunidades relevantes (Product Hunt, Reddit, grupos Facebook)
- Ter plano B: Ads pagas para aquisicao inicial ($200-500)

---

### Risco 5: Bugs criticos em producao
**Probabilidade**: Media
**Impacto**: Alto - Degrada experiencia, perda de usuarios
**Mitigacao**:
- Testes exaustivos pre-lancamento (Etapa 6)
- Sentry configurado para alertas de erros
- Monitoramento ativo nas primeiras 48h pos-lancamento
- Rollback plan preparado
- Comunicacao transparente com usuarios se houver problemas

---

### Risco 6: Performance ruim em producao
**Probabilidade**: Baixa
**Impacto**: Medio - Experiencia degradada
**Mitigacao**:
- Usar Vercel (otimizado para Next.js)
- Implementar caching basico (SWR, React Query)
- Usar Next.js Image para otimizar imagens
- Monitorar Vercel Analytics desde dia 1
- Fazer load testing basico pre-lancamento (opcional)

---

### Risco 7: Hipotese nao validada e time insistir em continuar
**Probabilidade**: Media
**Impacto**: Alto - Desperdicio de recursos
**Mitigacao**:
- Definir criterios claros de validacao no Briefing
- Criar relatorio de validacao objetivo com metricas
- Ter acordo pre-estabelecido: Se metricas X nao forem atingidas, pivotar
- Incluir stakeholders externos na analise de resultados (menos vies)
- Celebrar aprendizado mesmo se decisao for pivotar

---

### Risco 8: Dependencia de um unico desenvolvedor
**Probabilidade**: Alta (se time pequeno)
**Impacto**: Critico - Projeto para se desenvolvedor sair
**Mitigacao**:
- Documentar decisoes arquiteturais
- Codigo bem estruturado e legivel
- README detalhado com setup
- Pair programming em partes criticas (se houver 2+ devs)
- Considerar backup developer (freelancer sob demanda)

---

## Checklist de prontidao para inicio

### Documentacao e alinhamento
- [ ] Briefing de produto disponivel e lido
- [ ] Hipotese principal identificada
- [ ] Publico-alvo (persona) definido
- [ ] Stakeholders identificados e alinhados
- [ ] Expectativas de timeline discutidas e acordadas

### Budget e recursos
- [ ] Budget de infraestrutura aprovado ($500-2.000/mes)
- [ ] Conta Stripe criada e verificada
- [ ] Time alocado (minimo 1 dev full-stack)
- [ ] Designer disponivel (part-time ou full-time)

### Setup tecnico
- [ ] Ambiente de desenvolvimento preparado (Node.js, Git)
- [ ] Repositorio Git criado (GitHub, GitLab)
- [ ] Acesso a ferramentas necessarias (Vercel, banco, email service)
- [ ] Variaveis de ambiente sensíveis definidas

### Gestao
- [ ] Ferramenta de gestao de issues escolhida (GitHub Projects, Linear)
- [ ] Rituais definidos (standup, weekly sync)
- [ ] Canal de comunicacao do time criado (Slack, Discord)

### Legal e compliance basico
- [ ] Termos de uso preparados (pode ser template basico)
- [ ] Politica de privacidade preparada (LGPD basico)
- [ ] Politica de reembolso definida (se aplicavel)

## Proximos passos apos conclusao

### A) Se hipotese foi VALIDADA (Expandir)

1. **Priorizar proxima iteracao**:
   - Analise feedback: Quais features mais solicitadas?
   - Identifique gargalos: O que impede crescimento?
   - Defina roadmap de proximo trimestre

2. **Estruturar time**:
   - Contratar ou alocar mais desenvolvedores se necessario
   - Adicionar product manager (se ainda nao houver)
   - Considerar customer success para suporte

3. **Escalar aquisicao**:
   - Investir em marketing (ads, content, SEO)
   - Construir funil de vendas estruturado
   - Implementar programa de referral

4. **Fortalecer produto**:
   - Adicionar features secundarias priorizadas
   - Melhorar onboarding baseado em dados
   - Implementar analytics mais avancado

5. **Preparar para escala**:
   - Revisar arquitetura tecnica
   - Implementar testes automatizados
   - Melhorar monitoring e observability

---

### B) Se hipotese foi PARCIALMENTE VALIDADA (Perseverar)

1. **Analise profunda**:
   - Quais metricas foram atingidas e quais nao?
   - O que feedback qualitativo revela?
   - Qual parte da hipotese funciona e qual nao?

2. **Ajustar e testar novamente**:
   - Fazer pequenos ajustes (nao grande refactor)
   - Focar em melhorar metrica mais critica
   - Dar mais 4-6 semanas para nova validacao

3. **Testar com publico diferente**:
   - A persona pode estar errada?
   - Testar com segmento adjacente
   - Ajustar messaging e posicionamento

4. **Simplificar ainda mais**:
   - MVP pode estar complexo demais?
   - Remover features secundarias e focar so na core
   - Reduzir friccao (menos campos em formularios, menos etapas)

5. **Definir criterio de decisao**:
   - Se metricas X nao melhorarem em Y semanas, pivotar
   - Evitar perseverar indefinidamente

---

### C) Se hipotese NAO foi validada (Pivotar)

1. **Aceitar o aprendizado**:
   - Documentar o que foi aprendido
   - Celebrar execucao rapida (validou em 8 semanas, nao 8 meses)
   - Compartilhar aprendizados com time

2. **Analisar o que deu errado**:
   - Problema nao e relevante?
   - Solucao nao resolve o problema?
   - Publico-alvo estava errado?
   - Timing estava errado?
   - Precificacao estava errada?

3. **Decidir tipo de pivot**:
   - **Pivot de problema**: Mesmo publico, problema diferente
   - **Pivot de solucao**: Mesmo problema, solucao diferente
   - **Pivot de publico**: Mesmo problema, publico diferente
   - **Pivot de modelo de negocio**: Mesmo produto, monetizacao diferente

4. **Reusar aprendizado e codigo**:
   - Partes do MVP podem ser reusadas?
   - Usuarios atuais podem testar novo pivot?
   - Infraestrutura pode ser mantida?

5. **Executar novo ciclo de MVP**:
   - Voltar para definicao de hipotese
   - Executar nova estrategia MVP Builder
   - Manter disciplina de validacao rapida

---

### D) Proximos processos recomendados

Independente do resultado:

- **Estrategia de Growth**: Se validou e quer crescer
- **Processo de Roadmap**: Para planejar proximas features
- **Processo de Customer Success**: Para estruturar suporte
- **Processo de Fundraising**: Se precisa captar investimento

---

**Ultima atualizacao**: 2025-11-05
**Versao**: 1.0
**Mantido por**: Framework Business Team
