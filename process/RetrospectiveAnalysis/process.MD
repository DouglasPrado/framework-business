# Processo de Análise Retrospectiva de Crescimento

## Propósito

Guiar revisões quinzenais orientadas por dados para identificar aprendizados, detectar gargalos e priorizar melhorias que mantenham o negócio evoluindo a partir de métricas reais e feedback dos clientes.

## Objetivo

Ao final de cada ciclo de duas semanas, consolidar métricas críticas (tráfego, prospecção, vendas e entrega), sintetizar feedback qualitativo, registrar aprendizados classificados por manter/corrigir/testar e direcionar no máximo três ações priorizadas usando a matriz de decisão do framework.

## Escopo

### Dentro do escopo
- Planejar e conduzir sessão de retrospectiva quinzenal
- Consolidar métricas provenientes dos processos ativos (LandingPageCreation, TargetUserIdentification, UserInterviewValidation, entrega)
- Agrupar feedbacks de clientes, leads e time interno
- Classificar aprendizados em manter, corrigir e testar
- Aplicar matriz de decisão para selecionar até três iniciativas prioritárias
- Documentar decisões, owners e próximos checkpoints

### Fora do escopo
- Execução das ações priorizadas (endereçada nos processos responsáveis)
- Criação de dashboards complexos ou integrações novas de dados
- Revisão estratégica trimestral ou redefinição de metas anuais
- Coleta primária de dados não existente (entrevistas, pesquisas) fora dos processos vigentes
- Aprovação de investimentos ou mudanças estruturais sem validação prévia

## Etapas do Processo

### Etapa 1: Preparar agenda, insumos e participantes (15 minutos)

Objetivo: garantir que a sessão de retrospectiva tenha contexto, dados e participantes confirmados.

Passos:
- Revisar o histórico da última retrospectiva e pendências abertas
- Preencher o checklist em `_DATA/checklist-preparacao.MD` apontando owners de métricas e prazos de envio
- Confirmar agenda, duração (120 minutos) e participantes essenciais (owner de growth, marketing, vendas, customer success, produto)
- Compartilhar a pauta prévia e os templates que serão utilizados para que todos tragam dados atualizados

Outputs:
- Checklist de preparação atualizado com responsáveis e prazos
- Convite de calendário enviado com pauta e anexos do `_DATA/`
- Lista de dados pendentes com status (em coleta ou confirmado)

### Etapa 2: Compilar métricas quantitativas críticas (30 minutos)

Objetivo: consolidar números recentes de tráfego, prospecção, vendas e entrega comparando com ciclos anteriores e metas vigentes.

Passos:
- Coletar dados das ferramentas aprovadas e registrar em `_DATA/coleta-metricas.MD`
- Preencher para cada bloco: Tráfego (visitas landing, conversão), Prospecção (abordagens, respostas, conversas), Vendas (leads quentes, calls, fechamentos, receita), Entrega (tempo médio, NPS, depoimentos coletados)
- Calcular variação versus quinzena anterior e sinalizar desvios relevantes
- Anotar comentários com possíveis causas ou lacunas de dados

Outputs:
- Template de métricas preenchido com números absolutos e variação percentual
- Lista de métricas com status sinalizado (OK, Atenção, Alerta)
- Pendências de dados documentadas para resolução rápida

### Etapa 3: Organizar feedback qualitativo e evidências (20 minutos)

Objetivo: transformar feedbacks brutos em insumos estruturados para discussão.

Passos:
- Reunir feedbacks de entrevistas, NPS, mensagens de suporte e vendas desde a última retrospectiva
- Resumir cada entrada em `_DATA/analise-feedback.MD` indicando fonte, comportamento observado, expectativa e sentimento
- Identificar padrões repetidos (objeções, motivações de compra, aspectos da entrega)
- Marcar evidências importantes (quotes, links) para referência durante a sessão

Outputs:
- Mapa consolidado de feedbacks com pelo menos três tendências principais
- Lista de objeções críticas e drivers de compra mais citados
- Acervo de evidências organizado para consulta rápida

### Etapa 4: Conduzir sessão e classificar aprendizados (20 minutos)

Objetivo: facilitar discussão objetiva com o time, cruzando métricas e feedback para gerar aprendizados acionáveis.

Passos:
- Iniciar a sessão revisando objetivos, agenda e regras (foco em dados, zero culpabilização)
- Apresentar síntese das métricas e feedbacks, convidando responsáveis a adicionar contexto
- Registrar em `_DATA/registro-aprendizados.MD` os aprendizados validados nos blocos Manter, Corrigir e Testar
- Para cada aprendizado, identificar causa raiz, evidência quantitativa ou qualitativa e impacto esperado

Outputs:
- Registro de aprendizados com justificativa robusta por bloco
- Lista de gargalos e oportunidades priorizadas por impacto
- Log das decisões tomadas durante a sessão

### Etapa 5: Aplicar matriz de decisão e priorizar ações (20 minutos)

Objetivo: selecionar no máximo três ações com maior impacto utilizando critérios padronizados do framework.

Passos:
- Avaliar cada métrica chave contra os limiares da matriz em `_DATA/priorizacao-acoes.MD`
- Sinalizar gatilhos: conversão landing < 3%, conversão lead→cliente < 5%, entrega > 7 dias, preço aceito sem objeções relevantes, trabalho manual > 10h por cliente
- Propor ações por área (processos, copy/oferta, automações) e estimar impacto x esforço
- Priorizar até três ações, atribuindo owner, prazo e métrica de sucesso associada

Outputs:
- Matriz preenchida com status atual e decisões derivadas
- Backlog priorizado (máximo três ações) com responsáveis e próximos checkpoints
- Critérios de acompanhamento definidos para cada ação

### Etapa 6: Documentar relatório e comunicar próximos passos (15 minutos)

Objetivo: consolidar o registro final da retrospectiva e garantir visibilidade a toda a equipe.

Passos:
- Gerar resumo da sessão com aprendizados, ações e métricas-chave e anexar aos arquivos do processo
- Publicar atualização no canal oficial (ex: weekly update) com links para `_DATA/` e destacar bloqueios
- Registrar tarefas ou tickets em andamento nos processos responsáveis (ex: LandingPageCreation, UserInterviewValidation)
- Agendar follow-up para revisar progresso das ações antes da próxima retrospectiva

Outputs:
- Relatório da retrospectiva salvo em `_DATA/registro-aprendizados.MD` com data, participantes e próxima revisão
- Comunicação enviada com confirmação de leitura dos owners
- Follow-up registrado com data e responsáveis

## Pontos de Decisão

1. **Após Etapa 1:** Todos os dados críticos têm owner e prazo confirmado?  
   - Se não, remarcar sessão ou acionar responsáveis antes de seguir.
2. **Após Etapa 2:** Há métricas ausentes ou inconsistentes que inviabilizam decisões?  
   - Se sim, bloquear priorização até corrigir ou estimar dados.
3. **Após Etapa 4:** Os aprendizados possuem evidências suficientes?  
   - Se não, direcionar coleta adicional (entrevistas, análises) antes de priorizar ações.
4. **Após Etapa 5:** Existem mais de três ações ou ações sem owner e métrica clara?  
   - Se sim, refiná-las para manter foco e accountability.

## Resultados Esperados

1. Checklist de preparação concluído com participantes e insumos confirmados
2. Template de métricas preenchido com variação quinzenal e status por indicador
3. Sumário de feedback qualitativo com principais padrões e evidências
4. Registro de aprendizados categorizado em manter, corrigir e testar
5. Matriz de decisão aplicada com no máximo três ações priorizadas e owners definidos
6. Relatório publicado com próxima data de revisão e pendências acompanhadas

## Indicadores-Chave de Desempenho

- Cobertura das métricas essenciais ≥ 100% (nenhum campo crítico em branco)
- Tempo de entrega médio <= 7 dias; acima disso, ação obrigatória cadastrada
- Conversão de landing page ≥ 3% e conversão de lead em cliente ≥ 5%; desvios acionam revisão de copy/oferta
- Horas manuais por cliente ≤ 10h; excedente exige plano de automação
- Pelo menos 1 insight validado por fonte de feedback (entrevistas, NPS, suporte)
- Ações priorizadas limitadas a três com responsáveis e métricas de acompanhamento registradas

## Avisos e Armadilhas Comuns

- Confundir retrospectiva com reunião de status: foque em aprender e decidir, não apenas reportar números
- Ignorar dados ausentes: estimativas sem validação geram ações incorretas; preencha gaps antes de decidir
- Personalizar metas sem usar a matriz: mantenha critérios objetivos para evitar debates subjetivos
- Não documentar evidências: aprendizados sem fonte dificultam revisões futuras
- Exceder três ações: sobrecarga dilui foco e reduz execução das melhorias priorizadas
- Não conectar ações aos processos responsáveis: cada iniciativa precisa de owner claro e processo de execução
