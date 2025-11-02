# Checklist Operacional - SalesCallExecution

Use esta lista para garantir preparação completa, execução consultiva e follow-up disciplinado em cada call de vendas. Preencha campos obrigatórios, registre evidências em `_DATA/` e mantenha o pipeline atualizado.

## Informações da Oportunidade

- Nome do lead/empresa:
- Origem do lead:
- Data da call agendada:
- Owner da oportunidade:
- Valor proposto:
- Objetivo da call (fechar, avançar com decisor, validar ajuste):

---

## Etapa 1 – Preparar briefing e meta da call (45-60 min)

Owner:
Data:

### Tarefas
- [ ] Revisar histórico do lead (landing, outreach, indicações, interações anteriores).
- [ ] Confirmar dor principal, urgência e expectativa registrada.
- [ ] Identificar decisores, orçamento estimado e timeline desejada.
- [ ] Definir objetivo central da call (fechamento, next step específico).
- [ ] Preencher `_DATA/prep-call-briefing.MD` com contexto completo e red flags.
- [ ] Enviar confirmação da call com link, agenda e participantes.

### Output
- [ ] Briefing atualizado salvo em `_DATA/`.
- [ ] Evento na agenda compartilhada com lembrete automático.

---

## Etapa 2 – Personalizar proposta e materiais (45-60 min)

Owner:
Data:

### Tarefas
- [ ] Selecionar casos e métricas alinhados ao segmento do lead.
- [ ] Atualizar deck/demo com linguagem e exemplos específicos.
- [ ] Definir preço, bônus, garantias e condições de pagamento.
- [ ] Testar link de pagamento ou contrato simplificado.
- [ ] Preparar bullets-chave e perguntas estratégicas para a call.
- [ ] Compartilhar materiais internos relevantes com o time (se necessário).

### Output
- [ ] Materiais personalizados versionados em pasta compartilhada ou `_DATA/`.
- [ ] Link de pagamento validado e registrado no briefing.

---

## Etapa 3 – Ensaiar roteiro e logística (15-20 min)

Owner:
Data:

### Tarefas
- [ ] Adaptar `_DATA/roteiro-sales-call.MD` com abertura, diagnóstico, proposta e fechamento.
- [ ] Ensaiar respostas para objeções previstas.
- [ ] Testar equipamentos (áudio, vídeo), conexão e gravação (se autorizada).
- [ ] Abrir documento/planilha para notas em tempo real.
- [ ] Reconfirmar presença do lead (quando agendado com antecedência).

### Output
- [ ] Roteiro final com anotações específicas salvo em `_DATA/`.
- [ ] Checklist técnico concluído (equipamentos e gravação).

---

## Etapa 4 – Conduzir call consultiva (15-25 min)

Owner:
Data:

### Tarefas
- [ ] Iniciar call agradecendo, reforçando agenda e pedindo autorização para gravação/anotações.
- [ ] Atualizar diagnóstico confirmando dor, impacto e urgência.
- [ ] Apresentar proposta conectando dor → solução → resultado → prova social.
- [ ] Investigar objeções com perguntas de clarificação antes de responder.
- [ ] Registrar objeções e respostas em `_DATA/objection-log.MD`.
- [ ] Alinhar próximo passo com data e responsável (pagamento, segunda call, envio de materiais).

### Output
- [ ] Notas detalhadas alimentando `_DATA/pos-call-resumo.MD`.
- [ ] Objeções e compromissos registrados no log.

---

## Etapa 5 – Follow-up imediato (até 30 min pós-call)

Owner:
Horário previsto:

### Tarefas
- [ ] Completar `_DATA/pos-call-resumo.MD` com dor, proposta, decisão e próximos passos.
- [ ] Enviar e-mail/mensagem de follow-up com resumo, link de pagamento e prazo acordado usando `../_SHARED/templates/email-followup.MD` como base.
- [ ] Anexar materiais prometidos (deck, gravação, cases).
- [ ] Atualizar pipeline/CRM com status, ticket e data do próximo contato.
- [ ] Programar lembrete interno para checar pagamento ou resposta.

### Output
- [ ] Follow-up enviado (copiar texto e registrar no briefing).
- [ ] Pipeline atualizado com próxima ação agendada.

---

## Etapa 6 – Confirmar pagamento e acionar onboarding (até 4h)

Owner:
Status:

### Tarefas
- [ ] Monitorar confirmação do pagamento (gateway ou comprovante manual).
- [ ] Agradecer recebimento e reforçar próximos passos.
- [ ] Enviar resumo ao responsável por ClientDelivery com expectativas e dados do lead.
- [ ] Atualizar indicadores comerciais (taxa de fechamento, ticket, motivo de perda).
- [ ] Arquivar comprovação e mensagens de confirmação em `_DATA/`.
- [ ] Se pagamento não ocorrer, disparar sequência de follow-up D+1 e D+3 com os snippets do template compartilhado.

### Output
- [ ] Comprovante ou registro de pagamento armazenado.
- [ ] Handoff documentado para ClientDelivery.
- [ ] Registro de status final (Fechado, Follow-up, Perdido) no pipeline.

---

## Sequência de Follow-up Padrão (quando pagamento não confirmado)

- [ ] Follow-up 24h após call (usar variação 24h do template).
- [ ] Follow-up 72h após call (usar variação 48-72h do template).
- [ ] Mensagem final (usar roteiro de reengajamento do template, documentar motivo de perda).

---

## Checklist Final de Qualidade

- [ ] Todos os templates em `_DATA/` preenchidos e salvos com data/versão.
- [ ] Objeções registradas e categorizadas para análise futura.
- [ ] Follow-up enviado em até 30 minutos e anexado ao briefing.
- [ ] Status do lead atualizado no pipeline/CRM com próxima ação definida ou encerramento justificado.
- [ ] Pagamento confirmado ou sequência de follow-up ativa.
- [ ] Handoff para ClientDelivery documentado (quando venda fechada).
- [ ] Validador executado (ver [validator.MD](validator.MD)).

---

## Estrutura Recomendada de Evidências em `_DATA/`

```
_DATA/
├── prep-call-briefing.MD
├── roteiro-sales-call.MD
├── pos-call-resumo.MD
├── objection-log.MD
├── comprovantes/
│   ├── pagamento-YYYYMMDD.png
│   └── comprovante-transferencia.pdf
├── followups/
│   ├── followup-YYYYMMDD.md
│   └── followup-YYYYMMDD-reminder.md
└── recordings/ (quando autorizado)
    ├── call-YYYYMMDD.mp4
    └── call-YYYYMMDD-notas.txt
```

Mantenha nomenclatura consistente por lead (ex: `cliente-nome-YYYYMMDD`) para facilitar auditorias e retroalimentação em `RetrospectiveAnalysis`.
