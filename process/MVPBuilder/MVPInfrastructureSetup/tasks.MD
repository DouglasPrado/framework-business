# Tarefas - Setup de Infraestrutura para MVP

## Visão Geral

Este documento lista a sequência operacional de tarefas para executar o processo de Setup de Infraestrutura para MVP. Cada tarefa corresponde às etapas descritas no [process.MD](process.MD).

Tempo total estimado: 5-7 dias

## Lista de Tarefas

### Etapa 1: Configuração do Banco de Dados (1 dia)

#### Tarefa 1: Instalar Prisma
**Tempo estimado:** 5 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Abrir terminal no projeto
2. Executar: `npm install prisma @prisma/client`
3. Validar instalação verificando package.json

**Critérios de conclusão:**
- [ ] Prisma instalado
- [ ] @prisma/client instalado
- [ ] Dependências no package.json

---

#### Tarefa 2: Inicializar Prisma
**Tempo estimado:** 5 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Executar: `npx prisma init`
2. Verificar que pasta `/prisma` foi criada
3. Verificar que arquivo `prisma/schema.prisma` existe
4. Verificar que variável DATABASE_URL foi adicionada ao .env

**Critérios de conclusão:**
- [ ] Pasta /prisma criada
- [ ] schema.prisma existe
- [ ] .env tem DATABASE_URL

---

#### Tarefa 3: Criar banco PostgreSQL
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Escolher provider (Supabase, Neon ou Railway)
2. Criar conta no provider escolhido
3. Criar novo banco PostgreSQL
4. Copiar connection string
5. Salvar credenciais em local seguro

**Critérios de conclusão:**
- [ ] Banco PostgreSQL criado
- [ ] Connection string obtida
- [ ] Credenciais salvas

---

#### Tarefa 4: Configurar DATABASE_URL no .env
**Tempo estimado:** 10 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Abrir arquivo `.env`
2. Colar connection string na variável DATABASE_URL
3. Testar conexão: `npx prisma db pull`
4. Criar `.env.example` sem valores sensíveis

**Critérios de conclusão:**
- [ ] DATABASE_URL configurada
- [ ] Conexão testada e funcionando
- [ ] .env.example criado

---

#### Tarefa 5: Criar schema inicial com modelo User
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Abrir `prisma/schema.prisma`
2. Criar modelo User básico com campos: id, email, name, createdAt
3. Configurar provider como postgresql
4. Salvar arquivo

**Critérios de conclusão:**
- [ ] Schema Prisma com modelo User
- [ ] Provider configurado como postgresql
- [ ] Campos básicos definidos

---

#### Tarefa 6: Rodar primeira migration
**Tempo estimado:** 10 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Executar: `npx prisma migrate dev --name init`
2. Confirmar criação de migration
3. Verificar que tabela foi criada no banco
4. Verificar pasta `/prisma/migrations`

**Critérios de conclusão:**
- [ ] Migration executada com sucesso
- [ ] Tabela User criada no banco
- [ ] Pasta migrations criada

---

#### Tarefa 7: Testar Prisma Studio
**Tempo estimado:** 10 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Executar: `npx prisma studio`
2. Abrir navegador em http://localhost:5555
3. Verificar que tabela User aparece
4. Criar registro de teste manualmente
5. Validar que consegue criar/ler/atualizar dados

**Critérios de conclusão:**
- [ ] Prisma Studio abre sem erros
- [ ] Tabela User visível
- [ ] Consegue manipular dados

---

### Etapa 2: Implementação de Autenticação (2-3 dias)

#### Tarefa 8: Instalar NextAuth.js
**Tempo estimado:** 5 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Executar: `npm install next-auth @next-auth/prisma-adapter`
2. Executar: `npm install bcrypt @types/bcrypt`
3. Validar instalação no package.json

**Critérios de conclusão:**
- [ ] NextAuth instalado
- [ ] Prisma adapter instalado
- [ ] bcrypt instalado

---

#### Tarefa 9: Criar arquivo de configuração NextAuth
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor

**Passos:**
1. Criar `/app/api/auth/[...nextauth]/route.ts`
2. Importar NextAuth e configurações básicas
3. Configurar PrismaAdapter
4. Exportar handlers GET e POST

**Critérios de conclusão:**
- [ ] Arquivo route.ts criado
- [ ] NextAuth configurado
- [ ] Handlers exportados

---

#### Tarefa 10: Atualizar schema Prisma com modelos NextAuth
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Adicionar modelos: Account, Session, VerificationToken
2. Atualizar modelo User com campos NextAuth
3. Rodar migration: `npx prisma migrate dev --name add-nextauth`
4. Validar que tabelas foram criadas

**Critérios de conclusão:**
- [ ] Schema atualizado com modelos NextAuth
- [ ] Migration aplicada
- [ ] Tabelas criadas no banco

---

#### Tarefa 11: Configurar Credentials provider
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor

**Passos:**
1. Configurar Credentials provider no NextAuth
2. Implementar lógica de validação de email/senha
3. Adicionar hash de senha com bcrypt
4. Testar login básico

**Critérios de conclusão:**
- [ ] Credentials provider configurado
- [ ] Hash de senha implementado
- [ ] Login básico funcionando

---

#### Tarefa 12: Criar página de login
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Criar `/app/auth/signin/page.tsx`
2. Criar formulário com email e senha
3. Integrar com NextAuth signIn
4. Adicionar validação de formulário
5. Estilizar com TailwindCSS

**Critérios de conclusão:**
- [ ] Página de login criada
- [ ] Formulário funcional
- [ ] Validação implementada
- [ ] Design responsivo

---

#### Tarefa 13: Criar página de cadastro
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Criar `/app/auth/signup/page.tsx`
2. Criar formulário de cadastro
3. Criar API route para registro
4. Implementar validação e hash de senha
5. Redirecionar para login após sucesso

**Critérios de conclusão:**
- [ ] Página de cadastro criada
- [ ] API de registro funcionando
- [ ] Hash de senha no cadastro
- [ ] Redirecionamento funcionando

---

#### Tarefa 14: Implementar middleware de proteção de rotas
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor

**Passos:**
1. Criar `middleware.ts` na raiz
2. Implementar verificação de sessão
3. Configurar rotas protegidas
4. Redirecionar para login se não autenticado
5. Testar proteção

**Critérios de conclusão:**
- [ ] Middleware criado
- [ ] Rotas protegidas configuradas
- [ ] Redirecionamento funcionando
- [ ] Proteção testada

---

#### Tarefa 15: Testar fluxo completo de autenticação
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor

**Passos:**
1. Testar cadastro de novo usuário
2. Testar login com credenciais corretas
3. Testar login com credenciais incorretas
4. Testar sessão persistente (reload da página)
5. Testar logout
6. Testar acesso a rota protegida sem login

**Critérios de conclusão:**
- [ ] Todos os fluxos testados
- [ ] Sem erros ou bugs
- [ ] Sessão persistente funcionando
- [ ] Proteção de rotas funcionando

---

### Etapa 3: Integração com Stripe (2 dias)

#### Tarefa 16: Criar conta Stripe
**Tempo estimado:** 15 minutos
**Responsável:** Tech Lead

**Passos:**
1. Acessar https://stripe.com
2. Criar conta
3. Acessar dashboard
4. Ativar modo teste

**Critérios de conclusão:**
- [ ] Conta Stripe criada
- [ ] Acesso ao dashboard
- [ ] Modo teste ativo

---

#### Tarefa 17: Obter chaves API Stripe
**Tempo estimado:** 5 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. No dashboard Stripe, acessar "Developers" > "API keys"
2. Copiar "Publishable key" (modo teste)
3. Copiar "Secret key" (modo teste)
4. Adicionar ao .env:
   - STRIPE_PUBLISHABLE_KEY
   - STRIPE_SECRET_KEY

**Critérios de conclusão:**
- [ ] Chaves copiadas
- [ ] Variáveis adicionadas ao .env
- [ ] .env.example atualizado

---

#### Tarefa 18: Instalar Stripe SDK
**Tempo estimado:** 5 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Executar: `npm install stripe @stripe/stripe-js`
2. Validar instalação

**Critérios de conclusão:**
- [ ] Stripe SDK instalado
- [ ] Pacote no package.json

---

#### Tarefa 19: Configurar Stripe no backend
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Criar `/src/lib/stripe.ts`
2. Importar e inicializar Stripe com secret key
3. Exportar instância configurada
4. Criar helper functions se necessário

**Critérios de conclusão:**
- [ ] Arquivo stripe.ts criado
- [ ] Stripe inicializado
- [ ] Exportado para uso

---

#### Tarefa 20: Criar produtos no dashboard Stripe
**Tempo estimado:** 30 minutos
**Responsável:** Product Owner / Desenvolvedor

**Passos:**
1. Acessar dashboard Stripe > Products
2. Criar produto(s) de teste
3. Definir preços
4. Copiar price IDs
5. Adicionar price IDs ao código

**Critérios de conclusão:**
- [ ] Produtos criados no Stripe
- [ ] Preços definidos
- [ ] Price IDs obtidos

---

#### Tarefa 21: Implementar API route para checkout
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor

**Passos:**
1. Criar `/app/api/checkout/route.ts`
2. Implementar criação de checkout session
3. Adicionar validação de usuário autenticado
4. Retornar session ID
5. Testar com Postman/Insomnia

**Critérios de conclusão:**
- [ ] API route criada
- [ ] Checkout session funcionando
- [ ] Validação de auth implementada
- [ ] Testado com Postman

---

#### Tarefa 22: Criar página de pricing
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Criar `/app/pricing/page.tsx`
2. Exibir planos/produtos
3. Adicionar botões de compra
4. Integrar com Stripe Checkout
5. Estilizar com TailwindCSS

**Critérios de conclusão:**
- [ ] Página de pricing criada
- [ ] Produtos exibidos
- [ ] Botões funcionando
- [ ] Redirecionamento para Stripe Checkout

---

#### Tarefa 23: Criar webhook Stripe
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor

**Passos:**
1. Criar `/app/api/webhooks/stripe/route.ts`
2. Implementar verificação de assinatura
3. Escutar evento `checkout.session.completed`
4. Atualizar status no banco de dados
5. Configurar webhook secret no .env
6. Testar com Stripe CLI

**Critérios de conclusão:**
- [ ] Webhook criado
- [ ] Eventos sendo escutados
- [ ] Banco atualizado corretamente
- [ ] Testado com Stripe CLI

---

#### Tarefa 24: Testar checkout completo com cartões de teste
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor / QA

**Passos:**
1. Usar cartão de teste Stripe: 4242 4242 4242 4242
2. Completar checkout
3. Validar que webhook atualizou banco
4. Validar status de assinatura no app
5. Testar cartão que falha

**Critérios de conclusão:**
- [ ] Checkout completo funciona
- [ ] Webhook atualiza banco
- [ ] Status reflete corretamente
- [ ] Erros tratados adequadamente

---

### Etapa 4: Componentes Base (1-2 dias)

#### Tarefa 25: Instalar shadcn/ui (opcional)
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Executar: `npx shadcn-ui@latest init`
2. Responder prompts de configuração
3. Validar que components.json foi criado

**Critérios de conclusão:**
- [ ] shadcn/ui instalado (se usar)
- [ ] Configuração completa

---

#### Tarefa 26: Criar componente Layout
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Criar `/src/components/ui/Layout.tsx`
2. Implementar Header, Main, Footer
3. Adicionar navegação
4. Tornar responsivo
5. Documentar uso com JSDoc

**Critérios de conclusão:**
- [ ] Layout criado
- [ ] Header/Footer implementados
- [ ] Responsivo
- [ ] Documentado

---

#### Tarefa 27: Criar componentes Button, Input, Card
**Tempo estimado:** 3 horas
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Criar Button.tsx com variants
2. Criar Input.tsx com validação
3. Criar Card.tsx
4. Estilizar com TailwindCSS
5. Documentar cada componente

**Critérios de conclusão:**
- [ ] 3 componentes criados
- [ ] Variants implementadas
- [ ] Estilizados
- [ ] Documentados

---

#### Tarefa 28: Criar componentes Modal e Loading
**Tempo estimado:** 2 horas
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Criar Modal.tsx
2. Criar Loading.tsx (spinner)
3. Testar cada componente
4. Documentar

**Critérios de conclusão:**
- [ ] Modal funcional
- [ ] Loading/spinner funcional
- [ ] Documentados

---

#### Tarefa 29: Configurar tema TailwindCSS
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor Frontend

**Passos:**
1. Abrir `tailwind.config.ts`
2. Definir cores customizadas
3. Definir fontes
4. Definir espaçamentos customizados
5. Testar em componentes

**Critérios de conclusão:**
- [ ] Tema configurado
- [ ] Cores definidas
- [ ] Fontes configuradas
- [ ] Testado

---

### Etapa 5: Deploy Contínuo (0.5 dia)

#### Tarefa 30: Criar conta Vercel
**Tempo estimado:** 10 minutos
**Responsável:** Tech Lead

**Passos:**
1. Acessar https://vercel.com
2. Criar conta
3. Conectar com GitHub

**Critérios de conclusão:**
- [ ] Conta Vercel criada
- [ ] GitHub conectado

---

#### Tarefa 31: Conectar repositório ao Vercel
**Tempo estimado:** 15 minutos
**Responsável:** Tech Lead / DevOps

**Passos:**
1. No Vercel, clicar "New Project"
2. Selecionar repositório
3. Confirmar configurações (Next.js detectado)
4. Aguardar build inicial

**Critérios de conclusão:**
- [ ] Repositório conectado
- [ ] Build inicial completo

---

#### Tarefa 32: Configurar variáveis de ambiente no Vercel
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor / DevOps

**Passos:**
1. No Vercel, acessar projeto > Settings > Environment Variables
2. Adicionar todas as variáveis do .env:
   - DATABASE_URL
   - NEXTAUTH_SECRET
   - NEXTAUTH_URL
   - STRIPE_SECRET_KEY
   - STRIPE_PUBLISHABLE_KEY
   - STRIPE_WEBHOOK_SECRET
3. Aplicar para Production e Preview
4. Salvar

**Critérios de conclusão:**
- [ ] Todas as variáveis adicionadas
- [ ] Aplicadas para todos os ambientes
- [ ] Salvas com sucesso

---

#### Tarefa 33: Testar deploy em production
**Tempo estimado:** 30 minutos
**Responsável:** Desenvolvedor

**Passos:**
1. Fazer commit e push para main
2. Aguardar deploy automático
3. Acessar URL de production
4. Testar funcionalidades críticas:
   - Banco conectado
   - Login funciona
   - Stripe funciona
5. Validar que não há erros

**Critérios de conclusão:**
- [ ] Deploy completo sem erros
- [ ] App funcionando em production
- [ ] Funcionalidades críticas testadas
- [ ] Sem erros no console

---

### Etapa 6: Analytics e Monitoring (0.5 dia)

#### Tarefa 34: Configurar Google Analytics ou Posthog
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor

**Passos:**
1. Criar conta GA4 ou Posthog
2. Obter tracking ID
3. Instalar biblioteca necessária
4. Adicionar script de rastreamento
5. Testar que eventos são enviados

**Critérios de conclusão:**
- [ ] Analytics configurado
- [ ] Eventos sendo rastreados
- [ ] Dashboard mostrando dados

---

#### Tarefa 35: Configurar Sentry
**Tempo estimado:** 1 hora
**Responsável:** Desenvolvedor

**Passos:**
1. Criar conta Sentry
2. Executar: `npx @sentry/wizard@latest -i nextjs`
3. Configurar DSN no .env
4. Testar captura de erro
5. Validar que erros aparecem no dashboard

**Critérios de conclusão:**
- [ ] Sentry instalado
- [ ] DSN configurado
- [ ] Erros sendo capturados
- [ ] Dashboard funcionando

---

## Checklist de Conclusão

- [ ] Todas as 35 tarefas concluídas
- [ ] Prisma conectado e funcionando
- [ ] NextAuth completo (login, cadastro, proteção)
- [ ] Stripe em modo teste funcionando
- [ ] Componentes base criados
- [ ] Deploy automático na Vercel
- [ ] Analytics rastreando eventos
- [ ] Sentry capturando erros
- [ ] Todas as variáveis de ambiente documentadas
- [ ] README atualizado com instruções

---

**Próximo processo:** MVPCoreDevelopment (desenvolvimento da funcionalidade principal)
