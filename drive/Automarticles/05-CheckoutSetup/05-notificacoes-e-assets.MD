## Pacote de Notificações e Materiais Pós-Compra - Produto Automarticles

### 1. Brief da Thank You Page

**Objetivo:** Agradecer ao cliente pela compra, fornecer informações sobre o próximo passo e reforçar a proposta de valor do produto.

**Conteúdo da Página:**
- **Título:** Obrigado pela sua compra!
- **Mensagem de Agradecimento:** "Agradecemos por escolher o Automarticles! Sua compra foi realizada com sucesso."
- **Próximos Passos:**
  - "Você receberá um e-mail de confirmação em breve com os detalhes da sua compra."
  - "Acesse sua conta para começar a usar o Automarticles e explorar todos os recursos disponíveis."
- **Suporte:** "Se tiver alguma dúvida, entre em contato com nossa equipe de suporte através do e-mail suporte@automarticles.com."
- **Botão de Acesso:** "Acessar Minha Conta" (link para a página de login).

### 2. Estrutura do E-mail de Confirmação

**Assunto:** Confirmação de Compra - Automarticles

**Corpo do E-mail:**
```
Olá [Nome do Cliente],

Agradecemos por sua compra do Automarticles! 

Aqui estão os detalhes da sua transação:
- **Produto:** Automarticles
- **Valor:** R$ [Valor]
- **Data da Compra:** [Data]
- **Método de Pagamento:** [Método]

Você pode acessar sua conta e começar a usar o Automarticles através do link abaixo:
[Link para Acessar Minha Conta]

Se precisar de ajuda, não hesite em nos contatar pelo e-mail suporte@automarticles.com.

Obrigado por escolher o Automarticles!

Atenciosamente,
Equipe Automarticles
```

### 3. Conteúdo do Recibo Simples

**Recibo Simples - Automarticles**

```
-----------------------------------------
                RECIBO
-----------------------------------------
Data: [Data da Compra]
Cliente: [Nome do Cliente]
E-mail: [E-mail do Cliente]

Produto: Automarticles
Valor: R$ [Valor]

Método de Pagamento: [Método]
-----------------------------------------
Agradecemos pela sua compra!
Para dúvidas, entre em contato: suporte@automarticles.com
-----------------------------------------
```

### 4. Checklist de Notificações

**Notificações a serem enviadas:**

- **Cliente:**
  - E-mail de confirmação de compra (automático).
  - E-mail de agradecimento (pode ser o mesmo do de confirmação).
  
- **Time Interno:**
  - Notificação via Slack/CRM sobre a nova venda (incluir detalhes da transação).
  
- **Webhooks:**
  - Configurar webhook para enviar dados da transação para o CRM (ex: Salesforce, HubSpot).
  
- **CRM:**
  - Atualização automática do status do cliente e registro da nova compra.

### 5. Plano para Tracker Financeiro Semanal

**Objetivo:** Monitorar e reconciliar as vendas do Automarticles semanalmente.

**Estrutura do Tracker Financeiro:**
- **Colunas:**
  - Data da Transação
  - Nome do Cliente
  - Valor da Venda
  - Método de Pagamento
  - Status do Pagamento (Aprovado, Pendente, Chargeback)
  - Observações

**Frequência de Atualização:**
- Atualizar o tracker diariamente com novas vendas.
- Realizar uma revisão semanal (ex: toda segunda-feira) para verificar discrepâncias e reconciliar com os relatórios do gateway de pagamento.

**Responsável:** Designar um membro da equipe financeira para ser o owner do tracker e garantir que as atualizações sejam feitas corretamente.

---

Este pacote de notificações e materiais pós-compra garante que os clientes tenham uma experiência positiva após a compra do Automarticles, enquanto a equipe interna mantém um controle rigoroso sobre as transações financeiras.
