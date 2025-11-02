# Briefing do MVP Manual – LucroSeparado

## Identificação

- Data: 02/11/2025
- Responsável: Douglas Prado
- Produto/Serviço: LucroSeparado – Plano Mensal de acompanhamento financeiro para MEIs de produtos físicos
- Objetivo desta rodada: validar entrega manual do diagnóstico financeiro + acompanhamento quinzenal antes de automatizar cálculos e alertas

## Escopo do MVP Manual

- Promessa central: entregar em até 3 horas úteis um plano de “retirada ideal” (pró-labore + reservas de estoque e impostos) e acompanhar semanalmente o fluxo de caixa através de alertas personalizados no WhatsApp por 30 dias.
- Público atendido nesta rodada: MEIs que vendem produtos físicos (cosméticos artesanais, alimentação delivery, marketplaces) – até 30 clientes no piloto.
- Itens inclusos:
  - Diagnóstico inicial (coleta de dados + planilha consolidada)
  - Configuração manual de subcontas ou envelopes financeiros
  - Alertas semanais via WhatsApp com revisão de saldo e próximos passos
  - Sessões quinzenais de acompanhamento por áudio ou chamada de 20 minutos
- Itens explicitamente fora do escopo:
  - Integração automática com bancos ou ERPs
  - Emissão de nota fiscal automática (será manual)
  - Atendimento 24/7 (suporte focado em horário comercial 9h-18h BRT)

## Critérios de Sucesso

- SLA de entrega do diagnóstico inicial ≤ 3 horas úteis após recebimento do formulário completo.
- Envio de alertas semanais dentro do horário programado (segunda-feira até 12h).
- Satisfação do cliente ≥ “entregou o que prometeu” em follow-up (escala 1-3, meta ≥ 2,5).
- Taxa de execução sem retrabalho ≥ 85% (checklist concluído sem correções).
- Coleta de feedback estruturado em 100% das entregas durante o período beta.

## Recursos Disponíveis

- Time: Douglas Prado (Onboarding + Produção), Ana Luiza (QA + Financeiro), Carla Ferreira (advisory/prova social para materiais).
- Ferramentas aprovadas: Google Sheets, Notion, Typeform, WhatsApp Business, Toggl (para cronometrar), Google Drive.
- Materiais existentes:
  - Planilha-base de fluxo semanal (TargetUserIdentification insights).
  - Copy de onboarding e checklist “Lucro que Não Some”.
  - Landing page, checkout e página de obrigado configuradas.

## Métricas a Monitorar

- Tempo real gasto por etapa (recebimento, onboarding, produção, QA, entrega, follow-up).
- Número de ajustes solicitados após entrega.
- Tempo de resposta ao cliente (mensagens e e-mails).
- Evolução do saldo projetado vs. real em cada acompanhamento semanal.

## Riscos e Mitigações

- **Formulários incompletos:** incluir checklist de validação automática e mensagem padrão solicitando dados faltantes antes de iniciar produção.
- **Sobrecarga de atendimento manual:** limitar a 6 entregas por dia, registrar prioridades no board e pausar vendas se fila exceder 48h.
- **Inconsistência nos cálculos:** dupla checagem por Ana Luiza antes de enviar diagnóstico; usar planilha padrão bloqueada para fórmulas.
- **Comunicação fora do tom:** utilizar templates de e-mail/WhatsApp e revisar semanalmente.
- **Atrasos por dependências externas (dados bancários):** enviar lembrete automático após 12h sem resposta; marcar como “Em espera” no board.

## Suposições a Validar

- MEIs conseguem seguir instruções de separação manual com alertas de WhatsApp sem integrações bancárias.
- Tempo de 3 horas úteis é suficiente para consolidar dados e produzir o plano de retirada ideal.
- Alertas semanais + acompanhamento quinzenal são percebidos como alto valor (redução do “dinheiro que some”).
- Volume de 30 clientes é suportável com a equipe atual e garante aprendizado suficiente para priorizar automações.

## Próximos Passos

1. Mapear fluxo detalhado com tempos estimados por etapa (Etapa 2).
2. Configurar board operacional no Google Sheets com status padronizados.
3. Produzir templates de comunicação (onboarding, entrega, follow-up) com base no vocabulário validado.
4. Rodar piloto interno com 2 clientes beta (Carla e João) cronometrando cada etapa.
