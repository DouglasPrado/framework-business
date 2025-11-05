# Base de Conhecimento - Setup de Infraestrutura para MVP

## Propósito

Este documento fornece contexto teórico, boas práticas e referências sobre configuração de infraestrutura técnica para MVPs usando Next.js, Prisma, NextAuth e Stripe.

## Fundamentos Teóricos

### Stack Técnica Padrão

**Por que Next.js?**
- Framework React maduro e popular
- App Router moderno com Server Components
- API Routes integradas (backend + frontend)
- Deploy simples na Vercel
- Grande comunidade e documentação

**Por que Prisma?**
- ORM type-safe para TypeScript
- Migrations automáticas
- Prisma Studio para visualizar dados
- Suporte excelente para PostgreSQL
- Developer experience superior

**Por que NextAuth.js?**
- Solução completa de autenticação
- Integração nativa com Next.js
- Suporta múltiplos providers
- Sessões seguras
- Adapter para Prisma pronto

**Por que Stripe?**
- Líder de mercado em pagamentos
- API bem documentada
- Modo teste robusto
- Webhooks confiáveis
- SDKs oficiais

### Princípios de Infraestrutura

**1. Segurança First**
- Nunca commitar .env
- Usar variáveis de ambiente
- Hash de senhas com bcrypt
- HTTPS em production
- Validar inputs

**2. Developer Experience**
- Documentar tudo no README
- Instruções claras de setup
- .env.example completo
- Scripts npm úteis

**3. Observabilidade**
- Analytics desde dia 1
- Error tracking configurado
- Logs estruturados
- Monitoring ativo

## Boas Práticas

### Prisma

**Do:**
- Use migrations para controle de schema
- Documente modelos com comentários
- Use indexes para queries frequentes
- Teste migrations antes de production

**Don't:**
- Não use `prisma db push` em production
- Não delete migrations manualmente
- Não ignore warnings de breaking changes

### NextAuth

**Do:**
- Use NEXTAUTH_SECRET gerado: `openssl rand -base64 32`
- Configure NEXTAUTH_URL corretamente
- Implemente rate limiting em login
- Use sessões JWT para stateless

**Don't:**
- Não reutilize secrets entre ambientes
- Não armazene dados sensíveis na sessão
- Não confie apenas em client-side auth

### Stripe

**Do:**
- Sempre teste com cartões de teste
- Valide webhooks com signature
- Trate erros de pagamento gracefully
- Mantenha logs de transações

**Don't:**
- Não use chaves de production em desenvolvimento
- Não confie apenas em client-side
- Não ignore eventos de webhook

### Componentes

**Do:**
- Crie componentes reutilizáveis
- Use TypeScript para props
- Documente com JSDoc
- Siga padrão de nomenclatura

**Don't:**
- Não crie componentes muito complexos
- Não duplique código
- Não ignore acessibilidade

## Materiais de Apoio

### Documentação Oficial

- **Next.js:** https://nextjs.org/docs
- **Prisma:** https://www.prisma.io/docs
- **NextAuth:** https://next-auth.js.org
- **Stripe:** https://stripe.com/docs
- **TailwindCSS:** https://tailwindcss.com/docs
- **shadcn/ui:** https://ui.shadcn.com

### Tutoriais Recomendados

- Next.js App Router Tutorial
- Prisma Quickstart
- NextAuth.js Getting Started
- Stripe Checkout Integration

### Providers Recomendados

**Banco de Dados:**
- Supabase (free tier generoso)
- Neon (serverless PostgreSQL)
- Railway (simples de usar)

**Hosting:**
- Vercel (otimizado para Next.js)

**Analytics:**
- Google Analytics 4 (gratuito)
- Posthog (open source)

**Error Tracking:**
- Sentry (free tier 5k eventos/mês)

## Perguntas Frequentes

### Geral

**P: Quanto tempo leva o setup completo?**
R: 5-7 dias em média para um desenvolvedor full-stack experiente.

**P: Preciso conhecer todas as tecnologias antes?**
R: Não, mas familiaridade com React e TypeScript ajuda muito. O resto pode aprender fazendo.

**P: Posso usar outras tecnologias?**
R: Pode, mas essa stack foi escolhida por velocidade e confiabilidade. Trocar pode aumentar timeline.

### Prisma e Banco

**P: Qual provider de banco usar?**
R: Supabase para simplicidade, Neon para performance, Railway para flexibilidade.

**P: Como testar migrations localmente?**
R: Use banco PostgreSQL local com Docker ou banco de desenvolvimento no provider.

**P: E se migration quebrar?**
R: Prisma permite rollback. Sempre teste migrations em desenvolvimento primeiro.

### NextAuth

**P: Preciso implementar Google OAuth?**
R: Não é obrigatório no MVP. Email/senha funciona. Adicione OAuth depois se necessário.

**P: Como funciona a sessão?**
R: NextAuth usa JWT por padrão (stateless) ou database sessions (stateful). JWT é mais simples para MVP.

**P: E recuperação de senha?**
R: Implemente enviando email com token único e link para reset. Use serviço como Resend ou SendGrid.

### Stripe

**P: Preciso de conta business?**
R: Não, conta pessoal funciona em modo teste. Ative modo live quando validar.

**P: Webhooks não funcionam localmente, o que fazer?**
R: Use Stripe CLI: `stripe listen --forward-to localhost:3000/api/webhooks/stripe`

**P: Como testar cartões de crédito?**
R: Use cartões de teste do Stripe:
- Sucesso: 4242 4242 4242 4242
- Falha: 4000 0000 0000 0002

### Deploy

**P: Preciso pagar pela Vercel?**
R: Não, free tier é suficiente para MVP. Pague só se escalar muito.

**P: Como atualizo variáveis de ambiente?**
R: No dashboard Vercel, Settings > Environment Variables. Redeploy após mudanças.

**P: Deploy falhou, o que fazer?**
R: Verifique logs no Vercel dashboard. Erros comuns: variáveis faltando, build errors, migrations não aplicadas.

### Componentes

**P: Devo usar biblioteca de componentes pronta?**
R: shadcn/ui é recomendado - não é biblioteca, são componentes que você copia e customiza.

**P: Preciso criar todos os componentes agora?**
R: Crie apenas os básicos (Layout, Button, Input, Card). Adicione outros conforme necessidade.

## Troubleshooting Comum

### Prisma não conecta ao banco
- Verificar DATABASE_URL no .env
- Testar conexão com `npx prisma db pull`
- Verificar firewall/whitelist do provider
- Confirmar que banco existe

### NextAuth redirect loop
- Verificar NEXTAUTH_URL está correto
- Verificar que middleware não está bloqueando rotas de auth
- Limpar cookies do navegador

### Stripe webhook não funciona
- Verificar STRIPE_WEBHOOK_SECRET está correto
- Usar Stripe CLI localmente para testar
- Verificar que endpoint está acessível
- Validar signature do webhook

### Deploy falha na Vercel
- Verificar build passa localmente: `npm run build`
- Verificar todas as variáveis de ambiente configuradas
- Verificar Node.js version compatível
- Checar logs de build no dashboard

## Checklist de Qualidade

Antes de considerar setup completo:

**Banco de Dados:**
- [ ] Prisma conectado
- [ ] Migrations aplicadas
- [ ] Prisma Studio funciona
- [ ] Consegue criar/ler/atualizar dados

**Autenticação:**
- [ ] Cadastro funciona
- [ ] Login funciona
- [ ] Sessão persiste
- [ ] Logout funciona
- [ ] Rotas protegidas funcionam

**Pagamento:**
- [ ] Checkout funciona com cartão teste
- [ ] Webhooks atualizam banco
- [ ] Status de assinatura correto
- [ ] Erros tratados adequadamente

**Componentes:**
- [ ] Layout criado
- [ ] Componentes básicos criados
- [ ] TailwindCSS configurado
- [ ] Responsivo em mobile

**Deploy:**
- [ ] Deploy automático funciona
- [ ] Variáveis de ambiente configuradas
- [ ] App funciona em production
- [ ] Preview deploys funcionam

**Observabilidade:**
- [ ] Analytics rastreando
- [ ] Sentry capturando erros
- [ ] Logs acessíveis

## Glossário

**ORM:** Object-Relational Mapping - ferramenta que mapeia objetos para banco de dados

**Migration:** Mudança versionada no schema do banco de dados

**JWT:** JSON Web Token - formato de token de autenticação

**Webhook:** Endpoint que recebe eventos de serviços externos (ex: Stripe)

**Provider:** Serviço que fornece funcionalidade (ex: provider de autenticação Google)

**Adapter:** Código que conecta duas bibliotecas (ex: Prisma Adapter para NextAuth)

**Server Component:** Componente React que roda no servidor (Next.js App Router)

**API Route:** Endpoint de API criado no Next.js

**Middleware:** Código que intercepta requests antes de chegar à rota

**Environment Variables:** Variáveis de configuração que mudam por ambiente

---

**Última atualização:** 2025-11-05
**Mantido por:** Framework Business Team
**Versão:** 1.0
