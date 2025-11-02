# Validador - CheckoutSetup

## Propósito

Garantir que o checkout configurado esteja pronto para uso público, com pagamentos testados, notificações funcionando e controles financeiros ativos. Utilize este validador após concluir o checklist operacional para aprovar (ou reprovar) o lançamento.

## Como Usar

1. Revise cada seção correspondente às etapas do processo.
2. Marque os critérios atendidos com base nas evidências armazenadas em `_DATA/`.
3. Registre observações e ações corretivas quando necessário.
4. Use o checklist final para decidir sobre o go-live do checkout.

---

## Validação da Etapa 1 – Seleção do Gateway

**Critério 1.1 – Análise documentada**
- [ ] `_DATA/gateway-selection.MD` contém comparação de taxas, métodos suportados e decisão final.
- [ ] Gateway escolhido consta no catálogo `tools/` (ou aprovação documentada).
- [ ] Documentos necessários para cadastro listados e disponíveis.

**Critério 1.2 – Alinhamento estratégico**
- [ ] Justificativa da escolha considera requisitos de oferta, ticket médio e público.
- [ ] Riscos ou limitações do gateway foram registrados.

Evidências: `_DATA/gateway-selection.MD`

---

## Validação da Etapa 2 – Conta Configurada

**Critério 2.1 – Credenciais e segurança**
- [ ] Conta criada com e-mail institucional e 2FA habilitado (print ou log).
- [ ] Documentos enviados e verificação aprovada (status registrado em `_DATA/integration-log.MD`).

**Critério 2.2 – Dados financeiros**
- [ ] `_DATA/checkout-config.MD` registra dados bancários, responsáveis e limites configurados.
- [ ] Política antifraude ajustada conforme diretrizes comerciais.

Evidências: `_DATA/checkout-config.MD`, `_DATA/integration-log.MD`

---

## Validação da Etapa 3 – Produto e Checkout

**Critério 3.1 – Configuração do produto**
- [ ] Preço, parcelamento e métodos de pagamento coerentes com oferta.
- [ ] Termos de uso e política de cancelamento visíveis no checkout.
- [ ] Nome e descrição alinhados com landing page.

**Critério 3.2 – Documentação**
- [ ] Link final do checkout registrado em `_DATA/checkout-config.MD`.
- [ ] Capturas do checkout armazenadas em `_DATA/`.

Evidências: `_DATA/checkout-config.MD`, prints anexos

---

## Validação da Etapa 4 – Testes e Notificações

**Critério 4.1 – Pagamento aprovado**
- [ ] `_DATA/test-log.MD` possui transação aprovada (valor, método, timestamp, ID).
- [ ] Comprovante do gateway anexado (print ou PDF).

**Critério 4.2 – Notificações funcionais**
- [ ] `_DATA/notification-checklist.MD` confirma disparo de e-mails internos/cliente.
- [ ] Webhook ou integração configurada e validada (quando aplicável).
- [ ] Painel exibe transação e status correto.

**Critério 4.3 – Checklist de qualidade**
- [ ] Checklist compartilhado (`../_SHARED/templates/checklist-qualidade.MD`) executado e sem pendências críticas.

Evidências: `_DATA/test-log.MD`, `_DATA/notification-checklist.MD`, prints

---

## Validação da Etapa 5 – Jornada do Cliente

**Critério 5.1 – Integração com landing**
- [ ] `_DATA/integration-log.MD` registra atualização do CTA com link correto.
- [ ] Página de obrigado publicada e redirecionamento testado.

**Critério 5.2 – Comunicação pós-compra**
- [ ] `_DATA/confirmation-email.MD` adaptado com dados finais da oferta.
- [ ] `_DATA/receipt-template.MD` revisado e pronto para envio.
- [ ] Conteúdo do e-mail/página informa próximos passos e canais de suporte.

Evidências: `_DATA/integration-log.MD`, `_DATA/thankyou-page-brief.MD`, `_DATA/confirmation-email.MD`, `_DATA/receipt-template.MD`

---

## Validação da Etapa 6 – Controle e Handoff

**Critério 6.1 – Monitoramento financeiro**
- [ ] `_DATA/payment-tracker-guidelines.MD` preenchido com estrutura da planilha e cadência de atualização.
- [ ] Planilha ou dashboard criado e acessível (link registrado).
- [ ] Responsáveis definidos e comunicados.

**Critério 6.2 – Comunicação interna**
- [ ] `_DATA/integration-log.MD` documenta canais de alerta, contingências e owners.
- [ ] Link do checkout e documentos compartilhados com vendas/entrega.

Evidências: `_DATA/payment-tracker-guidelines.MD`, `_DATA/integration-log.MD`

---

## Checklist de Decisão Final

- [ ] Todos os critérios das etapas 1-6 atendidos sem pendências críticas.
- [ ] Testes de pagamento e notificações concluídos com evidências salvas.
- [ ] Página de obrigado, e-mail e recibo aprovados pelo responsável comercial.
- [ ] Planilha de controle ativa, com owners e cadência definida.
- [ ] Riscos e limitações documentados com plano de mitigação (quando aplicável).

### Resultado

- [ ] Aprovado para go-live (liberar link publicamente)
- [ ] Aprovado com ajustes menores (detalhar abaixo)
- [ ] Não aprovado (correções obrigatórias antes de liberar)

Observações finais:

Responsável pela validação:
Data:
