# Validator - MVPCoreDevelopment

Este documento define os critérios de validação para considerar o processo MVPCoreDevelopment concluído com sucesso.

---

## Critérios Técnicos

### 1. Implementação Frontend

**Componentes e Páginas**
- [ ] Todas as páginas da funcionalidade core foram criadas
- [ ] Todos os componentes necessários foram implementados
- [ ] Componentes estão usando TypeScript corretamente (tipos definidos para props)
- [ ] Não há erros de TypeScript no build
- [ ] Estrutura de rotas no Next.js está correta e funcionando

**Formulários e Validação**
- [ ] Todos os formulários implementados com React Hook Form
- [ ] Validação de dados funcionando no frontend
- [ ] Mensagens de erro de validação são claras e úteis
- [ ] Campos obrigatórios estão marcados adequadamente
- [ ] Formulários previnem submissão de dados inválidos

**Estados e Feedback Visual**
- [ ] Estados de loading implementados em todas as ações assíncronas
- [ ] Estados de erro implementados e testados
- [ ] Toasts ou mensagens de sucesso/erro funcionando
- [ ] Botões desabilitados durante loading (prevenir multiple submits)
- [ ] Spinners ou skeletons visíveis durante carregamento

**Responsividade e Design**
- [ ] Interface responsiva em desktop (>1024px)
- [ ] Interface responsiva em tablet (768px - 1024px)
- [ ] Interface responsiva em mobile (< 768px)
- [ ] Touch targets suficientemente grandes em mobile (mínimo 44x44px)
- [ ] Design consistente com resto do MVP
- [ ] Cores e tipografia seguindo padrões definidos
- [ ] Espaçamentos e alinhamentos consistentes

**Navegação**
- [ ] Navegação entre telas da funcionalidade funcionando
- [ ] Links e botões todos funcionais
- [ ] Fluxo de navegação intuitivo
- [ ] Estado preservado quando apropriado

---

### 2. Implementação Backend

**Schema e Banco de Dados**
- [ ] Schema Prisma atualizado com models necessários
- [ ] Migrations criadas e executadas no banco de desenvolvimento
- [ ] Relacionamentos entre models definidos corretamente
- [ ] Índices adicionados para performance (em campos filtrados frequentemente)
- [ ] Campos de timestamp (createdAt, updatedAt) implementados
- [ ] Dados de teste criados no banco de desenvolvimento

**API Routes**
- [ ] Todos os endpoints necessários implementados
- [ ] Métodos HTTP corretos usados (GET, POST, PUT, DELETE)
- [ ] Endpoints retornam status codes HTTP apropriados (200, 201, 400, 401, 403, 404, 500)
- [ ] Formato de resposta consistente em todos os endpoints
- [ ] Endpoints documentados (comentários ou documentação separada)

**Validação de Dados**
- [ ] Validação de dados implementada com Zod ou similar
- [ ] Schemas de validação criados para todos os inputs
- [ ] Erros de validação retornam mensagens claras (status 400)
- [ ] Validação cobre casos extremos (strings vazias, números negativos, etc)

**Autenticação e Autorização**
- [ ] Endpoints protegidos verificam autenticação (retornam 401 se não autenticado)
- [ ] Autorização implementada (usuário só acessa seus próprios recursos)
- [ ] Tentativas de acesso não autorizado retornam 403
- [ ] Session do usuário verificada corretamente (NextAuth getServerSession)
- [ ] Filtros por usuário aplicados em queries (ex: `where: { userId: session.user.id }`)

**Lógica de Negócio**
- [ ] Operações CRUD implementadas (Create, Read, Update, Delete)
- [ ] Lógica de negócio específica da funcionalidade core implementada
- [ ] Dados persistindo corretamente no banco PostgreSQL
- [ ] Relacionamentos entre entidades funcionando corretamente
- [ ] Edge cases tratados adequadamente

**Tratamento de Erros**
- [ ] Try/catch implementado em toda lógica assíncrona
- [ ] Erros logados adequadamente (console.error ou serviço de logging)
- [ ] Mensagens de erro não vazam informações sensíveis
- [ ] Diferentes tipos de erro tratados apropriadamente (validação, autorização, servidor)

**Performance**
- [ ] Queries Prisma usando `select` específico (não retornam campos desnecessários)
- [ ] `include` de relacionamentos limitado ao necessário
- [ ] Queries críticas executam em < 500ms
- [ ] Sem problemas de N+1 queries

---

### 3. Integração Frontend + Backend

**Chamadas de API**
- [ ] Frontend integrado com backend (chamadas de API funcionando)
- [ ] Dados fluindo corretamente do frontend para backend
- [ ] Respostas da API atualizando estado do frontend corretamente
- [ ] Funções de API client criadas (se centralizado em `lib/api.ts`)

**Estados de Loading**
- [ ] Loading states funcionando durante requests
- [ ] Usuário vê feedback visual durante ações assíncronas
- [ ] Interface não trava durante requests

**Tratamento de Erros**
- [ ] Try/catch implementado em todas as chamadas de API
- [ ] Erros da API capturados e tratados no frontend
- [ ] Mensagens de erro mostradas ao usuário (toasts, mensagens inline)
- [ ] Erros de validação mostrados em campos específicos do formulário
- [ ] Erro 401 redireciona para login (se aplicável)

**Integrações Externas**
- [ ] Integração com Stripe funcionando (se aplicável à funcionalidade core)
- [ ] Checkout session criado corretamente
- [ ] Webhook de confirmação de pagamento funcionando
- [ ] Banco atualizado após confirmação de pagamento
- [ ] Fluxo de pagamento testado em modo test

**Fluxo End-to-End**
- [ ] Usuário consegue completar fluxo principal sem erros
- [ ] Dados criados no frontend aparecem no banco de dados
- [ ] Dados atualizados no frontend refletem no banco
- [ ] Dados deletados no frontend são removidos do banco
- [ ] UI atualiza imediatamente após ações (ou mostra loading)

---

### 4. Qualidade de Código

**Padrões de Código**
- [ ] Código passa em linting (ESLint sem erros)
- [ ] Código formatado consistentemente (Prettier)
- [ ] Nomenclatura de variáveis e funções é clara e descritiva
- [ ] Não há código comentado ou console.logs desnecessários
- [ ] Código não contém duplicações desnecessárias

**TypeScript**
- [ ] Tipos definidos para props de componentes
- [ ] Tipos definidos para respostas de API
- [ ] Tipos definidos para schemas Zod
- [ ] Uso mínimo de `any` (apenas quando absolutamente necessário)
- [ ] Build do TypeScript passa sem erros

**Organização**
- [ ] Código organizado em pastas apropriadas
- [ ] Componentes reutilizáveis separados de específicos
- [ ] Funções utilitárias em `lib/` ou similar
- [ ] Lógica de negócio complexa extraída de componentes/routes

**Code Review**
- [ ] Code review completo realizado (self-review ou com outro dev)
- [ ] Decisões técnicas importantes documentadas
- [ ] Comentários adicionados onde lógica é complexa

---

## Critérios Funcionais

### 1. Funcionalidade Core

**Critérios de Aceite do Briefing**
- [ ] Todos os critérios de aceite definidos no Briefing de MVP foram atendidos
- [ ] Funcionalidade core demonstra claramente a proposta de valor do MVP
- [ ] Hipótese principal pode ser validada com a funcionalidade implementada

**Fluxos de Usuário**
- [ ] Usuário consegue completar o fluxo principal da funcionalidade sem confusão
- [ ] Todos os casos de uso principais funcionam corretamente
- [ ] Navegação entre telas é intuitiva
- [ ] Ações do usuário têm resultado esperado

**Dados e Persistência**
- [ ] Dados criados pelo usuário são salvos corretamente
- [ ] Dados persistem após refresh da página
- [ ] Dados atualizados refletem mudanças corretamente
- [ ] Dados deletados desaparecem da interface

**Integração de Pagamento (se aplicável)**
- [ ] Fluxo de pagamento completo funciona (criar checkout → pagar → confirmar)
- [ ] Status de pagamento atualiza corretamente
- [ ] Usuário recebe confirmação após pagamento
- [ ] Dados de pagamento salvos corretamente

---

### 2. Experiência do Usuário

**Clareza**
- [ ] Textos e labels são claros e compreensíveis
- [ ] Mensagens de erro são úteis (dizem como corrigir)
- [ ] Mensagens de sucesso confirmam ações realizadas
- [ ] Instruções são claras quando necessárias

**Feedback Visual**
- [ ] Usuário sempre sabe o que está acontecendo (loading, sucesso, erro)
- [ ] Estados hover/focus em elementos interativos
- [ ] Feedback imediato para ações (botão pressionado, campo preenchido)
- [ ] Animações sutis melhoram UX (opcional mas recomendado)

**Performance Percebida**
- [ ] Ações principais completam em < 2s
- [ ] Estados de loading para ações que levam > 500ms
- [ ] Interface não congela durante operações
- [ ] Feedback imediato mesmo se ação leva tempo (otimistic updates opcional)

**Acessibilidade Básica**
- [ ] Contraste de cores adequado (legível)
- [ ] Labels em inputs de formulário
- [ ] Navegação possível via teclado (tab, enter)
- [ ] Elementos interativos têm tamanho adequado (especialmente mobile)

---

## Critérios de Qualidade

### 1. Testes

**Testes Manuais**
- [ ] Checklist completo de casos de teste criado e executado
- [ ] Todos os casos de teste principais passando
- [ ] Casos de erro testados (dados inválidos, recursos não encontrados, não autorizado)
- [ ] Edge cases testados (campos vazios, inputs extremos, etc)

**Cross-Browser**
- [ ] Funcionalidade testada em Chrome
- [ ] Funcionalidade testada em Firefox
- [ ] Funcionalidade testada em Safari (se macOS disponível)
- [ ] Funcionalidade básica funcionando em todos os navegadores testados

**Cross-Device**
- [ ] Funcionalidade testada em desktop (> 1024px)
- [ ] Funcionalidade testada em tablet (768px - 1024px)
- [ ] Funcionalidade testada em mobile (< 768px)
- [ ] Funcionalidade testada em dispositivo iOS real ou simulador
- [ ] Funcionalidade testada em dispositivo Android real ou simulador

**Testes de API**
- [ ] Todos os endpoints testados com Postman ou Insomnia
- [ ] Casos de sucesso funcionando
- [ ] Casos de erro retornando status e mensagens corretas
- [ ] Coleção Postman criada e organizada

---

### 2. Performance

**Frontend**
- [ ] Tempo de carregamento inicial < 3s (em conexão normal)
- [ ] Ações principais completam em < 2s
- [ ] Sem re-renders excessivos (verificado com React DevTools)
- [ ] Tamanho de bundle JavaScript razoável (< 500KB)

**Backend**
- [ ] Queries de banco de dados < 500ms
- [ ] Endpoints de API < 1s para 90% das requests
- [ ] Sem problemas de N+1 queries
- [ ] Índices adicionados em campos filtrados frequentemente

**Mobile**
- [ ] Funcionalidade utilizável em conexão 3G
- [ ] Não há lags perceptíveis em mobile
- [ ] Touch interactions responsivas

---

### 3. Segurança

**Validação**
- [ ] Validação de dados no frontend E backend (defesa em profundidade)
- [ ] Inputs sanitizados para prevenir XSS
- [ ] SQL injection impossível (usando Prisma ORM)

**Autenticação e Autorização**
- [ ] Rotas protegidas verificam autenticação
- [ ] Recursos protegidos verificam autorização (ownership)
- [ ] Tentativas não autorizadas retornam erros apropriados (401, 403)
- [ ] Session tokens seguros (HttpOnly cookies se usando NextAuth)

**Dados Sensíveis**
- [ ] Secrets em variáveis de ambiente (não no código)
- [ ] Variáveis de ambiente não commitadas no repositório
- [ ] Erros não vazam informações sensíveis
- [ ] Dados de pagamento não salvos localmente (apenas tokens Stripe)

---

### 4. Deploy e Staging

**Deploy**
- [ ] Código commitado e pushed para repositório
- [ ] Deploy para staging completado com sucesso
- [ ] Migrations executadas no banco de staging (se aplicável)
- [ ] Variáveis de ambiente configuradas no ambiente de staging
- [ ] Build do Vercel (ou plataforma similar) passou sem erros

**Validação em Staging**
- [ ] Funcionalidade acessível via URL de staging
- [ ] Fluxo end-to-end testado em staging
- [ ] Integrações externas funcionando em staging (Stripe test mode, etc)
- [ ] Sem erros críticos nos logs de staging

---

### 5. Documentação

**Documentação Técnica**
- [ ] Componentes principais documentados (propósito, props, uso)
- [ ] API routes documentadas (endpoint, parâmetros, resposta)
- [ ] Models Prisma documentados (comentários no schema ou doc separada)
- [ ] Decisões técnicas importantes documentadas

**README**
- [ ] README.md atualizado com informações da funcionalidade core
- [ ] Instruções de setup atualizadas (se mudaram)
- [ ] Variáveis de ambiente documentadas (se novas)

**Processos**
- [ ] Especificação técnica preenchida (`_DATA/especificacao-tecnica-[nome].md`)
- [ ] Relatório final de conclusão criado
- [ ] Lições aprendidas documentadas

---

## Critérios de Validação com Stakeholders

### 1. Demonstração

**Apresentação**
- [ ] Funcionalidade demonstrada para stakeholders
- [ ] Todos os fluxos principais mostrados
- [ ] Proposta de valor do MVP claramente demonstrada
- [ ] Perguntas de stakeholders respondidas

**Feedback**
- [ ] Feedback de stakeholders coletado e documentado
- [ ] Stakeholders aprovaram a implementação OU
- [ ] Ajustes solicitados foram implementados ou documentados para backlog

---

## Checklist Final de Validação

### Implementação Completa
- [ ] Funcionalidade core 100% implementada (frontend + backend + integração)
- [ ] Todos os critérios de aceite do Briefing atendidos
- [ ] Todos os critérios técnicos aprovados
- [ ] Todos os critérios funcionais aprovados

### Qualidade Garantida
- [ ] Checklist de qualidade compartilhado 90%+ aprovado
- [ ] Code review completo realizado
- [ ] Sem bugs críticos conhecidos
- [ ] Sem console.errors ou warnings críticos
- [ ] Performance aceitável (< 2s para ações principais)

### Testes Abrangentes
- [ ] Testes manuais completos realizados
- [ ] Testado em múltiplos navegadores (Chrome, Firefox, Safari)
- [ ] Testado em múltiplos dispositivos (desktop, tablet, mobile)
- [ ] Testado em dispositivos reais (iOS e/ou Android)
- [ ] Edge cases e cenários de erro cobertos

### Deploy e Validação
- [ ] Deploy para staging bem-sucedido
- [ ] Funcionalidade validada em ambiente de staging
- [ ] Stakeholders validaram a implementação
- [ ] Ajustes críticos implementados

### Documentação
- [ ] Documentação técnica completa
- [ ] README atualizado
- [ ] Decisões técnicas documentadas
- [ ] Lições aprendidas capturadas

---

## Indicadores de Sucesso Quantitativos

### Metas Mínimas (Obrigatório)
- Critérios de aceite atendidos: 100%
- Checklist de qualidade: 90%+
- Bugs críticos: 0
- Performance ações principais: < 2s para 90% das ações
- Compatibilidade navegadores: 3+ navegadores testados
- Compatibilidade dispositivos: mobile + desktop testados

### Metas Ideais (Recomendado)
- Checklist de qualidade: 95%+
- Bugs médios: < 5
- Performance ações principais: < 1s para 50% das ações
- Compatibilidade navegadores: 4+ navegadores (Chrome, Firefox, Safari, Edge)
- Compatibilidade dispositivos: iOS + Android + desktop testados
- Testes em dispositivos reais: 2+ dispositivos

---

## Indicadores de Sucesso Qualitativos

### Experiência do Desenvolvedor
- [ ] Outro desenvolvedor consegue entender o código
- [ ] Código é manutenível e extensível
- [ ] Desenvolvedor consegue explicar decisões técnicas tomadas
- [ ] Documentação é útil e clara

### Experiência do Usuário
- [ ] Fluxo é intuitivo (usuário não precisa de tutorial)
- [ ] Feedback visual é claro e útil
- [ ] Performance percebida é boa (não parece lento)
- [ ] Erros são raros e bem tratados quando acontecem

### Validação de Proposta de Valor
- [ ] Funcionalidade demonstra claramente a proposta de valor do MVP
- [ ] Stakeholders estão confiantes de que pode validar hipótese
- [ ] Usuários conseguem experimentar a funcionalidade principal
- [ ] MVP está pronto para próxima fase (funcionalidades secundárias)

---

## Critérios de Reprovação (Blockers)

Se qualquer um desses critérios não for atendido, o processo NÃO pode ser considerado concluído:

### Crítico
- [ ] Funcionalidade core não implementada completamente
- [ ] Fluxo principal não funciona end-to-end
- [ ] Dados não persistem corretamente no banco
- [ ] Bugs críticos impedem uso da funcionalidade
- [ ] Autenticação/autorização não funciona (se aplicável)
- [ ] Pagamento não funciona (se aplicável e core para MVP)
- [ ] Deploy para staging falhou
- [ ] Stakeholders não aprovaram implementação

### Importante
- [ ] Performance inaceitável (> 5s para ações principais)
- [ ] Não funciona em mobile
- [ ] Não funciona em navegadores principais (Chrome, Firefox, Safari)
- [ ] Checklist de qualidade < 80%
- [ ] Mais de 5 bugs críticos conhecidos
- [ ] Documentação técnica ausente

---

## Próximos Passos Após Validação

Uma vez que todos os critérios forem atendidos:

1. Marcar processo MVPCoreDevelopment como CONCLUÍDO
2. Atualizar status no board de projeto (GitHub Projects, Linear, etc)
3. Celebrar conclusão da funcionalidade core
4. Preparar para próximo processo: **Desenvolvimento de Funcionalidades Secundárias**
5. Ou, se aplicável, validar funcionalidade com grupo pequeno de early adopters

---

**Última atualização:** 2025-11-05
**Mantido por:** Framework Business Team
**Parte de:** Estratégia MVPBuilder (Etapa 4)
