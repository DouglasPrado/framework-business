# Processo de Execução - Decision and Protection (Naming)

Este processo formaliza a decisão final do nome, inicia registros e prepara guia de uso e contingência.

## Visão geral do fluxo

```
DECISÃO FORMAL → CHECKLISTS DE REGISTRO → GUIA DE USO → PLANO DE CONTINGÊNCIA → MONITORAMENTO E HANDOFF
```

## Entradas obrigatórias

- Short list e recomendação final (`recomendacao-nome.MD`)
- Matriz de avaliação e alertas remanescentes
- Dados das verificações jurídicas e digitais prévias
- Contatos de jurídico, TI/digital, brand guardians

## DecisionProtection.1: Formalização da decisão

### Objetivo
Registrar oficialmente o nome escolhido e comunicar responsáveis.

### Sequência de ações
- Realizar reunião de decisão com sponsor e stakeholders.
- Revisar dados dos testes e riscos remanescentes.
- Registrar decisão em `ata-decisao-nome.MD` (nome, data, responsáveis, backups).
- Atualizar `shortlist-naming.MD` com status (escolhido, backups, descartado).
- Comunicar resultado aos times envolvidos (marketing, jurídico, TI, produto).

### Pontos de decisão
1. **Decisão unânime ou com consenso mínimo?**
   - ✅ Sim → prosseguir.
   - ❌ Não → registrar pendências e definir ações.
2. **Backups confirmados?**
   - ✅ Sim → registrar no plano de contingência.

### Outputs
- `_DATA/DecisionProtection/ata-decisao-nome.MD`
- Atualização em `_DATA/ViabilityFilters/shortlist-naming.MD`

## DecisionProtection.2: Checklists de registro e reservas

### Objetivo
Iniciar registros de marca e reservar domínios/handles.

### Sequência de ações
- Copiar `checklist-registro-nome.MD` (criar se necessário) e listar tarefas (jurídico, domínios, social, app).
- Submeter pedidos de registro de marca (jurídico) e registrar protocolo em `protocolos-registro.MD`.
- Registrar domínios relevantes e handles sociais; salvar comprovantes.
- Atualizar checklist com status (pendente, enviado, em análise, aprovado).
- Envolver times responsáveis para cada ação (jurídico, TI, marketing).

### Pontos de decisão
1. **Todos os protocolos submetidos?**
   - ✅ Sim → monitorar.
   - ❌ Não → acelerar ações críticas.
2. **Algum registro/handle indisponível?**
   - ✅ Sim → acionar plano de mitigação ou backup.

### Outputs
- `_DATA/DecisionProtection/checklist-registro-nome.MD`
- `_DATA/DecisionProtection/protocolos-registro.MD`
- Evidências em `_DATA/DecisionProtection/evidencias/`

## DecisionProtection.3: Guia de uso do nome

### Objetivo
Documentar escrita, pronúncia, narrativa e aplicações do nome.

### Sequência de ações
- Copiar `strategies/Naming/_DATA/templates/guia-uso-nome.MD` para `_DATA/DecisionProtection/`.
- Preencher com: pronúncia, maiúsculas/minúsculas, abreviações, hashtags, traduções.
- Descrever narrativa associada e contexto (como apresentar o nome).
- Incluir exemplos de uso correto/incorreto e orientações por canal.
- Validar guia com brand/marketing e jurídico.

### Pontos de decisão
1. **Guia cobre todos os canais prioritários?**
   - ✅ Sim → registrar aprovação.
   - ❌ Não → incluir orientações faltantes.
2. **Juridico valida restrições (ex.: uso com ® após registro)?**
   - ✅ Sim → prosseguir.

### Outputs
- `_DATA/DecisionProtection/guia-uso-nome.MD`
- Registro de aprovação (e-mail/ata) anexado

## DecisionProtection.4: Plano de contingência

### Objetivo
Preparar respostas caso o registro seja negado ou surjam conflitos.

### Sequência de ações
- Definir gatilhos (indeferimento, oposição, indisponibilidade de domínio).
- Registrar alternativas (nomes backup, ajustes ortográficos, plano de renome).
- Documentar ações (negociação, mudança de classe, variação) e responsáveis.
- Registrar em `plano-contingencia-nome.MD`.
- Validar plano com sponsor e jurídico.

### Pontos de decisão
1. **Backups prontos para ativação se necessário?**
   - ✅ Sim → registrar.
   - ❌ Não → preparar antes de concluir.
2. **Gatilhos e prazos claros?**
   - ✅ Sim → prosseguir.

### Outputs
- `_DATA/DecisionProtection/plano-contingencia-nome.MD`

## DecisionProtection.5: Monitoramento e handoff

### Objetivo
Acompanhar andamento dos registros e preparar fase de ativação.

### Sequência de ações
- Criar `monitoramento-registro.MD` com status (marca, domínios, social, app) e cadência de revisão.
- Definir responsáveis e datas de follow-up (ex.: quinzenal/mensal).
- Compartilhar documentação com times de ativação e governança.
- Atualizar cronograma geral do projeto.
- Registrar aprendizados e pendências.

### Pontos de decisão
1. **Monitoramento programado e owners definidos?**
   - ✅ Sim → encerrar etapa.
   - ❌ Não → ajustar.
2. **Todos os times receberam guia e status?**
   - ✅ Sim → handoff completo.

### Outputs
- `_DATA/DecisionProtection/monitoramento-registro.MD`
- `_DATA/DecisionProtection/handoff-decisao.MD`

## Indicadores de acompanhamento

- Tempo entre decisão e submissão de registros.
- Status dos registros (em análise, aprovado, exigência).
- Percentual de domínios/handles garantidos.
- Cumprimento do plano de contingência (quando acionado).

## Documentação e governança

- Todos os arquivos e evidências devem estar em `_DATA/DecisionProtection/`.
- Versione guia e checklists conforme atualizações.
- Manter sponsor e jurídico informados até conclusão dos registros.
