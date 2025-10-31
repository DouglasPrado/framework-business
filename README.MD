# README – Sistema Operacional Simplificado

## Propósito

Esta documentação centraliza como operamos negócios digitais com estratégias aplicáveis, processos padronizados e tarefas executáveis em escala. Cada processo descrito aqui gera um conjunto de tarefas.

## Como a estrutura se conecta

- `strategies/`: define teses, playbooks e gatilhos que originam processos. As decisões tomadas aqui orientam quais processos devem nascer ou ser revisados.
- `process/`: descreve o passo a passo operacional de cada iniciativa (process.MD, knowledge.MD e tasks.MD).
- `models/` (@models): reúne os modelos autorizados para qualquer entrega. Sempre use os modelos como base antes de publicar ou revisar materiais.
- `tools/`: catálogo aprovado de soluções que suportam os processos. Só é permitido referenciar ferramentas mapeadas aqui.
- `scripts/`: utilitários opcionais para automatizações ou indexações locais. Utilize apenas quando o processo exigir.
- Arquivos raiz (`README.MD`, `AGENTS.MD`, `CLAUDE.MD`): direcionamentos globais que complementam as instruções acima.

## @models e process

- Os modelos em `models/` são a fonte única de verdade para qualquer entrega. Copie-os antes de iniciar novos processos, tarefas.
- Alterou um model? Refaça todas as etapas construídas a partir dele (process.MD, knowledge, tasks, validator) para manter a aderência.
- Mantenha `models/process/README.MD` atualizado sempre que novos padrões, campos ou instruções forem adicionados aos modelos.

## Fluxo simplificado para criar ou revisar processos

1. Revise este `README.MD`, `process/README.MD` e o modelo correspondente em `models/process/`.
2. Crie ou atualize a pasta `process/<NomeDoProcesso>/`, copiando os arquivos modelo necessários (`process.MD`, `knowledge.MD`, `tasks.MD`, `validator.MD`, `_DATA` ).
3. Documente o processo: detalhe objetivo, escopo, etapas, respostas esperadas, indicadores e cuidados no `process.MD`.
4. Consolide referências, materiais de apoio, perguntas frequentes e checkpoints em `knowledge.MD`.
5. Liste a sequência operacional em `tasks.MD` de acordo com o `process.MD`
6. Ajuste arquivos complementares (por exemplo, `validator.MD`) para garantir que o pacote do processo permaneça coerente.

## Governança e boas práticas

- Trabalhe sempre em texto simples e alinhe o vocabulário com o que já está publicado.
- Todos os arquivos criados deverão ser em ingles e CamelCase `<NomeDoProcesso>`
- Quando atualizar qualquer arquivo, verifique as dependências (Processo ↔ Tarefas ↔ Validador ↔ Modelos) e atualize o que for necessário no mesmo ciclo.
- Evite planilhas e repositórios paralelos; concentre as informações na pasta do processo.

## Referências rápidas

- Estrutura padrão de processos: `process/README.MD`
- Modelos oficiais: `models/process/README.MD` e arquivos na mesma pasta
- Orientações gerais para Codex: `CLAUDE.MD`

## Estrutura

- models
  - process
    - \_DATA (paste)
    - knowledge.MD
    - process.MD
    - tasks.MD
    - README.MD
- strategies
  - knowledge.MD
  - process.MD
  - tasks.MD
