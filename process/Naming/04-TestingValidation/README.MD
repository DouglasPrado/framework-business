# Testing and Validation - Processo Naming

> Testa nomes finalistas com stakeholders internos e público-alvo antes da decisão final

## Objetivo do processo

Validar a short list de nomes por meio de testes qualitativos e/ou quantitativos, consolidar evidências (preferência, clareza, memorabilidade) e recomendar a melhor opção com alternativas de backup.

## Quando executar

- Após concluir `ViabilityFilters` com short list aprovada.
- Antes da reunião de decisão final e início dos protocolos de registro.
- Quando stakeholders solicitarem validação externa ou comparações baseadas em dados.

## Principais entregáveis

1. `roteiro-teste.MD` ou instrumento equivalente preparado.
2. Registro de amostra e execução (`registro-participantes.MD`, `registro-testes.MD`).
3. `relatorio-testes-naming.MD` com resultados, indicadores e citações.
4. Recomendação final (`recomendacao-nome.MD`) com nome preferido, backup e plano de mitigação.

## Dependências e conexões

- **Processo anterior:** `ViabilityFilters`.
- **Estratégia associada:** `strategies/Naming` (Etapa Testes e validação).
- **Templates base:** `strategies/Naming/_DATA/templates/roteiro-teste.MD`, outputs de long list/short list e matrizes de avaliação.

## Estrutura das pastas

```
process/Naming/04-TestingValidation/
  README.MD
  knowledge.MD
  process.MD
  tasks.MD
  validator.MD
  _DATA/
    README.MD
```

## Próximos passos

1. Revisar `knowledge.MD` para escolher métodos e indicadores de teste.
2. Executar o fluxo descrito em `process.MD`, salvando evidências em `_DATA/TestingValidation/`.
3. Utilizar `tasks.MD` como checklist e `validator.MD` para validar resultados antes da decisão final.
