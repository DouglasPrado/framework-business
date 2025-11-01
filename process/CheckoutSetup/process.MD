# Processo de Configuração de Checkout Mínimo

## Propósito

Disponibilizar um fluxo de pagamento online confiável em poucas horas, garantindo que clientes possam finalizar a compra com confirmação automática e que o time interno receba notificações e registros financeiros sem fricção.

## Objetivo

Publicar e validar um link de checkout com integrações essenciais (página de obrigado, e-mail de confirmação, recibo e controle financeiro), realizando testes completos para mitigar falhas antes de liberar ao público.

## Escopo

### Dentro do escopo
- Selecionar gateway aprovado e configurar conta, validações e métodos de pagamento
- Criar produto/oferta com preço, condições de parcelamento e campos obrigatórios
- Realizar pagamento simbólico para validar fluxo, antifraude e notificações
- Integrar checkout à landing page, thank you page e e-mails de confirmação
- Preparar recibo/contrato simples e planilha de controle de pagamentos
- Documentar evidências e configurar responsáveis por monitoramento diário

### Fora do escopo
- Negociação de contratos com gateways fora do catálogo `tools/`
- Emissão de nota fiscal ou integrações contábeis avançadas
- Automação complexa de CRM além de integrações básicas via e-mail/planilha/webhook
- Configuração de programas de afiliados ou marketplace
- Desenvolvimento de checkout próprio ou customizações via código extensivo

## Etapas do Processo

### Etapa 1: Definir requisitos e selecionar gateway (30-40 minutos)

**Objetivo:** Garantir que o gateway escolhido atende requisitos legais, operacionais e de experiência antes de criar conta.

**Passos:**
- Reunir dados da oferta: preço, tipos de pagamento (PIX, cartão, boleto), parcelamento máximo, políticas de reembolso e termos.
- Consultar catálogo `tools/` para confirmar gateways aprovados (Stripe, Hotmart, Kiwify, PagSeguro, etc.). Documentar pendências de aprovação.
- Mapear critérios obrigatórios no template `_DATA/gateway-selection.MD` (taxas, prazo de repasse, suporte a PIX, checkout transparente versus redirecionamento, integração com landing).
- Avaliar compliance: necessidade de emissão de NF, retenções, adequação a pessoa física ou jurídica.
- Registrar decisão final incluindo justificativa, link de acesso e contatos de suporte.

**Outputs:**
- `_DATA/gateway-selection.MD` preenchido com comparação e decisão
- Lista de documentos necessários para abertura da conta

### Etapa 2: Criar conta e habilitar recebimentos (30-45 minutos)

**Objetivo:** Configurar conta no gateway escolhido e garantir que pode receber pagamentos sem bloqueios.

**Passos:**
- Criar conta usando e-mail institucional e ativar autenticação em dois fatores.
- Enviar documentos solicitados (CPF/CNPJ, comprovante bancário, contrato social quando aplicável).
- Configurar dados bancários para saque ou repasse automático.
- Ajustar políticas de risco: limites de transação, regras antifraude, notificações de chargeback.
- Registrar acessos e responsáveis em `_DATA/checkout-config.MD` (secção “Dados de conta e segurança”).
- Confirmar aprovação ou status de verificação (print/nota adicionada em `_DATA/integration-log.MD`).

**Outputs:**
- Conta aprovada e apta a receber pagamentos
- `_DATA/checkout-config.MD` com dados de conta, métodos habilitados e responsáveis
- Evidência de ativação armazenada em `_DATA/integration-log.MD`

### Etapa 3: Configurar produto e checkout (40-60 minutos)

**Objetivo:** Criar o produto, link de pagamento e condições comerciais do checkout.

**Passos:**
- Definir nome interno e público do produto/Oferta (coerente com landing).
- Inserir preço, moeda, parcelamento e cupons (quando aplicável).
- Configurar campos obrigatórios (nome, e-mail, documento, telefone) e política de termos.
- Personalizar checkout com identidade mínima (logo, cores) e URL amigável.
- Configurar página de obrigado ou URL de redirecionamento para a landing (em branco até etapa 5).
- Registrar detalhes completos em `_DATA/checkout-config.MD` (seções “Produto” e “Checkout”).
- Gerar link/URL final e salvar no mesmo template.

**Outputs:**
- Link de checkout ativo salvo em `_DATA/checkout-config.MD`
- Capturas de tela ou prints do checkout armazenados em `_DATA/`

### Etapa 4: Testar fluxo e notificações (40-50 minutos)

**Objetivo:** Validar que pagamento, notificações e automações funcionam antes de disponibilizar ao público.

**Passos:**
- Realizar pagamento simbólico (cartão próprio com devolução, cupom de 100% ou modo teste quando suportado).
- Registrar dados do teste em `_DATA/test-log.MD` (valor, método, status, timestamp, evidências).
- Validar e-mails transacionais do gateway (confirmação do cliente e aviso interno); anexar prints.
- Configurar webhooks/integrações (ex: envio para CRM/Slack) e verificar disparo registrando em `_DATA/notification-checklist.MD`.
- Confirmar recebimento do valor em painel/relatório e registrar ID da transação.
- Se houver falhas, repetir testes após ajustes e documentar plano de ação.

**Outputs:**
- `_DATA/test-log.MD` com transações de teste aprovadas
- `_DATA/notification-checklist.MD` confirmando notificações e responsáveis
- Evidências (prints, e-mails, logs) anexadas em `_DATA/`

### Etapa 5: Integrar checkout à jornada do cliente (30-40 minutos)

**Objetivo:** Garantir experiência consistente do clique ao pós-pagamento.

**Passos:**
- Atualizar CTA da landing page com o novo link (ou embed) e registrar no `_DATA/integration-log.MD`.
- Criar ou atualizar página de obrigado seguindo `_DATA/thankyou-page-brief.MD` (mensagem de confirmação, próximos passos, contato de suporte).
- Configurar redirecionamento automático do checkout para a página de obrigado.
- Redigir e-mail de confirmação definitivo usando `_DATA/confirmation-email.MD` (incluindo dados do pedido, prazo de contato, link de suporte).
- Adaptar `_DATA/receipt-template.MD` com dados da oferta, valor pago, condições e assinatura digital.
- Sincronizar mensagens com equipe de vendas e suporte (Slack/CRM) e registrar responsáveis por disparo.

**Outputs:**
- Landing atualizada com link funcional (evidência registrada)
- Página de obrigado publicada e roteiros de comunicação completos
- Templates de e-mail e recibo revisados e salvos em `_DATA/`

### Etapa 6: Organizar controle e handoff (20-30 minutos)

**Objetivo:** Preparar monitoramento financeiro contínuo e comunicação interna.

**Passos:**
- Configurar planilha ou dashboard conforme `_DATA/payment-tracker-guidelines.MD` (colunas: data, cliente, valor, status, método, recibo enviado).
- Sincronizar notificações do gateway com a planilha (import manual, automação via webhook ou Zapier aprovado).
- Definir responsáveis e cadência de atualização no template (ex: verificação 2x por dia).
- Registrar no `_DATA/integration-log.MD` o canal principal para alertas (e-mail, WhatsApp, Slack) e contingências.
- Compartilhar link do checkout, página de obrigado e planilha com time comercial e de entrega.
- Atualizar documentação na pasta `_DATA/` com checklist final e próximos passos.

**Outputs:**
- Planilha/controle configurado e link registrado
- `_DATA/integration-log.MD` com handoff e responsáveis definidos
- Lista de próximos passos (ex: adicionar novo produto, automatizar nota fiscal) documentada

## Pontos de Decisão

1. **Após Etapa 1:** Gateway atende requisitos e está aprovado em `tools/`?  
   - Se não, solicitar aprovação ou escolher alternativa antes de seguir.

2. **Após Etapa 2:** Conta habilitada sem pendências de verificação?  
   - Se não, pausar próximo passo e resolver com suporte do gateway.

3. **Após Etapa 4:** Fluxo de pagamento e notificações passaram nos testes?  
   - Se não, corrigir e repetir testes antes de integrar à landing.

4. **Antes do go-live:** Página de obrigado, e-mail e recibo revisados e aprovados?  
   - Se não, bloquear publicação e ajustar com time comercial.

5. **Durante Etapa 6:** Responsáveis e cadência de monitoramento definidos?  
   - Se não, o checkout não deve ser liberado para tráfego pago ou orgânico.

## Resultados Esperados

1. Gateway escolhido com decisão documentada
2. Conta configurada e ativa para recebimentos
3. Link de checkout publicado e registrado
4. Testes concluídos com evidências
5. Página de obrigado, e-mail e recibo prontos
6. Plano de monitoramento financeiro operacional
7. Handoff completo para vendas e entrega

## Indicadores-Chave de Desempenho

- Tempo total para ativar checkout (meta: ≤ 3 horas)
- Número de falhas nos testes antes do go-live (meta: ≤ 1 iteração)
- Tempo de notificação interna após pagamento real (meta: ≤ 5 minutos)
- Percentual de transações com recibo enviado (meta inicial: 100%)
- Dias de reconciliação em atraso (meta: 0)

## Avisos e Armadilhas Comuns

1. **Documentação incompleta:** sem envio de documentos a conta pode ser bloqueada após primeira venda. Previna-se enviando tudo na Etapa 2.
2. **Link sem teste real:** gateways só validam antifraude com transação real; sempre realize teste com cartão/PIX antes do lançamento.
3. **Notificações desativadas:** verifique painéis que desabilitam e-mails padrão ao personalizar templates.
4. **Termos ausentes:** inclua política de cancelamento e reembolso no checkout; é requisito para evitar chargebacks.
5. **Planilha desatualizada:** sem responsável claro, transações podem passar despercebidas. Defina owner e horários fixos.
6. **Múltiplos links não documentados:** mantenha histórico em `_DATA/checkout-config.MD` para evitar uso de links antigos.

## Dependências

**Entradas necessárias:**
- Copy e CTA da landing page ([LandingPageCreation](../LandingPageCreation/process.MD))
- Oferta, preço e condições definidas pelo time comercial
- Informações fiscais e bancárias atualizadas (coordenação com finanças)

**Saídas habilitam:**
- Follow-ups e fechamentos em [SalesCallExecution](../SalesCallExecution/process.MD)
- Onboarding imediato em [ClientDelivery](../ClientDelivery/process.MD)
- Métricas financeiras para decisões em `strategies/ZeroUm`

## Referências

- [tasks.MD](tasks.MD)
- [knowledge.MD](knowledge.MD)
- [validator.MD](validator.MD)
- Templates em `_DATA/` (gateway-selection, checkout-config, test-log, notification-checklist, integration-log, thankyou-page-brief, confirmation-email, receipt-template, payment-tracker-guidelines)
