# E-mail de Confirmação – LucroSeparado

## Assunto

`[LucroSeparado] Pagamento confirmado e próximos passos do seu diagnóstico`

## Corpo do E-mail

```
Olá, {{first_name}}!

Confirmamos o recebimento do seu pagamento referente ao Plano Mensal LucroSeparado, realizado em {{data_pagamento}} no valor de R$ {{valor}}.

Resumo do pedido:
- Oferta/Plano: LucroSeparado – Plano Mensal Beta Novembro/25
- Valor pago: R$ {{valor}}
- Método de pagamento: {{metodo}}
- Número do pedido: {{id_transacao}}

Próximos passos:
1. Complete o formulário de diagnóstico (leva 5 minutos) → {{link_formulario}}
2. Reserve o melhor horário para nossa sessão inicial → {{link_agendamento}}
3. Entre no grupo exclusivo no WhatsApp para receber alertas e suporte → {{link_grupo}}

Você receberá seu plano de retirada ideal em até 3 horas úteis após o envio do formulário.

Materiais imediatos:
- Download do checklist “Lucro que Não Some”: {{link_checklist}}
- Página de obrigado com todas as instruções: https://lucroseparado.carrd.co/obrigado

Qualquer dúvida, basta responder este e-mail ou falar conosco pelo WhatsApp (+55 21 9XXXX-2208).

Obrigado por confiar na LucroSeparado!

Douglas Prado
Equipe LucroSeparado
suporte@lucroseparado.com
```

## Observações Operacionais

- Variáveis preenchidas via Zapier (payload do PagSeguro + planilha).
- Anexar recibo/nota fiscal quando emitido (até 5 dias úteis).
- Caso o gateway já envie e-mail padrão, programar este template como follow-up 5 minutos após confirmação.
