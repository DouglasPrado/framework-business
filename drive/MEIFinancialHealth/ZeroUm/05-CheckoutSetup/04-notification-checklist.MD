# Checklist de Notificações e Integrações – LucroSeparado

## E-mails Automáticos do Gateway

- [ ] Cliente recebe e-mail de confirmação PagSeguro com dados corretos (print esperado após Teste 1)
- [ ] Time interno recebe notificação de nova venda no e-mail finance@lucroseparado.com
- [ ] Link de recibo PagSeguro presente e funcionando
- [ ] Conteúdo revisado (ajustar texto padrão para incluir suporte@lucroseparado.com)

## Webhooks / Automação

- [ ] Webhook Zapier → Slack `#alerts-lucro` disparou com payload correto (`transactionStatus=PAID`)
- [ ] Automação Zapier → Google Sheets criou linha com ID da transação e valor
- [ ] Logs verificados sem erros (consultar histórico Zapier, guardar ID do evento)
- [ ] Falhas tratadas com plano de contingência (fallback: planilha preenchida manualmente + alerta via WhatsApp)

## Planilha de Controle

- [ ] Entrada registrada na aba `2025` (colunas preenchidas automaticamente)
- [ ] Recibo marcado como “enviado” após disparo do e-mail personalizado
- [ ] Responsável notificado (Douglas às 10h, Ana às 17h) – confirmar via Slack DM

## Alertas Manuais

- [ ] Mensagem automática para equipe de entrega (WhatsApp grupo `LucroSeparado | Entrega`)
- [ ] Cliente recebe instruções adicionais com link de onboarding (e-mail adicional usando `confirmation-email.MD`)
- [ ] Próximos passos definidos na planilha (coluna “Follow-up”)

## Observações

- Pendências encontradas: aguardar aprovação do gateway para finalizar testes; confirmar se boleto será mantido.
- Ações corretivas: revisar texto padrão do e-mail PagSeguro; garantir que link de redirecionamento funciona em mobile.
- Próxima revisão agendada para: 04/11/2025 às 18h (após testes PIX e cartão)
