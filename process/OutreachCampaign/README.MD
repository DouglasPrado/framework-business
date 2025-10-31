# Processo de OutreachCampaign

Este processo define uma cadência semanal para gerar abordagens personalizadas, iniciar conversas qualificadas e agendar calls para apresentar a proposta de valor. A execução combina canais pessoais, comunidades e outreach frio para alimentar a landing page ativa com tráfego qualificado e feedback comercial.

## Quando Usar

Use este processo quando:
- Existe uma landing page publicada ou oferta clara para direcionar os contatos (ex: [LandingPageCreation](../LandingPageCreation/process.MD)).
- Há perfis priorizados e dados de linguagem coletados nos processos anteriores de descoberta.
- É necessário gerar tração comercial inicial ou validar proposta de valor via conversas diretas.
- Existe disponibilidade diária (mínimo 2 horas) para executar prospecção, follow-ups e registro.

## Pré-requisitos

- Perfis priorizados documentados em [TargetUserIdentification](../TargetUserIdentification/process.MD).
- Insights de linguagem, dores e objeções provenientes de [UserInterviewValidation](../UserInterviewValidation/process.MD).
- Landing page, formulário ou CTA ativo para captura de leads ([LandingPageCreation](../LandingPageCreation/process.MD)).
- Acesso às contas dos canais escolhidos (WhatsApp, LinkedIn, Instagram, Telegram, e-mail, entre outros aprovados).
- Planilha ou CRM básico configurado para registrar status (utilize templates em `_DATA/`).

## Tempo Estimado

- Planejamento semanal (segunda-feira): 60 minutos.
- Execução de outreach (terça e quarta): 120 minutos/dia.
- Follow-ups e agendamento (quinta e sexta): 90 minutos/dia.
- Análise e ajustes (sábado): 60 minutos.
- Tempo contínuo recomendado: mínimo 2 horas/dia para manter cadência.

## Resultado Esperado

Ao final de cada semana, você terá:
- Lista de pelo menos 50 abordagens personalizadas registradas.
- Taxa de resposta maior que 10% com justificativa documentada quando não atingida.
- Entre 5 e 10 conversas qualificadas em andamento.
- Entre 2 e 3 calls agendadas com leads prioritários.
- Registro de objeções, aprendizados e próximos passos para iteração da campanha.

## Arquivos Principais

- [process.MD](process.MD) – etapas detalhadas por dia da semana.
- [tasks.MD](tasks.MD) – checklist operacional diário.
- [knowledge.MD](knowledge.MD) – boas práticas, scripts e troubleshooting.
- [validator.MD](validator.MD) – critérios para aprovar a execução da semana.
- Pasta `_DATA/` – templates para contatos, mensagens, controle de status e análise de métricas.

## Como Executar

1. Leia [process.MD](process.MD) antes de iniciar a semana para entender metas e decisões críticas.
2. Use [tasks.MD](tasks.MD) como checklist diário, registrando owners, datas e outputs.
3. Preencha os templates em `_DATA/` com as informações da semana (contatos, mensagens, métricas, objeções).
4. Documente evidências (prints, mensagens relevantes, agendas) dentro de `_DATA/` com data.
5. Valide a execução ao final da semana usando [validator.MD](validator.MD) antes de planejar a próxima rodada.

## Critérios de Qualidade

- Mensagens personalizadas com base em dor específica do perfil priorizado.
- Registro completo das abordagens, respostas e follow-ups com timestamps.
- Calls agendadas com briefing prévio e objetivo claro.
- Objeções classificadas e vinculadas ao perfil de origem.
- Métricas principais documentadas e comparadas com metas.

## Próximos Processos

1. **SalesCallPlaybook** (a criar) – condução das calls agendadas.
2. **ConversionFollowUp** (a criar) – nutrição pós-call ou pós-formulário.
3. **PaidTrafficExperiment** (opcional) – quando decidir ampliar alcance com mídia paga.

## Dependências

### Depende de
- [TargetUserIdentification](../TargetUserIdentification/process.MD)
- [UserInterviewValidation](../UserInterviewValidation/process.MD)
- [LandingPageCreation](../LandingPageCreation/process.MD)

### Habilita
- Pipeline de vendas inicial com métricas reais de interesse.
- Iteração rápida em copy da landing e materiais de outreach.
- Priorização de segmentos com base em respostas e objeções.

## Dicas para Sucesso

- Priorize qualidade das mensagens sobre volume bruto; personalize sempre com gatilhos de contexto.
- Combine canais: inicie no canal com maior calor (contatos diretos), avance para comunidades e finalize com outreach frio.
- Use blocos de tempo focados (pomodoros de 25 min) para escrever mensagens sem interrupções.
- Salve variações vencedoras de abordagem em `_DATA/matriz-mensagens.MD` para acelerar futuras semanas.
- Atualize o registro de status diariamente para evitar perda de follow-ups.

## Avisos Importantes

- Respeite políticas de spam dos canais (LinkedIn, Instagram, Telegram); limite abordagens frias a 10-15 mensagens/dia por canal.
- Documente consentimentos quando compartilhar landing page ou ofertas com dados pessoais.
- Se decidir testar tráfego pago, registre orçamento, plataforma e resultados em `_DATA/analise-metricas.MD` e valide com o responsável financeiro.
- Não avance para calls sem confirmar disponibilidade real e objetivo da conversa.
- Revise mensagens para evitar erros ortográficos ou inconsistências de tom.

## Métricas de Sucesso

- Abordagens semanais: mínimo 50.
- Taxa de resposta: meta > 10% (respostas positivas ou neutras).
- Conversas qualificadas: meta 5-10.
- Calls agendadas: meta 2-3.
- Tempo médio entre abordagem e resposta: monitorar tendência e reduzir a cada semana.
- Taxa de follow-up realizado em até 48h: meta ≥ 90%.

## Suporte e Referências

- [process.MD](process.MD)
- [tasks.MD](tasks.MD)
- [knowledge.MD](knowledge.MD)
- Templates em `_DATA/`
- Registros anteriores da campanha para comparação.

## Versão e Manutenção

- Versão: 1.0
- Criado em: 2025-10-31
- Responsável: Framework Business Team
- Revisar trimestralmente ou quando novos canais/aproaches forem incorporados.

## Estrutura de Arquivos

```
OutreachCampaign/
├── README.MD
├── process.MD
├── knowledge.MD
├── tasks.MD
├── validator.MD
└── _DATA/
    ├── planejamento-semanal.MD
    ├── matriz-mensagens.MD
    ├── registro-interacoes.MD
    ├── controle-objecoes.MD
    └── analise-metricas.MD
```

Atualize a pasta `_DATA/` com arquivos datados por semana (ex: `2025-11-03-planejamento.MD`) para manter histórico de desempenho.
