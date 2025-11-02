# Processo de Entrega ao Cliente

## Propósito

Garantir que cada cliente receba a entrega contratada com clareza, previsibilidade e padronização, desde o onboarding até o acompanhamento pós-entrega, assegurando satisfação, documentação completa e geração de depoimentos reutilizáveis.

## Objetivo

Concluir a entrega acordada com o cliente dentro do prazo combinado, com checklist de qualidade final aprovado, recebimento confirmado, instruções de uso documentadas e depoimento coletado ou mapeado para follow-up.

## Escopo

### Dentro do escopo
- Handoff completo das informações da venda e do MVP produzido
- Onboarding do cliente e alinhamento de expectativas
- Planejamento detalhado da execução com cronograma e responsáveis
- Produção, revisão e QA dos entregáveis prometidos
- Condução da reunião de entrega e confirmação de recebimento
- Pós-entrega com check-in, suporte inicial e coleta de depoimento

### Fora do escopo
- Renegociação comercial ou upsell (tratar pelo processo de vendas)
- Desenvolvimento de funcionalidades adicionais não previstas no MVP
- Suporte contínuo além do período de pós-entrega definido
- Ajustes estruturais em processos anteriores (ex: CheckoutSetup, ManualMVPDesign)
- Gestão financeira (faturamento, notas fiscais) fora dos itens de confirmação

## Etapas do Processo

### Etapa 1: Preparar handoff e plano de entrega (60 minutos)

Objetivo: consolidar todas as informações necessárias antes do contato com o cliente e estruturar o plano de execução interno.

Passos principais:
- Reunir dossiê de venda (resumo da oferta, escopo, restrições, expectativas) em `_DATA/brief-entrega.MD`
- Verificar pagamento e status do cliente em `CheckoutSetup` (comprovante, forma, pendências)
- Levantar entregáveis e materiais do processo `ManualMVPDesign` ou equivalente
- Definir responsáveis internos, prazos macro e indicadores de sucesso
- Registrar riscos ou dependências críticas (acessos, aprovações, recursos externos)

Use os templates:
- `_DATA/brief-entrega.MD`
- `_DATA/diagnostico-pendencias.MD`

Output esperado:
- Brief de entrega validado pelo time com escopo, premissas e deadlines
- Lista de pendências e responsáveis com datas de resolução

### Etapa 2: Executar onboarding e alinhamento com o cliente (45 minutos)

Objetivo: garantir que o cliente tenha clareza sobre o processo, forneça insumos e confirme acordos.

Passos principais:
- Enviar e-mail de boas-vindas usando `_DATA/onboarding-email.MD`
- Compartilhar formulário/checklist de informações necessárias (`_DATA/formulario-onboarding.MD`)
- Agendar call ou alinhar canal primário (e-mail, WhatsApp, Slack) para acompanhamento
- Conduzir reunião inicial seguindo `_DATA/roteiro-onboarding.MD`, revisando expectativas e cronograma
- Registrar decisões e ajustes em `_DATA/ata-onboarding.MD`

Output esperado:
- Informações críticas coletadas e armazenadas em `_DATA/onboarding/`
- Cronograma e milestones aprovados pelo cliente
- Confirmação escrita do cliente sobre escopo e próximos passos

### Etapa 3: Planejar execução detalhada e alocar recursos (120 minutos)

Objetivo: quebrar a entrega em tarefas operacionais com responsáveis, métricas de acompanhamento e checkpoints.

Passos principais:
- Mapear entregáveis em tarefas sequenciais no template `_DATA/plano-execucao.MD`
- Definir marcos internos (ex: revisão, homologação) e datas em `_DATA/cronograma-detalhado.MD`
- Validar disponibilidade do time e ferramentas aprovadas em `tools/`
- Estabelecer cadência de atualizações ao cliente (status report, mensagens semanais)
- Preparar estrutura para registrar tempo gasto por etapa (`_DATA/tracker-tempo.MD`)

Output esperado:
- Plano de execução detalhado com owners, datas e indicadores
- Cronograma compartilhável e atualizado
- Tracker configurado para monitorar esforço e status

### Etapa 4: Produzir, revisar e homologar entregáveis (tempo variável conforme escopo)

Objetivo: executar a entrega mantendo padrão de qualidade e histórico de revisões.

Passos principais:
- Produzir cada deliverable seguindo o checklist `_DATA/checklist-execucao.MD`
- Registrar checkpoints de revisão interna em `_DATA/log-revisoes.MD`
- Validar requisitos críticos com checklist de qualidade `_DATA/checklist-qa-entrega.MD` (adaptado de [`../_SHARED/templates/checklist-qualidade.MD`](../_SHARED/templates/checklist-qualidade.MD))
- Atualizar cliente conforme cadência definida (status, bloqueios, decisões)
- Organizar artefatos finais na pasta `_DATA/entregas/`

Output esperado:
- Entregáveis completos, revisados e aprovados internamente
- Checklist de QA concluído sem pendências críticas
- Histórico de revisões documentado

### Etapa 5: Realizar entrega oficial e garantir entendimento (60 minutos)

Objetivo: apresentar a solução, transferir conhecimento e confirmar que o cliente recebeu e sabe utilizar.

Passos principais:
- Preparar roteiro da apresentação usando `_DATA/roteiro-apresentacao.MD`
- Conduzir reunião de entrega registrando principais pontos em `_DATA/ata-entrega.MD`
- Compartilhar materiais finais (links, arquivos, instruções) usando `_DATA/pacote-instrucoes.MD`
- Confirmar recebimento formal via e-mail ou canal alinhado (`_DATA/mensagem-confirmacao.MD`)
- Alinhar próximos passos imediatos, suporte e período de garantia

Output esperado:
- Reunião de entrega realizada com gravação ou notas consolidadas
- Cliente confirma recebimento e entendimento por escrito
- Instruções de uso e próximos passos disponibilizados em canal acordado

### Etapa 6: Executar pós-entrega e capturar depoimentos (45 minutos + follow-up)

Objetivo: monitorar valor percebido, tratar ajustes rápidos e coletar prova social.

Passos principais:
- Agendar check-in 24-48h após entrega usando `_DATA/followup-pos-entrega.MD` (baseado em [`../_SHARED/templates/email-followup.MD`](../_SHARED/templates/email-followup.MD))
- Realizar follow-up registrando feedback em `_DATA/registro-feedback.MD`
- Formalizar solicitações de ajuste dentro do período de garantia (quando aplicável)
- Solicitar depoimento usando `_DATA/template-depoimento.MD` (texto/áudio/vídeo)
- Documentar caso completo para portfólio em `_DATA/relato-caso.MD`

Output esperado:
- Feedback do cliente registrado com status de ações derivadas
- Depoimento coletado ou plano de follow-up documentado
- Caso documentado com contexto, entregáveis e resultados iniciais

## Pontos de Decisão

1. **Após Etapa 1:** Há pendências críticas (acessos, pagamentos, escopo)?  
   - Se sim, bloquear onboarding até resolver e registrar responsável/data.

2. **Após Etapa 3:** O plano de execução cabe no prazo combinado e há capacidade interna confirmada?  
   - Se não, renegociar prazos com o cliente antes de iniciar produção.

3. **Antes da entrega oficial (Etapa 5):** Checklist de QA está 100% concluído?  
   - Se não, corrigir falhas antes de agendar apresentação.

4. **Após o check-in pós-entrega:** Valor percebido ≥ expectativa inicial?  
   - Se não, acionar playbook de retenção e planejar ajustes imediatos.

## Resultados Esperados

1. Brief de entrega consolidado com pendências mapeadas
2. Onboarding concluído com cronograma aprovado pelo cliente
3. Plano de execução detalhado com responsáveis e métricas
4. Entregáveis produzidos e validados com checklist de qualidade
5. Reunião de entrega finalizada e recebimento confirmado
6. Feedback registrado e depoimento coletado ou agendado
7. Caso documentado e arquivado na pasta `_DATA/relatos/`

## Indicadores-Chave de Desempenho

- Tempo total de entrega vs. prazo combinado (meta: ≤ prazo acordado)
- Percentual de itens do checklist de QA aprovados na primeira rodada (meta ≥ 90%)
- Taxa de satisfação do cliente no check-in (meta: NPS ≥ 8 ou equivalente)
- Percentual de entregas com depoimento capturado em até 7 dias (meta ≥ 70%)
- Número de ajustes pós-entrega dentro do período de garantia (meta: ≤ 2 ajustes menores)
- Tempo médio de resposta ao cliente durante execução (meta: ≤ 12h úteis)

## Avisos e Armadilhas Comuns

1. **Handoff incompleto:** Falta de contexto da venda gera retrabalho. Valide todos os itens do brief antes de contatar o cliente.
2. **Expectativas desalinhadas:** Confirme escopo, limites e cronograma por escrito durante o onboarding.
3. **Falta de rastreabilidade:** Centralize decisões e alterações em `_DATA/log-revisoes.MD`.
4. **Entrega sem QA:** Nunca agende apresentação sem checklist concluído.
5. **Silêncio pós-entrega:** Follow-up tardio reduz chances de depoimento. Programe lembretes automáticos.
6. **Depoimento genérico:** Forneça roteiro claro para que o cliente destaque contexto, problema, solução e resultados.

## Dependências

Entradas necessárias:
- Resumo da venda e contrato do processo `SalesCallExecution` (quando disponível)
- Confirmação de pagamento e itens financeiros de `CheckoutSetup`
- Entregáveis ou especificações do MVP vindo de `ManualMVPDesign`
- Lista de ferramentas aprovadas para comunicação e armazenamento (`tools/`)

Saídas habilitam:
- Documentação de casos para `ContentPublication` ou `RetrospectiveAnalysis`
- Materiais de prova social para `OutreachCampaign` e `SalesCallExecution`
- Insumos para melhoria contínua no `ManualMVPDesign` e demais processos

## Referências

- [tasks.MD](tasks.MD) – Checklist operacional detalhado
- [knowledge.MD](knowledge.MD) – Princípios, FAQs e materiais de apoio
- [validator.MD](validator.MD) – Critérios de qualidade antes de encerrar a entrega
- [_DATA/](./_DATA/) – Templates operacionais e registros
