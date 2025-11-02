# Guia da Planilha de Controle de Pagamentos – LucroSeparado

## Objetivo

Registrar todas as transações processadas pelo PagSeguro, garantindo conciliação diária, envio de recibos e disparo das ações de onboarding sem atrasos.

## Estrutura Recomendada

Planilha Google `Pagamentos LucroSeparado` com as colunas:

- Data da venda
- Nome do cliente
- E-mail
- Telefone / WhatsApp
- Valor pago
- Método (PIX, Cartão)
- Parcelas
- ID da transação PagSeguro
- Status (Aprovado, Pendente, Estornado, Chargeback)
- Recibo enviado? (Sim/Não + data)
- Nota fiscal emitida? (Sim/Não + número)
- Sessão de diagnóstico agendada? (Sim/Não + link)
- Responsável pelo follow-up
- Próximos passos / observações

Abas adicionais:
- `Resumo`: totais por dia e método.
- `Chargebacks`: registros detalhados de disputas.
- `Config`: links úteis (checkout, painel, suporte, automações Zapier).

## Cadência de Atualização

- Verificação diária às 10h00 e 17h00 (Douglas 10h / Ana Luiza 17h).
- Conciliação com painel PagSeguro toda segunda-feira às 18h, registrando no rodapé da aba `Resumo`.
- Atualizar status “Recibo enviado” e “NF emitida” até 2h após confirmação do pagamento.

## Responsabilidades

- Owner da planilha: Douglas Prado – douglas@lucroseparado.com
- Substituto: Ana Luiza (Financeiro) – financeiro@lucroseparado.com
- Canal para reportar falhas: Slack `#alerts-lucro` + e-mail suporte@lucroseparado.com

## Procedimentos Operacionais

1. Webhook PagSeguro → Zapier → Google Sheets cria linha preliminar.
2. Conferir valores e dados do cliente manualmente após importação.
3. Disparar e-mail de confirmação (template `06-confirmation-email.MD`) se ainda não enviado.
4. Emitir recibo/nota e marcar colunas correspondentes.
5. Registrar link de agendamento do onboarding na coluna “Sessão de diagnóstico agendada”.
6. Arquivar prints e comprovantes em `_DATA/evidencias/` no formato `AAAA-MM-DD-<descrição>.png`.

## Indicadores Recomendados

- Total diário por método de pagamento.
- Taxa de conversão (transações aprovadas / tentativas).
- Tempo médio entre pagamento e envio do recibo.
- Número de pendências > 24h sem follow-up.

## Observações

- Documentar alterações na automação Zapier em `09-integration-log.MD`.
- Gerar backup semanal (exportar CSV) toda sexta-feira às 18h.
