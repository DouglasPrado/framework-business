# Seleção de Gateway de Pagamento

## Identificação

- Data da análise: 31/10/2023
- Oferta / Produto: Automarticles
- Ticket médio previsto: R$ 99,00
- Volume esperado (transações/dia ou mês): 50 transações/mês
- Responsável pela escolha: [Nome do responsável]

## Plataformas Consideradas

1. Nome do gateway: Stripe
   - URL do painel: https://dashboard.stripe.com/
   - Suporte a métodos (PIX, cartão, boleto, etc.): Cartão de crédito, débito, PIX, e boleto.
   - Taxa por transação: 2,9% + R$ 0,30 por transação.
   - Taxa de recebimento (antecipação, saque): Não informado.
   - Prazo de repasse padrão: 7 dias após a transação.
   - Suporte local (idioma, atendimento): Suporte em português via chat e e-mail.
   - Observações: APIs robustas e fácil integração com CMS.

2. Nome do gateway: PagSeguro
   - URL do painel: https://pagseguro.uol.com.br/
   - Suporte a métodos (PIX, cartão, boleto, etc.): Cartão de crédito, débito, PIX, e boleto.
   - Taxa por transação: 4,99% + R$ 0,40 por transação (cartão), 2,99% para pagamentos via PIX.
   - Taxa de recebimento (antecipação, saque): Não informado.
   - Prazo de repasse padrão: 30 dias para pagamentos via cartão, 1 dia para PIX.
   - Suporte local (idioma, atendimento): Suporte em português via chat, telefone e e-mail.
   - Observações: Integração com CMS, mas pode ser menos flexível que Stripe.

## Critérios de Decisão

- Requisitos legais atendidos (pessoa física/jurídica, emissão de NF): Sim, ambos os gateways permitem a emissão de nota fiscal.
- Suporte a PIX: Sim, ambos os gateways suportam.
- Suporte a cartão de crédito (parcelamento máximo): Sim, ambos suportam parcelamento, mas o Stripe não especifica limite de parcelas.
- Fee médio projetado (% + valor fixo): Stripe: 2,9% + R$ 0,30; PagSeguro: 4,99% + R$ 0,40 (cartão).
- Prazo de repasse (dias úteis): Stripe: 7 dias; PagSeguro: 30 dias (cartão).
- Integração com landing / recursos de link único: Sim, ambos oferecem integração fácil.
- Disponibilidade de modo teste: Sim, ambos oferecem modo sandbox.
- Facilidade de gerar recibo/nota: Sim, ambos permitem a emissão de nota fiscal.
- Integração com ferramentas atuais (CRM, automações): Sim, Stripe possui APIs robustas para integração.
- Riscos identificados (limites de conta, retenções, reputação): Stripe apresenta menor risco em termos de taxas e prazos de repasse.

## Decisão Final

- Gateway escolhido: Stripe
- Justificativa resumida: O Stripe foi escolhido devido às suas taxas competitivas, prazos de repasse mais curtos e facilidade de integração com a plataforma Automarticles. Além disso, o suporte técnico e a segurança oferecida são adequados para garantir uma experiência de compra tranquila.
- Links importantes (cadastro, painel, suporte): 
  - Cadastro: https://dashboard.stripe.com/register
  - Painel: https://dashboard.stripe.com/
  - Suporte: https://support.stripe.com/
- Documentos necessários:
  - RG/CPF: CPF da empresa.
  - CNPJ/Contrato Social: CNPJ da empresa e contrato social.
  - Comprovante bancário: Comprovante de conta bancária para repasse.
  - Outros: Políticas de reembolso e cancelamento.
- Próximos passos imediatos (responsável e prazo):
  - Criar conta no Stripe: [Nome do responsável] até 07/11/2023.
  - Enviar documentação necessária: [Nome do responsável] até 14/11/2023.

## Aprovação

- Responsável pela aprovação: [Nome do responsável]
- Data: 31/10/2023
- Observações adicionais: Não informado.
