# SalesCallExecution

## Visão Geral

Este processo conduz a preparação, execução e follow-up de calls de vendas consultivas em leads qualificados, garantindo fechamento estruturado, registro de decisões e transição imediata para onboarding. A abordagem combina diagnóstico rápido, proposta personalizada e tratamento sistemático de objeções.

## Quando Usar

Use este processo quando:
- Um lead demonstrou interesse via landing page, outreach ou indicação e atende aos critérios de qualificação.
- Existe oferta clara validada por entrevistas e materiais de apoio (ex: apresentação, case, piloto).
- O objetivo é fechar a venda em até 1 dia após a call, com fluxo de pagamento e onboarding preparados.
- É necessário padronizar condução de calls entre membros do time comercial.

## Pré-requisitos

- Lead registrado com contexto completo no pipeline (origem, dores, expectativas).
- Oferta e termos comerciais definidos (preço, forma de pagamento, política de garantia).
- Ferramentas de reunião e gravação aprovadas em `tools/` (ex: Google Meet, Zoom) com links pré-configurados.
- Link de pagamento ativo (conforme processo futuro `CheckoutSetup`) ou instruções de pagamento manual.
- Material de suporte (deck, demo, piloto) atualizado e acessível.

## Tempo Estimado

- Preparação e personalização: 60-90 minutos
- Execução da call (com follow-up imediato): 30-45 minutos
- Follow-up estendido e confirmações finais: até 4 horas (janelas de resposta do lead)
- Total recomendado por lead ativo: 1 dia corrido

## Resultado Esperado

Ao final deste processo você terá:
- Call realizada com roteiro documentado e gravação/notas arquivadas.
- Proposta e próximos passos registrados em `_DATA/`.
- Link de pagamento enviado e status monitorado.
- Objeções tratadas e documentadas para aprendizado futuro.
- Pagamento confirmado ou plano de follow-up explícito com datas.
- Handoff suave para onboarding ou motivo de perda registrado.

## Arquivos Principais

- [process.MD](process.MD) – fluxo completo com etapas, entregáveis e pontos de decisão.
- [knowledge.MD](knowledge.MD) – princípios comerciais, frameworks, FAQs e scripts de objeção.
- [tasks.MD](tasks.MD) – checklist operacional para execução e registro.
- [validator.MD](validator.MD) – critérios de validação antes de considerar a venda concluída.
- Pasta `_DATA/` – templates para briefing, roteiro, resumo da call e log de objeções.

## Como Executar

1. Leia [process.MD](process.MD) para entender etapas e indicadores.
2. Preencha os templates em `_DATA/` durante preparação e pós-call.
3. Siga [tasks.MD](tasks.MD) marcando cada item com evidências anexadas.
4. Documente objeções, decisões e compromissos imediatamente após a call.
5. Valide a entrega usando [validator.MD](validator.MD) antes de encerrar o lead ou seguir para onboarding.

## Critérios de Qualidade

- Lead está qualificado e preparado antes da call (briefing completo).
- Call executada seguindo roteiro consultivo com registro de dor, impacto e urgência.
- Proposta apresentada com clareza (oferta, preço, bônus, prazo) e próxima ação confirmada.
- Link de pagamento enviado e follow-up programado em até 24h.
- Objeções tratadas e documentadas, com plano de ação definido.
- Handoff para onboarding realizado imediatamente após confirmação de pagamento.

## Próximos Processos

1. **CheckoutSetup** – garantir recebimento (quando disponível).
2. **ClientDelivery** – iniciar entrega do serviço/produto.
3. **RetrospectiveAnalysis** – alimentar aprendizados sobre objeções e gatilhos.

## Dependências

### Depende de
- [TargetUserIdentification](../TargetUserIdentification/process.MD) – perfis e priorização.
- [UserInterviewValidation](../UserInterviewValidation/process.MD) – linguagem e objeções.
- [LandingPageCreation](../LandingPageCreation/process.MD) – material de aquisição e promessa feita ao lead.

### Habilita
- Onboarding e entrega operacional (ClientDelivery).
- Aprimoramento de propostas, preços e argumentos (RetrospectiveAnalysis).
- Ajustes em copy e abordagens de outreach com base nas objeções registradas.

## Dicas para Sucesso

- Revise contatos anteriores com o lead para iniciar a call reconhecendo contexto e evitando repetição.
- Prepare perguntas abertas que investiguem impacto, urgência e priorização, não apenas orçamento.
- Tenha exemplos e casos prontos para reforçar valor em objeções comuns.
- Combine próxima ação durante a call (pagamento imediato, segunda call com decisor, envio de material).
- Envie follow-up por escrito até 30 minutos após call com resumo e próximos passos.

## Avisos Importantes

- Não conduza call sem link de pagamento válido ou clareza sobre condições comerciais.
- Evite apresentações longas; mantenha foco na dor do lead e no resultado prometido na landing.
- Documente objeções negativas mesmo quando venda fecha; isso ajuda na melhoria contínua.
- Se surgirem novos decisores, marque próxima call ainda durante a conversa atual.
- Bloqueie agenda para follow-up no mesmo dia; leads quentes esfriam rapidamente.

## Métricas de Sucesso

- Taxa de show rate das calls (> 80% das calls agendadas são realizadas).
- Tempo médio entre call e envio de follow-up (meta: ≤ 30 minutos).
- Taxa de fechamento pós-call (meta inicial: ≥ 30% em leads qualificados).
- Tempo entre pagamento e início de onboarding (meta: ≤ 2 horas).
- Número de objeções recorrentes registradas e tratadas (meta: 100% das calls documentadas).

## Suporte e Referências

- [process.MD](process.MD)
- [tasks.MD](tasks.MD)
- [knowledge.MD](knowledge.MD)
- Templates em `_DATA/`
- Registros de objeções e aprendizados no CRM ou planilha vinculada

## Versão e Manutenção

- Versão: 1.0
- Criado em: 2025-10-31
- Responsável: Framework Business Team
- Revisar sempre que oferta, preço ou objeções críticas mudarem.

## Estrutura de Arquivos

```
SalesCallExecution/
├── README.MD
├── process.MD
├── knowledge.MD
├── tasks.MD
├── validator.MD
└── _DATA/
    ├── prep-call-briefing.MD
    ├── roteiro-sales-call.MD
    ├── pos-call-resumo.MD
    └── objection-log.MD
```

Adicione evidências (gravações, prints de confirmação de pagamento, e-mails) na pasta `_DATA/` ou subpastas organizadas por lead.
