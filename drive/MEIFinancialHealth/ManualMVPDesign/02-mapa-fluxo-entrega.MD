# Mapa de Fluxo de Entrega – LucroSeparado (MVP Manual)

## Visão Geral do Fluxo

1. Recebimento e triagem
2. Onboarding e coleta de dados
3. Produção do diagnóstico
4. QA e ajustes
5. Entrega ao cliente
6. Follow-up e acompanhamento semanal

Tempo total estimado por cliente (SLA interno): 2h45min de trabalho ativo distribuído em até 3 horas úteis para a primeira entrega + 30 minutos semanais de acompanhamento.

---

## 1. Recebimento e Triagem

- **Tarefas**
  - Capturar submissão do Typeform (tempo estimado: 2 min)
  - Conferir dados mínimos obrigatórios (nome, contato, faturamento, despesas principais) (5 min)
  - Registrar entrada no board (3 min)
  - Enviar confirmação automática com prazo (template de onboarding) (3 min)
- **Responsável primário:** Douglas
- **Dependências:** webhook do Typeform ativo, planilha de controle liberada
- **Checkpoints**
  - Dados completos? → se não, mover para status “Aguardando informações” e disparar lembrete.
  - Cliente elegível (dentro do perfil MEI produtos físicos)? → se não, acionar fluxo de recusa ou reagendamento.
- **Gargalos potenciais e mitigação**
  - Alto volume de formulários simultâneos → criar fila no board, comunicar expectativa de prazo no e-mail.

## 2. Onboarding e Coleta Complementar

- **Tarefas**
  - Ligar ou enviar áudio confirmando objetivo e prazo (10 min)
  - Solicitar extratos ou prints de transações recentes (até 30 dias) (5 min)
  - Guiar configuração inicial de subcontas (vídeo curto + checklist) (10 min)
  - Atualizar board com “Dados completos” (2 min)
- **Responsável primário:** Douglas
- **Dependências:** cliente enviar anexos, acesso ao WhatsApp Business
- **Checkpoints**
  - Confirmar entendimento da promessa (retirada ideal + alertas semanais).
  - Verificar se limites e despesas foram informados (quando falta, mover para “Aguardando anexo”).
- **Gargalos**
  - Cliente demora a responder → lembrete automático após 12h; se 24h sem resposta, pausar e comunicar time de Growth.

## 3. Produção do Diagnóstico

- **Tarefas**
  - Importar dados da planilha padrão (5 min)
  - Calcular margem histórica, pró-labore recomendado, reserva de estoque e impostos (25 min)
  - Redigir plano textual (WhatsApp) com contexto e próximos passos (10 min)
  - Registrar tempo real no Toggl e board (2 min)
- **Responsável primário:** Douglas
- **Dependências:** planilha bloqueada com fórmulas, dados atualizados
- **Checkpoints**
  - Margem ≥ 15%? se não, destacar necessidade de ajuste no plano.
  - Pró-labore dentro da meta (20% da receita líquida)? se não, justificar recomendação.
- **Gargalos**
  - Dados inconsistentes → mover para “Revisar com cliente” e agendar chamada rápida.

## 4. QA e Ajustes

- **Tarefas**
  - Revisão independente da planilha e do plano textual (15 min)
  - Checar links, cálculos, formatação e clareza (10 min)
  - Aprovar registro no board (2 min)
- **Responsável primário:** Ana Luiza
- **Dependências:** acesso à planilha, tempo registrado pelo produtor
- **Checkpoints**
  - Campos obrigatórios preenchidos (valores, alertas, próximos passos).
  - Erros encontrados? registrar em coluna “Observações QA” e devolver para produção.
- **Gargalos**
  - Acúmulo de QA no final do dia → reservar janela fixa 11h-12h e 16h-17h.

## 5. Entrega ao Cliente

- **Tarefas**
  - Enviar e-mail de entrega com documento e links (5 min)
  - Enviar áudio personalizado no WhatsApp explicando pontos críticos (10 min)
  - Atualizar board para “Entregue” e disparar alerta no Slack (3 min)
- **Responsável primário:** Douglas
- **Dependências:** aprovação QA, templates de e-mail e áudio
- **Checkpoints**
  - Confirmar recebimento (cliente responde ou confirma no WhatsApp).
  - Registrar data/hora do envio no board e planilha.
- **Gargalos**
  - Cliente não confirma recebimento → follow reminder após 6h.

## 6. Follow-up e Acompanhamento Semanal

- **Tarefas**
  - Agendar follow-up 48h após entrega para feedback e dúvidas (10 min)
  - Configurar alertas semanais (segunda-feira) com checagem manual dos saldos (15 min)
  - Registrar feedback na planilha e atualizar padrões de qualidade se necessário (10 min)
  - Finalizar ciclo com relatório semanal interno (10 min)
- **Responsável primário:** Douglas (follow-up) e Ana Luiza (registro e ajustes)
- **Dependências:** planilha de acompanhamento, script de alerta, calendário
- **Checkpoints**
  - Feedback coletado? se não, relembrar cliente antes de encerrar ciclo.
  - Ajustes processados e documentados no inventário.
- **Gargalos**
  - Agenda conflitando com múltiplos clientes → bloquear horários fixos (seg 14h-16h, qui 10h-12h) para follow-ups.

---

## Pontos de Controle Gerais

- SLAs monitorados diariamente via board (coluna “Deadline SLA”).
- Cada etapa possui owner e backup designados; se o owner não puder executar em até 2 horas do prazo, acionar backup.
- Gargalos registrados no relatório do piloto com impacto e ações corretivas.
