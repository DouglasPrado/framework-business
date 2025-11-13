# Plano de Configuração de Conta para o Produto "Automarticles"

## 1. Status da Conta
**Gateway Escolhido**: Stripe  
**Status da Conta**: A conta ainda não foi criada. O processo de configuração inicia agora.

## 2. Documentos Necessários
Para a criação da conta no Stripe, os seguintes documentos devem ser preparados e enviados:
- **Cadastro de Pessoa Jurídica**: CPF/CNPJ da empresa.
- **Documentação Bancária**: Comprovante de conta bancária para repasse (ex: extrato bancário ou contrato de abertura de conta).
- **Contrato Social**: Documento que valida a existência da empresa (se aplicável).
- **Políticas de Reembolso e Cancelamento**: Documentação clara que descreve as políticas da empresa para evitar chargebacks.

## 3. Configuração de Segurança
- **Habilitação de Autenticação em Dois Fatores (2FA)**: 
  - Criar conta no Stripe usando e-mail institucional.
  - Habilitar 2FA imediatamente após a criação da conta.
- **Usuários**:
  - Definir usuários com acesso restrito ao painel do Stripe, garantindo que apenas pessoas autorizadas possam realizar alterações.

## 4. Limites e Políticas Antifraude
- **Limites de Transação**: 
  - Inicialmente, definir limites baixos para transações (ex: R$ 500,00) para proteger contra fraudes.
  - Revisar e ajustar limites gradualmente conforme o histórico de transações aumenta.
- **Políticas Antifraude**:
  - Configurar regras de antifraude no painel do Stripe, como bloqueio de transações suspeitas e verificação de identidade.
  - Documentar as regras de antifraude aprovadas e compartilhá-las com a equipe financeira.

## 5. Checklist de Aprovação
### Responsáveis e Prazos
- **Owner Principal do Checkout**: [Nome do responsável]
- **Data Alvo de Go-Live**: ___/___/___ (definir data)
- **Responsável por Monitoramento Diário**: [Nome do responsável]

### Etapas e Tarefas
- **Etapa 1: Criar Conta no Stripe**
  - [ ] Criar conta usando e-mail institucional.
  - [ ] Habilitar 2FA.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

- **Etapa 2: Enviar Documentação**
  - [ ] Preparar e enviar CPF/CNPJ, comprovante bancário e contrato social.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

- **Etapa 3: Configurar Conta**
  - [ ] Ajustar limites de transação e políticas antifraude.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

- **Etapa 4: Criar Produto e Checkout**
  - [ ] Definir nome, preço e condições de pagamento na plataforma Stripe.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

- **Etapa 5: Testar Fluxo de Pagamento**
  - [ ] Realizar testes com transações simbólicas para validar o sistema.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

- **Etapa 6: Integrar Checkout à Landing Page**
  - [ ] Atualizar CTA da landing page com o link do checkout.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

- **Etapa 7: Documentar Processo**
  - [ ] Registrar todas as etapas e evidências em `_DATA/`.
  - **Responsável**: [Nome do responsável]
  - **Data limite**: ___/___/___

## Conclusão
Este plano de configuração de conta para o produto "Automarticles" estabelece um fluxo claro para a criação e configuração da conta no Stripe, garantindo que todos os passos sejam seguidos e documentados adequadamente. O cumprimento dos prazos e a responsabilidade atribuída a cada tarefa são essenciais para garantir um go-live bem-sucedido e eficiente.
