# Validador - Engenharia Reversa de SaaS

## Propósito

Este documento define os critérios de validação e qualidade que devem ser atendidos ao executar o processo de Engenharia Reversa de SaaS. Use este validador para garantir que a análise seja completa, objetiva e gere hipóteses acionáveis de diferenciação.

## Critérios de Validação por Etapa

### Validação - Etapa 1: Coleta de Contexto

**Critério 1.1: Clareza de objetivos**
- [ ] Objetivos de negócio estão claramente articulados (não vagos como "entender mercado")
- [ ] Há especificidade sobre que decisões a análise informará
- [ ] Expectativas realistas sobre o que a análise pode entregar

**Critério 1.2: Especificidade de mercado-alvo**
- [ ] Mercado-alvo é específico (não apenas "empresas" ou "B2B")
- [ ] Geografia definida (Brasil, LATAM, global)
- [ ] Segmento claro (SMB, mid-market, enterprise)
- [ ] Vertical/indústria especificada (se aplicável)

**Critério 1.3: Documentação de restrições**
- [ ] Restrições de orçamento documentadas
- [ ] Timeline desejado especificado
- [ ] Capacidades técnicas da equipe avaliadas
- [ ] Outras limitações conhecidas listadas

**Critério 1.4: Critérios de diferenciação estabelecidos**
- [ ] Tipo de diferencial buscado está claro (preço, features, nicho, UX)
- [ ] O que NÃO quer fazer está documentado
- [ ] Premissas sobre mercado estão explícitas

**Como validar:**
Pergunte: "Se eu ler este contexto daqui a 1 mês, terei clareza sobre por que fiz a análise e o que busco?"
Se NÃO, refine objetivos e critérios.

---

### Validação - Etapa 2: Mapeamento de Competidores e URLs

**Critério 2.1: Número e relevância de competidores**
- [ ] Pelo menos 3 competidores identificados
- [ ] Competidores são relevantes (diretos ou próximos, não distantes)
- [ ] Inclui variedade (líder + challengers + nichos)
- [ ] Justificativa para escolha de competidores (por que esses?)

**Critério 2.2: Cobertura de URLs**
- [ ] Cada competidor tem no mínimo 2 URLs (home + pricing)
- [ ] URLs obrigatórias coletadas (homepage, pricing)
- [ ] URLs recomendadas incluídas quando possível (features, FAQ, about)
- [ ] Média de 4-6 URLs por competidor

**Critério 2.3: Qualidade das URLs**
- [ ] Todas URLs verificadas e funcionando
- [ ] URLs são públicas (não requerem login ou paywall)
- [ ] URLs não estão quebradas ou desatualizadas
- [ ] URLs relevantes para análise (não blog posts aleatórios)

**Critério 2.4: Organização**
- [ ] URLs organizadas em estrutura clara (planilha ou documento)
- [ ] Estrutura facilita coleta sistemática na Etapa 3
- [ ] Total de URLs mapeadas documentado

**Como validar:**
Pergunte: "Estas URLs fornecem informação suficiente para entender problema, solução, pricing, ICP e diferencial de cada competidor?"
Se NÃO, adicione mais URLs.

**Ponto de Decisão:**
Se URLs não fornecem cobertura suficiente, retorne e adicione mais URLs ou competidores alternativos.

---

### Validação - Etapa 3: Extração de Informações

**Critério 3.1: Completude da extração**
- [ ] Pelo menos 70% das informações planejadas foram coletadas
- [ ] Informações críticas completas: problema, solução, pricing, ICP
- [ ] Gaps claramente identificados (marcados como "N/A" ou "não disponível")
- [ ] Arquivo individual criado para cada competidor

**Critério 3.2: Evidência e citações**
- [ ] Citações diretas capturadas quando relevantes (taglines, value props)
- [ ] Fonte (URL) anotada para informações principais
- [ ] Screenshots incluídos para elementos visuais importantes (se aplicável)
- [ ] Linguagem específica preservada (não parafraseada demais)

**Critério 3.3: Objetividade**
- [ ] Informações são fatos observados, não interpretações
- [ ] Evita julgamento prematuro ("este pricing é ruim")
- [ ] Captura o que está lá, não o que esperava ver
- [ ] Viés minimizado

**Critério 3.4: Estrutura e organização**
- [ ] Formato consistente entre arquivos de competidores
- [ ] Informações organizadas em seções claras
- [ ] Fácil encontrar informação específica
- [ ] Pronto para análise na Etapa 4

**Como validar:**
Pergunte: "Tenho informação suficiente para criar análise estruturada de cada competidor sem precisar voltar às URLs?"
Se NÃO, complete gaps críticos.

**Ponto de Decisão:**
Se extração está abaixo de 70%, execute fallback manual para gaps críticos ou ajuste expectativas.

---

### Validação - Etapa 4: Análise Individual de Competidores

**Critério 4.1: Profundidade da análise**
- [ ] Análise vai além de repetir informações coletadas
- [ ] Identifica padrões e nuances
- [ ] Inclui insights sobre pontos fortes e fracos
- [ ] Conecta diferentes aspectos (ex: pricing revela algo sobre ICP)

**Critério 4.2: Completude das seções**
- [ ] Resumo executivo claro e conciso (2-3 frases)
- [ ] Problema e solução sintetizados
- [ ] Principal diferencial identificado e analisado
- [ ] Pricing analisado (não apenas listado)
- [ ] ICP observado descrito com evidência
- [ ] Features críticas listadas e categorizadas
- [ ] Posicionamento analisado
- [ ] Observações incluem insights únicos

**Critério 4.3: Consistência entre competidores**
- [ ] Formato é consistente entre todos os competidores
- [ ] Mesmas dimensões analisadas para todos
- [ ] Facilita comparação side-by-side
- [ ] Nível de profundidade similar

**Critério 4.4: Objetividade e evidência**
- [ ] Análise baseada em evidência das URLs
- [ ] Evita suposições não fundamentadas
- [ ] Distingue entre o que competidor diz e o que parece ser real
- [ ] Observações são balanceadas (não apenas críticas)

**Como validar:**
Pergunte: "Esta análise me ajuda a entender não só O QUE o competidor faz, mas COMO e POR QUÊ?"
Se NÃO, aprofunde análise.

---

### Validação - Etapa 5: Síntese Comparativa

**Critério 5.1: Identificação de convergências**
- [ ] Padrões comuns claramente identificados
- [ ] Convergências documentadas por dimensão (problema, pricing, ICP, features)
- [ ] "Table stakes" (essenciais do mercado) identificados
- [ ] Consensos sobre o problema e solução reconhecidos

**Critério 5.2: Identificação de divergências**
- [ ] Diferenças entre competidores documentadas
- [ ] Divergências analisadas (não apenas listadas)
- [ ] Dimensões de diferenciação exploradas identificadas
- [ ] Abordagens únicas destacadas

**Critério 5.3: Identificação de gaps**
- [ ] Pelo menos 3 gaps ou oportunidades identificadas
- [ ] Gaps baseados em evidência da análise
- [ ] Gaps são concretos e acionáveis (não abstratos)
- [ ] Potencial de cada gap avaliado

**Critério 5.4: Tabelas comparativas**
- [ ] Tabela de pricing criada e útil
- [ ] Tabela de features criada
- [ ] Tabela de ICP criada (se aplicável)
- [ ] Tabelas facilitam identificação de padrões

**Critério 5.5: Insights e implicações**
- [ ] Síntese vai além de listar - identifica padrões
- [ ] Insights principais documentados
- [ ] Implicações para diferenciação articuladas
- [ ] Conexões entre dimensões identificadas

**Como validar:**
Pergunte: "Esta síntese revela oportunidades claras de diferenciação que não eram óbvias antes da análise?"
Se NÃO, aprofunde análise comparativa.

**Ponto de Decisão:**
Se não identificou pelo menos 3 oportunidades claras, retorne e analise competidores adicionais ou aprofunde análise existente.

---

### Validação - Etapa 6: Hipóteses de Diferenciação

**Critério 6.1: Número e variedade**
- [ ] Pelo menos 5 hipóteses geradas
- [ ] Hipóteses exploram diferentes dimensões (ICP, solução, modelo, posicionamento)
- [ ] Variedade de níveis de ousadia (incrementais e radicais)
- [ ] Não são todas variações da mesma ideia

**Critério 6.2: Estrutura das hipóteses**
- [ ] Cada hipótese usa template estruturado
- [ ] PROBLEMA está claro em cada hipótese
- [ ] ICP ESPECÍFICO está definido
- [ ] ABORDAGEM DIFERENCIADA está articulada
- [ ] CONTRASTE com competidores está explícito

**Critério 6.3: Justificativa e evidência**
- [ ] Cada hipótese tem justificativa baseada na análise
- [ ] Não são ideias desconectadas da análise comparativa
- [ ] Evidência específica da síntese é citada
- [ ] Lógica da oportunidade é clara

**Critério 6.4: Avaliação de viabilidade**
- [ ] Riscos identificados para cada hipótese
- [ ] Premissas explicitadas
- [ ] Viabilidade avaliada (alta/média/baixa)
- [ ] Alinhamento com contexto de negócio verificado

**Critério 6.5: Priorização**
- [ ] Top 2-3 hipóteses priorizadas
- [ ] Critérios de priorização explícitos
- [ ] Recomendação clara com justificativa
- [ ] Próximos passos definidos

**Critério 6.6: Acionabilidade**
- [ ] Hipóteses podem ser testadas/validadas
- [ ] Clareza sobre como validar (ex: ZeroUm, entrevistas)
- [ ] Não são vagas demais para agir
- [ ] Não requerem capacidades impossíveis

**Como validar:**
Pergunte: "Posso tomar estas hipóteses e iniciar processo de validação imediatamente (ex: executar ZeroUm)?"
Se NÃO, refine para maior especificidade e acionabilidade.

---

## Checklist de Validação Completa

Use este checklist ao final do processo para garantir que todos os critérios foram atendidos:

### Qualidade do Contexto
- [ ] Objetivos claramente articulados (1.1)
- [ ] Mercado-alvo específico definido (1.2)
- [ ] Restrições documentadas (1.3)
- [ ] Critérios de diferenciação estabelecidos (1.4)

### Qualidade do Mapeamento
- [ ] Pelo menos 3 competidores relevantes (2.1)
- [ ] Mínimo 2 URLs por competidor (2.2)
- [ ] URLs verificadas e funcionando (2.3)
- [ ] Estrutura organizada (2.4)

### Qualidade da Extração
- [ ] Pelo menos 70% de completude (3.1)
- [ ] Citações diretas e fontes anotadas (3.2)
- [ ] Objetividade mantida (3.3)
- [ ] Formato consistente (3.4)

### Qualidade da Análise Individual
- [ ] Profundidade além de superfície (4.1)
- [ ] Todas seções completas (4.2)
- [ ] Consistência entre competidores (4.3)
- [ ] Baseado em evidência (4.4)

### Qualidade da Síntese
- [ ] Convergências identificadas (5.1)
- [ ] Divergências documentadas (5.2)
- [ ] Pelo menos 3 gaps identificados (5.3)
- [ ] Tabelas comparativas criadas (5.4)
- [ ] Insights e implicações articulados (5.5)

### Qualidade das Hipóteses
- [ ] Pelo menos 5 hipóteses geradas (6.1)
- [ ] Template estruturado usado (6.2)
- [ ] Justificativas baseadas em análise (6.3)
- [ ] Viabilidade avaliada (6.4)
- [ ] Top 2-3 priorizadas (6.5)
- [ ] Hipóteses acionáveis (6.6)

### Prontidão para Próximos Passos
- [ ] Hipótese escolhida pode alimentar ZeroUm ou processo de validação
- [ ] Clareza sobre como validar hipótese
- [ ] Alinhamento com contexto de negócio mantido
- [ ] Documentação completa e acessível

---

## Indicadores de Qualidade

### Indicadores Quantitativos

**KPI 1: Completude da extração**
- Meta: 70%+ das informações planejadas coletadas
- Medição: (Informações coletadas / Informações planejadas) x 100
- Sinal de alerta: Abaixo de 60% indica gaps críticos

**KPI 2: Número de competidores**
- Meta: 3-5 competidores
- Medição: Contagem de competidores analisados
- Sinal de alerta: Menos de 3 (padrões insuficientes) ou mais de 7 (perda de profundidade)

**KPI 3: Número de gaps/oportunidades**
- Meta: Pelo menos 3 oportunidades claras identificadas
- Medição: Contagem de gaps na síntese comparativa
- Sinal de alerta: Menos de 3 pode indicar análise superficial

**KPI 4: Número de hipóteses**
- Meta: 5-10 hipóteses
- Medição: Contagem de hipóteses geradas
- Sinal de alerta: Menos de 5 (exploração insuficiente) ou mais de 15 (falta de foco)

**KPI 5: Tempo até conclusão**
- Meta: 3-5 horas
- Medição: Tempo real gasto do início ao fim
- Sinal de alerta: Menos de 2 horas (superficial) ou mais de 8 horas (paralisia por análise)

### Indicadores Qualitativos

**Profundidade da análise**
- Vai além de taglines e informações superficiais
- Identifica nuances e padrões não óbvios
- Conecta dimensões (pricing + ICP + features)

**Objetividade**
- Baseada em evidência, não suposições
- Evita viés e julgamento prematuro
- Distingue fatos de interpretações

**Acionabilidade das hipóteses**
- Hipóteses são específicas e testáveis
- Clareza sobre como validar
- Alinhadas com contexto e recursos

**Alinhamento com contexto**
- Análise informada por objetivos definidos
- Hipóteses respeitam restrições
- Diferenciação alinha com critérios estabelecidos

---

## Sinais de Alerta

### Sinais de que o processo precisa revisão

**Sinal 1: Contexto vago ou ausente**
- Sintoma: Objetivos genéricos ("entender mercado"), mercado-alvo indefinido
- Impacto: Análise sem direção, hipóteses desconectadas de necessidades
- Ação: Retorne à Etapa 1, refine contexto com especificidade

**Sinal 2: Cobertura insuficiente de URLs**
- Sintoma: Apenas homepage de competidores, pricing ausente
- Impacto: Informações críticas (pricing, ICP, features) faltando
- Ação: Retorne à Etapa 2, adicione URLs essenciais

**Sinal 3: Extração superficial**
- Sintoma: Apenas taglines copiadas, sem contexto ou citações diretas
- Impacto: Análise rasa, padrões não identificados
- Ação: Retorne à Etapa 3, aprofunde extração com citações e evidência

**Sinal 4: Análise repetitiva**
- Sintoma: Análise individual apenas repete informações coletadas sem síntese
- Impacto: Não adiciona valor, não gera insights
- Ação: Retorne à Etapa 4, adicione observações, insights e análise crítica

**Sinal 5: Síntese sem padrões**
- Sintoma: Síntese apenas lista competidores lado a lado sem identificar convergências/divergências
- Impacto: Oportunidades de diferenciação não reveladas
- Ação: Retorne à Etapa 5, busque ativamente padrões e gaps

**Sinal 6: Hipóteses genéricas**
- Sintoma: Hipóteses vagas ("seremos melhores em UX"), sem especificidade
- Impacto: Não são testáveis ou acionáveis
- Ação: Retorne à Etapa 6, use template estruturado, seja específico

**Sinal 7: Hipóteses desconectadas**
- Sintoma: Hipóteses não baseadas em gaps identificados na análise
- Impacto: Diferenciação forçada, não fundamentada
- Ação: Retorne à Etapa 6, base hipóteses na síntese comparativa

**Sinal 8: Falta de priorização**
- Sintoma: Muitas hipóteses, nenhuma recomendação clara
- Impacto: Paralisia de decisão, próximos passos indefinidos
- Ação: Retorne à Etapa 6, priorize top 2-3 com critérios explícitos

**Sinal 9: Desalinhamento com contexto**
- Sintoma: Hipóteses requerem recursos/capacidades não disponíveis
- Impacto: Não são viáveis, desperdiçam tempo
- Ação: Retorne à Etapa 6, verifique alinhamento com contexto de negócio

**Sinal 10: Paralisia por análise**
- Sintoma: Mais de 8 horas gastas, ainda analisando mais competidores
- Impacto: Tempo desperdiçado, validação com usuários adiada
- Ação: PARE. Finalize com o que tem, passe para validação

---

## Critérios de Sucesso Final

O processo de Engenharia Reversa de SaaS é considerado bem-sucedido quando:

1. **Contexto claro e direcionado**
   - [ ] Objetivos, mercado-alvo e restrições documentados
   - [ ] Critérios de diferenciação estabelecidos
   - [ ] Análise está alinhada com contexto

2. **Mapeamento completo**
   - [ ] 3-5 competidores relevantes identificados
   - [ ] 15-30 URLs organizadas
   - [ ] Cobertura suficiente para análise (home + pricing + mais)

3. **Extração de qualidade**
   - [ ] 70%+ das informações planejadas coletadas
   - [ ] Citações diretas e fontes preservadas
   - [ ] Objetividade mantida

4. **Análise profunda**
   - [ ] 3-5 análises individuais completas
   - [ ] Profundidade além de superfície
   - [ ] Insights e observações documentados

5. **Síntese reveladora**
   - [ ] Convergências e divergências identificadas
   - [ ] Pelo menos 3 gaps/oportunidades claros
   - [ ] Padrões de mercado reconhecidos
   - [ ] Implicações para diferenciação articuladas

6. **Hipóteses acionáveis**
   - [ ] 5-10 hipóteses estruturadas geradas
   - [ ] Baseadas em evidência da análise
   - [ ] Top 2-3 priorizadas
   - [ ] Viabilidade e riscos avaliados
   - [ ] Próximos passos definidos

7. **Eficiência**
   - [ ] Processo completado em 3-5 horas
   - [ ] Não há paralisia por análise
   - [ ] Pronto para validação

8. **Documentação completa**
   - [ ] Todos artefatos criados e organizados
   - [ ] Acessível para equipe
   - [ ] Rastreável (fontes anotadas)

---

## Perguntas de Verificação Final

Antes de considerar o processo concluído, responda estas perguntas:

1. **Teste de contexto**
   - A análise está claramente conectada aos objetivos de negócio?
   - Hipóteses alinham com mercado-alvo e restrições?

2. **Teste de completude**
   - Tenho informação suficiente sobre problema, solução, pricing e ICP de cada competidor?
   - Gaps são aceitáveis ou críticos?

3. **Teste de profundidade**
   - A análise vai além de informações superficiais?
   - Identifiquei padrões não óbvios?

4. **Teste de diferenciação**
   - Identifiquei pelo menos 3 oportunidades claras de diferenciação?
   - Oportunidades são baseadas em gaps reais, não ideias aleatórias?

5. **Teste de acionabilidade**
   - As hipóteses são específicas o suficiente para validar?
   - Sei exatamente qual próximo passo tomar (ex: executar ZeroUm)?

6. **Teste de viabilidade**
   - As hipóteses priorizadas são alcançáveis com recursos disponíveis?
   - Alinhadas com capacidades e timeline?

7. **Teste de documentação**
   - Se eu ler esta análise daqui a 1 mês, terei contexto completo?
   - Consigo rastrear de volta às fontes se necessário?

8. **Teste de eficiência**
   - Gastei tempo proporcional ao valor gerado (não mais de 5 horas)?
   - Estou pronto para agir, ou ainda analisando?

**Se a resposta para qualquer pergunta for "não", revisite a seção relevante e refine.**

---

## Uso do Validador

### Quando usar este validador

- **Durante a execução:** Use critérios de cada etapa como checklist enquanto trabalha
- **Ao final de cada etapa:** Verifique que critérios foram atendidos antes de prosseguir
- **Ao final do processo:** Use checklist completo para verificação final
- **Antes de próximos passos:** Valide que está pronto para executar ZeroUm ou validação
- **Em reviews:** Use para revisão por pares ou aprovação de stakeholders

### Como usar os critérios

- Cada critério deve ser verificável com "sim" ou "não"
- Se critério falhar, refine elemento relevante antes de prosseguir
- Use "Perguntas de Verificação" como guia prático
- Use "Sinais de Alerta" para diagnóstico rápido de problemas

### Responsabilidade pela validação

- **Executor do processo:** Verifica critérios durante e após execução
- **Revisor (se aplicável):** Valida checklist completo antes de aprovar
- **Equipe:** Valida alinhamento das hipóteses com objetivos e contexto

---

**Última atualização:** 2025-01-06
**Versão:** 1.0
