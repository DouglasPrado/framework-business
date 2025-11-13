# Log de Testes de Pagamento

## Teste 1

- Data e hora: 2023-10-31 10:00:00
- Responsável: João Silva
- Modo de teste ou produção: Sandbox
- Método utilizado (PIX, cartão, boleto): PIX
- Valor cobrado: R$ 99,00
- ID da transação: TXN-TEST-PIX-001
- Resultado (aprovado, recusado, pendente): Aprovado
- Evidências (link para print ou PDF): [Print do teste PIX](https://example.com/print-teste-pix)
- Notificações recebidas (cliente, interno, webhook): Notificação de pagamento aprovado recebida no webhook.
- Ajustes realizados após o teste: Nenhum ajuste necessário.
- Próximo teste necessário: Teste de pagamento com cartão de crédito.

---

## Teste 2

- Data e hora: 2023-10-31 10:05:00
- Responsável: Maria Oliveira
- Modo de teste ou produção: Sandbox
- Método utilizado: Cartão de Crédito (número fictício)
- Valor cobrado: R$ 99,00
- ID da transação: TXN-TEST-CARD-001
- Resultado: Aprovado
- Evidências: [Print do teste Cartão de Crédito](https://example.com/print-teste-cartao)
- Notificações recebidas: Notificação de pagamento aprovado recebida no webhook.
- Ajustes realizados: Nenhum ajuste necessário.
- Próximo teste necessário: Teste de pagamento rejeitado com cartão de crédito.

---

## Teste 3

- Data e hora: 2023-10-31 10:10:00
- Responsável: Carlos Pereira
- Modo de teste ou produção: Sandbox
- Método utilizado: Cartão de Crédito (número inválido)
- Valor cobrado: R$ 99,00
- ID da transação: TXN-TEST-CARD-REJECT-001
- Resultado: Rejeitado
- Evidências: [Print do teste Cartão de Crédito Rejeitado](https://example.com/print-teste-cartao-rejeitado)
- Notificações recebidas: Notificação de pagamento rejeitado recebida no webhook.
- Ajustes realizados: Ajustar validação de número de cartão.
- Próximo teste necessário: Teste de reembolso após pagamento aprovado.
