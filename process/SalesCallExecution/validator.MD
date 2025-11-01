# Validador - SalesCallExecution

## Propósito

Garantir que calls de vendas sejam concluídas com qualidade consultiva, documentação adequada e transição imediata para onboarding ou próximos passos definidos. Execute este validador após completar o checklist operacional para confirmar se critérios mínimos foram atendidos.

## Como Usar

1. Revise cada seção equivalente às etapas do processo.
2. Marque critérios atendidos com base nas evidências arquivadas em `_DATA/`.
3. Documente observações e ajustes necessários quando algum critério não for atendido.
4. Utilize o checklist de decisão final para aprovar o avanço (pagamento/onboarding) ou definir correções.

---

## Validação da Etapa 1 – Briefing e qualificação

**Critério 1.1 – Contexto completo**
- [ ] `_DATA/prep-call-briefing.MD` contém origem do lead, dor principal, expectativa e decisores.
- [ ] Objetivo da call está definido (fechamento, decisão com terceiro, validação final).
- [ ] Evento de agenda confirmado com link e participantes corretos.

**Critério 1.2 – Qualificação**
- [ ] Lead mantém aderência ao ICP (perfil priorizado em TargetUserIdentification).
- [ ] Existe percepção de urgência ou problema ativo.
- [ ] Não há red flag bloqueadora sem plano de ação.

Evidências: `_DATA/prep-call-briefing.MD`, convites/agenda.

---

## Validação da Etapa 2 – Proposta personalizada

**Critério 2.1 – Materiais alinhados**
- [ ] Deck/demo foi atualizado com casos relevantes ou bullets personalizados.
- [ ] Link de pagamento ou contrato testado e registrado.
- [ ] Bônus/garantias revisados e alinhados com oferta comunicada na landing.

**Critério 2.2 – Consistência**
- [ ] Promessa feita ao lead está alinhada ao que será entregue (ver LandingPageCreation).
- [ ] Não existem discrepâncias entre preço comunicado e tabela oficial.

Evidências: materiais em `_DATA/` ou pasta compartilhada, anotações do briefing.

---

## Validação da Etapa 3 – Roteiro e logística

**Critério 3.1 – Preparação técnica**
- [ ] `_DATA/roteiro-sales-call.MD` contém adaptações específicas para o lead.
- [ ] Testes de áudio/vídeo foram realizados (anotação no briefing ou check no roteiro).
- [ ] Autorização para gravação e armazenamento confirmada (quando aplicável).

**Critério 3.2 – Planejamento da conversa**
- [ ] Perguntas de diagnóstico principais anotadas.
- [ ] Prova social selecionada e pronta para uso.
- [ ] Objeções prováveis listadas com plano de resposta.

Evidências: `_DATA/roteiro-sales-call.MD`, notas de preparação.

---

## Validação da Etapa 4 – Execução da call

**Critério 4.1 – Diagnóstico e proposta**
- [ ] Notas da call registram dor, impacto e urgência com linguagem do lead.
- [ ] Proposta foi apresentada conectando dor → solução → resultado → prova social.
- [ ] Compromisso claro confirmado (pagamento, próxima call, envio de materiais).

**Critério 4.2 – Objeções documentadas**
- [ ] Objeções e respostas registradas em `_DATA/objection-log.MD`.
- [ ] Nova objeção relevante adicionada ao repositório (quando aplicável).

Evidências: `_DATA/pos-call-resumo.MD`, `_DATA/objection-log.MD`, gravação/notas.

---

## Validação da Etapa 5 – Follow-up imediato

**Critério 5.1 – Comunicação**
- [ ] Follow-up enviado em até 30 minutos (timestamp registrado).
- [ ] Mensagem inclui resumo da dor, proposta, link de pagamento e prazo acordado.
- [ ] Materiais prometidos anexados ou compartilhados.

**Critério 5.2 – Pipeline**
- [ ] Pipeline/CRM atualizado com status e próxima ação datada.
- [ ] Lembretes de follow-up configurados (quando pagamento não imediato).

Evidências: `_DATA/pos-call-resumo.MD`, cópia do follow-up em `_DATA/followups/`.

---

## Validação da Etapa 6 – Confirmação e handoff

**Critério 6.1 – Pagamento**
- [ ] Comprovante ou confirmação do gateway arquivado.
- [ ] Agradecimento enviado ao lead/cliente com próxima etapa definida.
- [ ] Sequência de follow-up pós-call em andamento quando pagamento não realizado.

**Critério 6.2 – Onboarding**
- [ ] Resumo da call enviado ao responsável por ClientDelivery.
- [ ] Indicadores comerciais atualizados (taxa de fechamento, ticket, motivo).
- [ ] Status final registrado (Fechado, Follow-up, Perdido) com justificativa.

Evidências: `_DATA/comprovantes/`, `_DATA/followups/`, mensagens internas.

---

## Checklist de Decisão Final

- [ ] Critérios das etapas 1 a 6 atendidos.
- [ ] Evidências arquivadas e acessíveis em `_DATA/`.
- [ ] Objeções novas documentadas para revisão futura.
- [ ] Próximo processo (ClientDelivery ou follow-up) acionado.
- [ ] Métricas comerciais atualizadas para `RetrospectiveAnalysis`.

### Resultado

- [ ] Aprovado (pagamento confirmado, onboarding iniciado)
- [ ] Aprovado com ajustes (detalhar ações pendentes)
- [ ] Não aprovado (corrigir itens acima antes de avançar)

Observações finais:

Responsável pela validação:
Data:
