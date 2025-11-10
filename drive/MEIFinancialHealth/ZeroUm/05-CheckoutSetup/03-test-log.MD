# Log de Testes de Pagamento – LucroSeparado

## Teste 1

- Data e hora: 04/11/2025 09:30 BRT (agendado)
- Responsável: Douglas Prado
- Modo de teste ou produção: Produção com cupom 100% (`MEI-BETA100`)
- Método utilizado (PIX, cartão, boleto): PIX dinâmico
- Valor cobrado: R$0,99 (cobrança mínima para validar fluxo + devolução imediata)
- ID da transação: (será registrado após aprovação)
- Resultado (aprovado, recusado, pendente): pendente de execução
- Evidências (link para print ou PDF): será salvo em `_DATA/evidencias/teste-01-PIX.png`
- Notificações recebidas (cliente, interno, webhook): verificar e-mail do cliente, e-mail interno PagSeguro e disparo Zapier > Slack
- Ajustes realizados após o teste: desativar boleto se notificação atrasar; confirmar personalização da página de obrigado
- Próximo teste necessário: Teste 2 (cartão de crédito)

---

## Teste 2

- Data e hora: 04/11/2025 10:00 BRT (planejado)
- Responsável: Ana Luiza (Financeiro)
- Modo de teste ou produção: Produção com estorno imediato
- Método utilizado: Cartão de crédito (Visa corporativo)
- Valor cobrado: R$5,00 (estorno em até 24h)
- ID da transação: (registrar após aprovação)
- Resultado: pendente de execução
- Evidências: `teste-02-cartao.mp4` (gravação do fluxo) + recibo PagSeguro
- Notificações recebidas: e-mail cliente, e-mail interno, Slack #alerts-lucro
- Ajustes realizados: validar criação automática na planilha Google via webhook; revisar prazo de repasse configurado
- Próximo teste necessário: Teste 3 – boleto (avaliar se manteremos método ativo)

---

## Teste 3

- Data e hora: 04/11/2025 15:00 BRT (condicional)
- Responsável: Douglas Prado
- Modo de teste ou produção: Produção
- Método utilizado: Boleto (apenas se mantivermos método ativo)
- Valor cobrado: R$99,00 (será cancelado antes do vencimento)
- ID da transação: (caso emitido)
- Resultado: aguardando decisão sobre habilitar boleto
- Evidências: n/a
- Notificações recebidas: confirmar e-mail de emissão de boleto
- Ajustes realizados: se decidirmos desativar boleto, registrar justificativa no checkout-config
- Próximo teste necessário: Repetir PIX após primeiro pagamento real para garantir estabilidade
