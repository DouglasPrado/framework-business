# Validador - Definição de Escopo de MVP

## Propósito

Este documento fornece critérios objetivos de validação para garantir que o processo de Definição de Escopo de MVP foi executado com qualidade e completude. Use este validador antes de considerar o processo concluído e antes de avançar para o próximo processo (MVPIssuesMapping).

## Validação Geral do Processo

### Critérios de Completude

O processo está completo quando TODOS os critérios abaixo são atendidos:

- [ ] Todas as 20 tarefas do tasks.MD foram executadas
- [ ] Tempo total de execução foi de 4-5 dias (máximo 7 dias)
- [ ] Briefing de MVP foi criado e preenchido completamente
- [ ] Template de Funcionalidades foi preenchido
- [ ] Aprovação formal foi obtida e documentada
- [ ] Briefing foi compartilhado com todo o time
- [ ] Todos os stakeholders principais tiveram oportunidade de revisar

## Validação da Documentação Produzida

### Briefing de MVP

Verifique que o Briefing de MVP contém:

**Seção 1 - Visão Geral do Produto:**
- [ ] Nome do produto definido
- [ ] Descrição em uma linha clara e objetiva
- [ ] Categoria do produto especificada

**Seção 2 - Hipótese Principal:**
- [ ] Hipótese no formato: "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"
- [ ] QUEM está específico (não genérico como "pessoas" ou "usuários")
- [ ] RESULTADO está claro e é um objetivo, não uma solução
- [ ] DOR está específica e descreve obstáculo atual
- [ ] Premissas críticas da hipótese foram listadas (mínimo 2-3)

**Seção 3 - Público-Alvo:**
- [ ] Descrição clara do usuário principal
- [ ] Características demográficas documentadas
- [ ] Características comportamentais documentadas (dor, comportamento atual, motivações)
- [ ] Exemplo de usuário narrativo criado

**Seção 4 - Problema a Resolver:**
- [ ] Descrição detalhada do problema
- [ ] Impacto do problema documentado (custo em tempo/dinheiro/frustração)
- [ ] Soluções atuais inadequadas descritas

**Seção 5 - Solução Proposta:**
- [ ] Descrição clara de como o MVP resolve o problema
- [ ] Diferencial principal documentado

**Seção 6 - Funcionalidades do MVP:**
- [ ] Funcionalidade principal (core) descrita em detalhes
- [ ] Fluxo de usuário da funcionalidade core mapeado
- [ ] Critério de sucesso da funcionalidade core definido
- [ ] Conexão entre funcionalidade core e hipótese explicada
- [ ] Funcionalidades secundárias listadas (máximo 3)
- [ ] Cada funcionalidade secundária tem justificativa de por que é crítica

**Seção 7 - Scope Negativo:**
- [ ] Lista de features excluídas documentada (mínimo 2-3)
- [ ] Cada feature excluída tem razão da exclusão
- [ ] Cada feature excluída tem indicação de quando considerar no futuro

**Seção 8 - Métricas de Validação:**
- [ ] Métricas quantitativas definidas com valores específicos
- [ ] No mínimo: cadastros, taxa de ativação, conversão, retenção, NPS
- [ ] Critérios de decisão claros (hipótese validada / não validada / perseverar)
- [ ] Métricas qualitativas documentadas (entrevistas, surveys)

**Seção 9 - Stack Técnica:**
- [ ] Frontend, backend, banco de dados, autenticação, pagamento documentados
- [ ] Stack padrão validada (Next.js, Prisma, PostgreSQL, NextAuth, Stripe)
- [ ] Providers específicos definidos (hosting, analytics, email)

**Seção 10 - Timeline e Marcos:**
- [ ] Duração total de 6-8 semanas
- [ ] Marcos principais mapeados por semana
- [ ] Timeline aprovada por stakeholders

**Seção 11 - Orçamento:**
- [ ] Custos mensais de infraestrutura estimados
- [ ] Total mensal dentro de $30-100/mês (ou budget aprovado)
- [ ] Custos de time documentados se aplicável

**Seção 12 - Riscos Principais:**
- [ ] Mínimo 3 riscos identificados
- [ ] Cada risco tem probabilidade e impacto avaliados
- [ ] Cada risco tem mitigação específica definida

**Seção 13 - Time e Responsabilidades:**
- [ ] Papéis necessários identificados
- [ ] Responsáveis nomeados para cada papel
- [ ] Responsabilidades de cada papel documentadas

**Seção 14 - Critérios de Aceite:**
- [ ] Checklist de completude verificado
- [ ] Todos os itens do checklist marcados

**Seção 15 - Aprovações:**
- [ ] Aprovação de stakeholders documentada
- [ ] Data de aprovação registrada
- [ ] Nome e cargo dos aprovadores incluídos

### Template de Funcionalidades

Verifique que o Template de Funcionalidades contém:

**Funcionalidade Principal:**
- [ ] Nome claro da funcionalidade
- [ ] Descrição detalhada (mínimo 2-3 parágrafos)
- [ ] Conexão com hipótese explicada
- [ ] Fluxo de usuário completo mapeado (mínimo 3 passos)
- [ ] Requisitos funcionais listados (frontend, backend, banco)
- [ ] Critérios de aceite técnicos e de negócio definidos
- [ ] Casos de uso documentados (mínimo 1)

**Funcionalidades Secundárias:**
- [ ] Máximo 3 funcionalidades secundárias
- [ ] Cada uma tem descrição, justificativa, fluxo e requisitos
- [ ] Justificativa de criticidade para cada uma é convincente

**Scope Negativo:**
- [ ] Features excluídas documentadas com razão e momento futuro

## Validação de Qualidade

### Qualidade da Hipótese

**Critérios de qualidade alta:**
- [ ] Hipótese pode ser testada com métricas específicas
- [ ] Alguém externo ao projeto consegue entender a hipótese
- [ ] Você consegue imaginar como INVALIDAR a hipótese
- [ ] QUEM é específico o suficiente para encontrar 10+ pessoas que correspondam
- [ ] RESULTADO é um objetivo claro, não uma feature
- [ ] DOR é específica e foi validada com pesquisas/entrevistas

**Sinais de alerta (requerer revisão):**
- [ ] Hipótese contém jargão técnico ou de produto
- [ ] QUEM é genérico ("pessoas", "usuários", "todos")
- [ ] RESULTADO usa verbos vagos ("melhorar", "facilitar", "otimizar")
- [ ] DOR não foi validada com usuários reais
- [ ] Hipótese tenta testar múltiplas coisas ao mesmo tempo

### Qualidade do Escopo

**Critérios de qualidade alta:**
- [ ] Funcionalidade core pode ser desenvolvida em 2-3 semanas
- [ ] Cada funcionalidade secundária pode ser desenvolvida em 1 semana
- [ ] Total de funcionalidades (core + secundárias) é no máximo 4
- [ ] Scope negativo tem pelo menos 3 features documentadas
- [ ] Todas as funcionalidades têm conexão clara com validação da hipótese

**Sinais de alerta (requerer revisão):**
- [ ] Mais de 3 funcionalidades secundárias identificadas
- [ ] Funcionalidade core tem mais de 7 passos no fluxo de usuário
- [ ] Alguma funcionalidade secundária não tem justificativa convincente
- [ ] Scope negativo está vazio ou com menos de 2 features
- [ ] Timeline estimada acima de 8 semanas

### Qualidade das Métricas

**Critérios de qualidade alta:**
- [ ] Todas as métricas têm valores numéricos específicos
- [ ] Valores são realistas baseados em benchmarks de mercado
- [ ] Critérios de decisão estão claros (validado/não validado/perseverar)
- [ ] Métricas são mensuráveis com ferramentas disponíveis (GA4, banco de dados)
- [ ] Existe combinação de métricas de comportamento e de negócio

**Sinais de alerta (requerer revisão):**
- [ ] Métricas são vagas ("usuários satisfeitos", "boa adoção")
- [ ] Valores parecem excessivamente otimistas
- [ ] Não há critérios claros de decisão pós-validação
- [ ] Faltam métricas críticas (ex: conversão, retenção)

### Qualidade do Alinhamento

**Critérios de qualidade alta:**
- [ ] Todos os stakeholders principais aprovaram
- [ ] Aprovação está documentada (email, assinatura, ata)
- [ ] Não houve mais de 2 rodadas de revisão antes da aprovação
- [ ] Time de desenvolvimento revisou e considera viável
- [ ] Briefing foi compartilhado com todos os envolvidos

**Sinais de alerta (requerer revisão):**
- [ ] Múltiplas rodadas de revisão sem convergência
- [ ] Feedback contraditório entre stakeholders
- [ ] Aprovação apenas verbal
- [ ] Time técnico não foi consultado sobre viabilidade
- [ ] Stakeholders adicionando funcionalidades durante revisão

## Validação de Saídas (Outputs)

### Outputs obrigatórios produzidos:

- [ ] Briefing de MVP completo (documento)
- [ ] Template de Funcionalidades preenchido (documento)
- [ ] Documento de Síntese de Análise de Documentação
- [ ] Ata de reunião de aprovação com stakeholders
- [ ] Aprovação formal documentada

### Outputs opcionais (mas recomendados):

- [ ] Diagrama de fluxo de usuário da funcionalidade core
- [ ] Lista de perguntas e respostas com stakeholders
- [ ] Análise de riscos detalhada
- [ ] Apresentação resumida do Briefing (slides)

## Checklist de Consistência

Verifique consistência entre documentos:

### Entre Briefing e Template de Funcionalidades:
- [ ] Funcionalidade core é a mesma nos dois documentos
- [ ] Número de funcionalidades secundárias é igual
- [ ] Scope negativo é consistente
- [ ] Descrições de funcionalidades são alinhadas

### Entre Hipótese e Funcionalidades:
- [ ] Funcionalidade core valida RESULTADO da hipótese
- [ ] Público-alvo (QUEM) está alinhado com persona
- [ ] Funcionalidade aborda a DOR especificada

### Entre Métricas e Hipótese:
- [ ] Métricas permitem medir validação da hipótese
- [ ] Taxa de ativação está relacionada ao RESULTADO
- [ ] Métricas qualitativas capturam percepção sobre a DOR

## Critérios de Aprovação Final

O processo pode ser considerado CONCLUÍDO quando:

- [ ] TODOS os critérios de completude foram atendidos
- [ ] TODOS os critérios de qualidade foram atendidos
- [ ] NENHUM sinal de alerta está presente (ou foram tratados)
- [ ] TODOS os outputs obrigatórios foram produzidos
- [ ] Checklist de consistência está 100% validado
- [ ] Aprovação formal está documentada
- [ ] Time completo tem acesso ao Briefing final

## Ações Corretivas

Se algum critério de validação falhar:

### Falhas críticas (bloqueiam conclusão):
- Hipótese não está no formato padrão → Refazer Etapa 2
- Mais de 3 funcionalidades secundárias → Repriorizar usando "MVP funciona sem isso?"
- Métricas não são quantitativas → Refazer Tarefa 12
- Aprovação não está documentada → Obter documentação formal
- Briefing não foi compartilhado com time → Compartilhar imediatamente

### Falhas não críticas (recomendam revisão):
- Scope negativo vazio → Adicionar pelo menos 2-3 features excluídas
- Riscos insuficientes → Identificar riscos adicionais
- Timeline acima de 8 semanas → Revisar escopo e priorização
- Múltiplas rodadas de revisão → Realizar workshop de alinhamento

## Próximos Passos Após Validação

Quando todos os critérios forem atendidos:

1. Considerar processo MVPScopeDefinition concluído
2. Arquivar versão final do Briefing de MVP
3. Comunicar conclusão a todos os stakeholders
4. Iniciar próximo processo: MVPIssuesMapping
5. Usar Briefing de MVP como referência única durante todo desenvolvimento

## Registro de Validação

**Processo validado por:** [Nome do validador]
**Data de validação:** [DD/MM/AAAA]
**Versão do Briefing validada:** [v1.0, v1.1, etc.]

**Checklist de validação:**
- [ ] Completude: APROVADO
- [ ] Qualidade da Hipótese: APROVADO
- [ ] Qualidade do Escopo: APROVADO
- [ ] Qualidade das Métricas: APROVADO
- [ ] Qualidade do Alinhamento: APROVADO
- [ ] Outputs Produzidos: APROVADO
- [ ] Consistência: APROVADO

**Observações:**
[Registre aqui quaisquer observações, exceções ou ajustes necessários]

**Aprovação final:** [ ] SIM  [ ] NÃO (se não, documentar bloqueadores)

---

**Última atualização:** 2025-11-05
**Mantido por:** Framework Business Team
**Versão:** 1.0
