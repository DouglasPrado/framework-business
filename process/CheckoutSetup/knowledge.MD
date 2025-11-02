# Base de Conhecimento - CheckoutSetup

## Visão Geral

Checkouts mínimos devem equilibrar velocidade de implementação com confiabilidade operacional. A configuração correta garante que vendas aprovadas sejam notificadas em minutos, que o cliente receba orientações claras e que a equipe interna mantenha controle financeiro rigoroso desde a primeira transação.

## Objetivo Central

Fornecer orientações sobre seleção de gateways, configurações críticas, conformidade e resolução rápida de incidentes, viabilizando recebimento imediato sem comprometer a experiência do cliente ou a governança financeira.

## Princípios Fundamentais

1. **Segurança primeiro:** use e-mail institucional, autenticação em dois fatores e controle de acessos no painel.
2. **Conformidade tributária:** defina com antecedência se haverá nota fiscal, recibo ou contrato simples, evitando bloqueios posteriores.
3. **Experiência contínua:** landing, checkout, e-mail e página de obrigado devem contar a mesma história (promessa, prazos, suporte).
4. **Redundância de alertas:** combine e-mails automáticos, webhooks e planilha monitorada para reduzir risco de vendas despercebidas.
5. **Higiene de dados:** padronize nomes de produtos, IDs e campos para facilitar reconciliação, análise e auditorias futuras.

## Conceitos-Chave

### Gateway versus Plataforma de infoproduto
- **Gateway** (Stripe, PagSeguro): oferece infraestrutura de pagamento direta, com maior flexibilidade e necessidade de configuração manual.
- **Plataforma** (Hotmart, Kiwify): inclui checkout pronto, automações básicas e suporte a afiliados, porém com taxas específicas e menos controle.
- Avalie de acordo com o tipo de oferta, ticket médio e necessidade de automação.

### PIX e cartão de crédito
- PIX oferece confirmação praticamente instantânea e taxas menores.
- Cartão possibilita parcelamento, mas exige atenção a antifraude e chargebacks.
- Alguns gateways permitem link único com QR Code dinâmico e fallback para cartão; valide na etapa de seleção.

### Webhooks e integrações
- Webhooks enviam eventos em tempo real para CRMs, planilhas ou Slack.
- Garanta que URLs estejam seguras (HTTPS) e que haja logs de fallback.
- Se não houver webhook, configure exportação manual diária e registre no `payment-tracker-guidelines.MD`.

### Antifraude
- Limites baixos iniciais protegem contra uso indevido do checkout recém-criado.
- Ajuste gradualmente conforme histórico positivo de transações.
- Documente regras aprovadas com o time financeiro para evitar bloqueios injustificados.

## Perguntas Frequentes

### O gateway desejado não está em `tools/`. O que fazer?
Documente justificativa no `_DATA/gateway-selection.MD` e encaminhe solicitação de aprovação. Enquanto não houver resposta, utilize opção já aprovada para não atrasar o go-live.

### Como realizar teste sem gastar saldo?
- Alguns gateways oferecem modo sandbox; se disponível, realize em paralelo com teste real.
- Utilize cupom de 100% ou reembolso imediato após teste.
- Para PIX, transfira valor mínimo e registre reembolso na planilha.

### Preciso emitir nota fiscal?
- Consulte política da empresa e legislação local. Para PF, recibo simples pode ser suficiente inicialmente.
- Se NF for obrigatória, sincronize com processo de cobrança semanal ou conecte API/integração quando viável.

### Como lidar com chargebacks?
- Registre imediatamente na planilha e abra chamado no gateway dentro do prazo.
- Coletar evidências (e-mail, recibo, termos aceitos) e documentar no `_DATA/`.
- Avalie ajustes em antifraude e comunicação para evitar reincidência.

### Posso usar checkout direto no WhatsApp?
- Sim: compartilhe o link curto gerado pelo gateway.
- Garanta que `integration-log.MD` registre onde o link está sendo divulgado para rastreamento e atualizações futuras.

## Checkpoints de Qualidade

1. **Acesso e segurança:** conta com 2FA e usuários restritos.
2. **Fluxo testado:** transação real aprovada e notificação recebida em até 5 minutos.
3. **Comunicação clara:** página de obrigado e e-mail informam próximos passos e canais.
4. **Compliance visível:** política de reembolso e termos acessíveis no checkout.
5. **Governança:** planilha ou dashboard atualizado diariamente com owner definido.

## Boas Práticas Operacionais

- Nomeie links de checkout com versão e data (`checkout-oferta-v1`), facilitando auditoria.
- Crie QR Code derivado do link para apresentações e eventos, registrando uso no log.
- Centralize prints e comprovantes em `_DATA/evidencias/` com padrão `AAAA-MM-DD-<descrição>.png`.
- Configure alertas de estorno/pendência no painel para evitar perda de prazo de contestação.
- Teste redirecionamento da página de obrigado em dispositivos móveis; links do gateway podem abrir em telas externas.

## Riscos e Mitigações

- **Conta bloqueada após primeira venda**
  - Sinal: e-mail do gateway solicitando documentos adicionais.
  - Mitigação: enviar documentação completa antes do go-live e registrar confirmação.
- **Cliente não recebe confirmação**
  - Sinal: ausência de e-mail em até 5 minutos após pagamento.
  - Mitigação: revisar notificações, disparar e-mail manual com o template e corrigir integração.
- **Link desatualizado circulando**
  - Sinal: vendas ou leads chegando por checkout antigo.
  - Mitigação: registrar mudanças em `_DATA/integration-log.MD`, arquivar links antigos e comunicar equipe.
- **Falta de reconciliação financeira**
  - Sinal: diferença entre valores do painel e planilha.
  - Mitigação: reconciliar diariamente, atribuir owner e manter histórico de ajustes na planilha.
- **Chargeback por promessa não cumprida**
  - Sinal: reclamação do cliente em até 7 dias questionando entrega.
  - Mitigação: alinhar copy da landing com entrega real, reforçar prazos na página de obrigado e e-mail.

## Integrações com Outros Processos

- **LandingPageCreation:** CTA principal deve apontar para o link final aprovado e comunicar prazo de entrega coerente.
- **SalesCallExecution:** equipe comercial usa o link no follow-up e precisa receber notificações em tempo real.
- **ClientDelivery:** onboarding só começa após confirmação na planilha e envio do recibo.
- **ManualMVPDesign:** garante que promessa do checkout esteja alinhada ao fluxo de entrega.
- **RetrospectiveAnalysis:** usa métricas financeiras para avaliar desempenho do lançamento.

## Próximos Passos Recomendados

1. Monitorar primeiras 10 vendas manualmente para validar performance e notificações.
2. Avaliar necessidade de automatizar emissão de notas ou recibos após volume inicial.
3. Planejar revisão mensal de taxas e condições do gateway.
4. Atualizar estratégias de follow-up com dados reais (tempo entre compra e onboarding).

## Referências Internas

- [process.MD](process.MD)
- [tasks.MD](tasks.MD)
- [validator.MD](validator.MD)
- `_DATA/gateway-selection.MD`
- `_DATA/checkout-config.MD`
- `_DATA/test-log.MD`
- `_DATA/notification-checklist.MD`
- `_DATA/integration-log.MD`
- `_DATA/payment-tracker-guidelines.MD`
- [`../_SHARED/templates/checklist-qualidade.MD`](../_SHARED/templates/checklist-qualidade.MD) – base para o QA final antes do go-live
