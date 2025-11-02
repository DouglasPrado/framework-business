# Validador - ManualMVPDesign

## Propósito

Garantir que o MVP manual foi planejado, testado e documentado com rigor suficiente para operar com consistência e extrair aprendizados confiáveis antes de qualquer automação.

## Como Usar

1. Revise cada etapa após concluir o ciclo completo (planejamento → piloto → ajustes).
2. Marque os critérios atendidos com base nas evidências armazenadas em `_DATA/` e na ferramenta de gestão.
3. Registre observações e ações corretivas quando houver pendências.
4. Utilize o checklist final para decidir se o MVP manual está pronto para operação com clientes reais.

---

## Validação da Etapa 1 – Briefing e critérios

**Critério 1.1 – Escopo claro**
- [ ] `briefing-manual-mvp.MD` descreve oferta, público e promessas sem ambiguidades
- [ ] Metas de SLA e indicadores estão definidos com valores numéricos ou qualitativos claros
- [ ] Riscos e hipóteses prioritárias estão registrados com plano de acompanhamento

**Critério 1.2 – Alinhamento estratégico**
- [ ] Hipóteses citadas referenciam processos anteriores (ProblemHypothesisDefinition, UserInterviewValidation)
- [ ] Stakeholder responsável aprovou o briefing (indicar data e nome)
- [ ] Recursos necessários (time, ferramentas) confirmados e acessíveis

Evidência: `briefing-manual-mvp.MD`

---

## Validação da Etapa 2 – Fluxo de entrega

**Critério 2.1 – Cobertura completa**
- [ ] `mapa-fluxo-entrega.MD` contempla todas as macro etapas (recebimento → follow-up)
- [ ] Cada tarefa possui responsável primário e dependências claras
- [ ] Checkpoints de qualidade estão definidos para transições críticas

**Critério 2.2 – Estimativas realistas**
- [ ] Tempos planejados foram revisados após feedback inicial
- [ ] Gargalos potenciais têm mitigadores ou responsáveis definidos
- [ ] Fluxo foi revisado por pelo menos um stakeholder operacional

Evidência: `mapa-fluxo-entrega.MD`

---

## Validação da Etapa 3 – Ferramenta de gestão e checklist

**Critério 3.1 – Board/planilha operável**
- [ ] Ferramenta está listada em `tools/` ou aprovada explicitamente
- [ ] Colunas/status refletem o fluxo mapeado sem lacunas
- [ ] Campos obrigatórios (SLA, responsável, data limite) estão configurados e testados

**Critério 3.2 – Checklist executável**
- [ ] `checklist-execucao.MD` cobre todas as tarefas com critérios de conclusão
- [ ] `estrutura-board.MD` documenta convenções de preenchimento e rotinas
- [ ] Board/planilha contém ao menos um exemplo real preenchido

Evidências: `estrutura-board.MD`, `checklist-execucao.MD`, ferramenta de gestão

---

## Validação da Etapa 4 – Templates de comunicação

**Critério 4.1 – Consistência e clareza**
- [ ] Templates (`modelo-email-onboarding.MD`, `modelo-email-entrega.MD`, `modelo-email-follow-up.MD` derivado de [`../_SHARED/templates/email-followup.MD`](../_SHARED/templates/email-followup.MD)) incluem campos obrigatórios (CTA, prazos, canais)
- [ ] Mensagens usam linguagem validada em entrevistas (menção a dores e benefícios reais)
- [ ] Versões alternativas estão documentadas quando houver múltiplos segmentos

**Critério 4.2 – Integração operacional**
- [ ] Checklist e board referenciam o template correto em cada etapa
- [ ] Responsável por cada envio está definido
- [ ] Procedimento de armazenamento (Drive, Notion, e-mail) está documentado

Evidências: templates em `_DATA/`, board/checklist

---

## Validação da Etapa 5 – Piloto interno

**Critério 5.1 – Execução monitorada**
- [ ] Piloto foi executado com cenário representativo e escopo aprovado
- [ ] Tempos reais por etapa estão registrados em `relatorio-piloto.MD`
- [ ] Feedback do cliente teste (real ou simulado) está documentado

**Critério 5.2 – Aprendizado acionável**
- [ ] Desvios > 20% nos tempos possuem análise de causa e ação definida
- [ ] Gargalos identificados têm plano de mitigação ou ajustes no fluxo
- [ ] Backlog de melhorias foi atualizado e priorizado

Evidência: `relatorio-piloto.MD`

---

## Validação da Etapa 6 – Documentação final e materiais

**Critério 6.1 – Padrões de qualidade**
- [ ] `padroes-qualidade.MD` define critérios mensuráveis por etapa
- [ ] Checklist e board refletem os padrões revisados
- [ ] Há registro de aprovação do stakeholder responsável

**Critério 6.2 – Organização e inventário**
- [ ] `manual-operacional-final.MD` consolida fluxo, tempos atualizados e instruções
- [ ] `inventario-materiais.MD` lista 100% dos materiais com links, donos e data de revisão
- [ ] Pasta `_DATA/` contém apenas arquivos atuais (versionamento controlado)

Evidências: `padroes-qualidade.MD`, `manual-operacional-final.MD`, `inventario-materiais.MD`

---

## Checklist de Decisão Final

- [ ] Todos os critérios das etapas 1 a 6 foram atendidos sem pendências críticas
- [ ] Board/planilha testado com ao menos um caso real ou simulado
- [ ] Templates de comunicação aprovados por stakeholder de atendimento/produto
- [ ] Tempos reais e estimados alinhados (variação ≤ 20% ou plano de correção registrado)
- [ ] Materiais padrão acessíveis e inventário atualizado
- [ ] Próximos passos documentados (ex: automações, novos experimentos, métricas adicionais)

### Resultado

- [ ] Aprovar operação do MVP manual com clientes reais
- [ ] Aprovar com ressalvas (listar ajustes necessários abaixo)
- [ ] Repetir ou ajustar piloto antes de liberar operação

Observações finais:

Responsável pela validação:
Data:
