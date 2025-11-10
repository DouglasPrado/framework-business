# Checklist Operacional - Imersão e Contexto (Branding)

Use este checklist para controlar a execução de ContextImmersion no Branding. Marque cada item apenas após cumprir o critério de aceite e registrar os outputs correspondentes.

---

## Preparação

- [ ] Confirmar sponsor, owner e responsáveis por área.
- [ ] Criar pasta `_DATA/ContextImmersion/` com subarquivos necessários.
- [ ] Copiar `strategies/Branding/_DATA/templates/diagnostico-marca.MD` para `_DATA/ContextImmersion/`.
- [ ] Revisar outputs recentes de `TargetUserIdentification`, `ProblemHypothesisDefinition`, `UserInterviewValidation`.

---

## Etapa 1 - Alinhamento e briefing

- [ ] Agendar reunião de kick-off com stakeholders críticos.
- [ ] Coletar materiais estratégicos existentes (posicionamento atual, pesquisa, relatórios).
- [ ] Preencher `diagnostico-marca.MD` com objetivos, público, critérios e restrições.
- [ ] Registrar riscos e dependências mapeadas.
- [ ] Obter aprovação formal do briefing (e-mail ou ata registrada).

**Critérios de aceite**
- Briefing sem campos em branco.
- Lista de stakeholders interna e externa confirmada.
- Cronograma preliminar das entrevistas definido.

**Outputs**
- `_DATA/ContextImmersion/diagnostico-marca.MD`
- `_DATA/ContextImmersion/ata-briefing.MD` (ou registro equivalente)

---

## Etapa 2 - Entrevistas internas

- [ ] Personalizar roteiro usando `process/_SHARED/templates/script-entrevista.MD`.
- [ ] Conduzir ao menos 5 entrevistas com áreas chave (marketing, vendas, atendimento, produto, liderança).
- [ ] Registrar notas padronizadas em `_DATA/ContextImmersion/entrevistas-internas.csv` ou `.MD`.
- [ ] Taguear palavras-chave, dores e oportunidades citadas.
- [ ] Gerar resumo parcial destacando convergências e divergências.

**Critérios de aceite**
- 5 entrevistas mínimas registradas.
- Resumo parcial entregue ao sponsor.
- Lacunas identificadas documentadas.

**Outputs**
- `_DATA/ContextImmersion/entrevistas-internas.csv`
- `_DATA/ContextImmersion/resumo-interno.MD`

---

## Etapa 3 - Entrevistas externas

- [ ] Selecionar 5+ participantes (clientes ativos, prospects, leads perdidos, parceiros).
- [ ] Adaptar roteiro para percepção de marca e diferenciação.
- [ ] Registrar cada conversa (notas, gravações com consentimento) em `_DATA/ContextImmersion/entrevistas-externas`.
- [ ] Capturar linguagem literal e principais objeções percebidas.
- [ ] Consolidar insights com diferenças vs. visão interna.

**Critérios de aceite**
- 5 entrevistas mínimas concluídas.
- Citações-chave destacadas (≥ 10) para uso em etapas futuras.
- Relato de divergências entregue ao sponsor.

**Outputs**
- `_DATA/ContextImmersion/entrevistas-externas.csv`
- `_DATA/ContextImmersion/citacoes-clientes.MD`
- `_DATA/ContextImmersion/resumo-externo.MD`

---

## Etapa 4 - Benchmarking e referências

- [ ] Identificar pelo menos 6 referências (3 diretas, 3 aspiracionais).
- [ ] Preencher `strategies/Branding/_DATA/templates/matriz-inspiracao.MD` (copiar para `_DATA/ContextImmersion/matriz-inspiracao.MD`).
- [ ] Registrar pontos fortes, fracos, oportunidades copiáveis e alertas.
- [ ] Sinalizar potenciais colisões de posicionamento ou identidade.

**Critérios de aceite**
- Matriz preenchida com todas as referências.
- Insights priorizados com justificativa.
- Alertas documentados (ex.: semelhança de nome, tom de voz).

**Outputs**
- `_DATA/ContextImmersion/matriz-inspiracao.MD`
- `_DATA/ContextImmersion/benchmarking.MD`

---

## Etapa 5 - Consolidação e priorização

- [ ] Compilar entrevistas internas/externas em matriz comparativa.
- [ ] Elaborar SWOT textual (`_DATA/ContextImmersion/swot.MD`).
- [ ] Aplicar matriz impacto x esforço para priorizar oportunidades.
- [ ] Redigir `diagnostico-resumo.MD` com principais achados e recomendações.
- [ ] Confirmar agenda e participantes do workshop de Essência (Etapa 1).

**Critérios de aceite**
- SWOT revisada pelo sponsor.
- Top 5 oportunidades priorizadas com responsáveis preliminares.
- Agenda do workshop confirmada.

**Outputs**
- `_DATA/ContextImmersion/swot.MD`
- `_DATA/ContextImmersion/diagnostico-resumo.MD`
- `_DATA/ContextImmersion/agenda-workshop.MD`

---

## Hand-off

- [ ] Compartilhar pacote completo com stakeholders (diagnóstico, anexos, agenda).
- [ ] Registrar decisões pendentes e próximas ações.
- [ ] Atualizar `strategies/Branding/knowledge.MD` com aprendizados relevantes.
- [ ] Arquivar links e arquivos compartilhados no diretório oficial (Drive, Notion etc.).

---

## KPIs sugeridos para monitorar

- % de entrevistas concluídas vs. planejadas.
- Número de referências analisadas.
- Tempo total do ciclo de imersão.
- Satisfação do sponsor com o diagnóstico (escala 1-5).

---

## Observações

- Utilize apenas ferramentas presentes em `tools/`.
- Garanta consentimento antes de gravar entrevistas externas.
- Padronize nomenclatura dos arquivos (ex.: `YYYY-MM-DD_nome-entrevistado.md`).
- Documente aprendizados que possam alimentar o repositório `strategies/Branding/_DATA/`.
