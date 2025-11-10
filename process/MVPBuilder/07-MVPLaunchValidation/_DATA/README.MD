# Artefatos de Dados - MVPLaunchValidation

Este diretorio armazena templates, exemplos e outputs gerados durante a execucao do processo MVPLaunchValidation.

---

## Estrutura de Artefatos

### Templates

Templates a serem criados durante a execucao do processo:

**1. roteiro-entrevista.md**
- Template para entrevistas com early adopters
- Estrutura: Abertura, Uso do produto, Valor percebido, Comparacao, Futuro
- Perguntas abertas focadas em comportamento, nao opiniao
- Tempo estimado: 40 minutos por entrevista

**2. survey-satisfacao.md**
- Template de survey quantitativo
- Perguntas: NPS, CSAT, Frequencia, Valor, Alternativas, Willingness to pay
- Formato: Google Forms, Typeform ou similar
- Meta: 30-50 respostas

**3. template-relatorio-validacao.md**
- Estrutura completa do relatorio final
- Secoes: Sumario, Hipotese, Metricas, Feedback, Analise, Decisao, Aprendizados
- Formato: Markdown exportavel para PDF
- Publico: Stakeholders, investors, time

**4. dashboard-metricas.md**
- Especificacao do dashboard de metricas
- Metricas rastreadas: Cadastros, Ativacao, Retencao, Conversao, NPS
- Ferramentas: GA4, Posthog, Mixpanel, ou custom
- Atualizacao: Tempo real ou diaria

**5. plano-comunicacao.md**
- Template de comunicacao com early adopters
- Email de lancamento
- Email de follow-up
- Email de agradecimento pos-feedback
- Email de comunicacao da decisao

**6. analise-hipotese.md**
- Framework de analise da hipotese original
- Mapeamento: Componente -> Evidencias -> Validado/Invalidado
- Criterios de validacao para QUEM, RESULTADO, DOR
- Decisao: PIVOTAR / PERSEVERAR / EXPANDIR

### Examples

Exemplos de referencia para guiar a execucao:

**1. exemplo-entrevista-transcricao.md**
- Transcricao de uma entrevista exemplo
- Mostra como capturar insights e citacoes
- Demonstra perguntas de follow-up

**2. exemplo-survey-resultados.md**
- Resultados exemplo de survey tabulados
- Visualizacoes e graficos
- Analise de distribuicao de respostas

**3. exemplo-relatorio-validacao-completo.md**
- Relatorio completo exemplo (ficticio)
- Todos os componentes preenchidos
- Demonstra nivel de detalhe esperado

### Outputs

Artefatos gerados durante a execucao (exemplos):

**Durante Lancamento:**
- lista-early-adopters.md
- email-lancamento-enviado.md
- onboarding-screenshots/

**Durante Monitoramento:**
- metricas-semana-1.md
- metricas-semana-2.md
- metricas-semana-3.md
- metricas-semana-4.md
- dashboard-screenshot.png

**Durante Feedback Qualitativo:**
- entrevista-01-notas.md ate entrevista-15-notas.md
- insights-consolidados.md
- padroes-identificados.md
- citacoes-relevantes.md

**Durante Feedback Quantitativo:**
- survey-respostas-raw.csv
- survey-analise.md
- survey-graficos/

**Durante Analise:**
- analise-hipotese-completa.md
- mapeamento-evidencias.md
- decisao-justificada.md

**Final:**
- relatorio-validacao-final.md ou .pdf
- retrospectiva.md
- aprendizados.md
- proximos-passos.md

---

## Como Usar Este Diretorio

### Antes de Comecar

1. Revisar templates disponiveis
2. Adaptar templates ao contexto especifico do MVP
3. Configurar ferramentas necessarias (analytics, survey, etc)

### Durante a Execucao

1. Usar templates como base
2. Gerar outputs conforme processo avanca
3. Organizar arquivos em subpastas se necessario
4. Manter nomenclatura consistente

### Apos Conclusao

1. Arquivar todos outputs gerados
2. Documentar decisoes tomadas
3. Preservar evidencias para auditoria futura
4. Compartilhar relatorio final com stakeholders

---

## Nomenclatura de Arquivos

Seguir convencoes:

- Templates: `template-[nome].md`
- Exemplos: `exemplo-[nome].md`
- Outputs: `[nome]-[data ou numero].md`
- Screenshots: `[descricao]-[data].png`
- Dados brutos: `[nome]-raw.csv` ou `.json`

---

## Integracao com Processo

Cada etapa do [process.MD](../process.MD) gera artefatos especificos:

**Etapa 1: Preparar Lancamento**
- lista-early-adopters.md
- plano-comunicacao.md

**Etapa 2: Onboarding de Early Adopters**
- email-lancamento-enviado.md
- cadastros-confirmados.md

**Etapa 3: Monitoramento de Metricas**
- dashboard configurado
- metricas-semanais.md

**Etapa 4: Suporte e Ajustes Rapidos**
- log-suporte.md
- bugs-corrigidos.md

**Etapa 5: Feedback Qualitativo**
- entrevistas-01-a-15.md
- insights-consolidados.md

**Etapa 6: Feedback Quantitativo**
- survey criado
- survey-respostas.csv
- survey-analise.md

**Etapa 7: Analise de Validacao**
- analise-hipotese-completa.md
- mapeamento-evidencias.md

**Etapa 8: Decisao Estrategica**
- decisao-justificada.md
- relatorio-validacao-final.md

**Etapa 9: Retrospectiva e Transicao**
- retrospectiva.md
- aprendizados.md
- proximos-passos.md

---

## Referencias

- [process.MD](../process.MD) - Processo completo
- [tasks.MD](../tasks.MD) - Tarefas detalhadas
- [knowledge.MD](../knowledge.MD) - Base de conhecimento
- [validator.MD](../validator.MD) - Criterios de validacao

---

**Ultima atualizacao:** 2025-11-05
**Mantido por:** Framework Business Team
**Parte de:** Estrategia MVPBuilder (Etapa 7)
