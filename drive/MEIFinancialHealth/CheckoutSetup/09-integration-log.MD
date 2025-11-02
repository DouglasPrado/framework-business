# Log de Integrações e Handoff – LucroSeparado

## Atualizações de Link / CTA

- Data: 04/11/2025 (planejado)
- Responsável: Douglas Prado
- Página/canal: Landing page LucroSeparado (hero + CTA final)
- Link utilizado: https://pag.ae/ls-plano-mensal-beta
- Evidência: `_DATA/evidencias/cta-hero-2025-11-04.png` (a gerar após publicação)
- Observações: testar em desktop e mobile; atualizar QR Code usado em feiras (arquivo `qr-checkout-2025-11-04.png`).

## Página de Obrigado

- Data de publicação: 04/11/2025 (pós testes)
- URL: https://lucroseparado.carrd.co/obrigado
- Responsável: Douglas Prado
- Conteúdo revisado por: Ana Luiza (Financeiro)
- Observações: inclui CTA direto para formulário Typeform e link de agendamento Calendly.

## Comunicação Interna

- Times notificados: Growth, Financeiro, Onboarding (ClientDelivery)
- Canal utilizado: Slack `#go-live-lucro` + e-mail `ops@lucroseparado.com`
- Mensagem: resumo do link final, instruções de backup manual e plano de monitoramento 10h/17h.
- Data/hora de envio: 04/11/2025 às 09h15
- Confirmação de leitura: reações no Slack e resposta de Ana Luiza confirmando recebimento.

## Canais de Alerta e Contingências

- Canal principal: Slack `#alerts-lucro` (integração Zapier)
- Backup: e-mail para suporte@lucroseparado.com + grupo WhatsApp “LucroSeparado Ops”
- Procedimento em caso de pagamento não registrado: 1) verificar painel PagSeguro; 2) reprocessar webhook; 3) lançar manualmente na planilha e enviar e-mail ao cliente; 4) registrar ocorrência neste log.
- Responsável diário: Douglas (10h) / Ana Luiza (17h)

## Handoff Final

- Itens compartilhados: link do checkout, página de obrigado, template de e-mail, recibo, guia da planilha, credenciais 2FA documentadas no cofre da equipe.
- Local de evidências: `drive/MEIFinancialHealth/CheckoutSetup/_DATA/evidencias/` (criar pasta antes do go-live)
- Próximos passos: validar 5 primeiras vendas manualmente; preparar automação de nota fiscal após 10 vendas; revisar copy do e-mail de confirmação após feedback inicial.
- Observações: registrar no RetrospectiveAnalysis métricas dos primeiros 7 dias; garantir que landing, e-mails e checkout mostram mesma política de reembolso.
