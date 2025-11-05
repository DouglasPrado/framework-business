# Knowledge Base - MVPLaunchValidation

Este documento consolida conhecimentos, referencias e FAQs para o processo de lancamento e validacao do MVP.

---

## Materiais de Apoio

### Templates Compartilhados (Reutilizar)

- [Checklist de Qualidade](../../_SHARED/templates/checklist-qualidade.MD) - Checklist padrao de validacao
- [Template de Retrospectiva](../../_SHARED/templates/retrospectiva.MD) - Para retrospectivas de processo

### Templates Locais (Especificos deste Processo)

- Roteiro de Entrevista: `_DATA/roteiro-entrevista.md`
- Survey de Satisfacao: `_DATA/survey-satisfacao.md`
- Template de Relatorio de Validacao: `_DATA/template-relatorio-validacao.md`
- Dashboard de Metricas: `_DATA/dashboard-metricas.md`
- Plano de Comunicacao: `_DATA/plano-comunicacao.md`

### Processos Relacionados

- [MVPTestingPreLaunch](../MVPTestingPreLaunch/process.MD) - Testes pre-lancamento (entrada)
- [MVPCoreDevelopment](../MVPCoreDevelopment/process.MD) - Desenvolvimento core
- [ProblemHypothesisDefinition](../../ProblemHypothesisDefinition/process.MD) - Hipotese original

---

## Documentacao Tecnica de Referencia

### Lean Startup Methodology

**The Lean Startup (Eric Ries)**
- Build-Measure-Learn: https://theleanstartup.com/principles
- Validated Learning: https://www.forbes.com/sites/erikaandersen/2012/03/07/eric-ries-on-validated-learning/
- Pivot or Persevere: https://steveblank.com/2013/04/10/pivot-dont-jump-to-a-new-vision/

**Ash Maurya - Running Lean**
- Customer Interviews: https://blog.leanstack.com/the-updated-problem-interview-script-and-a-new-canvas-1e43ff267a5d
- Metrics That Matter: https://blog.leanstack.com/finding-the-right-metrics-for-your-startup-f5b7e3c9b0f8

### Analytics e Metricas

**Google Analytics 4**
- Documentacao: https://developers.google.com/analytics/devguides/collection/ga4
- Event tracking: https://support.google.com/analytics/answer/9216061
- Custom events: https://developers.google.com/analytics/devguides/collection/ga4/events

**Posthog**
- Documentacao: https://posthog.com/docs
- Event tracking: https://posthog.com/docs/integrate/client/js
- Feature flags: https://posthog.com/docs/feature-flags

**Mixpanel**
- Documentacao: https://developer.mixpanel.com/docs
- User analytics: https://mixpanel.com/blog/guide-to-user-analytics/

### Monitoramento

**Sentry**
- Documentacao: https://docs.sentry.io
- Error monitoring: https://docs.sentry.io/platforms/javascript/guides/nextjs/

**Vercel Analytics**
- Documentacao: https://vercel.com/docs/analytics
- Web Vitals: https://vercel.com/docs/analytics/web-vitals

### Customer Development

**Steve Blank - Customer Development**
- Customer Discovery: https://steveblank.com/category/customer-development/
- Getting Out of the Building: https://steveblank.com/2010/03/11/teaching-entrepreneurship-by-getting-students-out-of-the-building/

**The Mom Test (Rob Fitzpatrick)**
- How to talk to customers: https://www.momtestbook.com/
- Asking good questions: https://review.firstround.com/the-right-way-to-ask-the-wrong-questions

---

## Best Practices

### Early Adopters

**Quem sao Early Adopters:**
- Primeiros usuarios dispostos a usar produto imperfeito
- Tem a dor que voce esta resolvendo (DOR REAL)
- Dispostos a dar feedback honesto
- Tolerantes com bugs e features faltando
- Podem se tornar evangelistas do produto

**Como identificar:**
- Pessoas que ja tentaram resolver a dor de outras formas
- Usuarios que se engajaram durante validacao de problema
- Profissionais da area do problema
- Pessoas que pedem para testar o produto
- Comunidades relacionadas ao problema

**Quantos recrutar:**
- Minimo: 10-15 usuarios
- Ideal: 20-30 usuarios
- Foco em qualidade, nao quantidade
- Melhor 10 usuarios engajados que 100 desinteressados

### Metricas de Validacao

**Metricas Primarias (AARRR Framework):**

1. **Acquisition (Cadastros)**
   - O que medir: Numero de cadastros realizados
   - Meta MVP: 10-30 cadastros
   - Como: GA4, Posthog, banco de dados

2. **Activation (Ativacao)**
   - O que medir: Usuario completou acao core pela primeira vez
   - Meta MVP: 60%+ dos cadastros ativam
   - Como: Event tracking de acao core

3. **Retention (Retencao)**
   - O que medir: Usuario volta para usar novamente
   - Meta MVP: 40%+ voltam em 7 dias
   - Como: Cohort analysis

4. **Revenue (Conversao)**
   - O que medir: Usuario paga (se aplicavel)
   - Meta MVP: 10-20% dos usuarios ativados
   - Como: Stripe webhooks, analytics

5. **Referral (Indicacao)**
   - O que medir: Usuario indica para outros
   - Meta MVP: NPS > 30 (se aplicavel)
   - Como: Survey de NPS

**Metricas Secundarias:**
- Tempo medio de uso
- Features mais usadas
- Taxa de conclusao de onboarding
- Tempo para completar acao core
- Taxa de abandono

**Pirate Metrics para MVP:**
- Foco em Activation e Retention
- Acquisition e uma metrica de contexto (poucos usuarios esperado)
- Revenue opcional (depende do modelo)
- Referral e bonus (se acontecer naturalmente)

### Feedback Qualitativo

**Entrevistas (10-15 usuarios):**

**Estrutura de Entrevista:**
1. Abertura (5 min): Contexto, permissao para gravar, deixar confortavel
2. Uso do produto (15 min): Como usou, o que achou, dificuldades
3. Valor percebido (10 min): Resolveu problema? Quanto vale? Pagaria?
4. Comparacao (5 min): Com o que compararia? O que falta?
5. Futuro (5 min): Continuaria usando? Indicaria? Por que?

**Perguntas Poderosas:**
- "Me conta como foi sua primeira experiencia com o produto"
- "Qual problema especifico isso resolveu pra voce?"
- "Como voce resolvia isso antes?"
- "Quanto tempo/dinheiro/esforco isso te economizou?"
- "O que quase te fez desistir de usar?"
- "Se pudesse mudar uma coisa, o que seria?"
- "Voce pagaria por isso? Quanto?"

**Red Flags em Entrevistas:**
- Usuario elogia demais sem exemplos concretos
- Usuario diz que usaria mas nao usou ainda
- Usuario pede features sem explicar por que
- Usuario fala do futuro, nao do presente
- Usuario e educado demais (nao e honesto)

**Green Flags em Entrevistas:**
- Usuario ja usou multiplas vezes sem ser pedido
- Usuario tem exemplo especifico de valor gerado
- Usuario ja recomendou para alguem
- Usuario reclama de coisas especificas (sinal de uso real)
- Usuario quer pagar ou ja esta pagando

### Feedback Quantitativo

**Survey de Satisfacao (30-50 respostas):**

**Perguntas Essenciais:**
1. NPS: "Em uma escala de 0-10, quanto voce recomendaria este produto?"
2. CSAT: "Quao satisfeito voce esta com o produto?" (1-5)
3. Frequencia: "Com que frequencia voce usa?" (Diario/Semanal/Mensal/Raramente)
4. Valor: "Qual o principal valor que este produto te entrega?"
5. Alternativas: "Se este produto deixasse de existir, o que voce usaria?"
6. Pagaria: "Voce pagaria por este produto?" (Sim/Nao/Talvez)
7. Valor Monetario: "Quanto pagaria por mes?" (Faixas de preco)

**Distribuir Survey:**
- Email para todos os usuarios cadastrados
- Pop-up in-app apos 3-5 usos
- Link em email de follow-up
- Incentivo opcional (desconto, feature exclusiva)

**Taxa de Resposta Esperada:**
- 20-30% para early adopters (engajados)
- 10-15% para usuarios gerais
- Minimo: 30 respostas para insights validos

### Analise de Hipotese

**Framework de Validacao:**

1. **Revisar Hipotese Original:**
   - "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"
   - Exemplo: "Meu produto ajuda freelancers a organizar financas sem planilhas complexas"

2. **Coletar Evidencias:**
   - **QUEM**: Usuarios reais sao o publico-alvo? (demograficos, comportamentos)
   - **RESULTADO**: Usuarios estao alcancando resultado prometido? (metricas, depoimentos)
   - **DOR**: Solucao realmente evita a dor prometida? (comparacao, alternativas)

3. **Avaliar cada componente:**
   - **QUEM - VALIDADO**: 70%+ dos usuarios sao o publico-alvo
   - **RESULTADO - VALIDADO**: 60%+ alcancaram resultado
   - **DOR - VALIDADO**: 70%+ confirmam que evita dor

4. **Decisao:**
   - Se 3/3 validados: **EXPANDIR**
   - Se 2/3 validados: **PERSEVERAR** (ajustar componente nao validado)
   - Se 1/3 ou 0/3 validados: **PIVOTAR**

**Tipos de Pivot (se necessario):**
- **Customer Segment Pivot**: Mudar o QUEM (publico diferente valoriza mais)
- **Problem Pivot**: Mudar o RESULTADO (resolver problema diferente)
- **Solution Pivot**: Mudar como entrega valor (DOR diferente)
- **Zoom-in Pivot**: Focar em uma feature especifica
- **Zoom-out Pivot**: Expandir escopo

### Decisoes Estrategicas

**PIVOTAR - Quando e Como:**

**Sinais de que deve pivotar:**
- Retencao < 20% em 7 dias
- NPS < 0 (mais detratores que promotores)
- Usuarios nao completam acao core
- Ninguem quer pagar (se modelo pago)
- Feedback contradiz hipotese original
- Usuarios usam produto de forma muito diferente do esperado

**Como pivotar:**
1. Analisar o que FUNCIONOU (guardar isso)
2. Identificar componente errado da hipotese
3. Gerar nova hipotese baseada em aprendizados
4. Validar nova hipotese (voltar para ProblemHypothesisDefinition)
5. Nao jogar fora codigo/design reutilizavel

**PERSEVERAR - Quando e Como:**

**Sinais de que deve perseverar:**
- Resultados mistos mas promissores
- Alguns usuarios AMAM, outros nao entendem
- Metricas OK mas nao excelentes (30-50% das metas)
- Feedback claro sobre o que melhorar
- Produto certo, execucao precisa melhorar

**Como perseverar:**
1. Identificar maior gap (onboarding? feature faltando? UX?)
2. Fazer ajustes focados (nao refazer tudo)
3. Recrutar mais early adopters (mesmo perfil)
4. Re-validar em 2-3 semanas
5. Definir criterios claros: se X melhorar, expandir; se nao, pivotar

**EXPANDIR - Quando e Como:**

**Sinais de que deve expandir:**
- Retencao > 40% em 7 dias
- NPS > 30
- Usuarios completam acao core regularmente
- Feedback muito positivo e consistente
- Usuarios querem pagar (ou ja estao pagando)
- Crescimento organico (word-of-mouth)

**Como expandir:**
1. Aumentar aquisicao de usuarios (marketing, vendas)
2. Melhorar produto baseado em feedback
3. Adicionar features mais avancadas
4. Otimizar conversao e monetizacao
5. Construir time e processos
6. Investir em infraestrutura e escala

---

## FAQs

### Early Adopters e Lancamento

**P: Quantos early adopters sao suficientes para validar?**
R: Minimo 10-15 usuarios ativos. Ideal 20-30. Foco em qualidade de engajamento, nao quantidade. Melhor 10 usuarios usando toda semana do que 100 que usaram uma vez.

**P: Como recrutar early adopters se nao tenho audiencia?**
R: Comunidades online (Reddit, Facebook Groups, Discord), forums especializados, LinkedIn, direct outreach para pessoas que tem a dor, parcerias com influenciadores de nicho, anuncios pequenos e direcionados.

**P: Devo cobrar de early adopters?**
R: Depende do modelo. Se produto pago: oferecer desconto mas COBRAR (valida willingness to pay). Se freemium: deixar gratis mas perguntar se pagariam. Gratis total pode atrair usuarios nao qualificados.

**P: Early adopters nao estao usando. E agora?**
R: Sinal de problema. Acoes: 1) Entrevistar para entender por que, 2) Verificar se sao publico certo, 3) Onboarding pode estar ruim, 4) Produto pode nao resolver dor de verdade. Nao ignore esse sinal.

### Metricas e Analytics

**P: Minhas metricas estao baixas. Devo pivotar imediatamente?**
R: Nao necessariamente. Primeiro: 1) Analise qualitativa (entrevistas), 2) Verifique se onboarding esta claro, 3) De tempo (minimo 2 semanas), 4) Tente ajustes pequenos. Pivot e decisao seria baseada em evidencias qualitativas + quantitativas.

**P: Qual a metrica mais importante para MVP?**
R: **Retention (Retencao)**. Usuarios voltam = voce esta gerando valor. Sem retencao, nada mais importa. Segunda mais importante: **Activation** (usuario completa acao core).

**P: Quanto tempo monitorar antes de decidir?**
R: Minimo 2 semanas de uso ativo. Ideal 3-4 semanas. Tempo suficiente para usuarios voltarem (ou nao). Se produto e uso semanal/mensal, pode precisar de mais tempo.

**P: NPS de quanto e bom para MVP?**
R: NPS > 30 = excelente para MVP. NPS 0-30 = OK, tem potencial. NPS < 0 = problema serio. Para referencia: empresas estabelecidas consideram NPS 50+ como excelente.

### Entrevistas e Feedback

**P: Usuarios elogiam muito mas nao usam. Por que?**
R: "Sindrome do educado". Pessoas sao educadas demais para criticar. Solucao: Pergunte sobre COMPORTAMENTO passado, nao intencoes futuras. "Quando foi a ultima vez que usou?" e melhor que "Voce vai usar?".

**P: Como fazer usuarios serem honestos em entrevistas?**
R: 1) Deixe claro que feedback negativo AJUDA, 2) Pergunte sobre acoes, nao opinioes, 3) Use silencio (deixe eles falarem), 4) Nao defenda o produto, 5) Agradeca criticas.

**P: Devo fazer entrevistas ou survey primeiro?**
R: Entrevistas primeiro (qualitativo) para entender o "por que". Survey depois (quantitativo) para validar padroes em escala. Entrevistas dao profundidade, surveys dao amplitude.

**P: Usuarios pedem 50 features diferentes. O que fazer?**
R: Nao construa tudo. Procure PADROES: qual dor comum por tras dos pedidos? Foque no problema, nao na solucao especifica. Uma boa feature resolve multiplos pedidos.

### Decisoes Estrategicas

**P: Tenho medo de pivotar e "desperdicar" trabalho. Devo?**
R: Pivotar NAO e desperdicar. E aprender. Codigo e design podem ser reutilizados. Conhecimento e expertise permanecem. Pior que pivotar e insistir em algo que nao funciona.

**P: Quando sei que e hora de desistir (nao pivotar)?**
R: Desistir (shutdown) vs Pivotar sao diferentes. Desistir quando: 1) Sem aprendizados novos (tentou varios pivots), 2) Sem recursos (tempo/dinheiro), 3) Perdeu paixao/motivacao, 4) Oportunidade melhor apareceu. Pivotar = mudar direcao com aprendizados.

**P: Resultados sao mistos. Pivotar ou perseverar?**
R: Perseverar se consegue identificar O QUE ajustar e COMO medir melhoria. Pivotar se problema e fundamental (publico errado, problema errado, solucao errada). Regra: perseverar uma vez. Se nao melhorar, pivotar.

**P: Posso expandir com poucos usuarios?**
R: Sim, se metricas forem EXCELENTES. Melhor 10 usuarios com NPS 80 e retention 70% do que 100 usuarios com NPS 10 e retention 20%. Qualidade > quantidade para validacao.

### Proximo Passo Pos-Validacao

**P: Validei (EXPANDIR). Qual o proximo passo?**
R: 1) Criar roadmap de features baseado em feedback, 2) Definir estrategia de aquisicao, 3) Otimizar conversao e monetizacao, 4) Construir processos de suporte, 5) Considerar investimento/time.

**P: Pivotei. Devo usar o MVPBuilder de novo?**
R: Sim. Volte para ProblemHypothesisDefinition com nova hipotese. Pode reutilizar partes do codigo/design, mas processo de validacao deve ser repetido com foco na nova direcao.

**P: Perseverei. Como medir se melhorou?**
R: Definir ANTES: "Se [metrica X] melhorar para [valor Y] em [tempo Z], validou". Exemplo: "Se retention 7-day subir para 40% em 3 semanas, expandir. Se nao, pivotar". Ter criterios claros evita auto-engano.

---

## Checkpoints

### Checkpoint 1: Early Adopters Onboarded (Dia 3)

**Objetivo:** Validar que early adopters comecaram a usar.

**O que validar:**
- [ ] 10-30 early adopters identificados e contatados
- [ ] Comunicacao de lancamento enviada
- [ ] Onboarding preparado e funcional
- [ ] Primeiros cadastros realizados
- [ ] Suporte inicial disponivel

### Checkpoint 2: Dados Coletados (Semana 2-3)

**Objetivo:** Validar que metricas e feedback foram coletados.

**O que validar:**
- [ ] Metricas quantitativas rastreadas (cadastros, ativacao, retencao)
- [ ] 10-15 entrevistas realizadas
- [ ] Survey enviado e respostas coletadas (30-50)
- [ ] Feedback documentado e organizado
- [ ] Problemas criticos identificados e resolvidos

### Checkpoint 3: Decisao Tomada (Semana 4)

**Objetivo:** Validar que hipotese foi analisada e decisao tomada.

**O que validar:**
- [ ] Hipotese original revisitada
- [ ] Componentes da hipotese validados ou invalidados
- [ ] Analise qualitativa completa
- [ ] Analise quantitativa completa
- [ ] Decisao estrategica tomada (PIVOTAR/PERSEVERAR/EXPANDIR)
- [ ] Relatorio de validacao completo
- [ ] Retrospectiva realizada
- [ ] Proximo passo definido

---

## Glossario

**Early Adopter:** Primeiro usuario disposto a usar produto imperfeito e dar feedback.

**AARRR (Pirate Metrics):** Framework de metricas: Acquisition, Activation, Retention, Revenue, Referral.

**Activation:** Usuario completou acao core do produto pela primeira vez.

**Retention:** Usuario voltou para usar produto novamente apos primeiro uso.

**Churn:** Usuario parou de usar produto.

**Cohort Analysis:** Analise de grupos de usuarios que comecaram a usar no mesmo periodo.

**NPS (Net Promoter Score):** Metrica de 0-10 perguntando se usuario recomendaria. Formula: % Promotores (9-10) - % Detratores (0-6).

**CSAT (Customer Satisfaction Score):** Metrica de satisfacao (1-5 ou 1-7).

**Validated Learning:** Aprendizado com evidencias (metricas + feedback real).

**Pivot:** Mudanca fundamental em hipotese baseada em aprendizados.

**Perseverar:** Manter direcao mas fazer ajustes baseados em feedback.

**Expandir:** Investir em crescimento apos validacao de hipotese.

**Build-Measure-Learn:** Ciclo Lean Startup: construir MVP, medir resultados, aprender e decidir.

**Vanity Metrics:** Metricas que parecem boas mas nao indicam valor real (ex: pageviews sem conversao).

**Actionable Metrics:** Metricas que informam decisoes (ex: retention, activation).

---

## Checklist Rapido: Validacao Completa?

### Lancamento
- [ ] 10-30 early adopters onboarded
- [ ] MVP em producao e acessivel
- [ ] Metricas sendo rastreadas
- [ ] Suporte disponivel

### Metricas Quantitativas (2-4 semanas)
- [ ] Cadastros rastreados
- [ ] Ativacao rastreada (% que completa acao core)
- [ ] Retencao rastreada (% que volta em 7 dias)
- [ ] Conversao rastreada (se aplicavel)
- [ ] NPS coletado (se aplicavel)

### Feedback Qualitativo
- [ ] 10-15 entrevistas realizadas
- [ ] Insights documentados
- [ ] Padroes identificados

### Feedback Quantitativo
- [ ] Survey enviado
- [ ] 30-50 respostas coletadas
- [ ] Resultados analisados

### Analise de Hipotese
- [ ] Hipotese original revisitada
- [ ] QUEM validado ou invalidado
- [ ] RESULTADO validado ou invalidado
- [ ] DOR validado ou invalidado
- [ ] Evidencias documentadas

### Decisao Estrategica
- [ ] Decisao tomada: PIVOTAR / PERSEVERAR / EXPANDIR
- [ ] Justificativa documentada
- [ ] Proximo passo definido
- [ ] Relatorio completo criado
- [ ] Retrospectiva realizada

Se todos os itens estao marcados, validacao esta completa e pronta para proximo passo!

---

**Ultima atualizacao:** 2025-11-05
**Mantido por:** Framework Business Team
**Parte de:** Estrategia MVPBuilder (Etapa 7)
