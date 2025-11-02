# Checklist Operacional - ClientDelivery

Este checklist conduz o time do onboarding ao pós-entrega, garantindo que cada etapa cumpra prazos, mantenha comunicação com o cliente e gere documentação reutilizável (depoimentos, casos, aprendizados). Siga em paralelo ao plano de execução para assegurar previsibilidade e qualidade.

## Como Utilizar

1. Preencha as informações do cliente antes de iniciar.
2. Siga as etapas na ordem, marcando tarefas à medida que conclui.
3. Utilize os templates referenciados na pasta `_DATA/`.
4. Registre responsáveis e datas diretamente neste checklist ou no plano/cronograma.
5. Ao final, valide a entrega usando o `validator.MD`.

## Informações do Cliente

- Cliente:
- Owner do processo:
- Produto/Serviço contratado:
- Data de início:
- Prazo acordado para entrega:
- Canal principal de comunicação:

---

## Etapa 1 – Preparar handoff e plano de entrega (60 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Coletar dados da venda e contrato no `_DATA/brief-entrega.MD`
- [ ] Verificar status de pagamento em CheckoutSetup e anexar evidência
- [ ] Mapear pendências e riscos em `_DATA/diagnostico-pendencias.MD`
- [ ] Identificar entregáveis do MVP ou artefatos pré-existentes
- [ ] Definir responsáveis internos e disponibilidade
- [ ] Registrar KPIs e prazo acordado no brief

### Output

- [ ] Brief validado com escopo, metas e responsabilidades
- [ ] Pendências registradas com owner e data limite

---

## Etapa 2 – Executar onboarding e alinhamento com o cliente (45 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Antes do contato

- [ ] Enviar e-mail padrão usando `_DATA/onboarding-email.MD`
- [ ] Compartilhar formulário/checklist `_DATA/formulario-onboarding.MD`
- [ ] Agendar reunião ou confirmar canal prioritário

### Durante o onboarding

- [ ] Seguir pauta de `_DATA/roteiro-onboarding.MD`
- [ ] Reforçar escopo, limites e período de garantia
- [ ] Validar cronograma macro e entregáveis
- [ ] Confirmar responsáveis do lado do cliente

### Após o onboarding

- [ ] Registrar decisões em `_DATA/ata-onboarding.MD`
- [ ] Organizar arquivos enviados pelo cliente em `_DATA/onboarding/`
- [ ] Atualizar diagnóstico de pendências se necessário

### Output

- [ ] Cronograma aprovado pelo cliente
- [ ] Ata de onboarding salva e compartilhada internamente

---

## Etapa 3 – Planejar execução detalhada (120 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Listar entregáveis e tarefas no `_DATA/plano-execucao.MD`
- [ ] Montar cronograma detalhado com marcos em `_DATA/cronograma-detalhado.MD`
- [ ] Atribuir responsáveis e SLAs internos
- [ ] Configurar tracker de tempo em `_DATA/tracker-tempo.MD`
- [ ] Definir cadência de comunicação com cliente (ex: status semanal)
- [ ] Validar ferramentas aprovadas em `tools/` para execução

### Output

- [ ] Plano de execução aprovado pelo time
- [ ] Cronograma e cadência de comunicação publicados para o time

---

## Etapa 4 – Produzir, revisar e homologar entregáveis (tempo variável)

Owner(s):
Período estimado:

### Produção

- [ ] Executar cada entrega seguindo `_DATA/checklist-execucao.MD`
- [ ] Registrar dúvidas ou bloqueios no log de pendências
- [ ] Atualizar progresso no cronograma e tracker de tempo

### Revisão interna

- [ ] Registrar revisões em `_DATA/log-revisoes.MD`
- [ ] Garantir aprovação de pares/lead antes do QA
- [ ] Atualizar cliente sobre marcos relevantes

### QA final

- [ ] Executar `_DATA/checklist-qa-entrega.MD` (adaptado de `../_SHARED/templates/checklist-qualidade.MD`)
- [ ] Resolver pendências críticas identificadas no QA
- [ ] Organizar artes finais na pasta `_DATA/entregas/`

### Output

- [ ] Entregáveis finalizados e aprovados internamente
- [ ] Checklist de QA 100% concluído

---

## Etapa 5 – Realizar entrega oficial (60 minutos)

Owner:
Data da entrega: ___/___/___

### Pré-reunião

- [ ] Preparar apresentação/guia em `_DATA/roteiro-apresentacao.MD`
- [ ] Revisar materiais finais e links compartilháveis
- [ ] Configurar gravação (opcional) ou modelo de notas

### Durante a entrega

- [ ] Apresentar entregáveis seguindo roteiro
- [ ] Reforçar próximos passos e período de garantia
- [ ] Registrar decisões em `_DATA/ata-entrega.MD`

### Pós-reunião

- [ ] Enviar pacote de materiais usando `_DATA/pacote-instrucoes.MD`
- [ ] Confirmar recebimento com `_DATA/mensagem-confirmacao.MD`
- [ ] Atualizar status interno (ex: CRM, planilha de entregas)

### Output

- [ ] Entrega registrada com ata e/ou gravação
- [ ] Recebimento confirmado por escrito

---

## Etapa 6 – Pós-entrega e depoimento (45 minutos + follow-up)

Owner:
Data do check-in: ___/___/___

### Follow-up inicial (24-48h)

- [ ] Agendar check-in conforme combinado
- [ ] Conduzir conversa usando `_DATA/followup-pos-entrega.MD` (baseado em `../_SHARED/templates/email-followup.MD`)
- [ ] Registrar percepções em `_DATA/registro-feedback.MD`

### Depoimento e caso

- [ ] Solicitar depoimento com `_DATA/template-depoimento.MD`
- [ ] Registrar status (solicitado, enviado, publicado)
- [ ] Criar estudo de caso em `_DATA/relato-caso.MD`
- [ ] Atualizar pasta `_DATA/depoimentos/` com materiais recebidos

### Output

- [ ] Feedback documentado com plano de ação (se tiver ajustes)
- [ ] Depoimento obtido ou follow-up agendado
- [ ] Relato do caso pronto para revisão

---

## Checklist Final de Qualidade

- [ ] Pagamento confirmado e registrado na documentação
- [ ] Brief de entrega completo e acessível ao time
- [ ] Cronograma final compatível com prazo acordado
- [ ] Todos os entregáveis armazenados em `_DATA/entregas/`
- [ ] Checklist de QA concluído e arquivado
- [ ] Ata da entrega e confirmação do cliente registradas
- [ ] Feedback e depoimento documentados
- [ ] Validator executado com status “Aprovado” ou plano de ação definido

---

## Estrutura Recomendada de Arquivos

```
_DATA/
├── brief-entrega.MD
├── diagnostico-pendencias.MD
├── plano-execucao.MD
├── cronograma-detalhado.MD
├── tracker-tempo.MD
├── checklist-execucao.MD
├── checklist-qa-entrega.MD
├── log-revisoes.MD
├── onboarding/
│   ├── ata-onboarding.MD
│   └── anexos-cliente
├── entregas/
│   └── versoes-finais
├── relatos/
│   └── relato-caso-CLIENTE.MD
└── depoimentos/
    └── depoimento-CLIENTE.MD
```

Garanta que cada documento contenha owner, data de última atualização e status (ex: Em andamento, Concluído).

> Os arquivos `checklist-qa-entrega.MD` e `followup-pos-entrega.MD` devem ser atualizados a partir de `../_SHARED/templates/checklist-qualidade.MD` e `../_SHARED/templates/email-followup.MD`, respectivamente.
