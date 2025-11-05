# Checklist de Desenvolvimento - Qualidade de Código

Use este checklist antes de considerar desenvolvimento completo.

---

## 1. Código Frontend

### Componentes React

- [ ] Todos os componentes têm props tipadas com TypeScript
- [ ] Componentes estão organizados em pastas apropriadas (`components/ui/`, `components/feature/`)
- [ ] Componentes reutilizáveis separados de componentes específicos
- [ ] Componentes não têm mais de 300 linhas (considerar quebrar em sub-componentes)
- [ ] Lógica complexa extraída para hooks customizados quando apropriado
- [ ] Componentes são funcionais (não class components)
- [ ] Uso de hooks segue regras do React (não em condicionais ou loops)

### Estado e Efeitos

- [ ] Estado local usando `useState` quando apropriado
- [ ] Estado global apenas quando necessário (evitar over-engineering)
- [ ] `useEffect` tem array de dependências correto
- [ ] `useEffect` com cleanup quando necessário (timers, subscriptions)
- [ ] Não há loops infinitos em `useEffect`
- [ ] Estado derivado é calculado, não armazenado

### Formulários

- [ ] Formulários usam React Hook Form
- [ ] Validação implementada (required, min, max, pattern)
- [ ] Mensagens de erro são claras e úteis
- [ ] Estados de loading durante submit
- [ ] Prevenir múltiplos submits (botão desabilitado durante loading)
- [ ] Formulário reseta após sucesso (se apropriado)

### Performance Frontend

- [ ] Imagens otimizadas (usando `next/image` quando possível)
- [ ] Lazy loading para componentes pesados (se aplicável)
- [ ] Não há re-renders desnecessários (verificado com React DevTools)
- [ ] Funções passadas como props são memoizadas (useCallback) se causam re-renders
- [ ] Listas grandes usam key única e estável

---

## 2. Código Backend

### API Routes

- [ ] Todas as API routes estão em `app/api/` ou `pages/api/`
- [ ] Métodos HTTP usados corretamente (GET=leitura, POST=criação, PUT/PATCH=atualização, DELETE=deleção)
- [ ] Funções nomeadas pelos métodos HTTP exportadas (`export async function GET()`)
- [ ] API routes não têm mais de 100 linhas (considerar extrair lógica)
- [ ] Lógica de negócio complexa extraída para `lib/services/` ou funções separadas
- [ ] Respostas consistentes (sempre JSON, ou sempre Response)

### Validação de Dados

- [ ] Validação com Zod ou biblioteca similar
- [ ] Schemas de validação criados para todos os inputs
- [ ] Validação acontece ANTES de qualquer lógica de negócio
- [ ] Erros de validação retornam status 400 com mensagens claras
- [ ] Tipos TypeScript derivados de schemas Zod quando possível

### Autenticação e Autorização

- [ ] Sessão verificada em todas as rotas protegidas
- [ ] Não autenticado retorna 401
- [ ] Não autorizado (sem permissão) retorna 403
- [ ] Ownership verificado antes de permitir acesso/modificação
- [ ] Filtros por usuário em queries (`where: { userId: ... }`)

### Tratamento de Erros

- [ ] Try/catch em toda lógica assíncrona
- [ ] Erros logados adequadamente (console.error ou serviço de logging)
- [ ] Status codes HTTP corretos (200, 201, 400, 401, 403, 404, 500)
- [ ] Mensagens de erro não vazam informações sensíveis
- [ ] Diferentes tipos de erro tratados apropriadamente

### Prisma e Banco de Dados

- [ ] Schema Prisma está correto e atualizado
- [ ] Migrations criadas e executadas
- [ ] Relacionamentos definidos corretamente (`@relation`)
- [ ] Índices adicionados em campos filtrados (`@@index`)
- [ ] Queries usando `select` específico (não retornar campos desnecessários)
- [ ] `include` de relacionamentos limitado ao necessário
- [ ] Sem N+1 query problems
- [ ] Transações usadas quando múltiplas operações precisam ser atômicas

---

## 3. TypeScript

### Types e Interfaces

- [ ] Props de componentes tipadas
- [ ] Retorno de funções tipado
- [ ] Parâmetros de funções tipados
- [ ] Tipos compartilhados em `types/` ou `lib/types.ts`
- [ ] Uso mínimo de `any` (apenas quando absolutamente necessário)
- [ ] Uso de `unknown` ao invés de `any` quando possível
- [ ] Enums ou union types para valores fixos

### Build TypeScript

- [ ] `npm run build` ou `tsc` passa sem erros
- [ ] Sem erros de tipo no editor (VSCode)
- [ ] Warnings de tipo tratados (não ignorados com `@ts-ignore`)

---

## 4. Estilo e Formatação

### TailwindCSS

- [ ] Classes Tailwind consistentes
- [ ] Uso de design tokens (cores, espaçamentos da config)
- [ ] Não há CSS inline (style={{ }}) exceto casos específicos
- [ ] Classes condicionais usando libraries (clsx, cn) se necessário
- [ ] Responsividade usando breakpoints Tailwind (sm:, md:, lg:)

### Código Limpo

- [ ] Código formatado com Prettier
- [ ] Linting passa sem erros (ESLint)
- [ ] Não há código comentado (remover ou documentar razão)
- [ ] Não há console.log desnecessários (apenas logs úteis)
- [ ] Nomenclatura clara e descritiva
- [ ] Funções pequenas e focadas (< 50 linhas idealmente)
- [ ] Evitar duplicação (DRY - Don't Repeat Yourself)

---

## 5. Segurança

### Input e Output

- [ ] Inputs sanitizados (prevenir XSS)
- [ ] Outputs escapados quando necessário
- [ ] Validação no backend (nunca confiar apenas no frontend)
- [ ] SQL injection impossível (usando ORM - Prisma)

### Secrets e Credenciais

- [ ] Secrets em variáveis de ambiente (.env)
- [ ] `.env` no `.gitignore` (não commitado)
- [ ] Variáveis públicas do Next.js com prefixo `NEXT_PUBLIC_`
- [ ] API keys não expostas no frontend
- [ ] Tokens de sessão seguros (HttpOnly cookies)

### Dados Sensíveis

- [ ] Senhas hasheadas (se aplicável)
- [ ] Dados de pagamento não armazenados (apenas tokens)
- [ ] PII (Personally Identifiable Information) protegida
- [ ] Logs não incluem dados sensíveis

---

## 6. Performance

### Frontend

- [ ] Lighthouse score > 80 (Performance)
- [ ] First Contentful Paint < 2s
- [ ] Largest Contentful Paint < 3s
- [ ] Cumulative Layout Shift < 0.1
- [ ] Time to Interactive < 4s

### Backend

- [ ] APIs respondem em < 1s (90% das requests)
- [ ] Queries de banco < 500ms
- [ ] Índices em campos filtrados
- [ ] Sem queries desnecessárias (N+1 problems)

### Assets

- [ ] Imagens otimizadas e comprimidas
- [ ] Lazy loading de imagens abaixo da dobra
- [ ] Fonts otimizadas (subset, display: swap)
- [ ] Bundle JavaScript < 500KB (analisado com `@next/bundle-analyzer`)

---

## 7. Testes

### Testes Manuais

- [ ] Todos os fluxos principais testados
- [ ] Casos de erro testados
- [ ] Edge cases testados
- [ ] Testado em Chrome
- [ ] Testado em Firefox
- [ ] Testado em Safari (se macOS)
- [ ] Testado em mobile (iOS e/ou Android)

### Testes de API

- [ ] Endpoints testados com Postman/Insomnia
- [ ] Casos de sucesso funcionando
- [ ] Casos de erro retornando status corretos
- [ ] Coleção Postman criada e organizada

---

## 8. Acessibilidade (Básica)

### Semântica HTML

- [ ] Uso de tags semânticas (header, nav, main, article, etc)
- [ ] Headings em ordem (h1, h2, h3)
- [ ] Links têm texto descritivo (não "clique aqui")
- [ ] Botões são `<button>`, não `<div>` com onClick

### Formulários

- [ ] Labels associadas a inputs
- [ ] Inputs têm atributos apropriados (type, name, id)
- [ ] Mensagens de erro são anunciadas
- [ ] Campos obrigatórios marcados (required, aria-required)

### Navegação

- [ ] Navegação possível via teclado (tab, enter, space)
- [ ] Focus visível em elementos interativos
- [ ] Skip links (opcional mas recomendado)

### Contraste

- [ ] Contraste de texto adequado (WCAG AA: 4.5:1 para texto normal)
- [ ] Elementos interativos visualmente distinguíveis

---

## 9. Git e Versionamento

### Commits

- [ ] Commits pequenos e focados
- [ ] Mensagens de commit claras e descritivas
- [ ] Convenção de commits seguida (se houver, ex: Conventional Commits)
- [ ] Não há commits com "WIP" ou "temp" (ou foram squashed)

### Branches

- [ ] Branch principal limpa e funcional
- [ ] Features desenvolvidas em branches separadas (se aplicável)
- [ ] Merge/Pull requests revisados (se trabalho em equipe)

---

## 10. Documentação

### Código

- [ ] Componentes complexos têm comentários explicativos
- [ ] Funções complexas têm JSDoc ou comentários
- [ ] Decisões não-óbvias documentadas
- [ ] TODOs documentados com contexto (se houver)

### Projeto

- [ ] README.md atualizado
- [ ] Instruções de setup atualizadas
- [ ] Variáveis de ambiente documentadas (.env.example)
- [ ] Dependências listadas (package.json)

### API

- [ ] Endpoints documentados (comentários ou doc separada)
- [ ] Parâmetros e respostas descritos
- [ ] Coleção Postman com exemplos (opcional)

---

## 11. Deploy

### Pré-Deploy

- [ ] Build local passa sem erros (`npm run build`)
- [ ] Lint passa sem erros (`npm run lint`)
- [ ] TypeScript passa sem erros (`tsc --noEmit`)
- [ ] Variáveis de ambiente configuradas no ambiente de deploy
- [ ] Migrations de banco preparadas (se houver)

### Pós-Deploy

- [ ] Deploy completado com sucesso
- [ ] Aplicação acessível via URL de staging/produção
- [ ] Smoke test básico realizado
- [ ] Logs verificados (sem erros críticos)
- [ ] Monitoring configurado (opcional para MVP)

---

## 12. Code Review

### Self-Review

- [ ] Revisei todo o código que escrevi
- [ ] Removi código comentado ou debug
- [ ] Verifiquei que não há secrets commitados
- [ ] Testei localmente antes de push
- [ ] Build passa sem warnings críticos

### Peer Review (se aplicável)

- [ ] Pull request criado com descrição clara
- [ ] Reviewers conseguem entender mudanças
- [ ] Feedback de reviewers endereçado
- [ ] Aprovação de pelo menos 1 reviewer (se trabalho em equipe)

---

## Score de Qualidade

**Calculadora:** (Items marcados / Total de items aplicáveis) * 100

**Meta:** 90%+ para considerar desenvolvimento completo

**Seu score:** _____ %

**Items não aplicáveis (justificar):**
- [Item X não se aplica porque...]
- [Item Y não se aplica porque...]

---

## Notas Adicionais

[Espaço para notas sobre qualidade, decisões tomadas, débitos técnicos conhecidos]

---

**Última atualização:** 2025-11-05
**Versão:** 1.0
