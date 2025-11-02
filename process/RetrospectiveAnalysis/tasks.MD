# Tarefas - Análise Retrospectiva de Crescimento

## Visão Geral

Este documento descreve a sequência operacional para executar a retrospectiva quinzenal. Cada tarefa corresponde às etapas do [process.MD](process.MD) e deve ser executada na ordem indicada. Tempo total estimado: 120 minutos.

## Lista de Tarefas

### Tarefa 1: Preparar agenda, insumos e participantes
**Etapa correspondente:** Etapa 1  
**Tempo estimado:** 15 minutos  
**Responsável:** Owner de Growth / Operations Lead

**Objetivo:** Garantir que a reunião ocorra com dados atualizados, participantes corretos e templates prontos para uso.

**Passos:**
1. Revisar decisão e ações da retrospectiva anterior.
2. Atualizar `_DATA/checklist-preparacao.MD` com owners das métricas, status e prazos.
3. Confirmar disponibilidade dos participantes essenciais e enviar convite com pauta.
4. Compartilhar links para os templates do `_DATA/` com instruções de preenchimento antecipado.

**Ferramentas:**
- Agenda/calendário aprovado em `tools/`
- Planilha ou documento colaborativo aprovado (`_DATA/checklist-preparacao.MD`)

**Critérios de conclusão:**
- [ ] Checklist preenchido com todos os dados necessários e responsáveis definidos
- [ ] Convite enviado com pauta e links para templates
- [ ] Pendências de dados registradas com data prevista de entrega
- [ ] Participantes confirmados ou substitutos nomeados

**Output esperado:**
- Checklist salvo com data, responsável de cada métrica e status (OK, pendente, bloqueado)
- Pauta da sessão anexada ao convite e referenciada no repositório do processo

**Exemplo de output:**
```
Checklist atualizado em 15/03
- Tráfego: Maria (OK)
- Prospecção: João (pendente até 16/03)
- Vendas: Carla (OK)
- Entrega: Lucas (OK)
Pendências: João irá importar relatório do CRM antes da sessão.
```

---

### Tarefa 2: Compilar métricas quantitativas críticas
**Etapa correspondente:** Etapa 2  
**Tempo estimado:** 30 minutos  
**Responsável:** Owner de Growth com apoio dos responsáveis de área

**Objetivo:** Consolidar métricas de tráfego, prospecção, vendas e entrega com comparação frente ao ciclo anterior.

**Passos:**
1. Extrair dados das ferramentas aprovadas (analytics, CRM, planilhas) dentro do período definido.
2. Preencher `_DATA/coleta-metricas.MD` com números absolutos, variação percentual e status.
3. Validar consistência dos dados (mesmo intervalo de datas, fontes atualizadas).
4. Destacar anomalias e possíveis causas preliminares para discussão.

**Ferramentas:**
- Ferramentas de analytics e CRM aprovadas no catálogo
- Template `_DATA/coleta-metricas.MD`

**Critérios de conclusão:**
- [ ] Todos os campos obrigatórios preenchidos (visitas, conversão, abordagens, respostas, conversas, leads, calls, fechamentos, receita, tempo médio, NPS, depoimentos, horas manuais)
- [ ] Variações versus ciclo anterior calculadas
- [ ] Status (OK/Atenção/Alerta) atribuído a cada indicador
- [ ] Pendências ou lacunas documentadas

**Output esperado:**
- Template salvo com métricas atualizadas e comentários iniciais
- Lista de métricas em alerta para aprofundamento na sessão

**Exemplo de output:**
```
Tráfego
- Visitas: 1.200 (+18%) – OK
- Conversão: 2,6% (-0,4pp) – Alerta (abaixo de 3%)
Comentário: Teste de headline em andamento pode ter reduzido conversão.
```

---

### Tarefa 3: Organizar feedback qualitativo e evidências
**Etapa correspondente:** Etapa 3  
**Tempo estimado:** 20 minutos  
**Responsável:** Customer Success / Research Lead

**Objetivo:** Sintetizar feedbacks coletados desde a última retrospectiva para suportar decisões.

**Passos:**
1. Reunir feedbacks de entrevistas, NPS, suporte, vendas e redes sociais.
2. Classificar cada item em `_DATA/analise-feedback.MD` indicando fonte, contexto, comportamento, sentimento.
3. Marcar padrões repetidos (ex: objeção de preço, elogio da entrega) e associar a evidências.
4. Preparar highlights (quotes, links, prints) para apresentação durante a sessão.

**Ferramentas:**
- Banco de entrevistas e NPS (`UserInterviewValidation/_DATA/`)
- Template `_DATA/analise-feedback.MD`
- Repositório de suporte aprovado

**Critérios de conclusão:**
- [ ] Pelo menos três fontes de feedback representadas
- [ ] Principais objeções e motivos de compra destacados
- [ ] Evidências anexadas ou linkadas
- [ ] Conexão com métricas sinalizada quando aplicável

**Output esperado:**
- Documento com tendências qualitativas, citações-chave e sugestões iniciais
- Lista de perguntas em aberto a validar na sessão

**Exemplo de output:**
```
Fonte: Entrevista pós-venda (Cliente B2B)
Comportamento: Aceitou proposta em 48h
Motivador: "Entrega em até 5 dias foi decisiva"
Observação: Reforçar esse benefício na copy.
```

---

### Tarefa 4: Conduzir sessão e registrar aprendizados
**Etapa correspondente:** Etapa 4  
**Tempo estimado:** 20 minutos  
**Responsável:** Facilitador designado (geralmente Owner de Growth)

**Objetivo:** Guiar a retrospectiva quinzenal, validar aprendizados com base nas evidências e classificá-los.

**Passos:**
1. Relembrar objetivo da reunião, combinar regras e revisar agenda.
2. Apresentar síntese das métricas e feedbacks, convidando responsáveis para contextualizar.
3. Registrar aprendizados em `_DATA/registro-aprendizados.MD` dentro dos blocos Manter, Corrigir e Testar.
4. Para cada item, anotar causa raiz (usando 5 porquês), evidência e impacto esperado.

**Ferramentas:**
- Template `_DATA/registro-aprendizados.MD` (derivado de `../_SHARED/templates/retrospectiva.MD`)
- Dashboard/planilha das métricas compiladas
- Canal de videoconferência aprovado

**Critérios de conclusão:**
- [ ] Pelo menos um aprendizado documentado por bloco (Manter, Corrigir, Testar)
- [ ] Cada aprendizado contém evidência vinculada
- [ ] Gargalos críticos identificados com causa raiz preliminar
- [ ] Participantes alinharam percepção sobre principais temas

**Output esperado:**
- Registro da sessão com data, participantes, aprendizados e observações
- Lista de gargalos priorizados para avaliação na etapa seguinte

**Exemplo de output:**
```
Manter: Campanha LinkedIn Segmento CFO – Conversão 4,2%, manter investimento.
Corrigir: Formulário com 6 campos reduzindo conversão (evidência: queda 0,4pp). Ação sugerida: testar versão com 3 campos.
Testar: Aumentar preço em 20% para plano anual (clientes atuais não mencionaram objeção).
```

---

### Tarefa 5: Aplicar matriz de decisão e priorizar ações
**Etapa correspondente:** Etapa 5  
**Tempo estimado:** 20 minutos  
**Responsável:** Núcleo de decisão (Growth + área impactada)

**Objetivo:** Selecionar até três ações de maior impacto alinhadas à matriz de decisão do framework.

**Passos:**
1. Avaliar cada métrica contra os gatilhos da matriz em `_DATA/priorizacao-acoes.MD`.
2. Para indicadores em atenção/alerta, propor ações possíveis (processo, copy, automação).
3. Estimar impacto x esforço e discutir dependências ou riscos.
4. Escolher no máximo três ações, definir owner, prazo e métrica de sucesso.

**Ferramentas:**
- Template `_DATA/priorizacao-acoes.MD`
- Ferramenta de gestão de tarefas aprovada (para registrar follow-up)

**Critérios de conclusão:**
- [ ] Matriz preenchida com status atual de cada gatilho
- [ ] Até três ações priorizadas com owner e prazo
- [ ] Métrica de acompanhamento e expectativa de impacto documentadas
- [ ] Bloqueios ou dependências identificados

**Output esperado:**
- Backlog priorizado anexado ao relatório da retrospectiva
- Ações registradas no sistema/tarefa correspondente para execução

**Exemplo de output:**
```
Ação 1: Reduzir campos do formulário (Owner: Maria, Prazo: 22/03, Métrica: Conversão landing ≥ 3,5%)
Ação 2: Criar automação de onboarding (Owner: Lucas, Prazo: 29/03, Métrica: Tempo de entrega ≤ 6 dias)
```

---

### Tarefa 6: Documentar relatório e comunicar próximos passos
**Etapa correspondente:** Etapa 6  
**Tempo estimado:** 15 minutos  
**Responsável:** Owner de Growth / Operations Lead

**Objetivo:** Consolidar decisões em relatório acessível e garantir que todos saibam o que será feito.

**Passos:**
1. Duplicar [`../_SHARED/templates/retrospectiva.MD`](../_SHARED/templates/retrospectiva.MD) para `_DATA/registro-aprendizados.MD` (se ainda não existir) e preencher com resumo final, próximos checkpoints e anexos relevantes.
2. Compartilhar comunicação no canal oficial (ex: resumo semanal) com aprendizados, ações e métricas em destaque.
3. Garantir que cada owner confirme recebimento e crie tarefas nos processos responsáveis.
4. Registrar data da próxima retrospectiva e eventuais requisitos adicionais.

**Ferramentas:**
- Templates do `_DATA/`
- `../_SHARED/templates/retrospectiva.MD`
- Canal de comunicação interno aprovado
- Ferramenta de gestão de tarefas

**Critérios de conclusão:**
- [ ] Relatório final salvo com data, participantes e links para métricas
- [ ] Comunicação enviada e confirmada pelos owners das ações
- [ ] Tarefas criadas/atualizadas nos processos impactados
- [ ] Próxima sessão registrada no calendário

**Output esperado:**
- Registro final da retrospectiva com aprendizados, ações e responsáveis
- Mensagem recap enviada ao time com confirmação de leitura

**Exemplo de output:**
```
Resumo 15/03 enviado para #growth:
- Métricas principais anexas
- Ações priorizadas (reduzir formulário, automação onboarding)
- Próxima retro agendada para 29/03
Owners confirmaram em thread.
```

---

## Resumo de Entregáveis

- Checklist de preparação atualizado
- Template de métricas preenchido e validado
- Documento de feedback estruturado com evidências
- Registro de aprendizados Manter/Corrigir/Testar
- Matriz de decisão com até três ações priorizadas
- Relatório final comunicado ao time com follow-up agendado

Tempo total previsto: **120 minutos**
