# Processo de Engenharia Reversa de SaaS

## Propósito

Este processo guia a análise estruturada de competidores SaaS através da extração sistemática de informações de suas landing pages, páginas de pricing, FAQ e outros materiais públicos. O objetivo é identificar oportunidades de diferenciação e construir uma base sólida de conhecimento para criar um produto similar mas diferenciado.

## Objetivo

Analisar 3-5 competidores SaaS através de múltiplas URLs (home, pricing, FAQ, about, features) para extrair:
- Problema principal que resolvem
- Solução oferecida
- Principal diferencial competitivo
- Modelo de precificação
- ICP (Ideal Customer Profile) observado
- Fundamentos de negócio validados
- Oportunidades de diferenciação

O resultado deve fornecer contexto rico e acionável para alimentar estratégias de desenvolvimento de produto (como ZeroUm) com foco em criar alternativa diferenciada.

## Escopo

### Dentro do escopo
- Coleta de URLs públicas de 3-5 competidores SaaS
- Extração de informações através de web scraping automatizado
- Fallback manual quando scraping falhar
- Análise estruturada de cada competidor
- Síntese comparativa identificando padrões e gaps
- Geração de hipóteses de diferenciação
- Documentação de contexto de negócio, mercado e restrições

### Fora do escopo
- Análise de código-fonte ou aspectos técnicos internos
- Acesso a materiais privados ou behind paywall
- Criação de contas para acessar áreas restritas
- Análise financeira detalhada ou due diligence
- Decisão final sobre qual diferencial perseguir (estratégia posterior)
- Execução da construção do produto

## Etapas do Processo

### Etapa 1: Coleta de Contexto de Negócio (15 minutos)

Antes de analisar competidores, capture o contexto estratégico que guiará a análise.

Perguntas orientadoras:
- Qual é o objetivo do seu negócio? (validação, lançamento rápido, entrada em novo mercado)
- Qual mercado-alvo você pretende atacar? (geografia, segmento, vertical)
- Existem restrições conhecidas? (orçamento, timeline, capacidades técnicas)
- Por que você escolheu esses competidores específicos?
- Que tipo de diferenciação você busca? (preço, features, experiência, nicho)

Resultado esperado:
- Documento de contexto preenchido com objetivos, mercado-alvo e restrições
- Clareza sobre critérios de análise
- Alinhamento sobre o que constitui "diferenciação valiosa"

### Etapa 2: Mapeamento de Competidores e URLs (20 minutos)

Identifique os competidores e organize as URLs a serem analisadas.

Atividades:
1. Liste 3-5 competidores SaaS a analisar
2. Para cada competidor, colete URLs de:
   - Homepage (obrigatório)
   - Pricing page (obrigatório)
   - Features/Product page (recomendado)
   - FAQ/Help Center (recomendado)
   - About/Company page (opcional)
   - Case studies/Testimonials (opcional)
   - Documentation/API (se relevante)
3. Verifique que todas as URLs são públicas e acessíveis
4. Organize em estrutura de coleta

Resultado esperado:
- Lista de 3-5 competidores
- Média de 4-6 URLs por competidor (mínimo 2: home + pricing)
- Total de 15-30 URLs mapeadas
- Planilha ou documento estruturado com URLs organizadas

### Etapa 3: Extração de Informações (60-90 minutos)

Execute a coleta de informações das URLs mapeadas usando abordagem híbrida.

Abordagem de coleta:
1. **Primeira tentativa - AI Agent Web Scraping:**
   - Use ferramentas de web fetch/scraping para extrair conteúdo
   - AI processa conteúdo extraído e preenche template estruturado
   - Identifique gaps ou informações incompletas

2. **Fallback - Coleta Manual:**
   - Para URLs onde scraping falhou ou informação está incompleta
   - Humano acessa página, copia textos relevantes
   - Humano fornece conteúdo via input manual
   - AI processa conteúdo fornecido

Informações a extrair por competidor:
- Nome completo e tagline
- Problema principal que resolve
- Solução oferecida (como resolve)
- Principal diferencial competitivo
- Features principais (top 3-5)
- Pricing (planos, valores, modelo de cobrança)
- ICP observado (quem é o cliente ideal deles)
- Casos de uso mencionados
- Linguagem e posicionamento usado
- Social proof (clientes, métricas, testimonials)

Resultado esperado:
- Arquivo individual por competidor com informações estruturadas
- Formato: `competidor-[nome].md` com seções padronizadas
- Informações completas ou marcadas como "não disponível" quando não encontradas
- Screenshots ou citações diretas quando relevantes

### Etapa 4: Análise por Competidor (45-60 minutos)

Para cada competidor, sintetize as informações coletadas em perfil estruturado.

Estrutura de análise:
1. **Resumo executivo** (2-3 frases sobre o competidor)
2. **Problema e solução** (qual dor resolvem e como)
3. **Principal diferencial** (o que eles destacam como único)
4. **Pricing** (modelo, valores, tiers)
5. **ICP observado** (quem são os clientes ideais)
6. **Features críticas** (top 3-5 capacidades essenciais)
7. **Posicionamento** (como se comunicam e se posicionam)
8. **Observações** (insights únicos, pontos fortes/fracos)

Critérios de qualidade:
- Cada seção preenchida com informação concreta
- Evitar suposições - basear em evidência das URLs
- Destacar citações diretas quando relevantes
- Identificar gaps (informação não disponível publicamente)

Resultado esperado:
- Documento de análise individual por competidor
- Formato consistente entre todos os competidores
- Total de 3-5 documentos de análise
- Cada análise com 2-3 páginas de conteúdo estruturado

### Etapa 5: Síntese Comparativa e Identificação de Padrões (30-45 minutos)

Compare os competidores analisados para identificar padrões, convergências e divergências.

Análises comparativas:
1. **Padrões de problema/solução:**
   - Que problemas são comuns a todos?
   - Existem abordagens de solução convergentes?
   - Algum competidor ataca problema diferente?

2. **Análise de diferenciais:**
   - Que diferenciais são mais comuns?
   - Existem diferenciais únicos?
   - Que espaço de diferenciação parece saturado vs. aberto?

3. **Análise de pricing:**
   - Qual é a faixa de preço do mercado?
   - Existem modelos de cobrança dominantes?
   - Que oportunidades de pricing existem? (freemium, value-based, etc.)

4. **Análise de ICP:**
   - Todos atacam o mesmo perfil de cliente?
   - Existem nichos desatendidos?
   - Que segmentos parecem mais/menos competitivos?

5. **Análise de features:**
   - Que features são "table stakes" (esperadas por todos)?
   - Que features são diferenciais?
   - Que capacidades parecem ausentes no mercado?

Resultado esperado:
- Documento de síntese comparativa
- Tabelas ou listas comparando aspectos críticos
- Identificação de padrões claros (convergências)
- Identificação de gaps e oportunidades (divergências)

### Etapa 6: Geração de Hipóteses de Diferenciação (30-45 minutos)

Com base na análise comparativa, gere hipóteses acionáveis de como criar produto similar mas diferenciado.

Dimensões de diferenciação:
1. **Problema/ICP diferente:**
   - Atacar mesmo problema para ICP desatendido
   - Atacar subproblema negligenciado
   - Focar em nicho específico (vertical, geografia, tamanho)

2. **Solução diferente:**
   - Abordagem técnica distinta
   - Experiência de usuário superior
   - Simplificação radical (fazer menos, melhor)

3. **Modelo de negócio diferente:**
   - Pricing mais acessível ou transparente
   - Modelo de cobrança alternativo
   - Go-to-market diferenciado

4. **Posicionamento diferente:**
   - Linguagem e branding distintos
   - Foco em benefício negligenciado
   - Contrarian positioning (ir contra consenso)

Formato de hipótese:
Usar template: "Nosso produto resolve [PROBLEMA] para [ICP ESPECÍFICO] através de [ABORDAGEM DIFERENCIADA], diferente dos competidores que [COMO COMPETIDORES FAZEM]."

Resultado esperado:
- Documento com 5-10 hipóteses de diferenciação
- Cada hipótese com:
  - Declaração clara (usando template)
  - Justificativa baseada na análise
  - Riscos e premissas
  - Viabilidade inicial (alta/média/baixa)
- Recomendação de top 2-3 hipóteses mais promissoras
- Próximos passos sugeridos (ex: executar ZeroUm com hipótese escolhida)

## Pontos de Decisão

Ponto de Decisão 1: Após Etapa 2 (Mapeamento)
- Pergunta: As URLs coletadas fornecem informação suficiente sobre competidores?
- Se SIM: Prossiga para Etapa 3
- Se NÃO: Retorne e adicione mais URLs ou competidores alternativos

Ponto de Decisão 2: Após Etapa 3 (Extração)
- Pergunta: Conseguiu extrair pelo menos 70% das informações planejadas?
- Se SIM: Prossiga para Etapa 4
- Se NÃO: Execute fallback manual para gaps críticos ou ajuste expectativas

Ponto de Decisão 3: Após Etapa 5 (Síntese)
- Pergunta: Identificou pelo menos 3 oportunidades claras de diferenciação?
- Se SIM: Prossiga para Etapa 6
- Se NÃO: Retorne e analise competidores adicionais ou aprofunde análise

## Resultados Esperados

1. Contexto de negócio documentado (Etapa 1)
   - Objetivos, mercado-alvo, restrições claramente definidos

2. Mapa de competidores e URLs (Etapa 2)
   - 3-5 competidores identificados
   - 15-30 URLs organizadas

3. Informações extraídas (Etapa 3)
   - 3-5 arquivos com dados brutos por competidor
   - Screenshots ou citações quando relevantes

4. Análises individuais (Etapa 4)
   - 3-5 documentos de análise estruturada
   - Perfil completo de cada competidor

5. Síntese comparativa (Etapa 5)
   - Documento consolidado com padrões e gaps
   - Tabelas comparativas de aspectos críticos

6. Hipóteses de diferenciação (Etapa 6)
   - 5-10 hipóteses acionáveis
   - Recomendação de top 2-3 para perseguir
   - Próximos passos sugeridos

## Indicadores-Chave de Desempenho

- Completude da extração: meta de 70%+ das informações planejadas coletadas
- Número de competidores analisados: 3-5 (mínimo 3)
- Qualidade das hipóteses: pelo menos 3 hipóteses viáveis identificadas
- Tempo até conclusão: 3-5 horas para processo completo
- Acionabilidade: hipóteses podem alimentar diretamente estratégia ZeroUm ou similar
- Alinhamento: contexto de negócio reflete necessidades reais do projeto

## Avisos e Armadilhas Comuns

Aviso 1: Não analise apenas homepage
- Problema: Homepage frequentemente omite detalhes de pricing, features e ICP
- Solução: Sempre inclua pricing page e pelo menos mais 2-3 URLs

Aviso 2: Evite análise superficial
- Problema: Copiar apenas taglines sem entender problema real e solução
- Solução: Extraia citações, exemplos concretos, casos de uso específicos

Aviso 3: Não force diferenciação artificial
- Problema: Criar diferenciais que não resolvem problemas reais
- Solução: Base hipóteses em gaps observados, não em ideias desconectadas da análise

Aviso 4: Não ignore contexto de negócio
- Problema: Gerar hipóteses que não alinham com objetivos, mercado ou restrições
- Solução: Sempre retorne ao contexto (Etapa 1) ao gerar hipóteses

Aviso 5: Evite paralisia por análise
- Problema: Analisar dezenas de competidores sem tirar conclusões
- Solução: Limite a 3-5 competidores e foque em profundidade, não amplitude

Aviso 6: Não copie, diferencie
- Problema: Usar análise para criar clone exato
- Solução: Objetivo é similar mas diferenciado - sempre identifique o diferencial

## Dependências

Este processo depende de:
- Acesso à internet para web scraping/fetching
- URLs públicas de competidores (não requer login ou paywall)
- Ferramentas de web fetch ou capacidade de cópia manual
- Clareza sobre objetivos de negócio (mesmo que preliminar)

Este processo habilita:
- Estratégia ZeroUm (usa hipóteses de diferenciação como input)
- Processos de validação de problema (testa hipóteses geradas)
- Definição de posicionamento e proposta de valor
- Decisões de product roadmap e priorização

## Referências

Processos relacionados:
- Estratégia ZeroUm (usa outputs deste processo como Etapa 0)
- Definição de Hipótese de Problema (pode ser complementado por esta análise)
- Identificação de ICP (usa insights sobre ICP observado)

Templates relacionados:
- Template de Contexto de Negócio (pasta _DATA/templates)
- Template de Análise de Competidor (pasta _DATA/templates)
- Template de Síntese Comparativa (pasta _DATA/templates)
- Template de Hipóteses de Diferenciação (pasta _DATA/templates)

Artefatos compartilhados:
- Nenhum identificado ainda (processo novo, pode gerar artefatos compartilháveis futuramente)
