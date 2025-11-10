# Processo de OutreachCampaign

## Propósito

Gerar um fluxo contínuo de leads qualificados por meio de abordagens personalizadas, transformando perfis priorizados em conversas e calls agendadas que alimentem o funil comercial inicial.

## Objetivo

Executar uma cadência semanal que combine canais quentes, comunidades e outreach frio para:
- Realizar pelo menos 50 abordagens registradas.
- Alcançar taxa de resposta superior a 10%.
- Converter 5 a 10 interações em conversas qualificadas.
- Agendar 2 a 3 calls com fit alinhado ao ICP.

## Escopo

### Dentro do escopo
- Planejamento de contatos prioritários com base em perfis definidos.
- Personalização de mensagens por canal e contexto.
- Execução de outreach em canais diretos, comunidades e DMs frias.
- Registro de status, objeções e aprendizados.
- Follow-ups, agendamento de calls e preparação básica do roteiro.
- Análise semanal de métricas e ajustes na abordagem.

### Fora do escopo
- Execução das calls ou fechamento de vendas (processo separado).
- Automação massiva de mensagens sem personalização.
- Criação de anúncios complexos ou campanhas de mídia recorrentes.
- Gestão avançada de CRM (pipeline completo além do estágio inicial).
- Produção de materiais long-form (webinars, e-books) fora dos scripts da campanha.

## Etapas do Processo

### Etapa 1: Planejamento e priorização semanal (Segunda-feira – 60 minutos)

Objetivo: estruturar a lista de contatos prioritários e definir metas da semana.

Passos:
- Revisar métricas da semana anterior e registrar aprendizados em `_DATA/analise-metricas.MD`.
- Selecionar um foco principal de mensagem (dor/benefício) com base nos perfis priorizados.
- Mapear pelo menos 5 blocos de 10 contatos (50 no total) distribuídos entre canais quentes, comunidades e outreach frio.
- Preencher `_DATA/planejamento-semanal.MD` com nome, canal, contexto e prioridade.
- Identificar gatilhos de personalização para cada bloco (ex: menção a post, conexão em comum, problema citado).
- Definir meta diária (ex: 20 abordagens na terça, 20 na quarta, 10 follow-ups iniciados na quinta).

Outputs:
- Plano semanal preenchido.
- Lista segmentada de contatos priorizados por canal.
- Gatilhos e âncoras de personalização documentados.

### Etapa 2: Preparar mensagens e assets (Segunda-feira – 45 minutos)

Objetivo: construir variações de mensagens que acelerem a personalização sem perder relevância.

Passos:
- Selecionar prova social, dados ou ofertas a serem usados na semana.
- Produzir 3 variações de abertura (quente, morna, fria) e 3 CTA principais (call, feedback, resposta rápida).
- Registrar scripts em `_DATA/matriz-mensagens.MD`, alinhando cada variação a um canal e tipo de contato.
- Validar coerência com a landing page atual e atualizar links de tracking (UTMs, parâmetros de referência).
- Preparar snippets de follow-up (resposta a silêncio, objeções comuns, confirmação de call) utilizando [`../_SHARED/templates/email-followup.MD`](../_SHARED/templates/email-followup.MD).

Outputs:
- Matriz de mensagens atualizada com variações testáveis.
- Links rastreáveis revisados.
- Snippets de follow-up documentados.

### Etapa 3: Executar outreach ativo (Terça e Quarta-feira – 120 minutos/dia)

Objetivo: enviar abordagens personalizadas e registrar status em tempo real.

Passos diários:
- Bloquear dois blocos de foco de 60 minutos (manhã e tarde).
- Enviar 10 mensagens para contatos quentes (rede direta) priorizando WhatsApp/LinkedIn.
- Enviar 10 mensagens em comunidades (postagens, grupos, fóruns) com CTA claro.
- Enviar 10 mensagens de outreach frio por dia (DMs ou e-mails) respeitando limites de cada canal.
- Registrar cada tentativa em `_DATA/registro-interacoes.MD` com data, canal, script usado e status (enviado, respondido, silencioso).
- Marcar follow-ups necessários (24h, 48h, 72h) dentro do mesmo arquivo e/ou CRM utilizado, usando as variações do template compartilhado.
- Ajustar mensagens em tempo real caso taxa de resposta do bloco fique < 10%.

Outputs:
- Registro atualizado das abordagens por canal.
- Histórico de mensagens enviadas com link ou print armazenado.
- Ajustes rápidos de script documentados.

### Etapa 4: Gerenciar respostas e agendar calls (Quinta e Sexta-feira – 90 minutos/dia)

Objetivo: transformar respostas em conversas qualificadas e avançar leads quentes para calls.

Passos diários:
- Revisar todos os retornos e atualizar status em `_DATA/registro-interacoes.MD`.
- Qualificar respostas usando critérios mínimos: dor alinhada, autoridade para decidir, timing adequado.
- Documentar objeções no template `_DATA/controle-objecoes.MD` com causa raiz, segmento e resposta aplicada.
- Enviar follow-ups para contatos silenciosos conforme cadência definida.
- Agendar calls para leads qualificados, registrando data, objetivo e link de reunião.
- Preparar mini-briefing para cada call (problema percebido, canal de origem, próxima ação desejada).

Outputs:
- Agenda semanal com calls confirmadas.
- Objeções categorizadas e respondidas.
- Follow-ups executados e registrados.

### Etapa 5: Analisar métricas e ajustar (Sábado – 60 minutos)

Objetivo: consolidar resultados da semana, identificar gargalos e definir ajustes.

Passos:
- Compilar métricas principais: abordagens enviadas, respostas, conversas qualificadas, calls agendadas, origem dos leads.
- Calcular taxas (resposta, conversão para call, follow-up concluído) e comparar com metas.
- Registrar aprendizados, hipóteses e testes A/B planejados em `_DATA/analise-metricas.MD`.
- Atualizar ranking de canais e segmentos com base nas respostas.
- Definir ajustes para a próxima semana (novas mensagens, canais emergentes, mudanças de priorização).
- Revisar necessidade de tráfego pago complementar e documentar decisão.

Outputs:
- Relatório semanal em `_DATA/analise-metricas.MD`.
- Lista de ajustes prioritários para a semana seguinte.
- Decisão registrada sobre uso (ou não) de tráfego pago experimental.

### Etapa 6: Manutenção contínua (Diário, 10 minutos)

Objetivo: manter organização e compliance durante a semana.

Passos:
- Atualizar CRM ou planilha principal ao final de cada bloco de trabalho.
- Salvar evidências relevantes (prints, áudios, scripts refinados) em subpastas datadas dentro de `_DATA/`.
- Verificar limites de envio em cada canal e ajustar cadência se necessário.
- Garantir que mensagens sigam padrões éticos e políticas das plataformas.

Outputs:
- Registro consistente e auditável das interações.
- Histórico organizado para análise futura.

## Pontos de Decisão

1. **Após Etapa 1:** Há contatos suficientes para atingir 50 abordagens? Se não, ampliar busca em novos canais/comunidades antes de seguir.
2. **Durante Etapa 3:** Taxa de resposta do bloco está abaixo de 10%? Se sim, ajustar script ou canal antes de enviar o próximo bloco.
3. **Durante Etapa 4:** Lead atende critérios mínimos para call? Se não, nutrir via follow-up adicional antes de agendar.
4. **Na Etapa 5:** Resultados justificam teste de tráfego pago? Avaliar orçamento disponível (R$ 50-150) e registrar hipótese.
5. **Após análise semanal:** Algum segmento ou canal deve ser pausado? Documentar decisão e remover do planejamento da semana seguinte.

## Resultados Esperados

1. Pipeline semanal com no mínimo 50 abordagens registradas.
2. Taxa de resposta ≥ 10% com lições aprendidas quando abaixo da meta.
3. Registro de 5-10 conversas qualificadas com notas e próximos passos claros.
4. Agendamento de 2-3 calls com briefing e objetivo definidos.
5. Objeções classificadas por segmento e resposta sugerida.
6. Relatório semanal com métricas, aprendizados e plano de ajuste.

## Indicadores-Chave de Desempenho

- Número de abordagens enviadas por canal.
- Taxa de resposta por bloco (quente, comunidade, frio).
- Percentual de follow-ups realizados dentro do SLA (24-48h).
- Conversões para conversa qualificada e para call agendada.
- Tempo médio entre primeira abordagem e agendamento de call.
- Origem dos leads convertidos (rede, comunidade, frio, pago).

## Avisos e Armadilhas Comuns

1. **Mensagens genéricas:** reduzem taxa de resposta. Sempre referencie contexto específico.
2. **Falta de registro:** confiar em memória compromete follow-ups. Atualize `_DATA/registro-interacoes.MD` em tempo real.
3. **Excesso de outreach frio sem aquecimento:** pode gerar bloqueios. Misture com interações em posts e comunidades.
4. **Não qualificar antes da call:** gera desperdício de tempo. Confirme fit mínimo.
5. **Ignorar objeções recorrentes:** transforme-as em conteúdo e ajustes de mensagem.
6. **Tráfego pago sem rastreio:** só investir após configurar UTMs e métricas claras.

## Dependências

Entradas necessárias:
- Perfis priorizados e dores principais ([TargetUserIdentification](../02-TargetUserIdentification/process.MD)).
- Linguagem do cliente e objeções validadas ([UserInterviewValidation](../03-UserInterviewValidation/process.MD)).
- Landing page ou CTA ativo ([LandingPageCreation](../LandingPageCreation/process.MD)).
- Scripts e ativos aprovados em `_DATA/`.

Saídas habilitam:
- Processos de qualificação e fechamento (SalesCallPlaybook, ConversionFollowUp).
- Iterações em copy da landing e materiais de marketing.
- Atualização de estratégias comerciais em `strategies/`.

## Referências

- [TargetUserIdentification/process.MD](../02-TargetUserIdentification/process.MD)
- [UserInterviewValidation/process.MD](../03-UserInterviewValidation/process.MD)
- [LandingPageCreation/process.MD](../LandingPageCreation/process.MD)
- Templates da pasta `_DATA/`
- Registros anteriores da campanha
