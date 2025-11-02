# Log de Integrações e Handoff

Utilize este arquivo para documentar atualizações de link, comunicações internas e entregas relacionadas ao checkout.

## Atualizações de Link / CTA

- Data: 2025-10-31
- Responsável: Owner de Growth (Ana Martins)
- Página/canal atualizado (Landing, botão em e-mail, bio, etc.): Landing principal ZeroUm – CTA Hero
- Link utilizado: https://zeroum.carrd.co/checkout
- Evidência (print ou URL): `_DATA/evidencias/cta-hero-2025-10-31.png`
- Observações: Clique testado em desktop e mobile após publicação.

## Página de Obrigado

- Data de publicação/atualização: 2025-10-31
- URL: https://zeroum.carrd.co/obrigado
- Responsável: Ops Enablement (Bruno Costa)
- Conteúdo validado por: Owner de Growth (Ana Martins)
- Observações: Inclui resumo da oferta, link para onboarding e canal de suporte (support@zeroum.team).

## Comunicação Interna

- Times notificados (vendas, suporte, entrega): Vendas, Suporte, ClientDelivery
- Canal utilizado (Slack, e-mail, WhatsApp): Slack #go-live e e-mail `ops@zeroum.team`
- Mensagem enviada (resumo): “Checkout ZeroUm publicado, link final, página de obrigado e recibo anexados. Monitoramento 2x/dia pela equipe de Growth.”
- Data e hora: 2025-10-31 às 10h30
- Confirmação de leitura: Reações registradas no Slack + resposta de confirmação do time de Suporte.

## Canais de Alerta e Contingências

- Canal principal de notificações: Slack #alerts-checkout (integração via webhook)
- Backup/contingência em caso de falha: E-mail para ops@zeroum.team + ligação direta para Owner de Growth
- Procedimento em caso de pagamento não registrado: Conferir painel do gateway, reprocessar webhook e atualizar planilha manualmente; responder cliente em até 30 minutos.
- Responsável por acompanhar diariamente: Ana Martins (Growth) / backup Bruno Costa (Ops)
- Horários de verificação: 10h00 e 17h00 (horário de Brasília)

## Handoff Final

- Itens compartilhados (link checkout, página obrigado, templates, planilha): Link checkout, link página de obrigado, `confirmation-email.MD`, `receipt-template.MD`, planilha de pagamentos.
- Local onde evidências estão armazenadas: Pasta `_DATA/evidencias/checkout-go-live-2025-10-31/`
- Próximos passos combinados: Validar 5 primeiras vendas manualmente, automatizar nota fiscal após volume > 10 vendas, revisar copy da página de obrigado em 7 dias.
- Observações finais: Checklist de qualidade executado e sem pendências; monitoramento semanal será reportado na RetrospectiveAnalysis.
