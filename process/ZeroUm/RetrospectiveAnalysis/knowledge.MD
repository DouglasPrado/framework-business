# Base de Conhecimento - Análise Retrospectiva de Crescimento

## Visão Geral

Este documento reúne conceitos, frameworks e materiais de apoio para conduzir retrospectivas quinzenais orientadas por dados. Use-o para preparar a sessão, interpretar indicadores, transformar feedback em aprendizados acionáveis e manter consistência com o restante do framework.

## Conceitos Fundamentais

### Finalidade da retrospectiva
- Gerar aprendizados a partir de métricas e feedback real, não apenas discutir percepções
- Identificar rapidamente gargalos que impedem crescimento contínuo
- Testar hipóteses de melhoria em ciclos curtos, mantendo foco em impacto
- Garantir alinhamento entre equipes (aquisição, vendas, entrega) e evitar retrabalho

### Ritmo recomendado
- Frequência: a cada duas semanas (ou semanal se volume de dados justificar)
- Duração: 120 minutos com pauta clara (30 min métricas, 20 min feedback, 40 min aprendizados, 30 min priorização)
- Participantes mínimos: responsável de growth, marketing, vendas, customer success, produto/operacional

### Perguntas norteadoras
- O que melhorou desde a última retrospectiva? Por quê?
- O que piorou ou desacelerou? Quais hipóteses explicam isso?
- O que aprendemos sobre nossos clientes (compradores e não-compradores)?
- Quais ações priorizadas realmente geraram resultado? O que ficou bloqueado?

## Métricas Críticas por Bloco

### Tráfego da Landing Page
- **Visitas únicas:** volume total no período; fonte principal: analytics configurado em `LandingPageCreation/_DATA/plano-analytics.MD`
- **Taxa de conversão da landing:** leads capturados ÷ visitas; meta mínima 3%; abaixo disso revisar copy/público
- **Canais com maior contribuição:** identificar origem das visitas com melhor conversão, destacando anomalias

### Prospecção
- **Abordagens disparadas:** total de contatos enviados em cadências aprovadas
- **Taxa de resposta inicial:** respostas ÷ abordagens; atenção se < 20%
- **Conversas qualificadas:** reuniões ou trocas profundas agendadas; conectar com playbooks de `TargetUserIdentification`

### Vendas
- **Leads quentes gerados:** quantidade que avançou para proposta
- **Taxa lead → cliente:** fechamentos ÷ propostas; mínimo 5% para manter copy/Oferta atual
- **Receita nova no período:** registrar ticket médio e comparativo com ciclo anterior
- **Objeções recorrentes:** integrar com `UserInterviewValidation/_DATA/analise-padroes.MD`

### Entrega
- **Tempo médio de entrega:** dias entre venda e entrega prometida; > 7 dias aciona automação/gargalo
- **NPS ou score de satisfação:** mínimo desejável 8; acompanhar comentários críticos
- **Depoimentos coletados:** quantidade e qualidade; registrar fontes e autorização de uso
- **Horas manuais por cliente:** calcular total de horas investidas; > 10 horas sinaliza necessidade de automação

## Fontes de Dados e Dependências

- `LandingPageCreation`: métricas de tráfego, conversão e analytics (consultar `_DATA/plano-analytics.MD`)
- `TargetUserIdentification`: segmentação atual de público, cadências de contato e scripts
- `UserInterviewValidation`: biblioteca de linguagem, objeções, drivers de compra e aprendizados qualitativos
- Ferramentas no catálogo `tools/`: planilhas ou BI aprovados, CRM, plataforma de atendimento
- Repositório de atendimentos e tickets internos para capturar feedback de entrega
- Registro de ações anteriores (última retrospectiva) para avaliar progresso

Sempre valide se os dados foram atualizados antes da sessão. Caso alguma fonte esteja indisponível, documente e defina plano para regularizar dentro de 48 horas.

## Frameworks e Modelos

### Matriz de decisão (gatilhos obrigatórios)
- **Conversão landing < 3%:** revisar copy, proposta de valor, segmentação de tráfego
- **Conversão lead → cliente < 5%:** investigar preço, oferta, alinhamento da qualificação
- **Entrega > 7 dias:** mapear gargalo operacional e propor automação ou reforço de equipe
- **Preço aceito sem objeções relevantes:** sinal de margem para testar aumento de até 30%
- **> 10 horas manuais por cliente:** priorizar automação ou padronização imediata

Use a matriz em `_DATA/priorizacao-acoes.MD` para registrar status, diagnóstico e ação derivada.

### Estrutura Manter / Corrigir / Testar
- **Manter:** resultados que superaram meta, práticas com evidência forte de impacto; documente para replicar
- **Corrigir:** pontos abaixo da meta ou com riscos crescentes; detalhe causa raiz e ação corretiva
- **Testar:** hipóteses novas ou experimentos para validar oportunidades (ex: alteração de preço, novo canal)

### Análise de causa raiz (5 Porquês)
- Para cada desvio crítico, pergunte “por quê?” até chegar à origem controlável
- Registrar cadeia de causa em `_DATA/registro-aprendizados.MD` evita tratar sintomas superficiais

### Ciclo de feedback rápido
- Coleta contínua → Síntese quinzenal → Teste rápido → Mensuração → Nova coleta
- Mantenha backlog de experimentos com data de revisão e resultado esperado

## Boas Práticas

### Antes da sessão
- Garantir que cada responsável revise as métricas do seu bloco com antecedência
- Solicitar que participantes tragam feedback bruto (prints, gravações, quotes)
- Validar agenda clara com tempo para decisões, não apenas debate

### Durante a sessão
- Começar com vitórias para reforçar o que deve ser mantido
- Usar dados para sustentar percepções; opinião sem evidência volta para fila de coleta
- Registrar decisões em tempo real no template, evitando retrabalho posterior
- Fazer check oral dos gatilhos da matriz para não esquecer nenhum pilar

### Depois da sessão
- Publicar resumo ainda no mesmo dia para manter contexto fresco
- Vincular ações priorizadas aos processos corretos (ex: copy → LandingPageCreation, objeção → UserInterviewValidation)
- Agendar checkpoints intermediários se ações tiverem duração superior a duas semanas
- Arquivar artefatos na pasta `_DATA/` com data e versão

## Checkpoints de Qualidade

- **Checkpoint 1 – Dados prontos:** `checklist-preparacao` completo, nenhum owner pendente
- **Checkpoint 2 – Métricas consistentes:** `coleta-metricas` preenchido com comparação frente ao ciclo anterior e status de cada indicador
- **Checkpoint 3 – Feedback qualificado:** `analise-feedback` reúne ao menos três fontes diferentes e evidencia repetição
- **Checkpoint 4 – Aprendizados validados:** cada item em `registro-aprendizados` possui evidência quantitativa ou qualitativa associada
- **Checkpoint 5 – Ações acionáveis:** `priorizacao-acoes` contém até três iniciativas com owner, prazo e métrica alvo

## Perguntas Frequentes

**E se algum dado não estiver disponível a tempo?**  
Documente o gap no checklist, identifique responsável e defina prazo máximo de 48 horas para atualização. Se o dado impedir decisão crítica, adie apenas a priorização da área afetada.

**Como lidar com métricas conflitantes (ex: tráfego sobe, conversão cai)?**  
Analise coortes: compare canais ou campanhas separados, verifique qualidade dos leads e valide se houve mudanças em copy ou público. Registre hipóteses no bloco Corrigir antes de propor ação.

**Quando criar automação versus reforçar esforço manual?**  
Use o gatilho de >10h manuais/cliente. Primeiro liste tarefas repetitivas, avalie ferramentas aprovadas no catálogo `tools/` e estime esforço de implementação. Se automação for inviável no curto prazo, documente plano temporário e data para reavaliar.

## Materiais de Apoio

- `_DATA/checklist-preparacao.MD` – checklist para garantir insumos e participantes
- `_DATA/coleta-metricas.MD` – template de consolidação quantitativa
- `_DATA/analise-feedback.MD` – planilha textual para sintetizar feedbacks por fonte
- `_DATA/registro-aprendizados.MD` – registro oficial de aprendizados e causas raiz (preenchido a partir de `../_SHARED/templates/retrospectiva.MD`)
- `_DATA/priorizacao-acoes.MD` – matriz de decisão e backlog priorizado

## Conexões com Outros Processos

- `LandingPageCreation`: fornece métricas de aquisição e copy; ações de tráfego e oferta retornam para este processo
- `TargetUserIdentification`: alimenta dados de prospecção, segmentação e linguagem de abordagem
- `UserInterviewValidation`: origem principal de feedback qualitativo e objeções estruturadas
- `ProblemHypothesisDefinition`: garante alinhamento entre aprendizados e hipótese central; ajustes devem ser refletidos se padrões persistirem
- Processos de entrega ou sucesso do cliente devem receber as ações de correção identificadas (ex: automações, melhoria de onboarding)

## Glossário Essencial

- **Retrospectiva**: encontro periódico para revisar dados, aprender e decidir melhorias
- **Gatilho**: condição pré-definida que obriga avaliação e possível ação
- **Aprendizado acionável**: insight suportado por dados que gera mudança concreta em processos ou experimentos
- **Owner**: responsável pela execução e acompanhamento de uma ação priorizada

Mantenha este documento atualizado sempre que novos artefatos compartilhados surgirem ou quando as metas do negócio forem ajustadas.
