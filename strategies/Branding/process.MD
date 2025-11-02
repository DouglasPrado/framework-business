# Processo de Execução - Estratégia Brading

Este documento detalha o fluxo operacional necessário para construir, validar e lançar a estratégia Brading com consistência entre times e canais.

## Visão geral do fluxo

```
ETAPA 0 → ETAPA 1 → ETAPA 2 → ETAPA 3 → ETAPA 4 → ETAPA 6
                                ↘
                                 ETAPA 5 (paralela após aprovações verbais/visuais)
```

## ContextImmersion: Imersão e contexto

### Objetivo
Mapear objetivos do negócio, entendimento de público, proposta de valor pretendida e referências de mercado para orientar a criação da marca do zero.

### Entradas necessárias
- Lista de stakeholders internos e clientes/prospects para entrevista (consultar `process/ClientDelivery` e `process/UserInterviewValidation` para identificar contatos existentes)
- Agenda disponível para entrevistas e sessões de descoberta
- Dados de mercado ou pesquisas prévias sobre o segmento (quando houver)
- Referências aspiracionais indicadas pela liderança
- Inventário de artefatos já criados em `process/_SHARED/` e em processos relacionados (ex.: `TargetUserIdentification`, `ProblemHypothesisDefinition`, `UserInterviewValidation`)

### Sequência de ações

- Conduzir reunião de kick-off para alinhar metas, restrições e expectativas, registrando apontamentos em `_DATA/templates/diagnostico-marca.MD`
- Revisar outputs existentes nos processos `TargetUserIdentification`, `ProblemHypothesisDefinition` e `UserInterviewValidation` para evitar retrabalho e alinhar hipóteses já validadas
- Montar roteiro de entrevistas internas e externas (ponto de partida: `process/_SHARED/templates/script-entrevista.MD`)
- Agendar entrevistas com stakeholders prioritários
- Realizar entrevistas internas (mínimo 5 pessoas) e registrar percepções
- Realizar entrevistas externas (mínimo 5 clientes/prospects) e registrar linguagem
- Mapear benchmarking de 6 referências (3 diretas, 3 inspiracionais) e anotar aprendizados
- Consolidar análise SWOT textual e priorizar oportunidades e riscos

### Pontos de decisão
1. **Informações internas suficientes?**
   - ✅ Sim → Prosseguir para benchmarking
   - ❌ Não → Mapear lacunas e realizar entrevistas adicionais ou pesquisas rápidas
2. **Feedback externo coerente com hipóteses internas?**
   - ✅ Sim → Consolidar insight principal
   - ❌ Não → Destacar dissonâncias em relatório para tratar na Etapa 1

### Critérios de qualidade
- Briefing estratégico preenchido
- Pelo menos 10 entrevistas documentadas (5 internas, 5 externas)
- Matriz SWOT redigida em formato textual
- Prioridades classificadas por impacto x esforço
- Relatório compartilhado com liderança

### Outputs
- `diagnostico-marca.MD` preenchido com briefing estratégico completo
- Registro de entrevistas armazenado em `_DATA/ContextImmersion/` (planilhas/notas alinhadas aos templates dos processos reutilizados)
- Relatório resumo com oportunidades e riscos (pode ser `diagnostico-resumo.MD`)
- Agenda validada para workshop da Etapa 1

## Etapa 1: Essência e fundamentos

### Objetivo
Definir propósito, visão, missão, valores e personalidade da marca.

### Entradas necessárias
- Relatório de diagnóstico (ContextImmersion)
- Participantes confirmados para workshop (liderança, marketing, produto, atendimento)
- Template `plataforma-de-marca.MD`

### Sequência de ações

- Conduzir workshop colaborativo (2 horas) revisando diagnóstico e cocriando propósito, visão, missão, valores e personalidade
- Registrar decisões diretamente em `plataforma-de-marca.MD`
- Sintetizar narrativa preliminar e circular versão para feedback
- Coletar ajustes assíncronos e validar narrativa final com liderança executiva
- Converter essência em storytelling curto e preparar one-pager para comunicação interna

### Pontos de decisão
1. **Consenso mínimo sobre propósito e visão?**
   - ✅ Sim → Consolidar documentação
   - ❌ Não → Rodar sessão adicional focada em convergência
2. **Valores possuem comportamentos observáveis?**
   - ✅ Sim → Seguir
   - ❌ Não → Voltar ao grupo para exemplificar atitudes reais

### Critérios de qualidade
- Propósito, visão e missão documentados em frases claras
- Cinco traços de personalidade definidos com descrições
- Valores conectados a comportamentos verificáveis
- Aprovação formal registrada (e-mail ou ata)

### Outputs
- Seção de essência preenchida em `plataforma-de-marca.MD`
- One-pager para divulgação interna (`essencia-apresentacao.MD` ou slides)
- Checklist de comunicação para Etapa 2

## Etapa 2: Posicionamento e promessa

### Objetivo
Estabelecer promessa central, pilares de mensagem e diferenciais competitivos.

### Entradas necessárias
- Essência aprovada (Etapa 1)
- Dados de mercado e benchmarking (ContextImmersion)
- Lista de clientes/leads para validação

### Sequência de ações

- Construir matriz de posicionamento (eixo valor vs diferencial) e formular promessa central
- Selecionar 3-4 pilares de mensagem alinhados ao diagnóstico
- Detalhar benefícios, provas e objeções por pilar
- Escrever mensagens principais e variações por persona priorizada
- Preparar roteiro de validação externa e conduzir conversas com 3 clientes ou leads estratégicos
- Registrar feedback, incorporar ajustes necessários e obter aprovação final com liderança
- Atualizar `plataforma-de-marca.MD` com a versão consolidada

### Pontos de decisão
1. **Promessa clara e memorizável em 12 palavras?**
   - ✅ Sim → Avançar para detalhamento por persona
   - ❌ Não → Revisitar essência e ajustar narrativa
2. **Clientes validaram a promessa?**
   - ✅ Sim → Prosseguir
   - ❌ Não → Registrar objeções e revisar pilares

### Critérios de qualidade
- Promessa central alinhada ao propósito e à dor do público
- Pilares com benefícios, provas e objeções documentados
- Mensagens adaptadas para pelo menos duas personas prioritárias
- Feedback externo anexado ao registro do projeto

### Outputs
- Seção de posicionamento preenchida em `plataforma-de-marca.MD`
- Documento `mensagens-chave.MD` com variações por persona
- Registro de validação com clientes (`validacao-posicionamento.MD`)

## Etapa 3: Identidade verbal

### Objetivo
Construir guia de tom de voz, vocabulário e roteiros que reforcem a promessa.

### Entradas necessárias
- Plataforma de marca consolidada (Etapas 1 e 2)
- Linguagem coletada nas entrevistas do diagnóstico
- Necessidades de cada time (marketing, vendas, suporte)

### Sequência de ações

- Definir princípios de comunicação (fazer x evitar) e mapear vocabulário preferido e restrições
- Criar estrutura do guia verbal e redigir mensagens base por canal prioritário
- Criar roteiros para apresentações e pitch, incluindo exemplos positivos e negativos
- Revisar conteúdo com times envolvidos e rodar simulações de uso em calls reais ou simuladas
- Ajustar conforme feedback, finalizar manual e submeter para aprovação final

### Pontos de decisão
1. **Manual atende necessidades de todos os canais?**
   - ✅ Sim → Congelar versão 1
   - ❌ Não → Ajustar seções específicas antes de seguir para Etapa 4
2. **Roteiros testados em cenários reais?**
   - ✅ Sim → Documentar aprendizados
   - ❌ Não → Agendar sessões práticas adicionais

### Critérios de qualidade
- Guia inclui princípios, exemplos, palavras preferidas e proibidas
- Mensagens base revisadas pelos times que irão usar
- Evidência de teste em contexto real (call gravada ou feedback documentado)
- Versão publicada em repositório compartilhado

### Outputs
- Manual `identidade-verbal.MD` ou PDF
- Roteiro de pitch comercial atualizado
- Scripts de atendimento disponibilizados para time de suporte

## Etapa 4: Identidade visual

### Objetivo
Produzir ou atualizar o sistema visual com aplicações em cenários reais.

### Entradas necessárias
- Briefing validado a partir da plataforma de marca
- Referências visuais coletadas no diagnóstico
- Lista de aplicações prioritárias (digital, impresso, ambientes)

### Sequência de ações

- Validar briefing com time de design e montar moodboard com conceitos iniciais
- Desenvolver logotipo e variações, definir paleta e tipografias, esboçar iconografia e padrões gráficos
- Apresentar conceitos para feedback e iterar até aprovação
- Produzir aplicações prioritárias (site, social, pitch deck, embalagens) e testar legibilidade em diferentes suportes
- Ajustar conforme testes, compilar brand book visual e configurar biblioteca de ativos (Figma ou similar)

### Pontos de decisão
1. **Conceito visual aprovado?**
   - ✅ Sim → Avançar para aplicações
   - ❌ Não → Iterar com base no feedback e apresentar nova rodada
2. **Legibilidade e contraste validados?**
   - ✅ Sim → Preparar brand book
   - ❌ Não → Ajustar paleta ou tipografia

### Critérios de qualidade
- Logotipo com variações para fundo claro, escuro e monocromático
- Paleta com especificação completa (HEX, RGB, CMYK quando aplicável)
- Tipografias com orientações de uso
- Aplicações demonstrando uso correto e incorreto
- Guia visual distribuído para times

### Outputs
- Brand book visual (`identidade-visual.MD` ou PDF)
- Pasta de assets organizada (logotipos, fontes, modelos)
- Lista de pendências ou evoluções futuras

## Etapa 5: Experiências e jornada

### Objetivo
Alinhar touchpoints críticos à nova expressão da marca e preparar playbooks operacionais.

### Entradas necessárias
- Identidade verbal e visual aprovadas (Etapas 3 e 4)
- Dados de jornada do cliente (CRM, suporte, marketing)
- Template `guia-consistencia-canais.MD`

### Sequência de ações

- Mapear jornada atual com stakeholders (marketing, vendas, CS) e identificar momentos críticos
- Definir objetivos e expectativas por touchpoint e priorizar canais que exigem ajustes imediatos
- Escrever playbooks por canal (mensagem, peça, responsável, SLA) e atualizar template de consistência
- Implementar ajustes rápidos (copy, templates, scripts) e planejar produção de peças complexas
- Definir indicadores por canal, conduzir treinamento interno e ajustar com base no feedback do time

### Pontos de decisão
1. **Touchpoints críticos alinhados à promessa?**
   - ✅ Sim → Prosseguir para rollout
   - ❌ Não → Revisar mensagens e materiais específicos
2. **Responsáveis e SLAs definidos?**
   - ✅ Sim → Documentar
   - ❌ Não → Apoiar liderança na definição de ownership

### Critérios de qualidade
- Jornada documentada com momentos e emoções
- Playbooks por canal contendo mensagem, tom, peças e responsáveis
- Treinamento realizado com registro de presença
- Indicadores e SLAs publicados

### Outputs
- `guia-consistencia-canais.MD` preenchido
- Apresentação ou vídeo de treinamento
- Checklist de revisão contínua

## Etapa 6: Rollout e governança

### Objetivo
Lançar a marca internamente e externamente, mantendo disciplina de monitoramento.

### Entradas necessárias
- Entregáveis aprovados das Etapas 0 a 5
- Agenda de comunicação interna e externa
- Ferramentas de monitoramento (social listening, formulários, dashboards)

### Sequência de ações

- Preparar kit interno (apresentação, FAQ, roteiro de reunião) e agendar sessão de lançamento com todo o time
- Definir guardiões de marca por área e planejar cronograma de rollout externo por canal
- Configurar monitoramento de menções e feedbacks e organizar produção pendente
- Conduzir lançamento interno com Q&A, divulgar materiais de suporte e confirmar acompanhamento de métricas
- Executar comunicações externas conforme calendário, registrar feedbacks e métricas de forma recorrente e reunir guardiões periodicamente para ajustes

### Pontos de decisão
1. **Time interno compreendeu a nova marca?**
   - ✅ Sim → Iniciar comunicações externas
   - ❌ Não → Rodar sessões adicionais ou materiais de reforço
2. **Métricas alinhadas às metas?**
   - ✅ Sim → Manter ciclo de monitoramento
   - ❌ Não → Investigar causas e ajustar mensagens ou execução

### Critérios de qualidade
- Plano de acompanhamento documentado com marcos e responsáveis
- Guardião de marca formalmente designado
- Dashboard de métricas ativo e revisado continuamente
- Registro de ajustes realizados ao longo do ciclo

### Outputs
- Apresentação de lançamento (`rollout-apresentacao.MD` ou slides)
- Calendário editorial atualizado
- Dashboard ou planilha de reputação
- Relatório de fechamento do ciclo inicial

## Marcos de controle e feedbacks

- **Checkpoint 1 (após Etapa 2):** revisar alinhamento entre essência, posicionamento e roadmap de produtos.
- **Checkpoint 2 (após Etapa 4):** validar consistência entre manual verbal e visual.
- **Checkpoint 3 (primeiro ciclo de acompanhamento):** medir métricas iniciais e ajustar plano.
- **Revisão trimestral:** atualizar plataforma de marca conforme aprendizado de mercado.

## Relação com artefatos

- Todos os templates referenciados estão em `strategies/Brading/_DATA/templates`.
- Outputs das etapas devem ser salvos na mesma pasta, organizados por etapa (`ContextImmersion`, `Etapa-1`, etc.) para facilitar auditoria.
- Qualquer atualização na plataforma de marca deve ser replicada imediatamente em `process.MD`, `knowledge.MD` e `tasks.MD` para manter coerência.
