# Viability Filters - Processo Naming

> Avalia opções priorizadas com verificações técnicas, linguísticas e legais para formar a short list final

## Objetivo do processo

Aplicar filtros de viabilidade aos nomes gerados, checando pronúncia, significados, disponibilidade digital, conflitos jurídicos e adequação a requisitos críticos. O resultado é uma short list segura para testes com stakeholders e público.

## Quando executar

- Após concluir `process/Naming/02-GenerationConsolidation` com long list priorizada.
- Antes de investir em testes externos ou campanhas que exponham o nome.
- Sempre que novos critérios obrigatórios surgirem (ex.: expansão para novo mercado, novas classes de registro).

## Principais entregáveis

1. `matriz-avaliacao.MD` preenchida com notas ponderadas e classificação de risco.
2. Relatórios de disponibilidade digital (`disponibilidade-dominios.MD`, `disponibilidade-social.MD`).
3. `parecer-juridico.MD` ou registro das consultas realizadas.
4. `shortlist-naming.MD` com nomes elegíveis e status.
5. `alertas-riscos-remanescentes.MD` com planos de mitigação.

## Dependências e conexões

- **Processo anterior:** `GenerationConsolidation`.
- **Estratégia associada:** `strategies/Naming` (Etapa Filtros de viabilidade).
- **Templates base:** `strategies/Naming/_DATA/templates/matriz-avaliacao.MD`, outputs de `ContextBriefing` (`criterios-avaliacao`) e `ResearchInputs` (`alertas-linguisticos`).

## Estrutura das pastas

```
process/Naming/03-ViabilityFilters/
  README.MD
  knowledge.MD
  process.MD
  tasks.MD
  validator.MD
  _DATA/
    README.MD
```

## Próximos passos

1. Revisar `knowledge.MD` para compreender métodos de verificação e requisitos.
2. Executar o fluxo descrito em `process.MD`, salvando evidências em `_DATA/ViabilityFilters/`.
3. Usar `tasks.MD` como checklist e `validator.MD` para garantir qualidade antes de avançar para Testes e Validação.
