# Manual Operacional – LucroSeparado MVP Manual (Versão 1.0)

## Visão Geral

- **Objetivo:** entregar em até 3 horas úteis o diagnóstico de retirada ideal e acompanhar semanalmente MEIs de produtos físicos durante 30 dias.
- **Período:** Piloto beta novembro/2025 (30 vagas).
- **Equipe:** Douglas Prado (Onboarding, Produção, Entrega, Follow-up), Ana Luiza (QA, Financeiro, Planilha), Carla Ferreira (Advisory/feedback).

## Fluxo Resumido (detalhe em `02-mapa-fluxo-entrega.MD`)

1. Recebimento do formulário (Typeform) e triagem.
2. Onboarding com coleta de extratos e orientação de subcontas.
3. Produção manual do diagnóstico na planilha padrão.
4. QA independente e registro no board.
5. Entrega por e-mail + áudio WhatsApp.
6. Follow-up 48h + alertas semanais + relatório de 30 dias.

Tempo ativo médio por cliente: 2h45min para primeira entrega + 30 min/semana acompanhamento.

## Ferramentas e Acessos

- Google Sheets (`LucroSeparado - Operação Manual`) – board + planilha de diagnóstico.
- Typeform (Formulário Diagnóstico) – captura dados iniciais.
- WhatsApp Business – comunicação principal com clientes.
- Zapier – integrações Typeform/Sheets/Slack/PagSeguro.
- Google Drive – armazenamento de materiais (planilhas, PDFs, evidências).
- Calendly – agendamento dos encontros quinzenais.

Permissões atualizadas em `03-estrutura-board.MD` e `09-integration-log.MD`.

## Documentos Base

- Briefing e critérios de sucesso (`01-briefing-manual-mvp.MD`).
- Checklist de execução individual (`04-checklist-execucao.MD`).
- Padrões de qualidade (`08-padroes-qualidade.MD`).
- Templates de comunicação (`05`, `06`, `07`).
- Inventário de materiais (`10-inventario-materiais.MD`).
- Relatório do piloto (`09-relatorio-piloto.MD`) – atualizar ao final das entregas.

## Checkpoints Chave

- **SLA triagem:** formulário respondido e confirmado em ≤ 1h.
- **SLA diagnóstico:** entrega em ≤ 3h úteis após dados completos.
- **QA:** segunda revisão obrigatória antes de qualquer envio.
- **Follow-up:** 48h após entrega (obrigatória coleta de feedback).
- **Alertas:** segunda-feira até 12h com dados atualizados.
- **Retrospectiva:** sexta-feira 17h (tempo vs. meta, gargalos, melhorias).

## Indicadores de Acompanhamento

- SLA cumprido (%).
- Horas gastas por etapa (registradas no Toggl e no board).
- Satisfação média (escala 1-3).
- Número de exceções e retrabalhos.
- Receita recorrente gerada (via planilha de pagamentos).

Relatórios semanais arquivados na aba `Resumo Semana` da planilha.

## Procedimentos de Contingência

- Dados incompletos → mover para status `Aguardando dados`, enviar lembrete automático e notificar Growth se passar de 24h.
- Retrabalho necessário → registrar em `Observações QA`, corrigir em até 4h e documentar no relatório do piloto.
- Falha em integrações → seguir plano de contingência no `04-notification-checklist.MD` (registro manual e alerta para equipe).
- SLA ameaçado → escalar para Ana Luiza e pausar novas vendas até normalizar fila.

## Gestão de Conhecimento

- Evidências (prints, gravações) armazenadas em `drive/MEIFinancialHealth/ManualMVPDesign/_EVIDENCIAS/` (criar pasta por cliente).
- Atualizações de processo comunicadas no Slack #go-live-lucro e registradas aqui com histórico de versões.
- Ajustes maiores devem ser incorporados ao `08-padroes-qualidade.MD` e replicados no checklist.

## Histórico de Versões

- **v1.0 – 02/11/2025:** criação inicial do MVP manual com base nos processos ProblemHypothesisDefinition, TargetUserIdentification, LandingPageCreation e CheckoutSetup.
- Próxima revisão agendada para 18/11/2025 (após término do piloto).
