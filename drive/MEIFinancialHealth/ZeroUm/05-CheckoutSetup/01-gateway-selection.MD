# Seleção de Gateway de Pagamento – LucroSeparado

## Identificação

- Data da análise: 02/11/2025
- Oferta / Produto: LucroSeparado – Plano Mensal de Acompanhamento Financeiro
- Ticket médio previsto: R$99,00 (mensal) com possibilidade de planos trimestrais
- Volume esperado: 30 transações no primeiro mês (beta), projeção de 60/mês após abertura geral
- Responsável pela escolha: Douglas Prado

## Plataformas Consideradas

1. PagSeguro PagBank
   - URL do painel: https://acesso.pagseguro.uol.com.br/
   - Suporte a métodos: PIX dinâmico, cartão de crédito (à vista e parcelado), boleto
   - Taxa por transação: cartão 3,99% + R$0,40; PIX 0,99% (planos MEI)
   - Taxa de recebimento: saque gratuito para conta PagBank; TED R$1,99 (opcional)
   - Prazo de repasse padrão: PIX imediato; cartão D+30 (com opção de antecipação)
   - Suporte local: atendimento em pt-BR (telefone/WhatsApp), base de conhecimento ampla
   - Observações: gateway já utilizado por outros processos internos; emite links curtos e QR Code; aceita MEI com documentação simplificada.

2. Asaas
   - URL do painel: https://www.asaas.com/
   - Suporte a métodos: PIX, cartão, boleto, carnê
   - Taxa por transação: cartão 3,39% + R$0,39; PIX gratuito até determinado limite, depois 0,99%
   - Taxa de recebimento: transferência bancária gratuita (dois dias úteis)
   - Prazo de repasse padrão: PIX instantâneo; cartão D+30
   - Suporte local: chat e telefone em pt-BR; base técnica detalhada
  - Observações: painel robusto e com automações, porém exige integração manual para página de obrigado e cobra mensalidade após 300 cobranças.

## Critérios de Decisão

- Requisitos legais atendidos: ambos aceitam MEI com CNPJ e CCMEI; PagSeguro não exige contrato social adicional.
- Suporte a PIX: disponível nas duas opções.
- Suporte a cartão de crédito (parcelamento máximo): PagSeguro até 12x (repasse D+30); Asaas até 12x.
- Fee médio projetado: PagSeguro 3,99% + R$0,40 sobre R$99 → R$4,34; Asaas 3,39% + R$0,39 → R$3,74 (diferença marginal).
- Prazo de repasse: prioridade para PIX instantâneo; PagSeguro libera no ato.
- Integração com landing: PagSeguro gera link direto curto compatível com Carrd e WhatsApp; Asaas requer página intermediária ou botão com script.
- Disponibilidade de modo teste: PagSeguro não tem sandbox total, mas permite cupom 100% e estorno rápido; Asaas possui modo teste parcial.
- Facilidade de gerar recibo/nota: PagSeguro oferece comprovante automático; Asaas possui automação com Nota Fiscal de Serviços (não necessário nesta fase).
- Integração com ferramentas atuais: PagSeguro envia notificações por e-mail e API; integrações via webhook disponíveis; compatível com Zapier/Make.
- Riscos identificados: PagSeguro tem limite inicial de R$5 mil/dia (suficiente para o beta); Asaas cobra mensalidade se volume crescer, além de fluxo de aprovação mais lento.

## Decisão Final

- Gateway escolhido: PagSeguro PagBank (link de pagamento + checkout PagSeguro)
- Justificativa: suporte imediato a PIX e cartão, cadastro simplificado para MEI, experiência consolidada em links compartilháveis, integração rápida com Carrd e WhatsApp, além de custos compatíveis com ticket atual.
- Links importantes:
  - Cadastro: https://cadastro.pagseguro.uol.com.br/
  - Painel: https://acesso.pagseguro.uol.com.br/
  - Central de ajuda: https://faq.pagseguro.uol.com.br/
- Documentos necessários:
  - RG/CPF: cópia digital em PDF
  - CNPJ/CCMEI: documento atualizado (emitido em 2025)
  - Comprovante bancário: extrato conta PJ Itaú (últimos 90 dias)
  - Outros: selfie de verificação e comprovante de endereço em nome do titular
- Próximos passos imediatos:
  - Criar conta e ativar 2FA (Douglas – 03/11)
  - Enviar documentação e aguardar aprovação (Douglas – 03/11)
  - Configurar produto e gerar link de checkout (Douglas – 04/11)

## Aprovação

- Responsável pela aprovação: Douglas Prado (Owner de Go-to-Market)
- Data: 02/11/2025
- Observações adicionais: avaliar integração via webhook PagSeguro > Sheet após confirmação dos cinco primeiros pagamentos.
