# Tarefas - Engenharia Reversa de SaaS

## Visão Geral

Este documento lista a sequência operacional de tarefas para executar o processo de Engenharia Reversa de SaaS. Cada tarefa corresponde às etapas descritas no [process.MD](process.MD) e deve ser executada na ordem apresentada.

Tempo total estimado: 3-5 horas

## Lista de Tarefas

### Tarefa 1: Coletar contexto de negócio
**Etapa correspondente:** Etapa 1
**Tempo estimado:** 15 minutos
**Responsável:** Product Owner / Fundador / PM

**Objetivo:**
Capturar clareza sobre objetivos, mercado-alvo e restrições que guiarão toda a análise.

**Passos:**
1. Abra o template de contexto de negócio (_DATA/templates/contexto-negocio.md)
2. Responda perguntas sobre objetivos:
   - Por que fazer esta análise?
   - Que decisões ela informará?
   - O que você quer alcançar?
3. Defina mercado-alvo:
   - Geografia (Brasil, LATAM, global)
   - Segmento (SMB, mid-market, enterprise)
   - Vertical/indústria (se aplicável)
4. Liste restrições conhecidas:
   - Orçamento disponível
   - Timeline desejado
   - Capacidades técnicas da equipe
5. Estabeleça critérios de diferenciação:
   - Que tipo de diferencial busca? (preço, features, nicho, UX)
   - O que NÃO quer fazer?
6. Documente premissas sobre o mercado

**Ferramentas:**
- Template de Contexto de Negócio (_DATA/templates/)
- Editor de texto ou Google Docs

**Critérios de conclusão:**
- [ ] Objetivos claramente articulados
- [ ] Mercado-alvo específico definido (não apenas "empresas")
- [ ] Restrições documentadas
- [ ] Critérios de diferenciação estabelecidos
- [ ] Passa no Checkpoint 1 do knowledge.MD

**Output esperado:**
Documento de contexto com:
- Objetivos de negócio (2-3 frases)
- Mercado-alvo específico
- Restrições conhecidas
- Critérios de diferenciação preferidos

**Exemplo de output:**
```
OBJETIVOS:
Validar oportunidade de criar ferramenta de project management focada em equipes de design. Decisão: vale a pena entrar neste mercado? Se sim, qual diferencial perseguir?

MERCADO-ALVO:
- Geografia: Brasil inicialmente, LATAM depois
- Segmento: Equipes de design de 3-15 pessoas em startups e agências
- Vertical: Design/Creative

RESTRIÇÕES:
- Orçamento: R$ 50k para MVP
- Timeline: Lançar em 3 meses
- Capacidades: Equipe técnica pequena (2 devs), sem designer dedicado

CRITÉRIOS DE DIFERENCIAÇÃO:
- Busco: Nicho específico (design teams), UX superior, integrações com design tools
- NÃO quero: Competir em preço, criar ferramenta genérica
```

---

### Tarefa 2: Mapear competidores e URLs
**Etapa correspondente:** Etapa 2
**Tempo estimado:** 20 minutos
**Responsável:** Product Owner / Analista de Produto

**Objetivo:**
Identificar 3-5 competidores relevantes e organizar URLs para coleta sistemática.

**Passos:**
1. Liste 3-5 competidores SaaS a analisar:
   - Pelo menos 1 líder de mercado
   - 1-2 challengers (crescimento rápido)
   - 1-2 nichos ou especializados
2. Para cada competidor, colete URLs (use template de mapeamento):
   - Homepage (obrigatório)
   - Pricing page (obrigatório)
   - Features/Product (recomendado)
   - FAQ/Help Center (recomendado)
   - About/Company (opcional)
   - Case studies (opcional)
   - Documentation (se relevante)
3. Verifique que URLs estão funcionando:
   - Abra cada URL rapidamente
   - Confirme que são públicas (sem login)
   - Substitua URLs quebradas
4. Organize em planilha ou documento estruturado
5. Estime cobertura: média de quantas URLs por competidor?

**Ferramentas:**
- Template de Mapeamento de URLs (_DATA/templates/)
- Browser para verificar URLs
- Planilha ou Markdown para organização

**Critérios de conclusão:**
- [ ] Pelo menos 3 competidores identificados
- [ ] Cada competidor tem mínimo 2 URLs (home + pricing)
- [ ] Todas URLs verificadas e funcionando
- [ ] Lista organizada e pronta para Etapa 3
- [ ] Passa no Checkpoint 2 do knowledge.MD

**Output esperado:**
Planilha ou documento com estrutura:
```
COMPETIDOR 1: [Nome]
- Homepage: [URL]
- Pricing: [URL]
- Features: [URL]
- FAQ: [URL]
- About: [URL]

COMPETIDOR 2: [Nome]
...

TOTAL: X competidores, Y URLs
```

**Exemplo de output:**
```
COMPETIDOR 1: Notion
- Homepage: https://notion.so
- Pricing: https://notion.so/pricing
- Features: https://notion.so/product
- Help: https://notion.so/help
- About: https://notion.so/about

COMPETIDOR 2: Coda
- Homepage: https://coda.io
- Pricing: https://coda.io/pricing
- Features: https://coda.io/product
- Gallery: https://coda.io/gallery

COMPETIDOR 3: Airtable
- Homepage: https://airtable.com
- Pricing: https://airtable.com/pricing
- Features: https://airtable.com/features

TOTAL: 3 competidores, 13 URLs
```

**Ponto de Decisão 1:**
- URLs fornecem informação suficiente sobre competidores?
- Se NÃO: Adicione mais URLs ou competidores alternativos

---

### Tarefa 3: Extrair informações das URLs
**Etapa correspondente:** Etapa 3
**Tempo estimado:** 60-90 minutos
**Responsável:** AI Agent + Humano (fallback)

**Objetivo:**
Coletar informações estruturadas de cada competidor através de scraping automatizado com fallback manual.

**Passos:**
1. **Para cada competidor, execute coleta automatizada:**
   - Use ferramentas de web fetch para extrair conteúdo de cada URL
   - AI processa conteúdo e preenche template de análise
   - Marque informações coletadas com sucesso
   - Identifique gaps (informações não encontradas)

2. **Para gaps ou falhas de scraping, execute fallback manual:**
   - Humano acessa URL problemática
   - Copia textos relevantes (taglines, descrições, pricing)
   - Tira screenshots de elementos visuais importantes
   - Fornece conteúdo para AI processar

3. **Informações a extrair (use template de análise):**
   - Nome completo e tagline/slogan
   - Problema principal que resolve (como descrevem)
   - Solução oferecida (como funciona)
   - Principal diferencial competitivo
   - Features principais (top 3-5)
   - Pricing detalhado (tiers, valores, modelo)
   - ICP observado (descrições de clientes, cases, testimonials)
   - Casos de uso mencionados
   - Linguagem específica usada (citações diretas)
   - Social proof (clientes, métricas, logos)

4. **Organize outputs:**
   - Crie arquivo individual por competidor
   - Nomeie: `competidor-[nome-do-competidor].md`
   - Use template estruturado
   - Inclua fonte (URL) para cada informação

5. **Verifique completude:**
   - Calcule % de informações coletadas
   - Identifique gaps críticos vs. opcionais
   - Decida se precisa coleta adicional

**Ferramentas:**
- WebFetch ou ferramentas de scraping
- Template de Análise de Competidor (_DATA/templates/)
- Screenshot tool para capturas visuais
- Editor de texto

**Critérios de conclusão:**
- [ ] Arquivo individual criado para cada competidor (3-5 arquivos)
- [ ] Pelo menos 70% das informações planejadas coletadas
- [ ] Informações críticas (problema, solução, pricing, ICP) completas
- [ ] Citações diretas capturadas quando relevantes
- [ ] Fonte (URL) anotada para informações principais
- [ ] Gaps claramente marcados (ex: "N/A - não disponível")
- [ ] Passa no Checkpoint 3 do knowledge.MD

**Output esperado:**
Para cada competidor, arquivo markdown com:
```
# Análise: [Nome do Competidor]

## Informações Básicas
- Nome: [Nome completo]
- Tagline: "[Citação direta]"
- Website: [URL]
- Data da análise: [Data]

## Problema e Solução
- Problema: "[Como descrevem o problema]"
  Fonte: [URL da page]
- Solução: "[Como descrevem a solução]"
  Fonte: [URL]

## Principal Diferencial
"[Citação ou síntese do diferencial]"
Fonte: [URL]

## Features Principais
1. [Feature 1] - [breve descrição]
2. [Feature 2]
...
Fonte: [URL]

## Pricing
- Tier 1: [Nome] - [Preço] - [Principais limitações/benefícios]
- Tier 2: ...
Modelo de cobrança: [subscription/usage/freemium/etc.]
Fonte: [URL]

## ICP Observado
[Descrição do cliente ideal com base em cases, testimonials, linguagem]
Exemplos de clientes mencionados: [Lista]
Fonte: [URLs]

## Casos de Uso
- [Caso 1]
- [Caso 2]
...

## Linguagem e Posicionamento
Palavras-chave frequentes: [lista]
Tom: [profissional/casual/técnico/etc.]
Citações relevantes: "[citação 1]", "[citação 2]"

## Social Proof
- Clientes: [logos, nomes]
- Métricas: [usuários, empresas, etc.]
- Prêmios/Reconhecimentos: [lista]
Fonte: [URLs]

## Screenshots
[Links ou anexos de screenshots]

## Observações
[Insights únicos, pontos fortes/fracos observados]
```

**Ponto de Decisão 2:**
- Conseguiu extrair pelo menos 70% das informações planejadas?
- Se NÃO: Execute fallback manual para gaps críticos ou ajuste expectativas

---

### Tarefa 4: Analisar cada competidor individualmente
**Etapa correspondente:** Etapa 4
**Tempo estimado:** 45-60 minutos (15-20 min por competidor)
**Responsável:** Product Owner / Analista de Produto

**Objetivo:**
Sintetizar informações coletadas em análise estruturada e insights para cada competidor.

**Passos:**
1. Para cada arquivo de informações coletadas (Tarefa 3):

2. **Escreva resumo executivo (2-3 frases):**
   - Quem é o competidor?
   - O que fazem?
   - Para quem?

3. **Sintetize problema e solução:**
   - Qual dor resolvem? (síntese, não cópia)
   - Como resolvem? (alto nível)
   - Por que abordagem deles faz sentido (ou não)?

4. **Identifique principal diferencial:**
   - O que eles destacam como único?
   - É diferencial real ou apenas marketing?
   - Como comunicam esse diferencial?

5. **Analise pricing:**
   - Modelo de cobrança
   - Faixa de preço
   - O que diferencia cada tier?
   - Pricing revela algo sobre ICP? (ex: tier enterprise = foco B2B)

6. **Descreva ICP observado:**
   - Baseado em cases, testimonials, linguagem
   - Tamanho de empresa, indústria, role
   - ICP primário vs. secundário (se aplicável)

7. **Liste features críticas:**
   - Top 3-5 capacidades essenciais
   - O que parece ser "table stakes" vs. diferencial?

8. **Analise posicionamento:**
   - Como se comunicam? (tom, linguagem)
   - Que benefícios destacam?
   - Contra quem/o quê se posicionam?

9. **Adicione observações:**
   - Pontos fortes únicos
   - Pontos fracos ou gaps percebidos
   - Insights que não se encaixam em outras seções

**Ferramentas:**
- Arquivos de informações coletadas (Tarefa 3)
- Template de Análise de Competidor (seção de síntese)
- Editor de texto

**Critérios de conclusão:**
- [ ] Análise completa para cada competidor (3-5 documentos)
- [ ] Formato consistente entre todos
- [ ] Cada seção preenchida com informação concreta
- [ ] Insights vão além de repetir informações coletadas
- [ ] Observações incluem pontos fortes e fracos
- [ ] Passa no Checkpoint 4 do knowledge.MD

**Output esperado:**
Para cada competidor, seção de análise adicionada ao arquivo:
```
---
# ANÁLISE E SÍNTESE

## Resumo Executivo
[2-3 frases sobre o competidor]

## Problema e Solução (Síntese)
Problema: [Síntese do problema que resolvem]
Solução: [Como resolvem, alto nível]
Observação: [Por que abordagem faz sentido ou não]

## Principal Diferencial (Análise)
Diferencial comunicado: [O que destacam]
Diferencial real: [Avaliação se é real ou marketing]
Como comunicam: [Abordagem de messaging]

## Pricing (Análise)
Modelo: [subscription/usage/freemium/outro]
Faixa: [low-end a high-end]
Insights: [O que pricing revela sobre estratégia/ICP]

## ICP Observado (Síntese)
Primário: [Descrição do ICP principal]
Secundário: [Se aplicável]
Base: [Como chegou a essa conclusão - cases, testimonials, etc.]

## Features Críticas (Análise)
Table stakes: [Features que parecem essenciais]
Diferenciais: [Features únicas ou distintivas]

## Posicionamento (Análise)
Tom: [profissional/casual/técnico]
Benefícios destacados: [Lista]
Posicionamento contra: [Alternativas mencionadas]

## Observações
Pontos fortes: [Lista]
Pontos fracos/Gaps: [Lista]
Insights únicos: [Observações não categorizadas]
```

---

### Tarefa 5: Criar síntese comparativa
**Etapa correspondente:** Etapa 5
**Tempo estimado:** 30-45 minutos
**Responsável:** Product Owner / Analista de Produto

**Objetivo:**
Comparar competidores analisados para identificar padrões, convergências e oportunidades de diferenciação.

**Passos:**
1. Abra template de síntese comparativa

2. **Analise padrões de problema/solução:**
   - Crie tabela comparando como cada competidor descreve problema
   - Identifique problemas comuns a todos
   - Identifique problemas únicos a alguns
   - Sintetize: existe consenso sobre o problema?

3. **Compare diferenciais:**
   - Liste diferencial de cada competidor
   - Identifique diferenciais recorrentes (saturados)
   - Identifique diferenciais únicos (espaço aberto)
   - Avalie: que dimensões de diferenciação são exploradas?

4. **Analise pricing comparativamente:**
   - Crie tabela de pricing (tiers e valores)
   - Identifique faixa de mercado (low-end, mid, high-end)
   - Identifique modelos de cobrança dominantes
   - Identifique oportunidades (ex: ninguém tem freemium generoso)

5. **Compare ICPs:**
   - Liste ICP de cada competidor
   - Identifique sobreposição (todos atacam mesmo perfil?)
   - Identifique nichos desatendidos
   - Avalie: que segmentos são mais/menos competitivos?

6. **Analise features comparativamente:**
   - Liste features principais de cada competidor
   - Identifique "table stakes" (presentes em todos)
   - Identifique features diferenciais (presentes em poucos)
   - Identifique capacidades ausentes (ninguém oferece)

7. **Identifique gaps e oportunidades:**
   - O que todos fazem mal? (pontos fracos comuns)
   - O que ninguém faz? (capacidades ausentes)
   - Que nichos de ICP são ignorados?
   - Que modelos de pricing não são explorados?

8. **Documente padrões (convergências):**
   - Resuma o que é comum a todos ou maioria
   - Estes são provavelmente "table stakes" do mercado

9. **Documente divergências:**
   - Resuma onde competidores diferem
   - Estas são potenciais dimensões de diferenciação

**Ferramentas:**
- Análises individuais (Tarefa 4)
- Template de Síntese Comparativa (_DATA/templates/)
- Planilha para tabelas comparativas

**Critérios de conclusão:**
- [ ] Tabelas comparativas criadas (pricing, features, ICP)
- [ ] Convergências claramente identificadas
- [ ] Divergências documentadas
- [ ] Pelo menos 3 gaps ou oportunidades identificadas
- [ ] Síntese vai além de listar - identifica padrões
- [ ] Passa no Checkpoint 5 do knowledge.MD

**Output esperado:**
Documento de síntese com:
```
# Síntese Comparativa - [Mercado/Categoria]

## Competidores Analisados
1. [Competidor 1]
2. [Competidor 2]
3. [Competidor 3]
...

## Tabela Comparativa de Pricing
| Competidor | Modelo | Tier Básico | Tier Médio | Tier Alto | Observações |
|------------|--------|-------------|------------|-----------|-------------|
| [Nome]     | [...]  | [...]       | [...]      | [...]     | [...]       |

## Tabela Comparativa de Features
| Feature       | Comp 1 | Comp 2 | Comp 3 | Análise        |
|---------------|--------|--------|--------|----------------|
| [Feature]     | ✓      | ✓      | ✓      | Table stakes   |
| [Feature]     | ✓      | ✗      | ✗      | Diferencial    |

## Tabela Comparativa de ICP
| Competidor | ICP Primário | ICP Secundário | Observações |
|------------|--------------|----------------|-------------|
| [Nome]     | [...]        | [...]          | [...]       |

## Convergências (Padrões Comuns)

### Problema/Solução
- [Padrão 1: Todos resolvem X da forma Y]
- [Padrão 2: ...]

### Diferenciais
- [Padrão: Diferenciação comum em dimensão X]

### Pricing
- [Padrão: Faixa de mercado é USD X-Y]
- [Padrão: Modelo dominante é subscription]

### ICP
- [Padrão: Todos atacam segmento X]

### Features
- [Lista de table stakes - features presentes em todos]

## Divergências (Diferenças)

### Problema/Solução
- [Competidor X ataca subproblema único]

### Diferenciais
- [Lista de dimensões de diferenciação únicas]

### Pricing
- [Competidor Y tem modelo diferente]

### ICP
- [Competidor Z ataca nicho específico]

### Features
- [Features únicas por competidor]

## Gaps e Oportunidades Identificadas

1. **[Oportunidade 1]**
   - Descrição: [O que ninguém faz ou todos fazem mal]
   - Evidência: [Baseado em qual análise]
   - Potencial: [Por que é oportunidade]

2. **[Oportunidade 2]**
   ...

## Insights Principais

- [Insight 1]
- [Insight 2]
- [Insight 3]

## Implicações para Diferenciação

- [Implicação 1: Ex: "Table stakes são A, B, C - precisamos ter"]
- [Implicação 2: Ex: "Espaço aberto em dimensão X"]
- [Implicação 3: Ex: "ICP Y está desatendido"]
```

**Ponto de Decisão 3:**
- Identificou pelo menos 3 oportunidades claras de diferenciação?
- Se NÃO: Analise competidores adicionais ou aprofunde análise existente

---

### Tarefa 6: Gerar hipóteses de diferenciação
**Etapa correspondente:** Etapa 6
**Tempo estimado:** 30-45 minutos
**Responsável:** Product Owner / Fundador / PM

**Objetivo:**
Transformar análise comparativa em hipóteses acionáveis de como criar produto similar mas diferenciado.

**Passos:**
1. Revise síntese comparativa (Tarefa 5) e contexto de negócio (Tarefa 1)

2. **Para cada gap/oportunidade identificada, gere hipótese:**
   - Use template: "Nosso produto resolve [PROBLEMA] para [ICP ESPECÍFICO] através de [ABORDAGEM DIFERENCIADA], diferente dos competidores que [COMO COMPETIDORES FAZEM]."
   - Seja específico em cada elemento
   - Base em evidência da análise

3. **Explore 4 dimensões de diferenciação:**

   **A. Problema/ICP diferente:**
   - Mesmo problema para ICP desatendido
   - Subproblema negligenciado
   - Nicho vertical/geografia/tamanho

   **B. Solução diferente:**
   - Abordagem técnica distinta
   - UX radicalmente superior
   - Simplificação (fazer menos, melhor)

   **C. Modelo de negócio diferente:**
   - Pricing mais acessível/transparente
   - Modelo de cobrança alternativo
   - Go-to-market diferenciado

   **D. Posicionamento diferente:**
   - Linguagem e branding distintos
   - Benefício negligenciado
   - Contrarian (contra consenso)

4. **Para cada hipótese, documente:**
   - Declaração da hipótese (usando template)
   - Justificativa (base na análise)
   - Dimensão de diferenciação (A/B/C/D acima)
   - Riscos e premissas
   - Viabilidade inicial (alta/média/baixa)
   - Alinhamento com contexto de negócio

5. **Gere pelo menos 5-10 hipóteses**
   - Explore diferentes dimensões
   - Varie níveis de ousadia (incrementais e radicais)

6. **Priorize hipóteses:**
   - Avalie cada uma contra:
     - Viabilidade (recursos, capacidades)
     - Desejabilidade (ICP quer isso?)
     - Diferenciação (quão distintivo?)
     - Alinhamento com contexto
   - Selecione top 2-3 mais promissoras

7. **Defina próximos passos:**
   - Como validar hipótese escolhida?
   - Que processo usar? (ex: ZeroUm)
   - Que informação adicional é necessária?

**Ferramentas:**
- Síntese comparativa (Tarefa 5)
- Contexto de negócio (Tarefa 1)
- Template de Hipóteses de Diferenciação (_DATA/templates/)

**Critérios de conclusão:**
- [ ] Pelo menos 5 hipóteses geradas
- [ ] Cada hipótese usa template estruturado
- [ ] Justificativas baseiam-se na análise comparativa
- [ ] Riscos e viabilidade avaliados
- [ ] Top 2-3 hipóteses priorizadas e recomendadas
- [ ] Próximos passos definidos
- [ ] Alinhamento com contexto de negócio verificado
- [ ] Passa no Checkpoint 6 do knowledge.MD

**Output esperado:**
Documento de hipóteses:
```
# Hipóteses de Diferenciação - [Projeto]

Data: [Data]
Baseado em análise de: [Lista de competidores]

---

## Hipótese 1: [Título descritivo]

**Declaração:**
"Nosso produto resolve [PROBLEMA] para [ICP ESPECÍFICO] através de [ABORDAGEM DIFERENCIADA], diferente dos competidores que [COMO COMPETIDORES FAZEM]."

**Dimensão de diferenciação:** [Problema/ICP / Solução / Modelo de Negócio / Posicionamento]

**Justificativa:**
[Por que esta é oportunidade, baseado em qual evidência da análise]

**Riscos:**
- [Risco 1]
- [Risco 2]

**Premissas:**
- [Premissa 1: O que precisa ser verdade para isso funcionar]
- [Premissa 2]

**Viabilidade:** [Alta / Média / Baixa]
- Recursos: [Avaliação]
- Capacidades: [Avaliação]
- Timeline: [Estimativa]

**Alinhamento com contexto:** [Como alinha com objetivos, mercado, restrições]

---

## Hipótese 2: ...

[Repetir estrutura]

---

## Priorização e Recomendação

### Top 3 Hipóteses Priorizadas

**1. [Hipótese X] - RECOMENDADA**
- Por que: [Justificativa da priorização]
- Próximos passos: [O que fazer para validar]

**2. [Hipótese Y]**
- Por que: [Justificativa]
- Próximos passos: [...]

**3. [Hipótese Z]**
- Por que: [Justificativa]
- Próximos passos: [...]

### Critérios de Priorização Usados
- Viabilidade (recursos disponíveis)
- Desejabilidade (ICP valoriza?)
- Diferenciação (quão distinto?)
- Alinhamento com contexto de negócio

## Próximos Passos Recomendados

1. **Para Hipótese Escolhida ([Hipótese X]):**
   - Executar Estratégia ZeroUm usando esta hipótese como Etapa 0
   - Realizar entrevistas com ICP específico para validar problema
   - [Outros passos específicos]

2. **Validações Adicionais Necessárias:**
   - [Informação adicional a coletar]
   - [Premissas a testar]

3. **Decisões Pendentes:**
   - [Decisão 1 a ser tomada]
   - [Decisão 2]
```

---

## Resumo de Entregáveis

Ao final da execução de todas as tarefas, você deve ter:

1. **Contexto de Negócio** (Tarefa 1)
   - Objetivos, mercado, restrições documentados

2. **Mapa de Competidores e URLs** (Tarefa 2)
   - 3-5 competidores, 15-30 URLs organizadas

3. **Informações Extraídas** (Tarefa 3)
   - 3-5 arquivos com dados brutos por competidor

4. **Análises Individuais** (Tarefa 4)
   - 3-5 análises estruturadas e sintetizadas

5. **Síntese Comparativa** (Tarefa 5)
   - Documento com padrões, gaps, tabelas comparativas

6. **Hipóteses de Diferenciação** (Tarefa 6)
   - 5-10 hipóteses documentadas
   - Top 2-3 priorizadas
   - Próximos passos definidos

## Tempo Total

- Tarefa 1: 15 minutos
- Tarefa 2: 20 minutos
- Tarefa 3: 60-90 minutos
- Tarefa 4: 45-60 minutos
- Tarefa 5: 30-45 minutos
- Tarefa 6: 30-45 minutos

**Total: 3-5 horas**

## Notas Importantes

- Execute tarefas na ordem - cada depende da anterior
- Use checkpoints do knowledge.MD para verificar qualidade
- Não pule Tarefa 1 (contexto) - crítica para direcionar análise
- Limite profundidade para evitar paralisia (3-5 horas total)
- Priorize profundidade sobre amplitude (3-5 competidores, não 20)
- Base hipóteses na análise, não em ideias desconectadas
- Sempre retorne ao contexto ao priorizar hipóteses

## Próximos Passos Após Conclusão

Após completar todas as tarefas deste processo:

1. **Escolha uma hipótese priorizada** para perseguir
2. **Execute Estratégia ZeroUm** usando hipótese como Etapa 0
3. **Valide problema e diferencial** com ICP específico através de entrevistas
4. **Refine hipótese** baseado em aprendizados da validação
5. **Decida:** construir MVP, pivotar hipótese ou explorar alternativa

---

**Última atualização:** 2025-01-06
**Versão:** 1.0
