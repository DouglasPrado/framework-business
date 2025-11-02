# UserInterviewValidation

## Visão Geral

Este processo conduz a validação qualitativa com usuários reais por meio de 10 entrevistas estruturadas. Ele garante que hipóteses prioritárias sejam testadas rapidamente, que padrões de comportamento sejam identificados e que a linguagem do cliente seja documentada para alimentar decisões estratégicas posteriores.

## Quando Usar

Use este processo quando:
- Já existem hipóteses claras sobre problema ou solução que precisam de validação direta
- Perfis prioritários de usuários foram definidos e precisam ser confrontados com a realidade
- É necessário extrair linguagem do cliente para copy, posicionamento ou landing pages
- O time precisa confirmar ou refutar premissas antes de avançar com construção de produto
- Estratégias como ZeroUm ou Discovery estão na fase de entrevistas de problema

## Pré-requisitos

- Hipóteses priorizadas a partir de processos anteriores (ex: [ProblemHypothesisDefinition](../ProblemHypothesisDefinition/process.MD))
- Perfis de usuários-alvo identificados (ex: [TargetUserIdentification](../TargetUserIdentification/process.MD))
- Tempo reservado para conduzir 10 entrevistas de 5-15 minutos cada
- Disponibilidade de ferramenta de reunião (Zoom, Meet ou telefone) e local para registrar notas
- Acesso a canais onde os perfis podem ser recrutados

## Tempo Estimado

- Preparação (briefing, roteiro, plano de recrutamento): 0,5 dia
- Recrutamento e agendamento: 1-2 dias corridos
- Condução de 10 entrevistas: 1-1,5 dias (blocos distribuídos)
- Consolidação, análise e classificação das hipóteses: 0,5 dia
- Tempo total recomendado: 2-4 dias corridos (prioridade 1)

## Resultado Esperado

Ao concluir este processo você terá:
- 10 entrevistas realizadas e documentadas com perfis-alvo relevantes
- Roteiro de 5 perguntas principais ajustado aos objetivos da validação
- Registro de dores, soluções atuais, objeções e linguagem literal dos usuários
- Síntese dos padrões identificados entre entrevistados
- Classificação das hipóteses (validada, refutada ou inconclusiva)
- Próximos passos claros para iteração, expansão ou pivot

## Arquivos Principais

- [process.MD](process.MD) – fluxo detalhado com etapas, responsabilidades e saídas
- [knowledge.MD](knowledge.MD) – base de conhecimento com conceitos, boas práticas e FAQs
- [tasks.MD](tasks.MD) – checklist operacional com campos de acompanhamento
- [validator.MD](validator.MD) – critérios objetivos para validar a execução
- Pasta `_DATA/` – templates de briefing, roteiro, recrutamento, notas e análise

## Como Executar

1. Leia [process.MD](process.MD) para entender o fluxo completo e as decisões críticas
2. Abra [tasks.MD](tasks.MD) e preencha o checklist seguindo cada etapa
3. Utilize os templates em `_DATA/` para padronizar briefing, roteiro, recrutamento e documentação
4. Registre todas as evidências (notas, gravações, padrões) na mesma pasta durante a execução
5. Ao final, passe pelo [validator.MD](validator.MD) para garantir que nada ficou faltando

## Critérios de Qualidade

- 10 entrevistas completas com dados brutos registrados
- Padrões e aprendizados sintetizados em formato acionável
- Hipóteses classificadas com justificativas baseadas em evidências
- Linguagem do cliente capturada com citações literais e contexto
- Próximos passos definidos de acordo com os resultados da validação

## Próximos Processos

1. **Iterar hipóteses ou proposta de valor** usando insights consolidados
2. **Planejar experimentos** (MVP, landing page, oferta beta) com base nas hipóteses validadas
3. **Ajustar mensagens e copy** utilizando a biblioteca de linguagem do cliente
4. **Recrutar para testes adicionais** (ex: protótipos, testes de solução) conforme necessidade

## Dependências

### Depende de
- Declaração de hipótese atualizada ([Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md))
- Perfis priorizados em [TargetUserIdentification](../TargetUserIdentification/process.MD)
- Lista inicial de hipóteses a validar (problema, solução, objeções principais)

### Habilita
- Planejamento de MVPs e protótipos
- Construção de landing pages com mensagem validada
- Estratégias de aquisição baseadas em dores reais
- Priorização de roadmap orientada por evidências

## Dicas para Sucesso

- Combine perguntas abertas e follow-ups diretos para obter detalhes acionáveis
- Busque citações literais enquanto ouve; a linguagem exata é tão valiosa quanto a confirmação de hipóteses
- Faça o recrutamento em lotes (ex: 5 convites por bloco) para garantir pipeline constante
- Grave entrevistas sempre que possível e peça consentimento claro antes de iniciar
- Reavalie o roteiro após as primeiras 2 entrevistas e ajuste rapidamente

## Avisos Importantes

- Não adapte o roteiro durante a entrevista sem antes registrar o motivo
- Evite perguntas que induzam a resposta (“Você pagaria por X, certo?”)
- Se o recrutamento travar, revise se o perfil está acessível e os incentivos são claros
- Não tire conclusões com menos de 5 entrevistas concluídas; mantenha disciplina na amostragem
- Documente objeções e linguagem mesmo quando a entrevista parece “negativa”

## Métricas de Sucesso

- Taxa de comparecimento nas entrevistas ≥ 80% das pessoas confirmadas
- 100% das entrevistas com notas ou transcrições registradas
- Pelo menos 3 padrões principais identificados
- Cada hipótese classificada com justificativa baseada em citações ou comportamentos observados
- Tempo total dentro do intervalo de 2-4 dias corridos

## Suporte e Referências

- [process.MD](process.MD) – detalhamento completo das etapas
- [knowledge.MD](knowledge.MD) – conceitos, boas práticas e materiais de apoio
- Templates disponíveis em `_DATA/` para todos os passos críticos
- Caso identifique artefatos potencialmente compartilháveis, sinalize no `process/_SHARED/README.MD`

## Versão e Manutenção

- Versão: 1.0
- Criado em: 2025-10-31
- Responsável: Framework Business Team
- Atualizar sempre que mudanças ocorrerem no roteiro padrão ou na estratégia de validação

## Estrutura de Arquivos

```
UserInterviewValidation/
├── README.MD
├── process.MD
├── knowledge.MD
├── tasks.MD
├── validator.MD
└── _DATA/
    ├── briefing-entrevistas.MD
    ├── roteiro-entrevista-base.MD
    ├── plano-recrutamento.MD
    ├── tracker-recrutamento.MD
    ├── notas-entrevista.MD
    ├── analise-padroes.MD
    ├── classificacao-hipoteses.MD
    └── biblioteca-linguagem.MD
```

Após executar o processo, documentos derivados (notas, transcrições, relatórios) devem permanecer na pasta `_DATA/` organizados por etapa.

> O arquivo `roteiro-entrevista-base.MD` deve ser duplicado a partir de `../_SHARED/templates/script-entrevista.MD` antes de cada rodada.
