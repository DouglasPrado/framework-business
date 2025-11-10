# Processo de Execução - Context Briefing (Naming)

Este processo estabelece o briefing estratégico que direcionará todas as etapas de naming.

## Visão geral do fluxo

```
PREPARAÇÃO → ENTREVISTAS & COLETA → CONSOLIDAÇÃO → VALIDAÇÃO → CRONOGRAMA & HANDOFF
```

## Entradas obrigatórias

- Outputs estratégicos disponíveis (essência, posicionamento, identidade verbal, personas).
- Informações de produto/negócio (roadmap, data de lançamento, canais).
- Acesso às bases de domínio/marca para buscas preliminares.
- Stakeholders confirmados (sponsor, marketing, produto, jurídico, growth, CS).

## ContextBriefing.1: Preparação

### Objetivo
Planejar entrevistas e materiais para captar todas as restrições de naming.

### Sequência de ações
- Definir escopo do projeto (tipo de nome, abrangência, idiomas).
- Listar stakeholders internos e externos relevantes.
- Preparar roteiro de entrevista usando `process/_SHARED/templates/script-entrevista.MD`.
- Organizar referências estratégicas (plataforma de marca, mensagens, diferenciais).
- Agendar sessões de alinhamento com sponsor e áreas impactadas.

### Pontos de decisão
1. **Escopo e objetivos do naming documentados?**
   - ✅ Sim → prosseguir.
   - ❌ Não → alinhar com sponsor.
2. **Stakeholders confirmados?**
   - ✅ Sim → agendar entrevistas.

### Outputs
- `_DATA/ContextBriefing/stakeholders-list.MD`
- `_DATA/ContextBriefing/agenda-entrevistas.MD`

## ContextBriefing.2: Entrevistas e coleta de insumos

### Objetivo
Capturar expectativas, restrições e requisitos de cada área.

### Sequência de ações
- Conduzir entrevistas com sponsor, marketing, produto, jurídico, growth, CS.
- Registrar notas em `_DATA/ContextBriefing/entrevistas-iniciais.MD`.
- Anotar must-have, nice-to-have, fatores eliminatórios, tom desejado, referências.
- Coletar dados de mercado (concorrentes, benchmarks) e disponibilidade inicial de domínios/handles.
- Identificar riscos culturais, linguísticos e regulatórios.

### Pontos de decisão
1. **Informações suficientes para preencher o briefing?**
   - ✅ Sim → iniciar consolidação.
   - ❌ Não → agendar entrevistas adicionais ou solicitar materiais.
2. **Restrições críticas identificadas?**
   - ✅ Sim → registrar no briefing e definir plano de mitigação.

### Outputs
- `_DATA/ContextBriefing/entrevistas-iniciais.MD`
- `_DATA/ContextBriefing/restricoes-iniciais.MD`

## ContextBriefing.3: Consolidação do briefing

### Objetivo
Preencher o template de briefing com critérios priorizados e riscos.

### Sequência de ações
- Copiar `strategies/Naming/_DATA/templates/briefing-naming.MD` para `_DATA/ContextBriefing/`.
- Documentar objetivo estratégico, público, escopo, restrições e critérios.
- Criar matriz de critérios (`criterios-avaliacao.MD`) com pesos (1-5) e racional.
- Registrar riscos e dependências em `_DATA/ContextBriefing/riscos-dependencias.MD`.
- Elaborar versão 1 do briefing e compartilhar com stakeholders.

### Pontos de decisão
1. **Brieffing preenchido sem lacunas?**
   - ✅ Sim → enviar para revisão.
   - ❌ Não → preencher com dados faltantes.
2. **Critérios priorizados e ponderados?**
   - ✅ Sim → prosseguir.
   - ❌ Não → rodar sessão rápida de priorização com sponsor.

### Outputs
- `_DATA/ContextBriefing/briefing-naming.MD` (V1)
- `_DATA/ContextBriefing/criterios-avaliacao.MD`
- `_DATA/ContextBriefing/riscos-dependencias.MD`

## ContextBriefing.4: Validação e ajustes

### Objetivo
Obter aprovação formal do briefing e registrar ajustes.

### Sequência de ações
- Enviar briefing V1 aos stakeholders com prazo de feedback.
- Coletar comentários (e-mail, formulário, reunião) e registrar em `feedback-log.MD`.
- Ajustar briefing conforme decisões e resolver conflitos.
- Registrar aprovação formal (ata, e-mail, assinatura digital).

### Pontos de decisão
1. **Feedback crítico respondido?**
   - ✅ Sim → finalizar briefing.
   - ❌ Não → agendar call de alinhamento.
2. **Briefing aprovado e versionado?**
   - ✅ Sim → avançar para cronograma.
   - ❌ Não → documentar pendências.

### Outputs
- `_DATA/ContextBriefing/feedback-log.MD`
- `_DATA/ContextBriefing/briefing-naming.MD` (versão final)
- `_DATA/ContextBriefing/aprovacao-briefing.MD`

## ContextBriefing.5: Cronograma e handoff

### Objetivo
Planejar etapas seguintes e compartilhar briefing com a equipe de naming.

### Sequência de ações
- Montar cronograma das próximas etapas (Pesquisa, Geração, Filtros, Testes, Decisão).
- Definir marcos, responsáveis e datas em `_DATA/ContextBriefing/cronograma-naming.MD`.
- Realizar reunião de handoff com equipe de naming e stakeholders.
- Registrar canais de comunicação e checkpoints.
- Atualizar `strategies/Naming/knowledge.MD` com ajustes relevantes (se necessário).

### Pontos de decisão
1. **Cronograma aprovado?**
   - ✅ Sim → iniciar Etapa 1.
   - ❌ Não → ajustar antes de avançar.
2. **Todos os envolvidos têm acesso ao briefing e cronograma?**
   - ✅ Sim → concluir processo.

### Outputs
- `_DATA/ContextBriefing/cronograma-naming.MD`
- `_DATA/ContextBriefing/handoff-naming.MD`

## Indicadores de acompanhamento

- Tempo gasto para concluir briefing.
- Percentual de stakeholders que revisaram/aprovaram (meta ≥ 80%).
- Número de riscos críticos registrados com plano de mitigação.
- Quantidade de revisões (versões) até aprovação final.

## Documentação e governança

- Todos os registros devem ficar em `_DATA/ContextBriefing/`.
- Versões do briefing devem incluir data e responsável.
- Quaisquer aprendizados relevantes devem ser registrados na estratégia (`strategies/Naming/knowledge.MD`).
