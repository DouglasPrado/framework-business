# Drive Operacional de Resultados

Este diretório centraliza artefatos gerados pela execução dos processos documentados em `process/`. Cada pasta registra uma rodada específica, organizada em arquivos sequenciais que mostram o que foi executado e o output de cada tarefa.

## Como criar uma nova pasta de resultados

1. Identifique o processo executado e defina um nome em CamelCase que combine estrategia e processo e contexto (ex: `ZeroUm/ProblemHypothesisExpressFinancialHealth`).
2. Crie a pasta correspondente dentro de `drive/` e copie ou referencie os dados coletados no log oficial localizado em `process/<Processo>/_DATA/`.
3. Gere arquivos numerados (`01-`, `02-`, etc.) seguindo a ordem das tarefas do processo, descrevendo claramente o que foi feito e o resultado obtido.
4. Mantenha todo o conteúdo em português, sem tabelas e com linguagem alinhada ao restante do repositório.
5. Ao final, valide se os arquivos cobrem todas as etapas do processo e se apontam próximos passos quando aplicável.

## Convenções de nomenclatura

- Pastas: CamelCase combinando processo + objetivo ou ideia trabalhada.
- Arquivos: prefixo numérico (`01-`, `02-`, ...) seguido de descrição curta em minúsculas (ex: `01-contexto-inicial.MD`).
- Conteúdo: resumos objetivos, referências ao log original e marcação dos próximos passos.

## Pastas atuais
