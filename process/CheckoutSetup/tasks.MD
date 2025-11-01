# Checklist Operacional - CheckoutSetup

Este checklist orienta a configuração de um checkout mínimo funcional em até 3 horas, garantindo seleção do gateway, testes, integrações e controles financeiros. Use-o para registrar owners, prazos, evidências e confirmações antes de liberar o link ao público.

## Informações do Projeto

- Oferta / Produto:
- Gateway selecionado:
- Owner principal do checkout:
- Data alvo de go-live:
- Responsável por monitoramento diário:

---

## Etapa 1 – Selecionar gateway (30-40 min)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas
- [ ] Reunir requisitos da oferta (preço, parcelamento, políticas) e registrar em `_DATA/gateway-selection.MD`
- [ ] Consultar catálogo `tools/` e confirmar se gateway é aprovado
- [ ] Comparar taxas, prazos de repasse, suporte a PIX/cartão no template
- [ ] Validar compatibilidade com pessoa física/jurídica e requisitos fiscais
- [ ] Registrar decisão final, link do painel e contatos de suporte

### Output
- [ ] `_DATA/gateway-selection.MD` preenchido e aprovado
- [ ] Lista de documentos necessários para cadastro

---

## Etapa 2 – Configurar conta (30-45 min)

Owner:
Data início:
Data conclusão:

### Tarefas
- [ ] Criar conta no gateway com e-mail institucional e 2FA habilitado
- [ ] Enviar documentos obrigatórios (CPF/CNPJ, comprovante bancário, etc.)
- [ ] Configurar dados bancários / chaves PIX para repasse
- [ ] Ajustar limites de transação e políticas antifraude
- [ ] Registrar status de verificação e responsáveis em `_DATA/checkout-config.MD`
- [ ] Salvar evidência de aprovação em `_DATA/integration-log.MD`

### Output
- [ ] Conta liberada para receber pagamentos
- [ ] `_DATA/checkout-config.MD` atualizado (seção Dados de conta)

---

## Etapa 3 – Criar produto e checkout (40-60 min)

Owner:

### Tarefas
- [ ] Definir nome público e interno do produto/oferta
- [ ] Configurar preço, moeda, parcelamento e cupons (se houver)
- [ ] Habilitar métodos de pagamento necessários (PIX, cartão, boleto)
- [ ] Personalizar checkout (logo, cores, URL amigável, campos obrigatórios)
- [ ] Inserir política de reembolso e termos obrigatórios
- [ ] Registrar link final e capturas em `_DATA/checkout-config.MD`
- [ ] Armazenar prints do checkout em `_DATA/`

### Output
- [ ] Link de checkout ativo documentado
- [ ] Prints do checkout salvos para auditoria

---

## Etapa 4 – Testar pagamentos e notificações (40-50 min)

Owner:
Data do teste:

### Tarefas
- [ ] Realizar pagamento simbólico (cartão ou PIX) e registrar em `_DATA/test-log.MD`
- [ ] Validar e-mails transacionais do gateway (cliente e interno) com evidências
- [ ] Configurar webhooks/integrações e registrar disparos em `_DATA/notification-checklist.MD`
- [ ] Confirmar recebimento no painel e registrar ID da transação
- [ ] Resolver eventuais falhas e repetir testes até aprovação

### Output
- [ ] `_DATA/test-log.MD` com transação aprovada
- [ ] `_DATA/notification-checklist.MD` com notificações validadas
- [ ] Prints/logs anexados em `_DATA/`

---

## Etapa 5 – Integrar à jornada do cliente (30-40 min)

Owner:

### Tarefas
- [ ] Atualizar CTA da landing com o novo link e registrar em `_DATA/integration-log.MD`
- [ ] Criar/atualizar página de obrigado usando `_DATA/thankyou-page-brief.MD`
- [ ] Configurar redirecionamento pós-pagamento para a página de obrigado
- [ ] Adaptar `_DATA/confirmation-email.MD` com instruções e prazos
- [ ] Personalizar `_DATA/receipt-template.MD` com dados da oferta
- [ ] Alinhar com time comercial/suporte o envio de e-mail e recibo

### Output
- [ ] Landing com CTA atualizado (evidência anexada)
- [ ] Página de obrigado publicada e documentada
- [ ] E-mail de confirmação e recibo prontos para uso

---

## Etapa 6 – Organizar controle e handoff (20-30 min)

Owner:

### Tarefas
- [ ] Configurar planilha conforme `_DATA/payment-tracker-guidelines.MD`
- [ ] Definir cadência de atualização e responsáveis (registrar no template)
- [ ] Testar importação manual ou automática de transações
- [ ] Documentar canais de alerta e contingências em `_DATA/integration-log.MD`
- [ ] Compartilhar link do checkout, página de obrigado e planilha com times envolvidos

### Output
- [ ] Planilha de controle ativa e compartilhada
- [ ] Handoff/documentação registrada em `_DATA/integration-log.MD`

---

## Checklist Final de Qualidade

- [ ] Gateway aprovado em `tools/` e conta verificada
- [ ] Link de checkout testado com pagamento real ou modo teste
- [ ] Notificações internas funcionando (e-mail, webhook ou planilha)
- [ ] Página de obrigado acessível e coerente com promessa da landing
- [ ] E-mail de confirmação e recibo revisados e armazenados
- [ ] Planilha de controle com responsável e cadência definidos
- [ ] Evidências organizadas em `_DATA/` (templates atualizados + prints)
- [ ] Validador executado (ver [validator.MD](validator.MD))

---

## Estrutura Recomendada de `_DATA/`

```
_DATA/
├── gateway-selection.MD
├── checkout-config.MD
├── test-log.MD
├── notification-checklist.MD
├── integration-log.MD
├── thankyou-page-brief.MD
├── confirmation-email.MD
├── receipt-template.MD
└── payment-tracker-guidelines.MD
```
