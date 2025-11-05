# Knowledge Base - MVPSecondaryDevelopment

Este documento consolida conhecimentos, referencias, FAQs e checkpoints para o processo de desenvolvimento de funcionalidades secundarias do MVP.

---

## Materiais de Apoio

### Templates Compartilhados (Reutilizar)

- [Checklist de Qualidade](../../_SHARED/templates/checklist-qualidade.MD) - Checklist padrao para validacao de entregaveis digitais
- [Template de Retrospectiva](../../_SHARED/templates/retrospectiva.MD) - Template para retrospectivas de sprint/ciclo
- [Template de Email Followup](../../_SHARED/templates/email-followup.MD) - Template para emails transacionais
- [Template de Estrutura de Landing](../../_SHARED/templates/estrutura-landing.MD) - Estrutura padrao para landing pages
- [Template de Persona](../../_SHARED/templates/persona.MD) - Para entender melhor usuarios finais

### Templates Locais (Especificos deste Processo)

- Roadmap de Funcionalidades Secundarias: `_DATA/roadmap-secundarias.md`
- Criterios de Aceite: `_DATA/criterios-aceite-secundarias.md`
- Documentacao de Eventos de Analytics: `_DATA/eventos-analytics.md`

### Processos Relacionados

- [MVPScopeDefinition](../MVPScopeDefinition/process.MD) - Define escopo do MVP (entrada)
- [MVPIssuesMapping](../MVPIssuesMapping/process.MD) - Mapeia issues tecnicas (entrada)
- [MVPInfrastructureSetup](../MVPInfrastructureSetup/process.MD) - Configura infraestrutura (entrada)
- [MVPCoreDevelopment](../MVPCoreDevelopment/process.MD) - Desenvolve funcionalidade core (entrada)

---

## Documentacao Tecnica de Referencia

### Framework e Bibliotecas Core

Consulte knowledge.MD do processo MVPCoreDevelopment para referencias completas de:
- Next.js, React, TypeScript
- Prisma, PostgreSQL
- NextAuth.js
- TailwindCSS, React Hook Form, Zod

### Analytics e Monitoramento

**Google Analytics 4**
- Documentacao oficial: https://developers.google.com/analytics
- Setup Guide: https://developers.google.com/analytics/devguides/collection/ga4
- Event tracking: https://developers.google.com/analytics/devguides/collection/ga4/events
- Next.js integration: https://github.com/vercel/next.js/tree/canary/examples/with-google-analytics

**Posthog**
- Documentacao oficial: https://posthog.com/docs
- Next.js integration: https://posthog.com/docs/libraries/next-js
- Event tracking: https://posthog.com/docs/integrate/client/js#sending-events
- Feature flags: https://posthog.com/docs/feature-flags

**Sentry**
- Documentacao oficial: https://docs.sentry.io
- Next.js integration: https://docs.sentry.io/platforms/javascript/guides/nextjs/
- Error monitoring: https://docs.sentry.io/platforms/javascript/guides/nextjs/errors/
- Performance monitoring: https://docs.sentry.io/platforms/javascript/guides/nextjs/performance/

### Servicos de Email

**Resend**
- Documentacao oficial: https://resend.com/docs
- Next.js integration: https://resend.com/docs/send-with-nextjs
- React Email: https://react.email/docs/introduction

**SendGrid**
- Documentacao oficial: https://docs.sendgrid.com
- API Reference: https://docs.sendgrid.com/api-reference
- Email templates: https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-templates

**React Email**
- Documentacao oficial: https://react.email
- Components: https://react.email/docs/components/html
- Examples: https://react.email/examples

### Upload de Arquivos

**Uploadthing**
- Documentacao oficial: https://docs.uploadthing.com
- Next.js setup: https://docs.uploadthing.com/getting-started/appdir
- File router: https://docs.uploadthing.com/api-reference/server#file-routes

**Cloudinary**
- Documentacao oficial: https://cloudinary.com/documentation
- Upload API: https://cloudinary.com/documentation/upload_images
- Next.js integration: https://cloudinary.com/documentation/react_integration

### Bibliotecas de UI

**Recharts (graficos)**
- Documentacao oficial: https://recharts.org
- Examples: https://recharts.org/en-US/examples
- API: https://recharts.org/en-US/api

**React Hot Toast**
- Documentacao oficial: https://react-hot-toast.com
- API: https://react-hot-toast.com/docs

---

## Best Practices

### Dashboard Design

**Principios de Dashboard Eficaz**
1. Mostrar metricas mais importantes no topo
2. Usar visualizacoes apropriadas (numeros, graficos, tabelas)
3. Destacar mudancas e tendencias (vs semana passada, vs mes passado)
4. Adicionar acoes rapidas relacionadas as metricas
5. Evitar sobrecarga de informacao (less is more)

**Organizacao Visual**
- Layout em grid (2-3 colunas em desktop, 1 coluna em mobile)
- Cards para metricas individuais
- Graficos para tendencias ao longo do tempo
- Tabelas para detalhes (top 5, ultimas atividades)

**Exemplo de Estrutura**
```
Dashboard
├── Metricas Principais (cards)
│   ├── Total de usuarios
│   ├── Receita total
│   └── Taxa de conversao
├── Graficos de Tendencia
│   ├── Usuarios novos por dia (linha)
│   └── Receita por mes (barra)
└── Atividade Recente (tabela)
    └── Ultimas 5 transacoes
```

### Sistema de Notificacoes

**Quando Enviar Notificacoes**
- Acoes importantes completadas (compra, cadastro)
- Eventos que requerem atencao do usuario (pagamento falhado)
- Atualizacoes relevantes de status
- Nao abuse: usuario deve poder controlar frequencia

**Email vs In-App**
- **Email**: Eventos criticos, transacoes, informacoes importantes
- **In-App**: Atualizacoes menos urgentes, notificacoes sociais
- **Ambos**: Eventos muito importantes (com opcao de desabilitar)

**Template de Email Eficaz**
```html
- Assunto claro e acionavel
- Preheader text (primeira linha visivel)
- Logo e branding
- Mensagem principal clara e concisa
- Call-to-action (CTA) destacado
- Informacoes secundarias (se necessario)
- Footer com links de unsubscribe e contato
```

### Onboarding de Usuarios

**Principios de Bom Onboarding**
1. Guiar usuario para "aha moment" rapidamente
2. Mostrar valor antes de pedir muito esforco
3. Usar contexto e progressao (passo 1 de 3)
4. Permitir pular (nao forcar)
5. Celebrar conquistas (micro-wins)

**Formatos Comuns**
- **Product Tour**: Tooltips guiados mostrando interface
- **Checklist**: Lista de tarefas para completar setup
- **Tutorial Interativo**: Guiar usuario fazendo acoes reais
- **Video**: Explicacao rapida em video (1-2 min)

**O Que Evitar**
- Onboarding longo demais (> 5 minutos)
- Tooltips excessivos que atrapalham uso
- Informacoes irrelevantes para usuario iniciante
- Nao permitir pular (frustante para usuarios avancados)

### Performance e Otimizacao

**Otimizacoes para Dashboard**
- Usar SSR (Server-Side Rendering) ou Static Generation quando possivel
- Implementar caching de metricas que nao mudam frequentemente
- Paginar ou limitar dados em listas/tabelas
- Lazy loading de graficos complexos
- Debounce em filtros e buscas

**Otimizacoes para Notificacoes**
- Processar envio de notificacoes de forma assincrona
- Rate limiting para prevenir spam
- Queue system para emails (usar servico de email com queue)
- Batch notifications quando apropriado

---

## FAQs

### Dashboard

**P: Quais metricas devo incluir no dashboard?**
R: Foque nas metricas que importam para o usuario tomar decisoes. Para MVP, mantenha simples: 3-5 metricas principais + graficos de tendencia + atividade recente. Evite "vanity metrics" que nao levam a acoes.

**P: Devo usar biblioteca de graficos ou criar do zero?**
R: Use biblioteca (Recharts e opcao solida). Criar graficos do zero e trabalho desnecessario para MVP. Recharts e bem documentada, funciona bem com React, e cobre maioria dos casos de uso.

**P: Como lidar com usuarios sem dados ainda (empty state)?**
R: Mostre empty state util com CTA claro. Exemplo: "Voce ainda nao tem usuarios. Compartilhe este link para convidar: [link]". Empty state e oportunidade de guiar usuario para proxima acao.

### Perfil e Configuracoes

**P: Onde armazenar imagens de avatar?**
R: Nao armazene no banco de dados. Use servico externo como Uploadthing (simples, focado em Next.js), Cloudinary (mais features), ou S3 (mais controle, mais setup). Para MVP, Uploadthing e recomendado pela simplicidade.

**P: Como implementar "deletar conta"?**
R: Adicione soft delete (marcar como deletado ao invés de remover). Mantenha dados por periodo (30 dias) para permitir recuperacao. Notifique usuario que dados serao permanentemente deletados apos X dias. Considere implicacoes legais (GDPR, LGPD).

**P: Devo permitir usuario mudar email?**
R: Sim, mas com verificacao. Envie email de confirmacao para novo email antes de mudar. Notifique email antigo sobre mudanca. Considere re-autenticacao antes de permitir mudanca de email.

### Notificacoes

**P: Notificacoes in-app ou email?**
R: Depende do contexto e urgencia. Email para eventos criticos/transacionais. In-app para atualizacoes menos urgentes. Para MVP, comece com email (mais simples) e adicione in-app se necessario.

**P: Como prevenir que notificacoes sejam consideradas spam?**
R: 1) Use servico de email reputado (Resend, SendGrid). 2) Implemente SPF, DKIM, DMARC. 3) Respeite preferencias do usuario. 4) Nao envie emails com muita frequencia. 5) Sempre inclua opcao de unsubscribe clara.

**P: Como testar envio de emails em desenvolvimento?**
R: Use modo test/sandbox do servico de email. Ou use servico como Mailtrap para interceptar emails. Nunca envie emails reais para usuarios em ambiente de desenvolvimento.

### Onboarding

**P: Quanto tempo deve durar o onboarding?**
R: Maximo 5 minutos, idealmente 2-3 minutos. Se levar mais, divida em etapas opcionais. Usuario deve conseguir completar e ver valor rapidamente.

**P: Devo forcar usuario a completar onboarding?**
R: Nao. Sempre ofereça opcao de pular. Alguns usuarios preferem explorar por conta. Voce pode lembar usuario depois ou mostrar tooltips contextuais conforme usa produto.

**P: Como medir sucesso do onboarding?**
R: Metricas importantes: 1) Taxa de conclusao do onboarding. 2) Tempo para completar. 3) Taxa de ativacao (usuario completa acao chave apos onboarding). 4) Retencao de usuarios que completaram vs que pularam.

### Analytics

**P: Google Analytics ou Posthog?**
R: Google Analytics 4 (GA4) e mais maduro, amplamente usado, gratuito. Posthog e open-source, mais controle sobre dados, feature flags integrados. Para MVP, GA4 e suficiente. Se privacidade de dados e critica, considere Posthog.

**P: Quais eventos devo rastrear?**
R: Foque em eventos que indicam valor entregue e pontos de conversao:
- Signup (cadastro)
- Onboarding completed
- Core feature used (acao principal do MVP)
- Purchase/conversion
- Return visit (retencao)

**P: Como garantir compliance com GDPR/LGPD?**
R: 1) Obtenha consentimento antes de rastrear. 2) Permita opt-out facil. 3) Documente que dados coleta e porque. 4) Se na Europa/Brasil, implemente banner de cookies. 5) Consulte advogado se possivel (compliance nao e trivial).

### Paginas Institucionais

**P: Onde encontrar templates de Termos de Uso e Politica de Privacidade?**
R: Use geradores online como:
- Termly: https://termly.io
- GetTerms: https://getterms.io
- TermsFeed: https://www.termsfeed.com

Importante: Adapte para seu caso especifico. Consulte advogado se possivel.

**P: Preciso de landing page se MVP ja tem dashboard?**
R: Se MVP e private (requer cadastro), sim, precisa de landing page para visitantes nao autenticados verem proposta de valor. Se MVP e publico, landing page e home podem ser mesma coisa.

---

## Checkpoints

### Checkpoint 1: Funcionalidades Secundarias Basicas (Dia 3)

**Objetivo:** Validar que principais funcionalidades secundarias estao implementadas.

**O que validar:**
- [ ] Dashboard renderizando com dados reais
- [ ] Perfil de usuario editavel
- [ ] Upload de avatar funcionando
- [ ] Sistema de notificacoes basico implementado

**Como validar:**
1. Fazer login no MVP
2. Acessar dashboard e verificar metricas
3. Editar perfil e fazer upload de avatar
4. Trigger evento que gera notificacao e verificar recebimento

**Se checkpoint falhar:**
- Identificar funcionalidades faltando
- Priorizar conclusao antes de avancar para polimento

**Output esperado:**
- Funcionalidades secundarias principais funcionais

---

### Checkpoint 2: Onboarding e Polimento (Dia 6)

**Objetivo:** Validar onboarding e consistencia visual.

**O que validar:**
- [ ] Onboarding funcionando para novos usuarios
- [ ] Paginas institucionais completas
- [ ] Design consistente em todas as paginas
- [ ] Analytics rastreando eventos principais
- [ ] Todos os fluxos testados em pelo menos 2 navegadores

**Como validar:**
1. Criar novo usuario e passar por onboarding
2. Navegar por todas as paginas do MVP
3. Verificar consistencia visual
4. Verificar eventos no dashboard de analytics
5. Testar em Chrome e Firefox

**Se checkpoint falhar:**
- Completar onboarding
- Padronizar design
- Configurar analytics corretamente

**Output esperado:**
- MVP completo com boa UX e rastreamento funcionando

---

### Checkpoint 3: Qualidade Final (Dia 9)

**Objetivo:** Validar que MVP completo esta pronto para lancamento.

**O que validar:**
- [ ] Checklist de qualidade 90%+ aprovado
- [ ] Testado em multiplos navegadores e dispositivos
- [ ] Performance < 2s para acoes principais
- [ ] Todos os criterios de aceite do Briefing atendidos
- [ ] Stakeholders validaram MVP completo
- [ ] Deploy de staging funcionando sem erros
- [ ] Sem bugs criticos

**Como validar:**
1. Executar checklist de qualidade completo
2. Testar em Chrome, Firefox, Safari, mobile iOS e Android
3. Medir performance com Chrome DevTools
4. Revisar criterios de aceite do Briefing
5. Apresentar para stakeholders e coletar feedback
6. Validar staging

**Se checkpoint falhar:**
- Corrigir gaps identificados
- Nao avancar para lancamento ate qualidade estar adequada

**Output esperado:**
- MVP completo, validado e pronto para pre-lancamento

---

## Recursos Uteis

### Ferramentas de Desenvolvimento

**Essenciais**
- Visual Studio Code: https://code.visualstudio.com
- Postman: https://www.postman.com
- Chrome DevTools: https://developer.chrome.com/docs/devtools

**Design e UX**
- Figma: https://www.figma.com (design e prototipos)
- Excalidraw: https://excalidraw.com (wireframes rapidos)
- Coolors: https://coolors.co (paletas de cores)

**Testes e Qualidade**
- Responsively App: https://responsively.app
- BrowserStack: https://www.browserstack.com
- Lighthouse: Chrome DevTools > Lighthouse tab

### Inspiracao de Design

**Dashboards**
- Stripe Dashboard: https://stripe.com
- Linear: https://linear.app
- Vercel Dashboard: https://vercel.com

**Onboarding**
- Notion: https://notion.so
- Figma: https://figma.com
- Loom: https://loom.com

**Landing Pages**
- Stripe: https://stripe.com
- Linear: https://linear.app
- Vercel: https://vercel.com

### Comunidades e Suporte

**Onde Buscar Ajuda**
- Stack Overflow: https://stackoverflow.com
- Next.js Discord: https://nextjs.org/discord
- Reddit /r/webdev: https://reddit.com/r/webdev
- Indie Hackers: https://indiehackers.com (feedback de founders)

---

## Glossario

**Analytics:** Coleta e analise de dados sobre uso do produto

**Onboarding:** Processo de guiar novos usuarios para primeiras acoes e valor

**Dashboard:** Painel com visao geral de metricas e informacoes importantes

**Empty State:** Estado visual quando usuario ainda nao tem dados

**In-App Notification:** Notificacao dentro da aplicacao (nao email)

**Transactional Email:** Email automatico sobre acao/evento (confirmacao, recibo)

**Soft Delete:** Marcar registro como deletado sem remover do banco

**Banner de Cookies:** Aviso sobre uso de cookies (compliance GDPR/LGPD)

**CTA (Call-to-Action):** Botao ou link que convida usuario a acao

**Metric:** Medida quantitativa de aspecto do produto (usuarios, receita, etc)

**Feature Flag:** Configuracao para habilitar/desabilitar features em producao

**Rollback:** Reverter deploy para versao anterior

---

## Checklist Rapido: Funcionalidades Secundarias Essenciais

- [ ] Dashboard com metricas principais
- [ ] Perfil de usuario editavel
- [ ] Upload de avatar funcionando
- [ ] Sistema de notificacoes (email ou in-app)
- [ ] Onboarding para novos usuarios
- [ ] Paginas institucionais (termos, privacidade)
- [ ] Landing page (se aplicavel)
- [ ] Analytics configurado e rastreando eventos
- [ ] Design consistente em todo MVP
- [ ] Responsivo em mobile e desktop
- [ ] Testado em multiplos navegadores
- [ ] Performance aceitavel (< 2s)
- [ ] Checklist de qualidade 90%+ aprovado

---

## Licoes Aprendidas (Template)

A medida que voce avanca no processo, documente licoes aprendidas aqui:

### O que funcionou bem:
- [Adicionar conforme processo avanca]

### O que pode melhorar:
- [Adicionar conforme processo avanca]

### Decisoes tecnicas importantes:
- [Documentar decisoes e razoes]

### Bloqueios encontrados e como foram resolvidos:
- [Documentar para referencia futura]

### Feedback de usuarios de teste:
- [Documentar feedback se houver testes com usuarios reais]

---

**Ultima atualizacao:** 2025-11-05
**Mantido por:** Framework Business Team
**Parte de:** Estrategia MVPBuilder (Etapa 5)
