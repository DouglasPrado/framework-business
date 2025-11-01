# Guia para Planilha de Controle de Pagamentos

## Objetivo

Registrar todas as transações processadas pelo checkout, garantindo conciliação diária, monitoramento de pendências e envio de recibos.

## Estrutura Recomendada

Crie uma planilha (Google Sheets ou ferramenta aprovada) com as seguintes colunas:

- Data da venda
- Nome do cliente
- E-mail do cliente
- Valor pago
- Método (PIX, cartão, boleto)
- Parcelas (quando aplicável)
- ID da transação / Pedido
- Status (Aprovado, Pendente, Estornado, Chargeback)
- Recibo enviado? (Sim/Não + data)
- Nota fiscal emitida? (Sim/Não + número)
- Responsável pelo follow-up
- Próximos passos / observações

Adicione abas opcionais:
- `Resumo` com totais por período e método de pagamento
- `Chargebacks/Estornos` para acompanhamento de disputas
- `Config` com links úteis (checkout, painel, suporte)

## Cadência de Atualização

- Verificação diária em até 2 horários (ex: 10h e 17h) – anotar no rodapé da planilha.
- Reconciliar valores com painel do gateway pelo menos 1 vez/semana.
- Atualizar status para `Recibo enviado` e `NF emitida` assim que ações forem concluídas.

## Responsabilidades

- Owner da planilha:
- Substituto em caso de ausência:
- Canal para reportar falhas (Slack, e-mail, outro):

## Procedimentos Operacionais

1. Registrar automaticamente via webhook ou copiar do painel do gateway.
2. Validar manualmente dados críticos (valor, nome, método) após importação.
3. Emitir recibo/nota e marcar status correspondente.
4. Atualizar coluna “Próximos passos” com follow-up (ex: agendar onboarding).
5. Arquivar prints/comprovantes em pasta compartilhada (`_DATA/evidencias/` ou equivalente).

## Indicadores Recomendados

- Total recebido por dia/semana.
- Taxa de conversão de pagamentos (aprovados vs. tentativas).
- Tempo médio para envio de recibo.
- Quantidade de pendências abertas (>24h sem confirmação).

## Observações

- Se utilizar automações (Zapier, Make, etc.), documente fluxo e credenciais em `_DATA/integration-log.MD`.
- Realize backup semanal da planilha em PDF ou CSV.
