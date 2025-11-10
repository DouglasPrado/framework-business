# Processo de Execução - Testing and Validation (Naming)

Este processo conduz a validação dos nomes finalistas com stakeholders internos e público-alvo.

## Visão geral do fluxo

```
PLANEJAMENTO → PREPARAÇÃO DE MATERIAIS → EXECUÇÃO DE TESTES → ANÁLISE → RECOMENDAÇÃO & HANDOFF
```

## Entradas obrigatórias

- `shortlist-naming.MD`, `matriz-avaliacao.MD`, `alertas-riscos-remanescentes.MD`.
- Briefing de naming e metas de validação.
- Acesso a amostras de clientes/personas e stakeholders internos.

## TestingValidation.1: Planejamento dos testes

### Objetivo
Definir abordagem, amostra, cronograma e indicadores da validação.

### Sequência de ações
- Revisar objetivos (preferência mínima, clareza, diferenciação).
- Escolher método de teste (qualitativo, quantitativo, híbrido).
- Definir amostra (personas prioritárias, stakeholders internos, parceiros).
- Elaborar plano com cronograma, responsabilidades, KPI de sucesso.
- Registrar em `plano-testes-naming.MD`.

### Pontos de decisão
1. **Método de teste adequado ao contexto?**
   - ✅ Sim → prosseguir.
   - ❌ Não → reavaliar recursos e prazos.
2. **Amostra viável e representativa?**
   - ✅ Sim → seguir.
   - ❌ Não → ajustar tamanho ou perfil.

### Outputs
- `_DATA/TestingValidation/plano-testes-naming.MD`

## TestingValidation.2: Preparação de materiais

### Objetivo
Criar instrumentos e materiais neutros para aplicação dos testes.

### Sequência de ações
- Copiar `roteiro-teste.MD` para `_DATA/TestingValidation/` e ajustar perguntas.
- Preparar apresentações, protótipos ou formulários com contexto e nomes.
- Definir mensagens de convite, materiais de consentimento (se necessário).
- Organizar planilha ou ferramenta para registrar dados (`registro-testes.MD`).
- Validar materiais com sponsor/áreas críticas antes de aplicação.

### Pontos de decisão
1. **Instrumento revisado e aprovado?**
   - ✅ Sim → executar testes.
   - ❌ Não → coletar ajustes.
2. **Materiais garantem neutralidade e clareza?**
   - ✅ Sim → prosseguir.

### Outputs
- `_DATA/TestingValidation/roteiro-teste.MD`
- `_DATA/TestingValidation/material-apresentacao` (se aplicável)

## TestingValidation.3: Execução dos testes

### Objetivo
Aplicar o método definido e registrar dados qualitativos/quantitativos.

### Sequência de ações
- Convidar participantes e confirmar consentimento (quando necessário).
- Conduzir entrevistas, grupos, surveys ou testes A/B conforme plano.
- Registrar respostas em `registro-testes.MD` e `registro-participantes.MD`.
- Capturar citações, objeções, notas emocionais.
- Armazenar evidências (gravações, prints) na pasta `evidencias/`.

### Pontos de decisão
1. **Metas de amostra atingidas?**
   - ✅ Sim → avançar.
   - ❌ Não → estender testes até atingir volume mínimo.
2. **Problemas de execução (viés, falha de ferramenta)?**
   - Sim → ajustar e registrar impacto.

### Outputs
- `_DATA/TestingValidation/registro-participantes.MD`
- `_DATA/TestingValidation/registro-testes.MD`
- Evidências em `_DATA/TestingValidation/evidencias/`

## TestingValidation.4: Análise e consolidação

### Objetivo
Comparar resultados e preparar relatório com recomendações.

### Sequência de ações
- Compilar dados (preferência, clareza, memorabilidade, citação).
- Calcular métricas (percentuais, médias, gráficos) conforme plano.
- Comparar resultados com metas do briefing.
- Identificar riscos, objeções e insights relevantes.
- Redigir `relatorio-testes-naming.MD` com tabela comparativa e narrativas.

### Pontos de decisão
1. **Nome preferido atende metas definidas?**
   - ✅ Sim → recomendar.
   - ❌ Não → avaliar alternativas e possíveis ajustes.
2. **Objeções críticas requerem mitigação?**
   - ✅ Sim → incluir plano na recomendação.

### Outputs
- `_DATA/TestingValidation/relatorio-testes-naming.MD`

## TestingValidation.5: Recomendação e handoff

### Objetivo
Entregar recomendação final com evidências e próximos passos.

### Sequência de ações
- Preparar `recomendacao-nome.MD` com nome preferido, backup, plano de mitigação.
- Atualizar `matriz-avaliacao.MD` (se necessário) com dados dos testes.
- Apresentar resultados ao sponsor e stakeholders decisores.
- Registrar feedback e aprovações.
- Ajustar cronograma para Etapa 5 (Decisão e Proteção).

### Pontos de decisão
1. **Sponsor concorda com recomendação?**
   - ✅ Sim → avançar para decisão.
   - ❌ Não → ajustar ou rodar testes adicionais.
2. **Documentação completa para reunião de decisão?**
   - ✅ Sim → encerrar etapa.

### Outputs
- `_DATA/TestingValidation/recomendacao-nome.MD`
- Atualização em `_DATA/ViabilityFilters/matriz-avaliacao.MD` (caso necessário)
- `_DATA/TestingValidation/feedback-log.MD` (opcional)

## Indicadores de acompanhamento

- Taxa de preferência (%) por nome.
- Claridade percebida (média Likert).
- Número de objeções críticas levantadas.
- Prazo entre short list e recomendação final.

## Documentação e governança

- Todos os arquivos e evidências devem estar em `_DATA/TestingValidation/`.
- Versione instrumentos/relatórios e mantenha aprovadores informados.
- Garantir conformidade com LGPD/GDPR ao registrar dados de participantes.
