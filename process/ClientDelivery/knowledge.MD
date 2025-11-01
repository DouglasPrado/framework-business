# Base de Conhecimento - ClientDelivery

## Visão Geral

ClientDelivery organiza o ciclo completo de entrega ao cliente após a venda: alinhamento, execução, homologação, entrega oficial e pós-entrega. O foco é garantir previsibilidade, qualidade e geração de ativos de prova social (depoimentos e estudos de caso) enquanto mantemos rastreabilidade total das decisões tomadas.

## Objetivo Central

Entregar valor perceptível ao cliente dentro do prazo combinado, com comunicação transparente, documentação completa e evidências suficientes para nutrir vendas futuras (depoimentos, relatórios, aprendizados).

## Princípios Fundamentais

1. **Handoff completo antes de agir** – nada de acionar o cliente antes de consolidar o dossiê da venda.
2. **Tudo por escrito** – cada decisão, ajuste ou aprovação precisa de registro acessível a todo o time.
3. **Qualidade antes da pressa** – não entregue sem checklist de QA concluído.
4. **Cliente informado sempre** – nenhuma etapa fica sem comunicação proativa, mesmo quando não há novidades.
5. **Feedback vira ativo** – registre percepções positivas e negativas para alimentar melhorias e marketing.

## Conceitos-Chave

### Handoff
Conjunto de informações transferidas do processo comercial para a operação. Inclui escopo, objetivos, restrições, stakeholders e combinações financeiras. Deve estar consolidado no `_DATA/brief-entrega.MD` com pendências claras.

### Escopo firme
Documento ou e-mail que confirma o que será entregue, o que está fora, prazos e responsabilidades. Serve como referência para recusar solicitações fora do combinado durante a execução.

### Checklist de Qualidade
Sequência de verificações obrigatórias antes da entrega oficial. No ClientDelivery é operacionalizada por `_DATA/checklist-qa-entrega.MD` para garantir consistência e reduzir revisões pós-entrega.

### Período de Garantia
Janela acordada (ex: 7 dias) para ajustes menores gratuitos. Deve ser reforçada durante a entrega e monitorada via `_DATA/registro-feedback.MD`.

### Depoimento Estruturado
Relato do cliente que destaca contexto, desafio, solução e resultado. O template `_DATA/template-depoimento.MD` ajuda a guiar respostas e aumentar taxa de conversão.

## Perguntas Frequentes (FAQ)

**O que fazer se o cliente pedir algo fora do escopo?**  
Referencie o escopo confirmado em `_DATA/ata-onboarding.MD` e avalie se o pedido cabe na garantia. Se for extra, encaminhe para proposta adicional via SalesCallExecution.

**Como proceder se o pagamento ainda não compensou?**  
Pause o onboarding até os itens financeiros estarem concluídos. Registre bloqueio em `_DATA/diagnostico-pendencias.MD` e comunique o cliente sobre a pendência.

**Qual canal usar para atualizações?**  
Confirme na reunião de onboarding. Preferencialmente utilize ferramenta já aprovada em `tools/` e registre resumos em `_DATA/log-revisoes.MD`.

**Como lidar com atrasos internos?**  
Atualize o cronograma em `_DATA/cronograma-detalhado.MD`, comunique o cliente com antecedência mínima de 24h e apresente plano de contingência.

**E se o cliente não comparecer à entrega?**  
Envie nova proposta de horário usando `_DATA/mensagem-confirmacao.MD`. Se a entrega for assíncrona, grave vídeo ou áudio guiando os principais pontos e disponibilize junto às instruções.

## Checkpoints de Qualidade

1. **Antes do onboarding** – Brief aprovado sem pendências críticas (Etapa 1).
2. **Após o onboarding** – Cronograma confirmado e ata arquivada em `_DATA/onboarding/`.
3. **Antes da apresentação** – Checklist de QA 100% concluído em `_DATA/checklist-qa-entrega.MD`.
4. **Após entrega** – Recebimento confirmado por escrito e materiais arquivados em `_DATA/entregas/`.
5. **Após follow-up** – Feedback documentado, depoimento solicitado e próximos passos definidos.

## Boas Práticas de Comunicação

- Combine janela de resposta máxima (ex: 12h úteis) e cumpra rigorosamente.
- Use linguagem clara e contextualize decisões; evite jargões não explicados.
- Ao enviar materiais, inclua resumo executivo com “o que mudou” e “o que o cliente precisa fazer”.
- Registre comunicações críticas em canais persistentes (e-mail ou sistema) mesmo que a conversa ocorra em mensageiros.
- Em follow-ups, destaque resultados observáveis desde a entrega e peça feedback específico.

## Templates e Artefatos Internos

- `_DATA/brief-entrega.MD` – consolidação do handoff comercial.
- `_DATA/diagnostico-pendencias.MD` – pendências, riscos e responsáveis.
- `_DATA/onboarding-email.MD` – mensagem padrão de boas-vindas.
- `_DATA/formulario-onboarding.MD` – checklist de informações a coletar.
- `_DATA/roteiro-onboarding.MD` – pauta da reunião inicial.
- `_DATA/ata-onboarding.MD` – registro de decisões e confirmações.
- `_DATA/plano-execucao.MD` – desdobramento da entrega em tarefas.
- `_DATA/cronograma-detalhado.MD` – visão calendarizada dos marcos.
- `_DATA/tracker-tempo.MD` – controle de esforço utilizado por etapa.
- `_DATA/checklist-execucao.MD` – lista operacional durante produção.
- `_DATA/log-revisoes.MD` – histórico de versões e aprovações internas.
- `_DATA/checklist-qa-entrega.MD` – verificação final antes da entrega.
- `_DATA/roteiro-apresentacao.MD` – guia da reunião de entrega.
- `_DATA/ata-entrega.MD` – registro da apresentação e decisões do cliente.
- `_DATA/pacote-instrucoes.MD` – estrutura para manualizar uso e próximos passos.
- `_DATA/mensagem-confirmacao.MD` – mensagem para validar recebimento.
- `_DATA/followup-pos-entrega.MD` – script do check-in 24-48h depois.
- `_DATA/registro-feedback.MD` – documento para consolidar percepções.
- `_DATA/template-depoimento.MD` – prompts para coleta de depoimentos.
- `_DATA/relato-caso.MD` – estrutura do estudo de caso.

## Ferramentas Recomendadas (verificar em `tools/`)

- Comunicação síncrona: Zoom, Google Meet ou outra ferramenta aprovada.
- Comunicação assíncrona: Gmail/Outlook, Slack, WhatsApp Business (quando autorizado).
- Gestão de tarefas: Notion, Asana, Trello ou equivalente aprovado.
- Armazenamento de arquivos: Google Drive, Dropbox, ferramentas aprovadas.
- Automação de e-mails: plataformas homologadas no catálogo.
- Assinaturas eletrônicas (se necessário): soluções listadas em `tools/`.

## Materiais de Apoio

- Playbooks de onboarding consultivo (pendente adicionar em `_SHARED/references/` quando disponível).
- Exemplos de depoimentos em processos anteriores (armazenar em `_DATA/depoimentos/`).
- Guias de customer success (ex: frameworks de NPS, health score).
- Templates compartilhados futuros: acompanhe `process/_SHARED/` para novas versões padronizadas (ex: follow-up, checklist de qualidade global).

## Riscos e Mitigações

### Pagamento não confirmado
- **Mitigação:** trava o início, registra no diagnóstico e comunica cliente com SLA.

### Escopo mutável
- **Mitigação:** reforçar escopo por escrito e formalizar mudanças com novo acordo.

### Falta de recursos críticos
- **Mitigação:** mapear na Etapa 1, acionar responsáveis e escalar com 48h de antecedência.

### Atrasos internos
- **Mitigação:** revisar disponibilidade antes da Etapa 3, usar fallback de capacidade e manter cliente informado.

### Depoimento não coletado
- **Mitigação:** preparar pedido com prompts específicos, oferecer formatos alternativos (áudio, texto, survey) e agendar follow-up dedicado.

### Falta de documentação
- **Mitigação:** checklist obriga upload e organização em `_DATA/entregas/` e `_DATA/relatos/`.

## Integrações com Outros Processos

### Processos anteriores
- SalesCallExecution (a criar) – fornece resumo comercial e expectativas.
- CheckoutSetup (a criar) – comprova pagamento e dados de faturamento.
- ManualMVPDesign (a criar) – entrega artefatos do MVP para operação.

### Processos posteriores
- OutreachCampaign e SalesCallExecution – utilizam depoimentos e casos coletados.
- RetrospectiveAnalysis – usa registros de feedback e logs de execução.
- ContentPublication – aproveita estudos de caso e depoimentos aprovados.

## Documentação Recomendada em `_DATA/`

```
_DATA/
├── onboarding/
│   ├── ata-onboarding.MD
│   └── arquivos enviados pelo cliente
├── entregas/
│   ├── entrega-final-v1/
│   └── assets complementares
├── relatos/
│   └── relato-caso-CLIENTE.MD
├── depoimentos/
│   └── depoimento-cliente.MD
├── tracker-tempo.MD
├── cronograma-detalhado.MD
├── log-revisoes.MD
└── checklist-qa-entrega.MD
```

Mantenha convenção `cliente-nome-data` quando pertinente e garanta que todos os arquivos tenham owner e data de última atualização.

## Métricas e Monitoramento

- Atualize `_DATA/tracker-tempo.MD` diariamente para analisar esforço real.
- Registre NPS ou nota de satisfação em `_DATA/registro-feedback.MD`.
- Informe taxa de depoimentos capturados no painel central (quando disponível).
- Envie relatório quinzenal com entregas concluídas, status de depoimentos e ações em aberto para RetrospectiveAnalysis.

## Próximos Passos após a Entrega

1. Revisar feedbacks agregados e direcionar melhorias para ManualMVPDesign.
2. Atualizar repositório interno de provas sociais (move depoimento aprovado para `_DATA/depoimentos/` e notificar marketing/vendas).
3. Se houver oportunidades de upsell, sinalizar para SalesCallExecution com resumo do caso.
4. Garantir que aprendizados relevantes entrem no backlog de melhorias do produto/serviço.
