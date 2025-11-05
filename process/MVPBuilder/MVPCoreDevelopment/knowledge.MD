# Knowledge Base - MVPCoreDevelopment

Este documento consolida conhecimentos, referências, FAQs e checkpoints para o processo de desenvolvimento da funcionalidade core do MVP.

---

## Materiais de Apoio

### Templates Compartilhados (Reutilizar)

- [Checklist de Qualidade](../../_SHARED/templates/checklist-qualidade.MD) - Checklist padrão para validação de entregáveis digitais
- [Retrospectiva](../../_SHARED/templates/retrospectiva.MD) - Template para retrospectivas de sprint/ciclo

### Templates Locais (Específicos deste Processo)

- [Template de Especificação Técnica](_DATA/template-feature-spec.md) - Para documentar especificação técnica de funcionalidades
- [Checklist de Desenvolvimento](_DATA/checklist-desenvolvimento.md) - Checklist de qualidade de código
- [Template de Relatório de Progresso](_DATA/template-relatorio-progresso.md) - Para acompanhamento diário/semanal de desenvolvimento

### Processos Relacionados

- [MVPScopeDefinition](../MVPScopeDefinition/process.MD) - Processo que define o escopo do MVP (entrada)
- [MVPIssuesMapping](../MVPIssuesMapping/process.MD) - Processo que mapeia issues técnicas (entrada)
- [MVPInfrastructureSetup](../MVPInfrastructureSetup/process.MD) - Processo que configura infraestrutura (entrada)

---

## Documentação Técnica de Referência

### Framework e Bibliotecas Core

**Next.js**
- Documentação oficial: https://nextjs.org/docs
- App Router: https://nextjs.org/docs/app
- API Routes: https://nextjs.org/docs/app/building-your-application/routing/route-handlers
- Data Fetching: https://nextjs.org/docs/app/building-your-application/data-fetching

**React**
- Documentação oficial: https://react.dev
- Hooks: https://react.dev/reference/react/hooks
- useState: https://react.dev/reference/react/useState
- useEffect: https://react.dev/reference/react/useEffect

**TypeScript**
- Documentação oficial: https://www.typescriptlang.org/docs/
- TypeScript com React: https://react-typescript-cheatsheet.netlify.app/

### Banco de Dados e ORM

**Prisma**
- Documentação oficial: https://www.prisma.io/docs
- Schema: https://www.prisma.io/docs/concepts/components/prisma-schema
- Migrations: https://www.prisma.io/docs/concepts/components/prisma-migrate
- Prisma Client: https://www.prisma.io/docs/concepts/components/prisma-client
- Relações: https://www.prisma.io/docs/concepts/components/prisma-schema/relations

**PostgreSQL**
- Documentação oficial: https://www.postgresql.org/docs/

### Autenticação

**NextAuth.js**
- Documentação oficial: https://next-auth.js.org
- Getting Started: https://next-auth.js.org/getting-started/introduction
- Providers: https://next-auth.js.org/configuration/providers
- Session: https://next-auth.js.org/getting-started/client#usesession

### Pagamento

**Stripe**
- Documentação oficial: https://stripe.com/docs
- Checkout: https://stripe.com/docs/payments/checkout
- Webhooks: https://stripe.com/docs/webhooks
- Testing: https://stripe.com/docs/testing

### Frontend e UI

**TailwindCSS**
- Documentação oficial: https://tailwindcss.com/docs
- Customização: https://tailwindcss.com/docs/theme
- Responsive Design: https://tailwindcss.com/docs/responsive-design

**React Hook Form**
- Documentação oficial: https://react-hook-form.com
- Get Started: https://react-hook-form.com/get-started
- API: https://react-hook-form.com/api

**Zod**
- Documentação oficial: https://zod.dev
- Schema Validation: https://zod.dev/?id=basic-usage

### Data Fetching

**SWR**
- Documentação oficial: https://swr.vercel.app
- Getting Started: https://swr.vercel.app/docs/getting-started

**React Query (TanStack Query)**
- Documentação oficial: https://tanstack.com/query/latest
- Quick Start: https://tanstack.com/query/latest/docs/react/quick-start

### Deploy e Infraestrutura

**Vercel**
- Documentação oficial: https://vercel.com/docs
- Deployment: https://vercel.com/docs/deployments/overview
- Environment Variables: https://vercel.com/docs/projects/environment-variables

---

## Best Practices

### Estrutura de Código

**Organização de Pastas (Next.js App Router)**
```
src/
├── app/
│   ├── (auth)/          # Rotas de autenticação
│   ├── (dashboard)/     # Rotas protegidas
│   ├── api/             # API routes
│   └── layout.tsx       # Layout root
├── components/
│   ├── ui/              # Componentes base (Button, Card, etc)
│   └── feature/         # Componentes específicos da feature
├── lib/
│   ├── api.ts           # Cliente de API
│   ├── auth.ts          # Helpers de autenticação
│   └── utils.ts         # Funções utilitárias
└── types/
    └── index.ts         # Types TypeScript compartilhados
```

**Nomenclatura**
- Componentes: PascalCase (ex: `UserProfile.tsx`)
- Funções e variáveis: camelCase (ex: `getUserData`)
- Arquivos de API: kebab-case (ex: `user-profile.ts`)
- Constantes: UPPER_SNAKE_CASE (ex: `MAX_FILE_SIZE`)

### Performance

**Otimizações Essenciais**
1. Usar `select` específico em queries Prisma (não retornar campos desnecessários)
2. Limitar `include` de relacionamentos ao mínimo necessário
3. Adicionar índices no Prisma schema para campos filtrados frequentemente
4. Usar `loading="lazy"` em imagens abaixo da dobra
5. Implementar debounce em inputs de busca

**Quando Otimizar**
- Otimize queries que levam > 500ms
- Otimize componentes que causam re-renders excessivos
- Otimize bundles JavaScript > 500KB
- Não otimize prematuramente (medir primeiro, otimizar depois)

### Segurança

**Checklist de Segurança Essencial**
- [ ] Validação de dados no backend (nunca confiar apenas no frontend)
- [ ] Autenticação em todas as rotas protegidas
- [ ] Autorização verificando ownership de recursos
- [ ] Sanitização de inputs para prevenir XSS
- [ ] Rate limiting em endpoints críticos (opcional para MVP)
- [ ] HTTPS em produção (Vercel faz automaticamente)
- [ ] Variáveis de ambiente para secrets (nunca commitar secrets)
- [ ] CORS configurado adequadamente

**Validação de Dados**
```typescript
// Exemplo com Zod
import { z } from 'zod';

const createItemSchema = z.object({
  name: z.string().min(1).max(100),
  description: z.string().max(500).optional(),
  price: z.number().positive(),
});

// Uso em API route
export async function POST(req: Request) {
  const body = await req.json();
  const validated = createItemSchema.parse(body); // Throws se inválido
  // ...
}
```

**Autorização**
```typescript
// Exemplo: Verificar se usuário pode acessar recurso
const item = await prisma.item.findUnique({
  where: { id: itemId }
});

if (item.userId !== session.user.id) {
  return new Response('Forbidden', { status: 403 });
}
```

### Tratamento de Erros

**Padrão de Try/Catch**
```typescript
export async function POST(req: Request) {
  try {
    const session = await getServerSession();
    if (!session) {
      return new Response('Unauthorized', { status: 401 });
    }

    const body = await req.json();
    const validated = schema.parse(body);

    const result = await prisma.item.create({
      data: { ...validated, userId: session.user.id }
    });

    return Response.json(result, { status: 201 });
  } catch (error) {
    console.error('Error creating item:', error);

    if (error instanceof z.ZodError) {
      return Response.json({ error: error.errors }, { status: 400 });
    }

    return new Response('Internal Server Error', { status: 500 });
  }
}
```

**Frontend**
```typescript
async function handleSubmit(data) {
  setIsLoading(true);
  setError(null);

  try {
    const response = await fetch('/api/items', {
      method: 'POST',
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Something went wrong');
    }

    const result = await response.json();
    toast.success('Item created successfully!');
    return result;
  } catch (error) {
    setError(error.message);
    toast.error(error.message);
  } finally {
    setIsLoading(false);
  }
}
```

---

## FAQs

### Planejamento e Escopo

**P: Como sei se uma funcionalidade é "core" ou "secundária"?**
R: A funcionalidade core é aquela que demonstra a proposta de valor principal do MVP, definida no Briefing de MVP. Se remover a funcionalidade e o MVP perde sua razão de existir, ela é core. Funcionalidades secundárias melhoram a experiência mas não são essenciais para validar a hipótese.

**P: E se eu identificar uma funcionalidade importante que não está no Briefing?**
R: Documente no backlog mas não implemente agora. O foco é entregar a funcionalidade core definida. Novas funcionalidades podem ser avaliadas após conclusão do MVP ou em iterações futuras.

**P: Quanto tempo devo gastar em design visual?**
R: Para MVP, priorize funcionalidade sobre beleza. Use componentes base já criados, mantenha design simples e consistente. Gaste ~20% do tempo em visual, 80% em funcionalidade. Refinamento visual pode vir depois.

### Desenvolvimento Frontend

**P: Devo usar App Router ou Pages Router no Next.js?**
R: Se o projeto já está configurado, use o que está configurado (provavelmente definido em MVPInfrastructureSetup). Se está começando novo, use App Router (é o padrão atual do Next.js).

**P: Como proteger uma rota com autenticação?**
R: No App Router, use middleware ou verifique sessão no componente de página. No Pages Router, use `getServerSideProps` com `getServerSession`. Consulte documentação do NextAuth.js para padrões específicos.

**P: Devo criar testes automatizados para componentes?**
R: Para MVP, testes manuais são suficientes. Testes automatizados são valiosos mas consomem tempo. Priorize testes manuais abrangentes agora, adicione testes automatizados depois se necessário.

**P: Como lidar com imagens e assets?**
R: Use a pasta `public/` do Next.js. Para imagens, use o componente `next/image` que otimiza automaticamente. Para upload de imagens de usuários, considere serviços como Cloudinary ou Uploadthing.

### Desenvolvimento Backend

**P: Como estruturar API routes no Next.js App Router?**
R: Crie arquivo `route.ts` dentro de `app/api/[nome]/`. Export funções nomeadas pelos métodos HTTP: `GET`, `POST`, `PUT`, `DELETE`. Exemplo: `app/api/items/route.ts` com `export async function GET()`.

**P: Devo usar Prisma direto nas API routes ou criar camada de service?**
R: Para MVP, usar Prisma direto nas routes é OK e mais rápido. Se lógica de negócio fica complexa (> 30 linhas), extraia para função separada em `lib/services/`. Não sobre-engenheirar.

**P: Como fazer paginação com Prisma?**
R: Use `skip` e `take`:
```typescript
const items = await prisma.item.findMany({
  skip: (page - 1) * pageSize,
  take: pageSize,
});
```

**P: Como fazer soft delete?**
R: Adicione campo `deletedAt: DateTime?` no schema Prisma. Ao deletar, faça `update` setando `deletedAt: new Date()`. Em queries, filtre `where: { deletedAt: null }`.

### Integração e Testes

**P: Como testar endpoints que precisam autenticação no Postman?**
R: Crie um endpoint temporário de login que retorna um token ou cookie de sessão. Use esse token nos headers das outras requisições. Ou use o Prisma Studio para criar uma sessão manual.

**P: Stripe está falhando em localhost, o que fazer?**
R: Webhooks do Stripe não chegam em localhost. Use Stripe CLI para forward webhooks: `stripe listen --forward-to localhost:3000/api/webhooks/stripe`. Use test mode e test cards da documentação Stripe.

**P: Como debugar erro "Cannot read property X of undefined"?**
R: Adicione console.logs antes da linha do erro para ver o valor da variável. Use Chrome DevTools para adicionar breakpoints. Verifique que dados estão vindo do backend no formato esperado.

**P: Performance está ruim, por onde começar?**
R: 1) Use Chrome DevTools Network tab para identificar requests lentos. 2) Otimize queries Prisma lentas (adicione índices, use select específico). 3) Adicione loading states para ações lentas inevitáveis.

### Deploy e Produção

**P: Como executar migrations no banco de produção?**
R: Nunca rode `prisma migrate dev` em produção. Use `prisma migrate deploy` que só executa migrations pendentes sem criar novas. Configure no seu CI/CD ou rode manualmente antes do deploy.

**P: Variáveis de ambiente não funcionam no Vercel, o que fazer?**
R: Configure variáveis de ambiente no Dashboard da Vercel (Settings → Environment Variables). Para Next.js, variáveis públicas precisam prefixo `NEXT_PUBLIC_`. Re-deploy após adicionar variáveis.

**P: Como reverter um deploy ruim?**
R: Na Vercel, vá em Deployments, encontre o deploy anterior que estava funcionando, e clique em "Promote to Production". Isso faz rollback instantâneo.

---

## Checkpoints

### Checkpoint 1: Frontend Funcional Visualmente (Dia 5)

**Objetivo:** Validar que frontend está completo visualmente antes de integrar com backend.

**O que validar:**
- [ ] Todas as páginas da funcionalidade core criadas e acessíveis
- [ ] Todos os componentes renderizando corretamente
- [ ] Formulários com validação funcionando (mesmo sem enviar para API)
- [ ] Estados de loading e erro visualmente implementados
- [ ] Responsividade funcionando em mobile e desktop
- [ ] Design consistente e profissional
- [ ] Navegação entre telas fluida

**Como validar:**
1. Abrir cada página da funcionalidade no navegador
2. Testar responsividade (Chrome DevTools device toolbar)
3. Preencher e submitar formulários (pode apenas console.log por enquanto)
4. Verificar que não há erros no console
5. Fazer walkthrough de todo o fluxo visual

**Se checkpoint falhar:**
- Identificar o que está faltando
- Priorizar completar visual básico antes de avançar
- Não precisa ser perfeito, mas precisa estar completo

**Output esperado:**
- Frontend visualmente completo e pronto para integração com backend

---

### Checkpoint 2: Backend com Endpoints Testados (Dia 10)

**Objetivo:** Validar que backend está funcional e testado antes de integrar com frontend.

**O que validar:**
- [ ] Schema Prisma atualizado e migrations executadas
- [ ] Todos os endpoints de API implementados
- [ ] Validação de dados com Zod funcionando
- [ ] Autenticação e autorização implementadas
- [ ] Tratamento de erros consistente
- [ ] Todos os endpoints testados manualmente com Postman
- [ ] Dados persistindo corretamente no banco (verificado no Prisma Studio)
- [ ] Queries Prisma otimizadas (usando select específico)

**Como validar:**
1. Abrir coleção Postman com todos os endpoints
2. Testar cada endpoint (GET, POST, PUT, DELETE)
3. Testar com dados válidos e inválidos
4. Verificar dados no Prisma Studio após criação/atualização
5. Verificar logs de erro (console do servidor)

**Se checkpoint falhar:**
- Identificar endpoints que não estão funcionando
- Corrigir antes de avançar para integração
- Backend precisa estar 100% funcional isoladamente

**Output esperado:**
- Backend completamente funcional e testado
- Pronto para integração com frontend

---

### Checkpoint 3: Integração Completa (Dia 13)

**Objetivo:** Validar que frontend e backend estão integrados e funcionando end-to-end.

**O que validar:**
- [ ] Frontend e backend integrados
- [ ] Fluxo completo end-to-end funcionando (do clique no botão até dados no banco)
- [ ] Estados de loading aparecendo durante requests
- [ ] Erros da API sendo tratados e mostrados ao usuário
- [ ] Integração com Stripe funcionando (se aplicável)
- [ ] Dados atualizando corretamente na UI após ações
- [ ] Funcionalidade testada em múltiplos navegadores (Chrome, Firefox, Safari)
- [ ] Funcionalidade testada em mobile (iOS e/ou Android)
- [ ] Checklist de qualidade 80%+ aprovado

**Como validar:**
1. Percorrer fluxo completo da funcionalidade como usuário real
2. Criar, ler, atualizar e deletar recursos
3. Verificar dados no Prisma Studio após cada ação
4. Testar em diferentes navegadores
5. Testar em dispositivo mobile real
6. Executar checklist de qualidade parcial

**Se checkpoint falhar:**
- Identificar onde integração está quebrando
- Debugar usando Chrome DevTools (Network tab, Console)
- Corrigir antes de considerar desenvolvimento completo

**Output esperado:**
- Funcionalidade core 100% funcional end-to-end
- Pronta para testes finais e validação com stakeholders

---

## Recursos Úteis

### Ferramentas de Desenvolvimento

**Essenciais**
- Visual Studio Code: https://code.visualstudio.com/
- Postman: https://www.postman.com/
- Chrome DevTools: https://developer.chrome.com/docs/devtools/

**Extensões VSCode Recomendadas**
- ESLint (dbaeumer.vscode-eslint)
- Prettier (esbenp.prettier-vscode)
- Tailwind CSS IntelliSense (bradlc.vscode-tailwindcss)
- Prisma (Prisma.prisma)
- Error Lens (usernamehw.errorlens)

**Ferramentas de Teste**
- Responsively App: https://responsively.app/ (teste multi-device)
- BrowserStack: https://www.browserstack.com/ (teste cross-browser)
- Lighthouse: https://developers.google.com/web/tools/lighthouse (performance)

### Templates e Boilerplates

**Starters Úteis**
- Create Next App: `npx create-next-app@latest`
- Next.js + Prisma: https://github.com/prisma/prisma-examples/tree/latest/typescript/rest-nextjs-api-routes
- Next.js + NextAuth: https://next-auth.js.org/getting-started/example

### Comunidades e Suporte

**Onde Buscar Ajuda**
- Stack Overflow: https://stackoverflow.com/
- Next.js Discord: https://nextjs.org/discord
- Prisma Discord: https://pris.ly/discord
- Reddit /r/nextjs: https://www.reddit.com/r/nextjs/
- Reddit /r/reactjs: https://www.reddit.com/r/reactjs/

**Como Fazer Boas Perguntas**
1. Descreva o que você está tentando fazer
2. Mostre o código relevante (mínimo necessário)
3. Descreva o que você esperava que acontecesse
4. Descreva o que realmente aconteceu (erro, comportamento inesperado)
5. Mencione o que você já tentou

---

## Glossário

**API Route:** Endpoint de backend no Next.js (arquivo em `app/api/` ou `pages/api/`)

**Component:** Função React que retorna JSX e pode ser reutilizada

**Edge Case:** Cenário incomum ou extremo que pode causar bugs (ex: input vazio, número negativo)

**End-to-End (E2E):** Teste do fluxo completo do início ao fim (do frontend ao banco de dados)

**Hook:** Função React que começa com "use" e permite usar state e outros recursos (ex: useState, useEffect)

**Migration:** Arquivo que descreve mudanças no schema do banco de dados

**ORM:** Object-Relational Mapping - biblioteca que abstrai operações de banco (ex: Prisma)

**Props:** Parâmetros passados para componentes React

**Schema:** Estrutura do banco de dados definida em Prisma (models, campos, relações)

**Seed:** Popular banco de dados com dados iniciais para desenvolvimento

**Server Component:** Componente React que roda no servidor (padrão no Next.js App Router)

**Client Component:** Componente React que roda no navegador (precisa de "use client" no App Router)

**Soft Delete:** Marcar registro como deletado sem removê-lo fisicamente do banco

**State:** Dados que mudam ao longo do tempo em um componente React

**Toast:** Notificação temporária que aparece na tela (ex: "Item criado com sucesso!")

**Validation:** Verificação de que dados estão no formato correto

**Webhook:** Endpoint que recebe notificações de serviços externos (ex: Stripe)

---

## Lições Aprendidas (Template)

À medida que você avança no processo, documente lições aprendidas aqui:

### O que funcionou bem:
- [Adicionar conforme processo avança]

### O que pode melhorar:
- [Adicionar conforme processo avança]

### Decisões técnicas importantes:
- [Documentar decisões e razões]

### Bloqueios encontrados e como foram resolvidos:
- [Documentar para referência futura]

---

**Última atualização:** 2025-11-05
**Mantido por:** Framework Business Team
**Parte de:** Estratégia MVPBuilder (Etapa 4)
