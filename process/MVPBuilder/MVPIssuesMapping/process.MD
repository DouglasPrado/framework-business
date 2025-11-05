# Processo de Mapeamento de Issues para MVP

## Propósito

Este processo guia a transformação do Briefing de MVP (escopo de produto) em backlog técnico estruturado de issues de desenvolvimento. O objetivo é criar issues detalhadas que podem ser executadas pelo time técnico, com dependências mapeadas, prioridades definidas e timeline realista.

## Objetivo

Criar backlog técnico completo incluindo:
- Repositório Git configurado com projeto Next.js inicializado
- Issues detalhadas para todas as funcionalidades (core e secundárias)
- Issues de setup técnico (banco, autenticação, pagamento, deploy)
- Priorização e estimativa de todas as issues
- Milestones definidos (Setup, Core, Secundário, Launch)
- Board kanban configurado para gestão de projeto
- Timeline técnica validada (6-8 semanas)

O resultado deve permitir que o time técnico comece desenvolvimento imediatamente seguindo as issues criadas.

## Escopo

### Dentro do escopo
- Criação de repositório Git e estrutura inicial do projeto Next.js
- Mapeamento de funcionalidades em issues técnicas específicas
- Criação de issues de infraestrutura (Prisma, NextAuth, Stripe, deploy)
- Definição de critérios de aceite para cada issue
- Estimativa de tempo realista por issue
- Priorização por dependência e valor
- Criação de milestones alinhados com etapas de desenvolvimento
- Configuração de board kanban para acompanhamento
- Validação de timeline total (deve estar em 6-8 semanas)

### Fora do escopo
- Desenvolvimento ou escrita de código (apenas setup inicial)
- Design de interfaces ou criação de wireframes
- Definição de arquitetura complexa ou decisões técnicas profundas
- Execução das issues criadas (processo separado)
- Refinamento contínuo durante desenvolvimento

## Etapas do Processo

### Etapa 1: Setup de Repositório e Projeto Inicial (0.5 dia)

Criar repositório Git, inicializar projeto Next.js com TypeScript e configurar estrutura básica.

**Execução:**
1. Criar repositório no GitHub/GitLab com nome do projeto
2. Configurar acesso para time completo
3. Inicializar projeto Next.js: \`npx create-next-app@latest --typescript\`
4. Criar estrutura de pastas padrão
5. Configurar ESLint e Prettier
6. Criar README.md com instruções de setup local
7. Fazer commit inicial e push

**Resultado esperado:**
Repositório configurado, projeto Next.js rodando localmente, estrutura de pastas criada e README documentado.

**Tempo estimado:** 0.5 dia (4 horas)

---

### Etapa 2: Mapeamento de Funcionalidades em Issues (1.5 dias)

Transformar cada funcionalidade do Briefing de MVP em issues técnicas detalhadas.

**Execução:**
1. Revisar Briefing de MVP e Template de Funcionalidades
2. Para funcionalidade principal, criar 3-5 issues técnicas
3. Para cada funcionalidade secundária, criar 2-3 issues
4. Usar Template de Issue para cada uma
5. Adicionar labels apropriadas

**Resultado esperado:**
Mínimo 10-15 issues de funcionalidades criadas seguindo template padrão.

**Tempo estimado:** 1.5 dias (12 horas)

---

### Etapa 3: Criação de Issues de Setup Técnico (0.5 dia)

Criar issues para tarefas de infraestrutura essenciais.

**Execução:**
1. Criar issue: Setup Prisma + PostgreSQL
2. Criar issue: Implementar NextAuth.js
3. Criar issue: Integrar Stripe em modo teste
4. Criar issue: Configurar deploy Vercel
5. Criar issue: Componentes base
6. Marcar todas como P0

**Resultado esperado:**
7-8 issues de setup técnico criadas, todas marcadas como P0.

**Tempo estimado:** 0.5 dia (4 horas)

---

### Etapa 4: Priorização e Estimativa (1 dia)

Ordenar issues por dependência e valor, estimar tempo e validar timeline.

**Execução:**
1. Classificar issues em P0, P1, P2, P3
2. Mapear dependências
3. Estimar cada issue em horas
4. Calcular timeline total
5. Validar que cabe em 6-8 semanas

**Resultado esperado:**
Todas as issues priorizadas, estimadas e timeline validada.

**Tempo estimado:** 1 dia (8 horas)

---

### Etapa 5: Criação de Milestones e Configuração de Board (0.5 dia)

Organizar issues em milestones e configurar board kanban.

**Execução:**
1. Criar 4 milestones
2. Atribuir issues aos milestones
3. Configurar GitHub Projects
4. Adicionar issues ao board
5. Definir rituais de acompanhamento

**Resultado esperado:**
Milestones criados, board kanban configurado, rituais definidos.

**Tempo estimado:** 0.5 dia (4 horas)

---

## Critérios de Aceite

- Repositório Git criado e time tem acesso
- Projeto Next.js rodando localmente
- Mínimo 15-20 issues criadas
- Todas as issues têm critérios de aceite claros
- Timeline validada em 6-8 semanas
- Board kanban configurado

---

**Criado em:** 2025-11-05
**Versão:** 1.0
