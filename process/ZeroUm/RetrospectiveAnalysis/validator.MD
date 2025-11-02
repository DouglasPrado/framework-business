# Validador - Análise Retrospectiva de Crescimento

## Propósito

Definir critérios objetivos para avaliar a qualidade de cada etapa da retrospectiva quinzenal. Utilize este validador durante e após a execução para garantir que decisões sejam fundamentadas em dados confiáveis e resultem em ações acionáveis.

## Critérios de Validação por Etapa

### Validação - Etapa 1: Preparar agenda, insumos e participantes

**Critério 1.1: Cobertura de participantes**
- [ ] Todos os papéis críticos estão confirmados ou com substituto nomeado
- [ ] Convite contém pauta, horário e links para templates
- [ ] Agenda foi enviada com pelo menos 24h de antecedência

**Critério 1.2: Dados atribuídos**
- [ ] Cada métrica essencial possui owner identificado
- [ ] Prazo de envio anterior à sessão está registrado
- [ ] Pendências ou riscos foram documentados no checklist

**Critério 1.3: Histórico revisado**
- [ ] Pendências da retrospectiva anterior foram revisadas
- [ ] Ações ainda abertas têm status atualizado
- [ ] Lições anteriores relevantes foram relembradas para comparação

**Como validar:** conferir `_DATA/checklist-preparacao.MD` e o convite do calendário; ausência de qualquer item reflete necessidade de reorganizar a sessão.

---

### Validação - Etapa 2: Compilar métricas quantitativas

**Critério 2.1: Integridade dos dados**
- [ ] Todos os campos obrigatórios foram preenchidos sem deixar lacunas
- [ ] Período analisado é consistente entre as fontes
- [ ] Há evidência da origem dos dados (ferramenta, relatório)

**Critério 2.2: Consistência temporal**
- [ ] Comparação com ciclo anterior está registrada
- [ ] Variação percentual foi calculada corretamente
- [ ] Mudanças de contexto (campanhas, sazonalidade) foram anotadas

**Critério 2.3: Sinalização de status**
- [ ] Cada indicador possui status (OK/Atenção/Alerta) coerente com as metas
- [ ] Desvios críticos foram destacados para discussão
- [ ] Ausência de dados críticos foi marcada como bloqueio

**Como validar:** revisar `_DATA/coleta-metricas.MD`; se algum indicador essencial estiver em branco ou sem status, a etapa deve ser refeita.

---

### Validação - Etapa 3: Organizar feedback qualitativo

**Critério 3.1: Diversidade de fontes**
- [ ] Pelo menos três fontes de feedback estão representadas
- [ ] Cada fonte possui data e contexto
- [ ] Feedback informal está identificado para ser validado posteriormente

**Critério 3.2: Estrutura e síntese**
- [ ] Feedbacks estão resumidos em linguagem acionável (comportamento, motivação, objeção)
- [ ] Tendências repetidas foram agrupadas
- [ ] Relação com métricas foi indicada quando aplicável

**Critério 3.3: Evidências anexadas**
- [ ] Quotes, prints ou links estão disponíveis para consulta
- [ ] Cada insight possui evidência clara (qualitativa ou quantitativa)
- [ ] Itens sem evidência estão marcados como hipótese

**Como validar:** analisar `_DATA/analise-feedback.MD`; caso faltem evidências ou fontes duplicadas, requisitar complemento antes da sessão.

---

### Validação - Etapa 4: Conduzir sessão e registrar aprendizados

**Critério 4.1: Cobertura das categorias**
- [ ] Há pelo menos um item nos blocos Manter, Corrigir e Testar
- [ ] Nenhuma decisão ficou sem registro
- [ ] Aprendizados negativos foram tratados sem atribuir culpados

**Critério 4.2: Evidência vinculada**
- [ ] Cada aprendizado referencia métrica ou feedback específico
- [ ] Causa raiz está descrita (5 porquês ou similar)
- [ ] Impacto esperado foi estimado

**Critério 4.3: Participação equilibrada**
- [ ] Responsáveis das áreas impactadas validaram os aprendizados
- [ ] Conflitos ou divergências foram resolvidos ou registrados
- [ ] Tempo da sessão respeitou a agenda pactuada

**Como validar:** verificar `_DATA/registro-aprendizados.MD` (preenchido a partir de [`../_SHARED/templates/retrospectiva.MD`](../_SHARED/templates/retrospectiva.MD)) imediatamente após a sessão; se qualquer item carecer de evidência, registrar ação para coletá-la antes da priorização.

---

### Validação - Etapa 5: Aplicar matriz de decisão e priorizar ações

**Critério 5.1: Gatilhos avaliados**
- [ ] Todos os gatilhos da matriz foram verificados (conversão, vendas, entrega, preço, esforço manual)
- [ ] Status de cada gatilho está marcado (Ativo/Inativo)
- [ ] Ações derivadas respeitam o gatilho correspondente

**Critério 5.2: Priorização limitada**
- [ ] Máximo de três ações prioritárias foi respeitado
- [ ] Ações adicionais foram registradas em backlog secundário
- [ ] Cada ação possui owner, prazo e métrica de sucesso

**Critério 5.3: Avaliação impacto x esforço**
- [ ] Impacto esperado foi qualificado (alto/médio/baixo) com base em dados
- [ ] Esforço considerou recursos disponíveis e dependências
- [ ] Riscos ou pré-requisitos foram explicitados

**Como validar:** consultar `_DATA/priorizacao-acoes.MD`; se houver mais de três ações ou itens sem owner, bloquear comunicação final até corrigir.

---

### Validação - Etapa 6: Documentar relatório e comunicar

**Critério 6.1: Registro completo**
- [ ] Relatório inclui data, participantes, aprendizados e ações
- [ ] Links para métricas e feedbacks foram incorporados
- [ ] Próxima data de retrospectiva está definida

**Critério 6.2: Comunicação efetiva**
- [ ] Mensagem foi enviada ao canal oficial com resumo executivo
- [ ] Owners confirmaram recebimento e compromisso
- [ ] Stakeholders externos relevantes foram informados (quando necessário)

**Critério 6.3: Seguimento garantido**
- [ ] Ações foram registradas nos processos responsáveis
- [ ] Bloqueios possuem plano de desbloqueio documentado
- [ ] Checkpoints intermediários foram agendados

**Como validar:** revisar a mensagem de recap, confirmação dos owners e o registro final em `_DATA/registro-aprendizados.MD` (template compartilhado).

---

## Checklist Final de Qualidade

- [ ] Todos os templates em `_DATA/` atualizados com data e responsável
- [ ] Pelo menos um insight validado por fonte de feedback
- [ ] Nenhuma métrica crítica ficou sem status
- [ ] Máximo de três ações priorizadas com métricas de sucesso claras
- [ ] Comunicação final enviada e confirmada
- [ ] Próxima retrospectiva agendada e visível no calendário

## Indicadores de Sucesso do Processo

- Sessão realizada dentro do tempo planejado (≤ 120 minutos)
- Cobertura de métricas essenciais igual ou superior a 100%
- Ações concluídas até a retrospectiva seguinte ≥ 80%
- Redução de métricas em alerta ao longo de dois ciclos consecutivos
- Feedback qualitativo utilizado para embasar ao menos uma decisão por ciclo

Revise este validador sempre que a matriz de decisão ou as metas do negócio forem atualizadas.
