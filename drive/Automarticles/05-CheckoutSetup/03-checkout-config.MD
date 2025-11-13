# Documento de Configuração do Checkout para o Produto "Automarticles"

## 1. Dados do Produto
- **Produto**: Automarticles
- **Descrição**: Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS.
- **Preço**: R$ 99,00
- **Landing Page**: [https://example.com/automarticles/landing](https://example.com/automarticles/landing)
- **Página de Agradecimento**: [https://example.com/automarticles/obrigado](https://example.com/automarticles/obrigado)
- **E-mail de Suporte**: contato@automarticles.com

## 2. Condições Comerciais
- **Preço**: R$ 99,00
- **Métodos de Pagamento**: PIX, Cartão de Crédito
- **Parcelamento**: Até 3 vezes sem juros (se aplicável).
- **Política de Reembolso**: O cliente pode solicitar reembolso em até 7 dias após a compra, desde que não tenha utilizado o serviço.
- **Termos de Uso**: O uso do Automarticles está sujeito aos termos e condições disponíveis na landing page.

## 3. URL do Checkout
- **Slug Sugerido**: `checkout-automarticles`
- **URL do Checkout**: [https://example.com/checkout-automarticles](https://example.com/checkout-automarticles)

## 4. Campos Obrigatórios
- Nome Completo
- E-mail
- Telefone
- CPF/CNPJ
- Endereço (opcional, se necessário para emissão de recibo)

## 5. Termos e Políticas Vinculadas
- **Política de Cancelamento**: O cliente pode cancelar a assinatura a qualquer momento, com efeito no próximo ciclo de cobrança.
- **Política de Reembolso**: Detalhes sobre como solicitar um reembolso e as condições para a devolução.
- **Termos de Uso**: Os termos de uso devem ser claramente apresentados durante o checkout e devem incluir informações sobre a utilização do serviço, direitos e deveres do usuário.

## 6. Integrações e Webhooks
- **Integrações**:
  - **CRM**: Integrar com o CRM para registrar informações do cliente e status da transação.
  - **Planilha de Controle**: Utilizar webhooks para enviar dados de transações para uma planilha de controle em tempo real.
- **Webhooks**:
  - **Pagamento Aprovado**: URL para receber notificações de pagamento aprovado.
  - **Pagamento Rejeitado**: URL para receber notificações de pagamento rejeitado.
  - **Reembolso Processado**: URL para receber notificações de reembolso.

## 7. Evidências Esperadas
- **Prints do Checkout**: Capturas de tela do checkout configurado, incluindo campos obrigatórios e layout.
- **Logs de Teste**: Registros de transações de teste realizadas, incluindo status e timestamps.
- **E-mails de Notificação**: Prints dos e-mails de confirmação enviados ao cliente e à equipe interna.
- **Documentação**: Arquivos e documentos enviados para a criação da conta no Stripe, incluindo CPF/CNPJ, comprovante bancário e contrato social.

---

## Próximos Passos
1. **Criar Conta no Stripe**: Seguir o plano de configuração e criar a conta utilizando o e-mail institucional.
2. **Enviar Documentação**: Preparar e enviar todos os documentos necessários conforme listado.
3. **Configurar Conta**: Ajustar limites de transação e políticas antifraude no Stripe.
4. **Criar Produto e Checkout**: Configurar o produto "Automarticles" no Stripe com as condições comerciais definidas.
5. **Testar Fluxo de Pagamento**: Realizar testes com transações simbólicas para validar o sistema.
6. **Integrar Checkout à Landing Page**: Atualizar a landing page com o link do checkout.
7. **Documentar Processo**: Registrar todas as etapas e evidências em `_DATA/`.

---

Este documento estabelece um guia claro para a configuração do checkout do produto "Automarticles", garantindo que todas as etapas sejam seguidas e documentadas adequadamente para um go-live bem-sucedido.
