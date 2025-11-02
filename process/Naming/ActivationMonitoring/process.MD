# Processo de Execução - Activation and Monitoring (Naming)

Este processo coordena o lançamento do nome aprovado e o monitoramento contínuo da sua percepção e uso.

## Visão geral do fluxo

```
PLANO DE ATIVAÇÃO → ATUALIZAÇÃO DE MATERIAIS → TREINAMENTO & COMUNICAÇÃO → MONITORAMENTO → LOG DE AJUSTES & HANDOFF
```

## Entradas obrigatórias

- `guia-uso-nome.MD` e documentação final de `DecisionProtection`.
- Checklists e planos de branding (ExperienceJourney, RolloutGovernance) quando aplicáveis.
- Lista de materiais/canais existentes e owners.
- Ferramentas de monitoramento (analytics, social listening, SEO, pesquisa interna).

## ActivationMonitoring.1: Plano de ativação

### Objetivo
Definir cronograma, canais, responsáveis e mensagens para ativar o nome.

### Sequência de ações
- Revisar decisão final, plano de governança e status de registros.
- Criar `plano-ativacao-nome.MD` com ondas (interno → parceiros → público), canais e prazos.
- Priorizar materiais críticos (site, landing, contratos, suporte, pitches) e registrar owners.
- Validar plano com sponsor/brand guardian e times de comunicação.

### Pontos de decisão
1. **Plano cobre todos os canais apontados no briefing?**
   - ✅ Sim → prosseguir.
   - ❌ Não → incluir itens pendentes.
2. **Cronograma está sincronizado com status de registro e lançamentos?**
   - ✅ Sim → avançar.

### Outputs
- `_DATA/ActivationMonitoring/plano-ativacao-nome.MD`

## ActivationMonitoring.2: Atualização de materiais

### Objetivo
Garantir que todos os pontos de contato reflitam o novo nome.

### Sequência de ações
- Criar `checklist-atualizacao-materiais.MD` classificando itens por prioridade.
- Atualizar materiais internamente ou acionar donos (marketing, produto, legal, suporte).
- Salvar evidências (links, prints, arquivos) na pasta `evidencias/atualizacoes-materiais/`.
- Registrar status (feito, pendente, backlog) e data/owner.
- Documentar backlog para itens secundários com prazo e responsável.

### Pontos de decisão
1. **Materiais críticos atualizados antes do go-live?**
   - ✅ Sim → seguir.
   - ❌ Não → renegociar cronograma ou priorizar recursos.
2. **Backlog registrado e comunicado?**
   - ✅ Sim → prosseguir.

### Outputs
- `_DATA/ActivationMonitoring/checklist-atualizacao-materiais.MD`
- Evidências em `_DATA/ActivationMonitoring/evidencias/`

## ActivationMonitoring.3: Treinamentos e comunicação

### Objetivo
Alinhar equipes internas, parceiros e, quando aplicável, público externo.

### Sequência de ações
- Planejar sessão sincrônica ou conteúdo assíncrono (`treinamento-nome.MD`).
- Distribuir guia de uso, FAQ, pronúncia, scripts de atendimento.
- Disparar comunicados internos (e-mail, intranet, Slack) e externos (press release, social) conforme plano.
- Registrar presença/confirmar acesso aos materiais.
- Manter canal para dúvidas (e-mail, Slack, formulário) e registrar interações relevantes.

### Pontos de decisão
1. **Times críticos confirmaram treinamento/comunicação?**
   - ✅ Sim → documentar.
   - ❌ Não → agendar reforço.
2. **Canal de suporte documentado?**
   - ✅ Sim → incluir nos comunicados.

### Outputs
- `_DATA/ActivationMonitoring/treinamento-nome.MD`
- `_DATA/ActivationMonitoring/comunicados/`

## ActivationMonitoring.4: Monitoramento de percepção e uso

### Objetivo
Acompanhar indicadores e feedbacks após o lançamento.

### Sequência de ações
- Definir KPIs (menções positivas/negativas, brand search, SEO, NPS/CSAT, dúvidas internas, tickets).
- Configurar dashboards/planilhas (`monitoramento-marca-nome.MD`) com responsáveis e cadência.
- Criar alertas automáticos (social listening, Google Alerts) se aplicável.
- Realizar checkpoints (ex.: 24h, 72h, semanal, mensal) registrando resultados.

### Pontos de decisão
1. **Dashboard e alertas funcionando?**
   - ✅ Sim → seguir.
   - ❌ Não → ajustar antes de prosseguir.
2. **Indicadores dentro das metas?**
   - ✅ Sim → manter acompanhamento.
   - ❌ Não → documentar em log e propor ajustes.

### Outputs
- `_DATA/ActivationMonitoring/monitoramento-marca-nome.MD`
- Evidências/prints em `_DATA/ActivationMonitoring/evidencias/`

## ActivationMonitoring.5: Log de ajustes e handoff contínuo

### Objetivo
Registrar melhorias, garantir governança e transferir aprendizados.

### Sequência de ações
- Atualizar `log-ajustes-nome.MD` com feedbacks (internos/externos), ações tomadas e responsáveis.
- Integrar acompanhamento aos rituais de governança (brand, marketing, CX).
- Preparar `relatorio-pos-ativacao.MD` (opcional) com resultados iniciais e próximos passos.
- Handoff para squads ou áreas que continuarão monitoramento (growth, CX, branding).
- Atualizar documentação estratégica com aprendizados relevantes.

### Pontos de decisão
1. **Ritual de governança configurado?**
   - ✅ Sim → registrar data/owner.
   - ❌ Não → alinhar antes de encerrar.
2. **Aprendizados e backlog documentados?**
   - ✅ Sim → concluir etapa.

### Outputs
- `_DATA/ActivationMonitoring/log-ajustes-nome.MD`
- `_DATA/ActivationMonitoring/handoff-ativacao.MD`
- (Opcional) `_DATA/ActivationMonitoring/relatorio-pos-ativacao.MD`

## Indicadores de acompanhamento

- % de materiais atualizados (checklist).
- Sentimento de menções (positivo, neutro, negativo).
- Variação de brand search/SEO.
- Número de dúvidas internas recebidas/resolvidas.
- NPS/CSAT após implantação do novo nome.

## Documentação e governança

- Todos os arquivos devem permanecer em `_DATA/ActivationMonitoring/`.
- Versionar plano, checklists e dashboards conforme ajustes.
- Integrar monitoramento aos rituais de marca/governança contínua.
