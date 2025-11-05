# Validador - Setup de Infraestrutura para MVP

## Propósito

Este documento fornece critérios objetivos para validar que o processo de Setup de Infraestrutura foi executado com qualidade e completude.

## Validação Geral do Processo

### Critérios de Completude

- [ ] Todas as 35 tarefas do tasks.MD executadas
- [ ] Tempo total: 5-7 dias (máximo 10 dias)
- [ ] Todas as issues P0 (setup) concluídas
- [ ] README atualizado com instruções
- [ ] Variáveis de ambiente documentadas

## Validação do Banco de Dados

### Prisma + PostgreSQL

- [ ] Prisma instalado (`@prisma/client` no package.json)
- [ ] Banco PostgreSQL criado e acessível
- [ ] DATABASE_URL configurada no .env
- [ ] Schema Prisma criado com modelos básicos
- [ ] Migrations aplicadas com sucesso
- [ ] Prisma Studio abre sem erros (`npx prisma studio`)
- [ ] Consegue criar/ler/atualizar/deletar dados

**Teste funcional:**
- [ ] Executar `npx prisma studio` sem erros
- [ ] Criar registro manualmente no Prisma Studio
- [ ] Validar que registro aparece no banco

**Sinais de alerta:**
- Erro "Can't reach database server"
- Migration falha ao executar
- Prisma Studio não carrega tabelas

## Validação de Autenticação

### NextAuth.js

- [ ] NextAuth instalado (`next-auth` no package.json)
- [ ] Prisma Adapter instalado
- [ ] Arquivo `/app/api/auth/[...nextauth]/route.ts` existe
- [ ] Schema Prisma atualizado com modelos NextAuth
- [ ] Página de login criada (`/app/auth/signin`)
- [ ] Página de cadastro criada (`/app/auth/signup`)
- [ ] Middleware de proteção implementado (`middleware.ts`)
- [ ] NEXTAUTH_SECRET configurado no .env
- [ ] NEXTAUTH_URL configurado no .env

**Testes funcionais:**
- [ ] Consegue cadastrar novo usuário
- [ ] Consegue fazer login com credenciais corretas
- [ ] Login falha com credenciais incorretas
- [ ] Sessão persiste após reload da página
- [ ] Logout funciona corretamente
- [ ] Rota protegida redireciona para login se não autenticado
- [ ] Rota protegida é acessível após login

**Sinais de alerta:**
- Redirect loop infinito
- Sessão não persiste
- Erro "NEXTAUTH_URL is not set"
- Senha não está sendo hasheada

## Validação de Pagamento

### Stripe

- [ ] Stripe SDK instalado (`stripe` no package.json)
- [ ] Conta Stripe criada (modo teste)
- [ ] Chaves API obtidas (publishable + secret)
- [ ] STRIPE_SECRET_KEY configurado no .env
- [ ] STRIPE_PUBLISHABLE_KEY configurado no .env
- [ ] Arquivo `/src/lib/stripe.ts` existe
- [ ] Produtos criados no dashboard Stripe
- [ ] API route de checkout criada (`/app/api/checkout`)
- [ ] Página de pricing criada
- [ ] Webhook criado (`/app/api/webhooks/stripe`)
- [ ] STRIPE_WEBHOOK_SECRET configurado

**Testes funcionais:**
- [ ] Consegue iniciar checkout
- [ ] Checkout redireciona para Stripe
- [ ] Pagamento com cartão teste (4242 4242 4242 4242) funciona
- [ ] Webhook recebe evento `checkout.session.completed`
- [ ] Status de pagamento atualiza no banco de dados
- [ ] Falha de pagamento é tratada adequadamente

**Sinais de alerta:**
- Webhook não recebe eventos
- Status não atualiza no banco
- Erro "Invalid API Key"
- Checkout quebra em production

## Validação de Componentes

### Componentes Base

- [ ] Pasta `/src/components/ui` criada
- [ ] Layout.tsx criado e funcional
- [ ] Button.tsx criado com variants
- [ ] Input.tsx criado com validação
- [ ] Card.tsx criado
- [ ] Modal.tsx criado
- [ ] Loading.tsx (spinner) criado
- [ ] TailwindCSS configurado com tema customizado
- [ ] Componentes são responsivos (mobile)
- [ ] Componentes documentados com JSDoc

**Testes funcionais:**
- [ ] Todos os componentes renderizam sem erros
- [ ] Variants de botão funcionam (primary, secondary, outline)
- [ ] Modal abre e fecha corretamente
- [ ] Loading spinner é visível
- [ ] Layout é responsivo em diferentes tamanhos de tela

**Sinais de alerta:**
- Componentes quebram em mobile
- Estilos Tailwind não aplicam
- TypeScript errors em props

## Validação de Deploy

### Vercel

- [ ] Conta Vercel criada
- [ ] Repositório conectado ao Vercel
- [ ] Deploy inicial completo sem erros
- [ ] Todas as variáveis de ambiente configuradas no Vercel
- [ ] Preview deploys funcionam para PRs
- [ ] Production deploy na branch main funciona
- [ ] App funciona em production (sem erros 500)

**Testes funcionais:**
- [ ] Fazer push para main e validar deploy automático
- [ ] Acessar URL de production e testar:
  - [ ] Página inicial carrega
  - [ ] Login funciona
  - [ ] Checkout funciona
  - [ ] Nenhum erro no console do navegador
- [ ] Criar PR e validar preview deploy

**Sinais de alerta:**
- Build falha no Vercel
- Variáveis de ambiente faltando
- App funciona local mas quebra em production
- Database não conecta em production

## Validação de Observabilidade

### Analytics

- [ ] Google Analytics 4 ou Posthog configurado
- [ ] Tracking ID/API key configurado
- [ ] Script de rastreamento instalado
- [ ] Eventos básicos sendo rastreados:
  - [ ] Page views
  - [ ] Sign up
  - [ ] Login
  - [ ] Checkout iniciado

**Testes funcionais:**
- [ ] Navegar no app e validar eventos no dashboard analytics
- [ ] Eventos aparecem em tempo real
- [ ] Dados estão sendo coletados corretamente

### Error Tracking

- [ ] Sentry instalado
- [ ] DSN configurado no .env
- [ ] Sentry capturando erros
- [ ] Source maps configurados (para stack traces legíveis)

**Testes funcionais:**
- [ ] Forçar erro no app (ex: throw new Error("Test"))
- [ ] Validar que erro aparece no dashboard Sentry
- [ ] Stack trace está legível

**Sinais de alerta:**
- Eventos não aparecem no dashboard
- Sentry não captura erros
- Source maps quebrados (stack traces ilegíveis)

## Validação de Documentação

### README e .env

- [ ] README.md atualizado com:
  - [ ] Instruções de setup local
  - [ ] Lista de variáveis de ambiente necessárias
  - [ ] Como rodar projeto
  - [ ] Scripts npm disponíveis
  - [ ] Troubleshooting básico
- [ ] .env.example criado com todas as variáveis (sem valores)
- [ ] Comentários explicando cada variável de ambiente

**Teste funcional:**
- [ ] Seguir README do zero e conseguir rodar projeto
- [ ] Todas as variáveis do .env estão em .env.example

## Checklist de Consistência

### Entre Código e Configuração

- [ ] Todas as variáveis usadas no código estão no .env
- [ ] Todas as variáveis do .env estão no .env.example
- [ ] Todas as variáveis do .env estão configuradas no Vercel
- [ ] Schema Prisma corresponde ao banco de dados
- [ ] Models NextAuth estão sincronizados com schema

### Entre Ambientes

- [ ] App funciona localmente
- [ ] App funciona em preview (Vercel)
- [ ] App funciona em production (Vercel)
- [ ] Variáveis de ambiente corretas em cada ambiente

## Critérios de Aprovação Final

O processo está APROVADO e COMPLETO quando:

- [ ] TODOS os critérios de validação acima atendidos
- [ ] TODAS as 35 tarefas concluídas
- [ ] ZERO bugs críticos (P0) não resolvidos
- [ ] Time técnico validou infraestrutura
- [ ] Deploy em production funcionando
- [ ] Analytics e monitoring ativos
- [ ] Documentação completa

## Ações Corretivas

### Se Validação Falhar

**Falhas críticas (bloqueiam aprovação):**
- Banco de dados não conecta → Revisar DATABASE_URL, verificar firewall
- NextAuth não funciona → Verificar NEXTAUTH_SECRET, NEXTAUTH_URL, schema Prisma
- Stripe webhooks não funcionam → Configurar STRIPE_WEBHOOK_SECRET, testar com Stripe CLI
- Deploy falha → Verificar build local, variáveis de ambiente, logs Vercel

**Falhas não críticas (recomendam revisão):**
- Componentes não responsivos → Revisar TailwindCSS, testar em mobile
- Analytics não rastreando → Verificar tracking ID, testar eventos
- Documentação incompleta → Adicionar seções faltantes ao README

## Registro de Validação

**Processo validado por:** [Nome do validador]
**Data de validação:** [DD/MM/AAAA]

**Checklist de validação:**
- [ ] Banco de Dados: APROVADO
- [ ] Autenticação: APROVADO
- [ ] Pagamento: APROVADO
- [ ] Componentes: APROVADO
- [ ] Deploy: APROVADO
- [ ] Observabilidade: APROVADO
- [ ] Documentação: APROVADO

**Observações:**
[Registre aqui quaisquer observações, exceções ou problemas encontrados]

**Aprovação final:** [ ] SIM  [ ] NÃO (se não, documentar bloqueadores)

---

**Última atualização:** 2025-11-05
**Mantido por:** Framework Business Team
**Versão:** 1.0
