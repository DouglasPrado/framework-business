# Processo de Definição de Escopo de MVP

## Propósito

Este processo guia a análise de documentação existente e definição sistemática de escopo para construção de um Minimum Viable Product (MVP). O objetivo é transformar materiais dispersos (briefings, pesquisas, entrevistas) em um documento estruturado de Briefing de MVP que serve como contrato e referência única para todo o desenvolvimento.

## Objetivo

Criar um Briefing de MVP completo e aprovado que inclua:
- Hipótese principal clara e testável
- Funcionalidade core (principal) bem definida
- Funcionalidades secundárias priorizadas (máximo 3)
- Scope negativo documentado (o que NÃO entra no MVP)
- Métricas de validação quantitativas
- Stack técnica validada
- Timeline e orçamento aprovados

O resultado deve ser específico o suficiente para guiar o desenvolvimento e flexível o suficiente para permitir ajustes durante construção.

## Escopo

### Dentro do escopo
- Leitura e análise de toda documentação existente do projeto
- Identificação e formulação da hipótese principal de valor
- Definição da funcionalidade core que valida a hipótese
- Priorização de funcionalidades secundárias críticas
- Documentação explícita do scope negativo
- Definição de métricas quantitativas de validação
- Validação do stack técnica padrão (Next.js, Prisma, PostgreSQL, Stripe)
- Criação de timeline realista (6-8 semanas)
- Identificação de riscos principais e mitigações
- Aprovação formal com stakeholders

### Fora do escopo
- Desenvolvimento técnico ou escrita de código
- Criação de wireframes ou protótipos visuais detalhados
- Mapeamento de issues técnicas (processo separado: MVPIssuesMapping)
- Setup de repositório ou infraestrutura
- Pesquisa de mercado ou análise competitiva aprofundada
- Definição de estratégia de Go-to-Market
- Planejamento de produto além do MVP (roadmap futuro)

## Etapas do Processo

### Etapa 1: Leitura e Análise de Documentação (1-2 dias)

Acessar pasta especificada (Google Drive, Notion ou equivalente) e realizar leitura estruturada de todos os documentos disponíveis sobre o projeto.

**Perguntas orientadoras:**
- Quais documentos existem na pasta do projeto?
- Qual o problema principal mencionado nos materiais?
- Quem é o público-alvo descrito?
- Quais soluções foram propostas?
- Existem hipóteses já formuladas?
- Quais funcionalidades foram mencionadas?
- Há contradições entre documentos?

**Execução:**
1. Listar todos os documentos disponíveis na pasta
2. Criar estrutura de anotações para consolidar informações
3. Ler cada documento identificando: problema, solução, público-alvo, hipóteses, funcionalidades
4. Destacar contradições ou gaps de informação
5. Preparar lista de perguntas para stakeholders

**Resultado esperado:**
Documento de síntese com principais insights, problemas identificados, público-alvo descrito, hipóteses encontradas e lista de perguntas para validação.

**Tempo estimado:** 1-2 dias

---

### Etapa 2: Identificação da Hipótese Principal (0.5 dia)

Extrair ou formular a hipótese principal de valor que o MVP deve validar, usando formato estruturado.

**Perguntas orientadoras:**
- Qual é a hipótese mais crítica a validar?
- Quem é o beneficiário (QUEM)?
- Qual resultado ele busca (RESULTADO)?
- Qual a principal dor ou obstáculo (DOR)?
- A hipótese é mensurável?

**Execução:**
1. Revisar anotações da Etapa 1
2. Identificar a hipótese mais crítica a validar
3. Reformular no formato: "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"
4. Validar com stakeholders se a hipótese está correta
5. Documentar hipóteses secundárias para contexto

**Resultado esperado:**
Hipótese principal clara, validada com stakeholders e documentada no formato padrão. A hipótese deve ser mensurável e testável com métricas.

**Tempo estimado:** 0.5 dia

---

### Etapa 3: Definição de Funcionalidades (1 dia)

Identificar qual é a funcionalidade core que valida a hipótese principal e quais funcionalidades secundárias são absolutamente críticas para o MVP funcionar.

**Perguntas orientadoras:**
- Se tivéssemos apenas 1 funcionalidade, qual validaria nossa hipótese?
- Quais funcionalidades são essenciais para o MVP funcionar?
- O MVP funciona sem essa funcionalidade?
- O que NÃO deve entrar no MVP?

**Execução:**
1. Fazer a pergunta: "Se tivéssemos apenas 1 funcionalidade, qual validaria nossa hipótese?"
2. Descrever detalhadamente a funcionalidade principal (fluxo de usuário, requisitos, critérios)
3. Listar todas as funcionalidades secundárias mencionadas na documentação
4. Priorizar funcionalidades secundárias usando critério: "O MVP funciona sem isso?"
5. Selecionar no máximo 3 funcionalidades secundárias críticas
6. Documentar explicitamente o que NÃO entra no MVP (scope negativo)
7. Validar com stakeholders

**Resultado esperado:**
Template de Funcionalidades preenchido com:
- Funcionalidade principal descrita em detalhes
- Lista de funcionalidades secundárias priorizadas (máximo 3)
- Documento "O que NÃO entra no MVP" com justificativas
- Validação com stakeholders concluída

**Tempo estimado:** 1 dia

---

### Etapa 4: Criação do Briefing do MVP (1-2 dias)

Consolidar toda análise em documento estruturado de Briefing do MVP que será a referência principal para todo o desenvolvimento.

**Perguntas orientadoras:**
- Todos os elementos críticos estão documentados?
- As métricas de validação são quantitativas e realistas?
- O timeline é viável (6-8 semanas)?
- O orçamento está aprovado?
- Os riscos principais foram identificados?

**Execução:**
1. Preencher template de Briefing MVP com todas as informações coletadas
2. Definir métricas quantitativas de validação (cadastros, ativação, conversão, retenção, NPS)
3. Validar stack técnica padrão (Next.js, Prisma, PostgreSQL, NextAuth, Stripe)
4. Criar timeline realista de 6-8 semanas
5. Estimar orçamento mensal de infraestrutura ($30-80/mês)
6. Identificar 3-5 riscos principais e mitigações
7. Definir time e responsabilidades

**Resultado esperado:**
Briefing de MVP completo preenchido seguindo template padrão, incluindo todos os elementos: hipótese, funcionalidades, métricas, stack, timeline, orçamento, riscos e responsabilidades.

**Tempo estimado:** 1-2 dias

---

### Etapa 5: Revisão e Aprovação (0.5-1 dia)

Realizar revisão formal do Briefing MVP com stakeholders e obter aprovação documentada.

**Perguntas orientadoras:**
- Todos os stakeholders revisaram o documento?
- Há objeções ou ajustes necessários?
- A aprovação está documentada?
- O time completo tem acesso ao Briefing?

**Execução:**
1. Agendar reunião de revisão com stakeholders principais
2. Apresentar Briefing MVP destacando: hipótese, funcionalidades, timeline, orçamento
3. Coletar feedback e objeções
4. Realizar ajustes necessários
5. Obter aprovação formal documentada (email, assinatura digital, ata de reunião)
6. Compartilhar versão final do Briefing com todo o time
7. Documentar aprovação e versão final

**Resultado esperado:**
Briefing de MVP aprovado formalmente por todos os stakeholders, com aprovação documentada e compartilhado com todo o time de desenvolvimento.

**Tempo estimado:** 0.5-1 dia

---

## Entradas Essenciais

- Pasta com documentação do projeto (Google Drive, Notion, repositório)
- Acesso a stakeholders para validações (disponibilidade de resposta em até 48h)
- Materiais existentes: briefing inicial, pesquisas de mercado, entrevistas com usuários, personas, hipóteses preliminares
- Orçamento pré-aprovado para infraestrutura ($500-2.000/mês)
- Definição de time disponível (mínimo 1 desenvolvedor full-stack)

## Ferramentas e Artefatos de Apoio

### Ferramentas
- Google Docs ou Notion para documentação
- Google Drive ou pasta compartilhada para acesso a materiais
- Ferramenta de comunicação com stakeholders (email, Slack, Teams)

### Templates necessários
- Template de Briefing de MVP (disponível em _DATA)
- Template de Funcionalidades (disponível em _DATA)
- Template de Declaração de Hipótese (disponível em process/_SHARED/templates/)

## Requisitos

### Competências necessárias
- Análise de documentação e síntese de informações
- Pensamento estratégico de produto (entender problema vs. solução)
- Comunicação com stakeholders
- Priorização de funcionalidades (framework de trade-offs)
- Noções de viabilidade técnica

### Conhecimentos desejáveis
- Metodologia Lean Startup
- Jobs-to-be-Done framework
- Conceitos de MVP vs. MLP
- Experiência em product discovery

### Responsável típico
Product Owner, Product Manager ou Fundador/CEO com visão de produto

## Critérios de Aceite

O processo está completo quando:
- Todos os documentos existentes foram lidos e analisados
- Hipótese principal formulada no formato padrão e validada com stakeholders
- Funcionalidade core identificada e descrita em detalhes
- Funcionalidades secundárias priorizadas (máximo 3)
- Scope negativo documentado explicitamente
- Briefing de MVP preenchido completamente
- Métricas de validação definidas com valores quantitativos
- Stack técnica validada
- Timeline realista (6-8 semanas) definida
- Orçamento aprovado
- Riscos identificados com mitigações
- Aprovação formal documentada
- Briefing compartilhado com todo o time

## Indicadores de Sucesso

- Tempo de execução: máximo 4-5 dias
- Aprovação na primeira ou segunda revisão com stakeholders
- Clareza da hipótese: testável por alguém externo ao projeto
- Especificidade da funcionalidade core: desenvolvedor consegue entender o que construir
- Consenso no time: 100% dos stakeholders aprovam o Briefing

## Riscos e Mitigações

### Risco 1: Documentação insuficiente ou contraditória
**Probabilidade:** Média
**Impacto:** Alto (pode atrasar 2-3 dias)
**Mitigação:** Agendar sessão de discovery com stakeholders para preencher gaps. Preparar perguntas específicas antecipadamente.

### Risco 2: Stakeholders não chegam a consenso sobre hipótese ou funcionalidades
**Probabilidade:** Média
**Impacto:** Alto (pode inviabilizar o processo)
**Mitigação:** Realizar workshop de alinhamento facilitado. Usar técnicas de votação e priorização objetiva. Escalonar para decisor final se necessário.

### Risco 3: Escopo excessivamente grande (mais de 3 funcionalidades secundárias)
**Probabilidade:** Alta
**Impacto:** Alto (MVP de 8 semanas se torna 12-16 semanas)
**Mitigação:** Aplicar rigorosamente o critério "O MVP funciona sem isso?". Documentar features excluídas com promessa de revisão pós-validação.

### Risco 4: Métricas de validação muito ambiciosas ou genéricas
**Probabilidade:** Média
**Impacto:** Médio (dificulta decisão pós-lançamento)
**Mitigação:** Referenciar benchmarks de mercado. Consultar métricas de produtos similares. Definir critérios de "validado", "não validado" e "perseverar".

## Observações Importantes

- Este processo é a base para todo o desenvolvimento do MVP. Invista tempo necessário para fazê-lo bem.
- O Briefing de MVP não é imutável, mas mudanças após aprovação devem passar por processo de change request formal.
- Scope negativo é tão importante quanto scope positivo. Documente claramente o que NÃO entra.
- Métricas de validação devem ser quantitativas sempre que possível. Evite "sentir que funcionou".
- Timeline de 6-8 semanas é agressiva mas viável com escopo bem controlado. Se estimar mais, revise o escopo.

## Próximos Passos

Após conclusão deste processo:
1. Iniciar processo MVPIssuesMapping (mapeamento técnico de funcionalidades em issues)
2. Configurar repositório Git e ferramentas de gestão de projeto
3. Iniciar processo MVPInfrastructureSetup (setup técnico da base)

## Integrações com Outros Processos

### Processos anteriores recomendados:
- ProblemHypothesisDefinition - Para definir hipótese inicial se não existir
- TargetUserIdentification - Para definir persona se não existir

### Processos posteriores:
- MVPIssuesMapping - Próximo passo obrigatório
- MVPInfrastructureSetup - Etapa de implementação técnica
- MVPCoreDevelopment - Desenvolvimento da funcionalidade principal

---

**Criado em:** 2025-11-05
**Mantido por:** Framework Business Team
**Versão:** 1.0
**Baseado em:** Estratégia MVPBuilder
