# Configuração do Checkout – LucroSeparado

## Identificação

- Gateway utilizado: PagBank PagSeguro (link de pagamento)
- Data de criação do checkout: agendada para 04/11/2025 (em preparação)
- Responsável pela configuração: Douglas Prado
- E-mail de login do gateway: finance@lucroseparado.com
- ID interno do produto: `LS-PLANO-MENSAL-01`

## Dados da Conta e Segurança

- Status de verificação: Documentação enviada (02/11) – aguardando aprovação automática do PagSeguro
- Documentos enviados: RG + selfie, CCMEI atualizado, comprovante bancário (Itaú conta PJ), comprovante de endereço
- Métodos de autenticação habilitados: 2FA via aplicativo PagBank + SMS backup
- Usuários com acesso ao painel: Douglas Prado (owner), Ana Luiza (financeiro) com perfil de leitura
- Limites configurados: valor por transação R$1.200; limite diário R$8.000 (solicitado aumento após primeira semana)
- Políticas antifraude: aprovação manual para valores > R$500; bloqueio de países fora do Brasil; notificações instantâneas por e-mail

## Produto / Oferta

- Nome interno: LucroSeparado – Plano Mensal Beta
- Nome apresentado ao cliente: Plano Mensal LucroSeparado (Beta Novembro/25)
- Descrição resumida: Acompanhamento financeiro com IA + mentorias quinzenais para MEIs de produtos físicos
- Valor à vista: R$99,00 (recorrência mensal manual)
- Parcelamento permitido: até 3x sem juros (demais parcelas com juros do gateway)
- Métodos habilitados: PIX dinâmico, cartão de crédito, boleto (desativado após validação – avaliar demanda)
- Cupom configurado: `MEI-BETA100` (100% desconto para testes internos e convidados do piloto)
- Política de reembolso destacada: reembolso integral em até 7 dias via e-mail suporte@lucroseparado.com, conforme art. 49 CDC

## Checkout

- URL final do checkout: https://pag.ae/ls-plano-mensal-beta (slug reservado, publicar após aprovação)
- URL alternativa (modo teste/sandbox): cupom `MEI-BETA100` aplicado em ambiente de produção (não há sandbox)
- Campos obrigatórios: nome completo, e-mail, CPF, telefone com DDD, CEP
- Termos e política vinculados: https://lucroseparado.notion.site/termos-e-politica e https://lucroseparado.notion.site/reembolso
- Layout escolhido: tema padrão PagSeguro com cor principal #1F6FEB; logo 600x200 em PNG; botão CTA “Garantir minha vaga”
- URL de redirecionamento pós-pagamento: https://lucroseparado.carrd.co/obrigado
- Observações de customização: mensagem personalizada “Verifique seu e-mail em até 5 minutos para receber o diagnóstico” + suporte WhatsApp (21) 9XXXX-2208

## Integrações

- Webhooks configurados: Zapier Webhook (https://hooks.zapier.com/hooks/catch/1234567/abcdef) – evento `transaction.approved`
- Ferramentas conectadas: Google Sheets `Pagamentos LucroSeparado` (aba `2025`), Slack #alerts-lucro (via Zapier), MailerLite (tag `Cliente LucroSeparado`)
- Responsável por monitorar falhas: Douglas Prado (backup Ana Luiza)
- Logs relevantes: teste webhook ID `evt_pagseguro_882001` (planejado para 04/11 após primeira transação)

## Evidências

- Links para prints/screen recordings: adicionar em `_DATA/evidencias/checkout-2025-11-04/` após go-live
- Comprovante de transação teste: reservado para transação `TESTE-PIX-001` (prevista 04/11 09h30)
- Observações finais: aguardando liberação formal do gateway; revisar se boleto permanecerá ativo ou será desativado após validação inicial.
