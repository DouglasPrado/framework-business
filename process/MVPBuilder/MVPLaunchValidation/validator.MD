# Validator - MVPLaunchValidation

Este documento define criterios de validacao para o processo de lancamento e validacao do MVP.

---

## Objetivo da Validacao

Verificar se o MVP foi lancado, testado com usuarios reais, metricas foram coletadas, hipotese foi analisada e decisao estrategica foi tomada com base em evidencias.

---

## Areas de Validacao

### 1. Lancamento e Onboarding de Early Adopters

**Criterios de Aprovacao:**

- Early adopters identificados (minimo 10, ideal 20-30)
- Lista de early adopters documentada com contatos
- Comunicacao de lancamento enviada
- Onboarding preparado e funcional
- Primeiros cadastros realizados (minimo 5)
- Suporte inicial disponivel e responsivo
- MVP acessivel em producao

**Evidencias Necessarias:**

- Lista de early adopters com nome, email, perfil
- Email de lancamento enviado (copia)
- Screenshot ou video de onboarding
- Confirmacao de primeiros cadastros (dashboard ou banco)
- Canal de suporte definido (email, chat, etc)

**Criterios de Rejeicao:**

- Menos de 10 early adopters identificados
- Comunicacao nao enviada
- Onboarding quebrado ou confuso
- Nenhum cadastro realizado
- Sem canal de suporte

---

### 2. Monitoramento de Metricas Quantitativas

**Criterios de Aprovacao:**

- Analytics configurado e rastreando eventos
- Metricas primarias sendo coletadas:
  - Cadastros (Acquisition)
  - Ativacao (Activation) - usuario completa acao core
  - Retencao (Retention) - usuario volta em 7 dias
  - Conversao (Revenue) - se aplicavel
  - NPS - se aplicavel
- Dashboard de metricas criado e acessivel
- Dados coletados por minimo 2 semanas
- Metricas documentadas com valores reais

**Evidencias Necessarias:**

- Screenshot de dashboard de metricas
- Relatorio com metricas numericas:
  - Total de cadastros
  - Taxa de ativacao (% que completa acao core)
  - Taxa de retencao 7-day (% que volta)
  - Taxa de conversao (se aplicavel)
  - NPS score (se aplicavel)
- Periodo de coleta especificado (data inicio - data fim)

**Criterios de Rejeicao:**

- Analytics nao configurado
- Metricas nao sendo rastreadas
- Dados coletados por menos de 2 semanas
- Dashboard inexistente ou inacessivel
- Metricas sem valores numericos reais

---

### 3. Feedback Qualitativo (Entrevistas)

**Criterios de Aprovacao:**

- Minimo 10 entrevistas realizadas
- Entrevistas com early adopters que USARAM o produto
- Roteiro de entrevista seguido
- Insights documentados por entrevista
- Padroes identificados entre entrevistas
- Citacoes diretas capturadas
- Audio ou notas de entrevista salvos

**Evidencias Necessarias:**

- Lista de entrevistados (nome, data, duracao)
- Documento com insights principais por entrevista
- Padroes identificados (minimo 3-5)
- Citacoes diretas relevantes
- Analise consolidada de todas entrevistas

**Criterios de Rejeicao:**

- Menos de 10 entrevistas
- Entrevistas com pessoas que NAO usaram
- Sem documentacao de insights
- Sem padroes identificados
- Apenas opinioes, sem comportamentos observados

---

### 4. Feedback Quantitativo (Survey)

**Criterios de Aprovacao:**

- Survey criado com perguntas relevantes:
  - NPS ou similar
  - Satisfacao (CSAT)
  - Frequencia de uso
  - Valor percebido
  - Willingness to pay
- Survey enviado para todos usuarios cadastrados
- Minimo 30 respostas coletadas
- Resultados tabulados e analisados
- Distribuicao de respostas documentada

**Evidencias Necessarias:**

- Copia do survey (perguntas)
- Numero de respostas coletadas
- Resultados tabulados (numeros e percentuais)
- Graficos ou visualizacoes (opcional)
- Analise dos resultados

**Criterios de Rejeicao:**

- Survey nao criado ou nao enviado
- Menos de 30 respostas
- Perguntas irrelevantes ou mal formuladas
- Resultados nao analisados
- Sem documentacao

---

### 5. Analise da Hipotese Original

**Criterios de Aprovacao:**

- Hipotese original revisitada e documentada
- Cada componente da hipotese analisado:
  - QUEM: Usuarios reais sao o publico-alvo?
  - RESULTADO: Usuarios alcancaram resultado prometido?
  - DOR: Solucao evita a dor prometida?
- Evidencias mapeadas para cada componente
- Cada componente marcado como VALIDADO ou INVALIDADO
- Justificativa clara baseada em dados

**Evidencias Necessarias:**

- Hipotese original escrita (da ProblemHypothesisDefinition)
- Analise de cada componente:
  - QUEM - VALIDADO/INVALIDADO + evidencias
  - RESULTADO - VALIDADO/INVALIDADO + evidencias
  - DOR - VALIDADO/INVALIDADO + evidencias
- Citacao de metricas e feedback como evidencias
- Conclusao sobre hipotese geral

**Criterios de Rejeicao:**

- Hipotese original nao revisitada
- Componentes nao analisados individualmente
- Sem evidencias concretas
- Analise baseada em achismos, nao dados
- Componentes nao marcados como validados/invalidados

---

### 6. Decisao Estrategica

**Criterios de Aprovacao:**

- Decisao clara tomada: PIVOTAR, PERSEVERAR ou EXPANDIR
- Decisao baseada em criterios definidos:
  - PIVOTAR: 0-1 componentes validados
  - PERSEVERAR: 2 componentes validados
  - EXPANDIR: 3 componentes validados
- Justificativa detalhada da decisao
- Proximo passo especificado
- Criterios futuros definidos (se perseverar)
- Nova hipotese rascunhada (se pivotar)

**Evidencias Necessarias:**

- Decisao explicita: PIVOTAR / PERSEVERAR / EXPANDIR
- Justificativa com base em:
  - Numero de componentes validados
  - Metricas especificas
  - Feedback qualitativo
  - Feedback quantitativo
- Proximo passo documentado
- Timeline para proximo passo

**Criterios de Rejeicao:**

- Decisao nao tomada
- Decisao nao alinhada com criterios
- Sem justificativa
- Justificativa sem base em dados
- Proximo passo indefinido

---

### 7. Relatorio de Validacao

**Criterios de Aprovacao:**

- Relatorio completo criado
- Estrutura seguida:
  - Sumario executivo
  - Hipotese original
  - Metricas quantitativas
  - Feedback qualitativo
  - Feedback quantitativo
  - Analise da hipotese
  - Decisao estrategica
  - Proximo passo
  - Aprendizados
- Todos os dados consolidados
- Graficos e visualizacoes (se aplicavel)
- Documento acessivel e compartilhavel

**Evidencias Necessarias:**

- Relatorio final em formato MD, PDF ou Doc
- Todas secoes preenchidas
- Dados numericos incluidos
- Citacoes de feedback incluidas
- Conclusoes claras
- Documento salvo em `_DATA/`

**Criterios de Rejeicao:**

- Relatorio nao criado
- Secoes faltando
- Dados nao consolidados
- Sem conclusoes
- Documento inacessivel

---

### 8. Retrospectiva e Aprendizados

**Criterios de Aprovacao:**

- Retrospectiva realizada com time
- O que funcionou documentado (minimo 3 itens)
- O que nao funcionou documentado (minimo 3 itens)
- Aprendizados capturados (minimo 5 itens)
- Acoes de melhoria identificadas
- Documentacao salva para proxima iteracao

**Evidencias Necessarias:**

- Documento de retrospectiva
- Lista: O que funcionou
- Lista: O que nao funcionou
- Lista: Aprendizados
- Lista: Acoes de melhoria
- Data e participantes da retrospectiva

**Criterios de Rejeicao:**

- Retrospectiva nao realizada
- Listas vazias ou muito superficiais
- Sem aprendizados capturados
- Sem acoes de melhoria

---

### 9. Transicao para Proximo Passo

**Criterios de Aprovacao:**

- Decisao comunicada para stakeholders
- Artefatos organizados e arquivados
- Codigo/design preservado se necessario
- Proximo processo identificado:
  - Se PIVOTAR: ProblemHypothesisDefinition
  - Se PERSEVERAR: MVPCoreDevelopment ou MVPSecondaryDevelopment
  - Se EXPANDIR: Roadmap de crescimento
- Handoff preparado para proximo time/fase
- Knowledge.MD atualizado

**Evidencias Necessarias:**

- Email ou documento comunicando decisao
- Artefatos organizados em `_DATA/`
- Codigo commitado e documentado
- Proximo processo especificado
- Documento de handoff (se aplicavel)

**Criterios de Rejeicao:**

- Decisao nao comunicada
- Artefatos desorganizados
- Codigo nao preservado
- Proximo passo indefinido
- Sem handoff preparado

---

## Criterios Gerais de Qualidade

### Completude

- Todos os 9 itens acima validados
- Todas evidencias disponiveis
- Nenhuma etapa pulada
- Processo seguido do inicio ao fim

### Tracabilidade

- Metricas rastreadas desde lancamento
- Feedback documentado com fontes
- Decisoes justificadas com evidencias
- Links entre hipotese, dados e decisao claros

### Utilizabilidade

- Relatorio legivel e compreensivel
- Dados organizados e acessiveis
- Decisao clara para stakeholders
- Proximo passo executavel

---

## Checklist Final de Validacao

Marque cada item ao validar:

### Lancamento
- [ ] 10-30 early adopters onboarded
- [ ] Comunicacao enviada
- [ ] MVP em producao
- [ ] Suporte disponivel

### Metricas
- [ ] Analytics configurado
- [ ] Cadastros rastreados
- [ ] Ativacao rastreada
- [ ] Retencao rastreada
- [ ] Dashboard criado
- [ ] Minimo 2 semanas de dados

### Feedback Qualitativo
- [ ] 10+ entrevistas realizadas
- [ ] Insights documentados
- [ ] Padroes identificados
- [ ] Citacoes capturadas

### Feedback Quantitativo
- [ ] Survey criado e enviado
- [ ] 30+ respostas coletadas
- [ ] Resultados analisados

### Analise
- [ ] Hipotese revisitada
- [ ] Componentes analisados (QUEM/RESULTADO/DOR)
- [ ] Evidencias mapeadas
- [ ] Validado/Invalidado marcado

### Decisao
- [ ] Decisao tomada (PIVOTAR/PERSEVERAR/EXPANDIR)
- [ ] Justificativa documentada
- [ ] Proximo passo definido

### Documentacao
- [ ] Relatorio completo
- [ ] Retrospectiva realizada
- [ ] Aprendizados capturados
- [ ] Artefatos organizados

### Transicao
- [ ] Decisao comunicada
- [ ] Handoff preparado
- [ ] Proximo processo identificado

---

## Niveis de Validacao

### Validacao Minima (Aceitavel)

- 10 early adopters onboarded
- 2 semanas de dados coletados
- 10 entrevistas + 30 respostas survey
- Hipotese analisada
- Decisao tomada e justificada
- Relatorio basico criado

### Validacao Ideal (Recomendada)

- 20-30 early adopters onboarded
- 3-4 semanas de dados coletados
- 15 entrevistas + 50 respostas survey
- Analise profunda da hipotese
- Decisao bem fundamentada
- Relatorio completo com visualizacoes
- Retrospectiva detalhada

### Validacao Exemplar (Excelencia)

- 30+ early adopters onboarded
- 4+ semanas de dados coletados
- 15+ entrevistas + 50+ respostas survey
- Analise quantitativa e qualitativa profunda
- Decisao fundamentada com cenarios alternativos
- Relatorio completo, visual e acionavel
- Retrospectiva com acoes de melhoria implementadas
- Aprendizados compartilhados com time e comunidade

---

## Criterios de Rejeicao Completa

O processo deve ser considerado INCOMPLETO se:

- Menos de 10 early adopters onboarded
- Menos de 2 semanas de dados
- Menos de 10 entrevistas
- Menos de 30 respostas survey
- Hipotese nao analisada
- Decisao nao tomada
- Relatorio nao criado
- Retrospectiva nao realizada

Nestes casos, retornar ao processo e completar itens faltantes antes de prosseguir.

---

## Aprovacao Final

**Processo validado quando:**

- Todas as 9 areas validadas
- Checklist final 100% completo
- Evidencias disponiveis para auditoria
- Decisao tomada e comunicada
- Proximo passo claro

**Responsavel pela validacao:** Product Owner ou Founder

**Proximos passos:**
- Se PIVOTAR: Iniciar ProblemHypothesisDefinition com nova hipotese
- Se PERSEVERAR: Retornar a MVPCoreDevelopment ou MVPSecondaryDevelopment com ajustes
- Se EXPANDIR: Criar roadmap de crescimento e expansao

---

**Ultima atualizacao:** 2025-11-05
**Mantido por:** Framework Business Team
**Parte de:** Estrategia MVPBuilder (Etapa 7)
