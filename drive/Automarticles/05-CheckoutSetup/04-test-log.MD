# Documento de Testes do Checkout para o Produto "Automarticles"

## 1. Dados do Produto
- **Produto**: Automarticles
- **Preço**: R$ 99,00
- **URL do Checkout**: [https://example.com/checkout-automarticles](https://example.com/checkout-automarticles)

## 2. Lista de Testes

### Testes em Modo Sandbox (Teste)
1. **Teste de Pagamento com PIX**
   - **Método**: PIX
   - **Valor**: R$ 99,00
   - **ID da Transação**: TXN-TEST-PIX-001
   - **Resultado Esperado**: Notificação de pagamento aprovado recebida.
   - **Registro de Notificação**: URL de webhook para pagamento aprovado.

2. **Teste de Pagamento com Cartão de Crédito**
   - **Método**: Cartão de Crédito (número fictício)
   - **Valor**: R$ 99,00
   - **ID da Transação**: TXN-TEST-CARD-001
   - **Resultado Esperado**: Notificação de pagamento aprovado recebida.
   - **Registro de Notificação**: URL de webhook para pagamento aprovado.

3. **Teste de Pagamento Rejeitado com Cartão de Crédito**
   - **Método**: Cartão de Crédito (número inválido)
   - **Valor**: R$ 99,00
   - **ID da Transação**: TXN-TEST-CARD-REJECT-001
   - **Resultado Esperado**: Notificação de pagamento rejeitado recebida.
   - **Registro de Notificação**: URL de webhook para pagamento rejeitado.

4. **Teste de Reembolso**
   - **Método**: Reembolso (simulação após pagamento aprovado)
   - **ID da Transação**: TXN-TEST-PIX-001
   - **Resultado Esperado**: Notificação de reembolso processado recebida.
   - **Registro de Notificação**: URL de webhook para reembolso.

### Testes em Modo Live
1. **Teste de Pagamento com PIX**
   - **Método**: PIX
   - **Valor**: R$ 99,00
   - **ID da Transação**: TXN-LIVE-PIX-001
   - **Resultado Esperado**: Notificação de pagamento aprovado recebida.
   - **Registro de Notificação**: URL de webhook para pagamento aprovado.

2. **Teste de Pagamento com Cartão de Crédito**
   - **Método**: Cartão de Crédito
   - **Valor**: R$ 99,00
   - **ID da Transação**: TXN-LIVE-CARD-001
   - **Resultado Esperado**: Notificação de pagamento aprovado recebida.
   - **Registro de Notificação**: URL de webhook para pagamento aprovado.

3. **Teste de Pagamento Rejeitado com Cartão de Crédito**
   - **Método**: Cartão de Crédito (número inválido)
   - **Valor**: R$ 99,00
   - **ID da Transação**: TXN-LIVE-CARD-REJECT-001
   - **Resultado Esperado**: Notificação de pagamento rejeitado recebida.
   - **Registro de Notificação**: URL de webhook para pagamento rejeitado.

4. **Teste de Reembolso**
   - **Método**: Reembolso (simulação após pagamento aprovado)
   - **ID da Transação**: TXN-LIVE-PIX-001
   - **Resultado Esperado**: Notificação de reembolso processado recebida.
   - **Registro de Notificação**: URL de webhook para reembolso.

## 3. Registro de Notificações Recebidas
- **Notificações de Pagamento Aprovado**
  - **ID da Transação**: TXN-TEST-PIX-001
  - **Timestamp**: 2023-10-31 10:00:00
  - **Método**: PIX
  - **Status**: Aprovado

- **Notificações de Pagamento Rejeitado**
  - **ID da Transação**: TXN-TEST-CARD-REJECT-001
  - **Timestamp**: 2023-10-31 10:05:00
  - **Método**: Cartão de Crédito
  - **Status**: Rejeitado

- **Notificações de Reembolso Processado**
  - **ID da Transação**: TXN-TEST-PIX-001
  - **Timestamp**: 2023-10-31 10:10:00
  - **Método**: PIX
  - **Status**: Reembolsado

## 4. Checklist de Correções
- [ ] Verificar se todos os campos obrigatórios estão sendo validados corretamente.
- [ ] Confirmar se as notificações de pagamento estão sendo recebidas em tempo real.
- [ ] Validar se a política de reembolso está sendo aplicada corretamente.
- [ ] Testar a integração com o CRM para garantir que os dados do cliente estão sendo registrados.
- [ ] Checar se a planilha de controle está recebendo dados de transações corretamente.

---

## Próximos Passos
1. **Executar os testes em modo sandbox** e registrar os resultados.
2. **Revisar as notificações recebidas** e corrigir quaisquer falhas identificadas.
3. **Realizar testes em modo live** após a validação dos testes em sandbox.
4. **Documentar todos os resultados** e evidências em `_DATA/`.

---

Este documento garante que todos os testes necessários para o checkout do produto "Automarticles" sejam realizados e registrados adequadamente, permitindo um go-live seguro e eficiente.
