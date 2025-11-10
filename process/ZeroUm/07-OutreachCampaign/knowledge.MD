# Base de Conhecimento - OutreachCampaign

## Visão Geral

A campanha de outreach semanal transforma perfis priorizados em conversas reais. Esta base reúne fundamentos, boas práticas, materiais de apoio e respostas para dúvidas recorrentes ao executar o ciclo multicanal.

## Objetivo Central

Garantir que cada semana gere aprendizados comercialmente relevantes enquanto mantém cadência de prospecção, follow-ups e agendamento de calls.

## Princípios Fundamentais

1. **Personalização contextual:** sempre conecte a mensagem a um evento, dor ou objetivo específico do contato.
2. **Cadência consistente:** blocos diários garantem volume sem comprometer qualidade.
3. **Registro em tempo real:** dados atualizados permitem decisões rápidas e evitam perda de follow-ups.
4. **Otimização contínua:** cada semana deve produzir hipóteses e ajustes para a seguinte.
5. **Canal certo para o momento certo:** escolha o canal conforme relação prévia, tipo de comunidade e receptividade.

## Segmentação e Priorização

- Inicie pelos contatos quentes: clientes anteriores, pessoas que já demonstraram interesse, conexões de primeiro grau.
- Amplie para comunidades específicas (grupos de WhatsApp/Telegram, fóruns, Facebook Groups) com regras claras e foco no problema validado.
- Reserve outreach frio para perfis que atendem perfeitamente aos critérios mas ainda não conhecem a oferta.
- Use notas de [TargetUserIdentification](../02-TargetUserIdentification/process.MD) para validar acessibilidade e disponibilidade.

## Preparação de Mensagens

- Utilize `_DATA/matriz-mensagens.MD` para organizar variações por canal.
- Estruture cada mensagem em quatro blocos: gatilho (por que estou entrando em contato), contexto (qual problema percebi), proposta de valor (como posso ajudar), CTA (ação desejada).
- Inclua prova social relevante quando possível (número, depoimento, caso). Evite exageros ou promessas impossíveis.
- Adapte tom ao canal: mais direto em WhatsApp, mais formal em LinkedIn, mais conversacional em Instagram.

## Cadência Recomendada

- **Dia 0 (Segunda):** preparar lista e scripts.
- **Dia 1 (Terça):** executar blocos 1 e 2 (rede direta + comunidade) pela manhã e tarde.
- **Dia 2 (Quarta):** executar blocos 3 e 4 (outreach frio + complementos de comunidade).
- **Dia 3 (Quinta):** responder retornos, enviar primeiro follow-up aos silenciosos.
- **Dia 4 (Sexta):** consolidar conversas, agendar calls, segundo follow-up conforme necessidade.
- **Dia 5 (Sábado):** analisar métricas, revisar objeções e atualizar scripts.

## Registro e Controle

- `_DATA/registro-interacoes.MD` deve conter: data/hora, nome do contato, canal, mensagem usada, status, próxima ação e data do próximo follow-up.
- `_DATA/controle-objecoes.MD` agrupa objeções por categoria (preço, prioridade, autoridade, solução existente). Use para refinar copy.
- `_DATA/analise-metricas.MD` consolida resultados e decisões. Inclua gráficos simples (listas com porcentagens) quando relevante.

## Uso de Tráfego Pago

- Utilize apenas após duas semanas com cadência consistente e quando canais orgânicos atingirem limite de volume.
- Budget sugerido: R$ 50-150 para testes rápidos (Meta Ads, LinkedIn Ads, Google Ads com segmentação restrita).
- Sempre configurar UTM com parâmetros `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` conectados ao bloco testado.
- Documente hipótese do teste, público alvo, criativo usado e resultado em `_DATA/analise-metricas.MD`.

## Scripts de Follow-up

- **Após 24h (silêncio):** relembre o gatilho inicial e ofereça CTA alternativo (ex: enviar material).
- **Após 48h:** introduza prova social ou dado relevante para reforçar urgência.
- **Após 72h:** confirme se a dor continua presente e ofereça desinscrição respeitosa para preservar relacionamento.

## Perguntas Frequentes

### Quantos contatos devo enviar por canal?
Equilibre volume e segurança: 10 mensagens por canal/dia é um bom ponto de partida. Ajuste conforme limite da plataforma e respostas recebidas.

### Como evitar bloqueios em redes sociais?
Aqueça o contato com interações (curtidas, comentários) antes de enviar DM fria. Alterne formatos (texto, áudio curto). Respeite limites de conexão e personalize cada mensagem.

### O que fazer quando a taxa de resposta cai abaixo de 10%?
Revise os quatro blocos da mensagem. Verifique se o gatilho está claro, se o problema citado é relevante e se o CTA é específico. Teste nova variação em pequenos lotes.

### Como priorizar leads para call?
Use critérios BANT simplificados: Budget (tem orçamento?), Authority (decisor ou influenciador?), Need (dor atual e intensa), Timing (quando pretende agir?). Avance apenas se três critérios forem positivos.

### Como documentar objeções?
Preencha `_DATA/controle-objecoes.MD` com data, segmento, resumo da objeção, resposta aplicada e status (resolvida, pendente, insight para produto). Isso alimenta melhorias em copy, produto e precificação.

## Checkpoints de Qualidade

1. Mensagens personalizadas com referência explícita ao contexto do contato.
2. Registro de todas as interações com timestamp e próxima ação definida.
3. Follow-up enviado em até 48h para 90% dos contatos sem resposta.
4. Calls agendadas com briefing que inclua objetivo, dor e resultado esperado.
5. Relatório semanal completo com métricas, aprendizados e ajustes priorizados.
6. Objeções categorizadas e tratadas com respostas padrão atualizadas.

## Boas Práticas por Canal

- **WhatsApp:** prefira áudio curto apenas após autorização. Use mensagens curtas, com CTA único e link da landing.
- **LinkedIn:** personalize com referência ao cargo e conteúdo recente do contato. Evite anexos na primeira mensagem.
- **Instagram:** responda stories ou posts recentes antes de enviar DM direta. Utilize linguagem leve, mantendo profissionalismo.
- **Telegram/Comunidades:** leia regras antes de postar. Ofereça valor (insight, resumo de pesquisa) antes de inserir CTA.
- **E-mail frio:** linha de assunto direta com benefício. Corpo curto (3-4 frases) com CTA claro (responder, agendar, acessar landing).

## Materiais de Apoio

- Templates em `_DATA/` (planejamento, matriz de mensagens, registro, controle de objeções, análise).
- Anotações de entrevistas e dores críticas em `_DATA/` dos processos anteriores.
- Estudo de caso interno de outreach (quando disponível) deve ser anexado em subpasta `_DATA/referencias/`.
- Ferramentas aprovadas no diretório `tools/` (CRM leve, encurtadores, automações simples).

## Riscos e Mitigações

- **Banimento de canal:** manter limites diários e evitar links repetidos em massa. Se ocorrer, migrar para canal alternativo e revisar abordagem.
- **Mensagens sem rastreio:** sempre usar links com UTM e registrar no template de métricas.
- **Volume insuficiente:** agendar bloco extra ou ampliar comunidades na Etapa 1.
- **Objeções recorrentes de preço:** validar com responsável por pricing e adaptar copy.
- **Falta de tempo para follow-up:** automatizar lembretes com calendário ou ferramenta aprovada.

## Integrações com Outros Processos

### Processos anteriores
- [ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD)
- [TargetUserIdentification](../02-TargetUserIdentification/process.MD)
- [UserInterviewValidation](../03-UserInterviewValidation/process.MD)
- [LandingPageCreation](../LandingPageCreation/process.MD)

### Processos posteriores
- SalesCallPlaybook (a criar)
- ConversionFollowUp (a criar)
- PaidTrafficExperiment (a criar)

## Próximos Passos Após a Semana

1. Atualizar indicadores em dashboards ou planilhas centrais.
2. Compartilhar aprendizados relevantes com time de produto e marketing.
3. Preparar variações de mensagem ou ofertas para próxima semana.
4. Realimentar backlog de conteúdos com objeções recorrentes.
5. Ajustar metas semanais conforme sazonalidade ou capacidade.

## Referências Internas

- [process.MD](process.MD)
- [tasks.MD](tasks.MD)
- [validator.MD](validator.MD)
- Templates `_DATA/planejamento-semanal.MD`, `_DATA/matriz-mensagens.MD`, `_DATA/registro-interacoes.MD`, `_DATA/controle-objecoes.MD`, `_DATA/analise-metricas.MD`
- [`../_SHARED/templates/email-followup.MD`](../_SHARED/templates/email-followup.MD) – variações padrão para follow-ups assíncronos
