# Processo de Execução - Imersão e Contexto (Branding)

Este processo descreve operacionalmente ContextImmersion da estratégia de Branding, garantindo coleta estruturada de dados, alinhamento entre times e documentação dos insights que orientarão as etapas subsequentes.

## Visão geral do fluxo

```
ALINHAMENTO → ENTREVISTAS INTERNAS → ENTREVISTAS EXTERNAS → BENCHMARKING → CONSOLIDAÇÃO
```

## Entradas obrigatórias

- Sponsor definido e lista preliminar de stakeholders internos.
- Documentos já existentes: posicionamento atual, hipóteses de problema/solução, personas, entrevistas anteriores.
- Acesso a ferramentas aprovadas para registro de entrevistas e benchmarking.
- Templates localizados em `strategies/Branding/_DATA/templates/` e `process/_SHARED/templates/`.

## Etapa 1: Alinhamento e briefing

### Objetivo
Formalizar briefing estratégico com objetivos, critérios de sucesso e restrições.

### Sequência de ações
- Reunir sponsor e líderes das áreas impactadas (marketing, produto, atendimento, vendas).
- Revisar aprendizados recentes de `TargetUserIdentification`, `ProblemHypothesisDefinition` e `UserInterviewValidation`.
- Preencher `diagnostico-marca.MD` com metas, público, restrições e critérios.
- Compartilhar versão preliminar para comentários e ajustes.
- Registrar aprovação formal do briefing.

### Pontos de decisão
1. **Briefing aprovado por todas as áreas críticas?**
   - ✅ Sim → Seguir para planejamento das entrevistas.
   - ❌ Não → Registrar pendências e agendar novo alinhamento.
2. **Existem lacunas de dados já identificadas?**
   - ✅ Sim → Incluir na pauta de entrevistas e benchmarking.
   - ❌ Não → Confirmar com sponsor se volume atual é suficiente.

### Outputs
- `diagnostico-marca.MD` aprovado.
- Lista de stakeholders internos e externos confirmada.
- Cronograma preliminar das entrevistas.

## Etapa 2: Entrevistas internas

### Objetivo
Capturar percepções de equipes chave sobre o momento atual, dores e aspirações da marca.

### Sequência de ações
- Selecionar pelo menos 5 representantes (liderança, marketing, vendas, atendimento, produto/ops).
- Personalizar roteiro de entrevista a partir de `process/_SHARED/templates/script-entrevista.MD`.
- Conduzir entrevistas (presencial ou remoto) documentando insights em `_DATA/ContextImmersion/entrevistas-internas`.
- Destacar linguagem, exemplos concretos, preocupações e expectativas.
- Registrar tags (área, tema, palavras-chave) para facilitar síntese.

### Pontos de decisão
1. **Volume e diversidade suficientes?**
   - ✅ Sim → Prosseguir para entrevistas externas.
   - ❌ Não → Incluir novas vozes ou aprofundar temas críticos.
2. **Existem divergências significativas entre áreas?**
   - ✅ Sim → Sinalizar no diagnóstico para discussão no workshop.
   - ❌ Não → Apenas registrar como alinhamento.

### Outputs
- Notas centralizadas no diretório `_DATA/ContextImmersion/entrevistas-internas`.
- Resumo parcial com principais padrões internos.

## Etapa 3: Entrevistas externas

### Objetivo
Validar percepções com clientes, prospects e parceiros, coletando linguagem literal.

### Sequência de ações
- Selecionar 5+ participantes a partir de bases de `UserInterviewValidation`, CRM ou indicações internas.
- Ajustar roteiro com foco em percepção da marca, comparação com concorrentes, expectativas e linguagem.
- Registrar cada entrevista (áudio, vídeo ou notas detalhadas) com consentimento.
- Mapear dores, benefícios percebidos, emoções e sugestões.
- Consolidar citações-chave para alimentar identidade verbal e mensagens futuras.

### Pontos de decisão
1. **As respostas confirmam ou divergem das hipóteses internas?**
   - Se divergirem, registrar e destacar para análise.
2. **Foram capturadas evidências suficientes de linguagem do cliente?**
   - Se não, planejar entrevistas adicionais ou pesquisas complementares.

### Outputs
- Notas/planilhas de entrevistas externas em `_DATA/ContextImmersion/entrevistas-externas`.
- Lista de citações literais e palavras-chave.
- Registro de objeções e oportunidades mencionadas pelos entrevistados.

## Etapa 4: Benchmarking e referências

### Objetivo
Comparar a marca com referências diretas e aspiracionais para identificar oportunidades.

### Sequência de ações
- Selecionar ao menos 6 referências (3 diretas, 3 inspiracionais).
- Documentar posicionamento, identidade visual e verbal, proposta de valor, diferenciais.
- Identificar boas práticas, lacunas e alertas para o projeto.
- Utilizar `strategies/Branding/_DATA/templates/matriz-inspiracao.MD` para organizar insights.

### Pontos de decisão
1. **As referências cobrem os principais territórios da categoria?**
   - ✅ Sim → Prosseguir.
   - ❌ Não → Adicionar novos exemplos (inclusive internacionais).
2. **Existem riscos de confusão ou similaridade excessiva?**
   - ✅ Sim → Documentar no diagnóstico como alerta.

### Outputs
- `matriz-inspiracao.MD` atualizada (ou documento equivalente).
- Relatório de benchmarking em `_DATA/ContextImmersion/benchmarking.MD`.

## Etapa 5: Consolidação e priorização

### Objetivo
Transformar aprendizados em diagnóstico acionável e agenda para a etapa seguinte.

### Sequência de ações
- Compilar insights das entrevistas internas e externas em formato comparativo.
- Elaborar análise SWOT textual destacando forças, fraquezas, oportunidades e ameaças.
- Priorizar oportunidades usando matriz impacto x esforço.
- Produzir `diagnostico-resumo.MD` com principais achados, recomendações e próximos passos.
- Validar agenda e participantes do workshop de essência com sponsor.

### Pontos de decisão
1. **Diagnóstico responde às perguntas-chave do briefing?**
   - ✅ Sim → Compartilhar com liderança.
   - ❌ Não → Revisitar entrevistas ou benchmarking.
2. **Stakeholders concordam com prioridades definidas?**
   - ✅ Sim → Encaminhar para Etapa 1.
   - ❌ Não → Registrar ajustes e reconduzir discussão.

### Outputs
- Análise SWOT em `_DATA/ContextImmersion/swot.MD`.
- `diagnostico-resumo.MD` compartilhado com stakeholders.
- Agenda confirmada para workshop de essência.

## Indicadores de acompanhamento

- Entrevistas realizadas vs. planejadas.
- Quantidade de referências analisadas.
- Prazo entre kick-off e entrega do diagnóstico.
- Número de oportunidades priorizadas (recomenda-se ≤ 5 com plano claro).

## Documentação e governança

- Todos os materiais devem ficar em `_DATA/ContextImmersion/`.
- Atualizações relevantes devem ser replicadas em `strategies/Branding/knowledge.MD` para manter a estratégia alinhada.
- Ao finalizar, realizar handoff formal com o time responsável pela Etapa 1 (Essência e Fundamentos).
