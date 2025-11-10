# Checklist Operacional - Viability Filters (Naming)

Use este checklist para executar a etapa ViabilityFilters. Marque cada item após cumprir o critério de aceite e salvar os outputs em `_DATA/ViabilityFilters/`.

---

## Preparação

- [ ] Revisar `longlist-naming.MD`, `priorizacao-longlist.MD`, `criterios-avaliacao.MD`, `alertas-linguisticos.MD`.
- [ ] Definir verificações necessárias (linguística, domínios, social, jurídico) e responsáveis.
- [ ] Criar `plano-checagens.MD` com atividades, prazos, ferramentas e owners.
- [ ] Confirmar acesso às bases (INPI, USPTO, domínios, redes sociais, app stores).

---

## ViabilityFilters.1 - Revisão da long list e plano de checagens

- [ ] Registrar plano e cronograma (`plano-checagens.MD`).
- [ ] Validar prioridades com sponsor e equipe de naming.

**Critério de aceite**
- Plano aprovado e comunicado aos responsáveis.

**Outputs esperados**
- `_DATA/ViabilityFilters/plano-checagens.MD`

---

## ViabilityFilters.2 - Verificações linguísticas/culturais

- [ ] Avaliar pronúncia, fonética, significados, gírias em idiomas relevantes.
- [ ] Consultar fontes confiáveis ou falantes nativos, quando necessário.
- [ ] Registrar achados em `alertas-riscos-remanescentes.MD` com risco (baixo/médio/alto) e recomendação.
- [ ] Atualizar `matriz-avaliacao.MD` com notas ponderadas para critérios linguísticos.

**Critério de aceite**
- 100% dos nomes avaliados.
- Alertas críticos documentados com plano.

**Outputs esperados**
- `_DATA/ViabilityFilters/alertas-riscos-remanescentes.MD`
- Atualização de `_DATA/ViabilityFilters/matriz-avaliacao.MD`

---

## ViabilityFilters.3 - Disponibilidade digital

- [ ] Verificar domínios prioritários (principal, variações, países).
- [ ] Checar handles em redes sociais e plataformas críticas.
- [ ] Documentar resultados em `disponibilidade-dominios.MD` e `disponibilidade-social.MD`.
- [ ] Salvar evidências (prints, links) em `evidencias/`.
- [ ] Atualizar `matriz-avaliacao.MD` com notas de disponibilidade.

**Critério de aceite**
- Status registrado para todos os nomes priorizados.
- Evidências armazenadas com data/hora.

**Outputs esperados**
- `_DATA/ViabilityFilters/disponibilidade-dominios.MD`
- `_DATA/ViabilityFilters/disponibilidade-social.MD`
- `_DATA/ViabilityFilters/evidencias/` preenchida

---

## ViabilityFilters.4 - Busca jurídica preliminar

- [ ] Consultar bases oficiais de marcas registradas nas classes relevantes.
- [ ] Registrar resultados e protocolos em `parecer-juridico.MD`.
- [ ] Atualizar `matriz-avaliacao.MD` com notas e risco legal.
- [ ] Sinalizar conflitos e sugerir mitigação (variação, classe alternativa, negociação).

**Critério de aceite**
- Parecer jurídico preliminar registrado.
- Riscos legais classificados (baixo/médio/alto).

**Outputs esperados**
- `_DATA/ViabilityFilters/parecer-juridico.MD`
- Atualização de `_DATA/ViabilityFilters/matriz-avaliacao.MD`

---

## ViabilityFilters.5 - Consolidação e short list

- [ ] Consolidar notas e riscos na matriz.
- [ ] Classificar opções (verde, amarelo, vermelho) e gerar `shortlist-naming.MD`.
- [ ] Atualizar `alertas-riscos-remanescentes.MD` com riscos e plano de mitigação.
- [ ] Compartilhar resultados com sponsor e equipe (pré-teste).

**Critério de aceite**
- Short list final com 3-5 nomes elegíveis.
- Riscos remanescentes documentados e aceitos.
- Sponsor aprova short list para testes.

**Outputs esperados**
- `_DATA/ViabilityFilters/shortlist-naming.MD`
- Atualização de `_DATA/ViabilityFilters/alertas-riscos-remanescentes.MD`
- `_DATA/ViabilityFilters/matriz-avaliacao.MD` (versão final)

---

## Encerramento

- [ ] Versionar documentos principais (matriz, short list) e salvar evidências finais.
- [ ] Atualizar cronograma e responsáveis para Etapa 4 (Testes e Validação).
- [ ] Registrar aprendizados no `feedback-log.MD` (se utilizado) ou estratégia.
- [ ] Garantir backup dos arquivos e permissões adequadas.
- [ ] Registrar feedback do sponsor sobre clareza das recomendações.
