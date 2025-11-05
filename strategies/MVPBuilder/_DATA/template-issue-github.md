# Template de Issue GitHub - MVP Builder

Use este template ao criar issues no GitHub/GitLab para o desenvolvimento do MVP.

---

## Template Basico

```markdown
## Descricao

[Descreva claramente o que precisa ser feito. Seja especifico e objetivo.]

## Contexto

[Explique por que essa issue existe. Como se relaciona com outras funcionalidades?]

## Criterios de Aceite

- [ ] [Criterio 1 - deve ser testavel e mensuravel]
- [ ] [Criterio 2]
- [ ] [Criterio 3]
- [ ] [Criterio 4]

## Tarefas Tecnicas

- [ ] [Tarefa especifica 1]
- [ ] [Tarefa especifica 2]
- [ ] [Tarefa especifica 3]

## Definicao de Done

- [ ] Codigo desenvolvido e funcional
- [ ] Testado manualmente (casos principais)
- [ ] Code review realizado (se trabalho em equipe)
- [ ] Documentacao atualizada (se aplicavel)
- [ ] Deploy realizado e validado
- [ ] Issue movida para "Done" no board

## Dependencias

- Depende de: #[numero da issue]
- Bloqueia: #[numero da issue]

## Estimativa de Tempo

[X horas] ou [X pontos]

## Observacoes

[Qualquer informacao adicional relevante]
```

---

## Exemplos de Issues

### Exemplo 1: Feature Frontend

```markdown
## Descricao

Criar pagina de listagem de projetos com filtros por categoria e valor.

## Contexto

Essa e a interface principal da funcionalidade core do MVP. Usuarios precisam visualizar projetos curados e filtrar conforme suas preferencias.

## Criterios de Aceite

- [ ] Pagina renderiza lista de projetos com: titulo, descricao curta, valor, categoria
- [ ] Usuario pode filtrar por categoria (dropdown)
- [ ] Usuario pode filtrar por valor minimo (slider ou input)
- [ ] Filtros atualizam lista em tempo real
- [ ] Pagina e responsiva (funciona em mobile)
- [ ] Loading state exibido enquanto carrega dados
- [ ] Mensagem de erro amigavel se API falhar
- [ ] Empty state exibido se nenhum projeto corresponder aos filtros

## Tarefas Tecnicas

- [ ] Criar rota `/app/projects/page.tsx`
- [ ] Criar componente `ProjectCard` reutilizavel
- [ ] Criar componente `ProjectFilters` com dropdown e slider
- [ ] Implementar fetch de dados da API `/api/projects`
- [ ] Adicionar estados de loading e erro
- [ ] Implementar logica de filtragem no frontend
- [ ] Garantir responsividade com TailwindCSS
- [ ] Adicionar empty state

## Definicao de Done

- [ ] Codigo desenvolvido e funcional
- [ ] Testado em Chrome, Safari, Firefox
- [ ] Testado em mobile (iOS e Android)
- [ ] Code review aprovado
- [ ] Deploy realizado e validado em preview
- [ ] Issue movida para "Done"

## Dependencias

- Depende de: #12 (API de listagem de projetos)
- Depende de: #8 (Componentes base: Button, Card)

## Estimativa de Tempo

8 horas

## Observacoes

- Usar React Hook Form para filtros se necessario validacao
- Considerar usar SWR ou React Query para cache de dados
- Design reference: [link para Figma/wireframe se houver]
```

---

### Exemplo 2: Feature Backend (API)

```markdown
## Descricao

Criar endpoint GET `/api/projects` que retorna lista paginada de projetos com suporte a filtros.

## Contexto

Esse endpoint alimenta a pagina de listagem de projetos (frontend). Deve retornar apenas projetos aprovados e respeitar filtros de categoria e valor.

## Criterios de Aceite

- [ ] Endpoint GET `/api/projects` criado
- [ ] Retorna JSON com array de projetos
- [ ] Suporta paginacao (parametros: page, limit)
- [ ] Suporta filtro por categoria (parametro: category)
- [ ] Suporta filtro por valor minimo (parametro: minValue)
- [ ] Retorna apenas projetos com status "approved"
- [ ] Retorna status 200 para sucesso
- [ ] Retorna status 500 para erro interno
- [ ] Tempo de resposta < 500ms para 100 projetos
- [ ] Testado com Postman/Insomnia

## Tarefas Tecnicas

- [ ] Criar arquivo `/app/api/projects/route.ts`
- [ ] Implementar funcao GET handler
- [ ] Adicionar validacao de query params (Zod)
- [ ] Implementar query do Prisma com filtros
- [ ] Implementar paginacao (skip/take)
- [ ] Adicionar error handling
- [ ] Testar casos: sucesso, filtros, paginacao, erro
- [ ] Documentar endpoint (comentarios ou README)

## Definicao de Done

- [ ] Codigo desenvolvido e funcional
- [ ] Todos os criterios de aceite atendidos
- [ ] Testado com Postman (casos: sucesso, filtros, erro)
- [ ] Tempo de resposta validado (< 500ms)
- [ ] Code review aprovado
- [ ] Deploy realizado e endpoint funcionando em preview

## Dependencias

- Depende de: #5 (Schema Prisma com model Project)
- Depende de: #3 (Configuracao banco de dados)

## Estimativa de Tempo

4 horas

## Observacoes

- Usar Zod para validacao: `z.object({ page: z.string().optional(), ... })`
- Considerar adicionar cache basico (Next.js revalidate) se performance for critica
- Formato de resposta:
  ```json
  {
    "projects": [...],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 150
    }
  }
  ```
```

---

### Exemplo 3: Setup/Infraestrutura

```markdown
## Descricao

Configurar NextAuth.js com autenticacao via email/senha (Credentials provider).

## Contexto

Autenticacao e pre-requisito para todas as funcionalidades protegidas do MVP. Usuarios devem poder se cadastrar, fazer login e manter sessao ativa.

## Criterios de Aceite

- [ ] NextAuth instalado e configurado
- [ ] Rota `/api/auth/[...nextauth]/route.ts` criada
- [ ] Credentials provider configurado (email/senha)
- [ ] Prisma Adapter integrado
- [ ] Schema Prisma atualizado com modelos NextAuth (User, Account, Session, VerificationToken)
- [ ] Migration executada com sucesso
- [ ] Usuario consegue fazer login via `/api/auth/signin`
- [ ] Sessao persiste entre reloads (cookie)
- [ ] Logout funciona via `/api/auth/signout`
- [ ] Middleware de protecao de rotas funcional

## Tarefas Tecnicas

- [ ] Instalar NextAuth: `npm install next-auth @next-auth/prisma-adapter`
- [ ] Criar `/app/api/auth/[...nextauth]/route.ts`
- [ ] Configurar Credentials provider com validacao de email/senha
- [ ] Atualizar `prisma/schema.prisma` com modelos NextAuth
- [ ] Rodar migration: `npx prisma migrate dev --name add-nextauth`
- [ ] Configurar variaveis de ambiente: NEXTAUTH_SECRET, NEXTAUTH_URL
- [ ] Criar middleware.ts para proteger rotas
- [ ] Testar fluxo: cadastro → login → acesso a rota protegida → logout
- [ ] Adicionar hash de senha com bcrypt

## Definicao de Done

- [ ] NextAuth completamente configurado
- [ ] Todos os criterios de aceite validados
- [ ] Testado fluxo completo localmente
- [ ] Testado em deploy preview
- [ ] Documentacao de setup adicionada ao README
- [ ] Variaveis de ambiente configuradas no Vercel

## Dependencias

- Depende de: #3 (Configuracao Prisma + PostgreSQL)

## Estimativa de Tempo

6 horas

## Observacoes

- Seguir documentacao oficial: https://next-auth.js.org/
- Usar `bcrypt` para hash de senhas: `npm install bcrypt @types/bcrypt`
- Gerar NEXTAUTH_SECRET: `openssl rand -base64 32`
- Exemplo de protecao de rota:
  ```typescript
  import { getServerSession } from "next-auth"

  export default async function ProtectedPage() {
    const session = await getServerSession()
    if (!session) redirect("/api/auth/signin")
    // ...
  }
  ```
```

---

### Exemplo 4: Bug

```markdown
## Descricao

Formulario de cadastro nao valida email duplicado e retorna erro 500.

## Contexto

Bug reportado por usuario de teste. Ao tentar cadastrar com email ja existente, aplicacao quebra com erro 500 ao inves de mostrar mensagem amigavel.

## Comportamento Esperado

- Usuario tenta cadastrar com email ja cadastrado
- Sistema valida email duplicado
- Retorna erro 400 com mensagem: "Email ja cadastrado. Faca login ou use outro email."
- Nao salva nada no banco

## Comportamento Atual

- Usuario tenta cadastrar com email ja cadastrado
- Sistema tenta inserir no banco
- Prisma retorna erro de unique constraint
- Sistema retorna erro 500
- Frontend mostra mensagem generica de erro

## Passos para Reproduzir

1. Cadastrar usuario com email `teste@example.com`
2. Fazer logout
3. Tentar cadastrar novamente com mesmo email
4. Ver erro 500

## Criterios de Aceite

- [ ] Validacao de email duplicado implementada antes de insert
- [ ] Retorna status 400 (Bad Request) para email duplicado
- [ ] Mensagem de erro amigavel exibida no frontend
- [ ] Testado fluxo completo (cadastro duplicado)

## Tarefas Tecnicas

- [ ] Adicionar validacao no endpoint `/api/auth/signup`:
  ```typescript
  const existingUser = await prisma.user.findUnique({ where: { email } })
  if (existingUser) return res.status(400).json({ error: "Email ja cadastrado" })
  ```
- [ ] Atualizar frontend para exibir mensagem de erro especifica
- [ ] Adicionar test case para email duplicado

## Definicao de Done

- [ ] Bug corrigido
- [ ] Testado localmente
- [ ] Testado em preview deploy
- [ ] Validacao funcionando corretamente
- [ ] Code review aprovado

## Labels

bug, P0 (critico), auth

## Estimativa de Tempo

1 hora

## Observacoes

- Considerar adicionar validacao tambem no frontend (melhor UX)
```

---

## Labels Recomendadas

Crie as seguintes labels no GitHub:

**Por tipo**:
- `feature` - Nova funcionalidade
- `bug` - Correcao de bug
- `setup` - Configuracao de infraestrutura
- `docs` - Documentacao
- `refactor` - Refatoracao de codigo
- `test` - Testes

**Por area**:
- `frontend` - Interface/UI
- `backend` - API/servidor
- `database` - Banco de dados
- `auth` - Autenticacao
- `payment` - Sistema de pagamento
- `devops` - Deploy/CI/CD

**Por prioridade**:
- `P0` - Critico (bloqueia lancamento)
- `P1` - Alto (importante para MVP)
- `P2` - Medio (desejavel mas nao bloqueante)
- `P3` - Baixo (pode ser pos-lancamento)

**Por status**:
- `blocked` - Bloqueada por outra issue
- `in-progress` - Em desenvolvimento
- `ready-for-review` - Pronta para code review
- `needs-testing` - Precisa de testes

---

## Boas Praticas ao Criar Issues

1. **Titulo claro e descritivo**
   - Bom: "Criar pagina de listagem de projetos com filtros"
   - Ruim: "Pagina de projetos"

2. **Criterios de aceite testaveis**
   - Bom: "Usuario consegue filtrar por categoria e lista atualiza"
   - Ruim: "Filtros funcionam"

3. **Estimativas realistas**
   - Adicione 20-30% de buffer em estimativas
   - Issues > 8h considere quebrar em issues menores

4. **Dependencias explicitas**
   - Sempre linke issues relacionadas com `#numero`
   - Deixa claro ordem de desenvolvimento

5. **Adicione screenshots/wireframes**
   - Se houver design, anexe imagem ou link Figma
   - Facilita entendimento

6. **Atualize a issue conforme progride**
   - Marque checklist conforme completa
   - Comente blockers ou mudancas

7. **Use templates consistentes**
   - Mantenha mesmo formato em todas as issues
   - Facilita leitura e revisao

---

**Criado em**: 2025-11-05
**Versao**: 1.0
**Parte de**: Estrategia MVP Builder
