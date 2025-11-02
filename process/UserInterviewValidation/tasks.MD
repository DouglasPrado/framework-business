# Checklist Operacional - UserInterviewValidation

Este checklist orienta a execução completa do processo de validação com entrevistas de usuários. Utilize-o para planejar, conduzir e analisar 10 entrevistas em 2-4 dias corridos, garantindo que todas as evidências sejam documentadas e que hipóteses sejam classificadas com base em dados reais.

## Como Utilizar

1. Preencha as informações do projeto antes de iniciar.
2. Siga cada etapa na ordem proposta, marcando as tarefas concluídas.
3. Use os templates disponíveis na pasta `_DATA/`.
4. Documente owners, datas e links diretamente neste checklist ou no tracker.
5. Ao final, execute o checklist de qualidade para confirmar a completude.

## Informações do Projeto

Projeto/Produto:
Owner principal:
Hipótese principal a validar:
Perfil prioritário:
Período planejado (início e fim):

---

## Etapa 1 – Preparar briefing de validação (45 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Revisar declaração de hipótese atual ([Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md))
- [ ] Selecionar até 3 hipóteses prioritárias (problema, solução, objeções)
- [ ] Definir métricas de sucesso das entrevistas (ex: % que confirmam a dor)
- [ ] Confirmar perfis-alvo que serão abordados
- [ ] Registrar objetivos e métricas no template `_DATA/briefing-entrevistas.MD`
- [ ] Listar pelo menos 5 perguntas que precisam de resposta após a rodada

### Campos do Briefing

- Objetivo da rodada:
- Hipóteses prioritárias:
- Perfis-alvo:
- Indicadores de sucesso:
- Risco principal se hipóteses forem refutadas:

### Output

- [ ] Arquivo `briefing-entrevistas.MD` preenchido na pasta `_DATA/`

---

## Etapa 2 – Construir roteiro de entrevista (60 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Copiar `../_SHARED/templates/script-entrevista.MD` para `_DATA/roteiro-entrevista-base.MD` antes de personalizar
- [ ] Definir abertura, reforço de consentimento e fechamento da entrevista
- [ ] Escrever 5 perguntas principais alinhadas às hipóteses
- [ ] Adicionar follow-ups que explorem exemplos, números e emoções
- [ ] Incluir lembretes sobre evitar perguntas indutivas
- [ ] Validar o roteiro com outro membro do time (ou revisar em voz alta)
- [ ] Salvar o roteiro finalizado em `_DATA/roteiro-entrevista-base.MD`

### Checklist de Perguntas

- [ ] Perguntas são abertas e exploratórias
- [ ] Ordem facilita fluxo natural (contexto → problema → impacto → objeções)
- [ ] Perguntas evitam mencionar a solução diretamente
- [ ] Existem follow-ups para aprofundar cada resposta

### Output

- [ ] Arquivo `roteiro-entrevista-base.MD` completo na pasta `_DATA/` (derivado do template compartilhado)

---

## Etapa 3 – Planejar recrutamento e mensagens (45 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Definir canais primários de recrutamento (ex: e-mail, DM, grupos)
- [ ] Escrever mensagem inicial de convite (incluindo benefício e tempo)
- [ ] Definir script de follow-up e agradecimento pós-entrevista
- [ ] Estabelecer incentivo, se aplicável (ex: gift card, acesso antecipado)
- [ ] Popular `_DATA/plano-recrutamento.MD` com estratégia e cronograma
- [ ] Criar tracker de convites em `_DATA/tracker-recrutamento.MD` com 15+ contatos
- [ ] Preparar mensagem curta para lembretes no dia da entrevista

### Output

- [ ] Arquivo `plano-recrutamento.MD` preenchido
- [ ] Arquivo `tracker-recrutamento.MD` com lista inicial de prospects

---

## Etapa 4 – Executar recrutamento e agendar entrevistas (1-2 dias corridos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Enviar convites iniciais para pelo menos 15 potenciais entrevistados
- [ ] Registrar status de cada convite no tracker (convidado, aceitou, recusou)
- [ ] Realizar follow-up após 24h se não houver resposta
- [ ] Agendar entrevistas confirmadas (registrar data, horário e canal)
- [ ] Enviar lembrete 12-24h antes com link e contexto
- [ ] Confirmar consentimento para gravação (texto padrão no convite ou pré-entrevista)
- [ ] Atualizar tracker com comparecimento e motivos de ausência

### Métricas

- Convites enviados:
- Entrevistas confirmadas:
- Comparecimentos:
- Taxa de comparecimento (meta ≥ 80%):

### Output

- [ ] `tracker-recrutamento.MD` atualizado com status de convites e comparecimentos
- [ ] Lista de 10 entrevistas agendadas ou realizadas

---

## Etapa 5 – Conduzir entrevistas e registrar evidências (1-1,5 dias)

Owner(es):
Período agendado:

### Antes da entrevista

- [ ] Checar roteiro impresso ou aberto em tela
- [ ] Revisar objetivo específico daquela conversa
- [ ] Preparar ferramenta de gravação ou documento de notas

### Durante a entrevista

- [ ] Iniciar agradecendo e reforçando objetivo + duração
- [ ] Obter consentimento expresso para gravação ou anotar que a pessoa não autorizou
- [ ] Seguir roteiro, deixando o entrevistado falar 80% do tempo
- [ ] Usar follow-ups para obter exemplos e números concretos
- [ ] Registrar citações literais diretamente em `_DATA/notas-entrevista.MD`

### Após cada entrevista

- [ ] Nomear arquivo de notas como `entrevista-XX-nome.MD`
- [ ] Destacar dores, soluções atuais, objeções e gatilhos no documento
- [ ] Anotar linguagem destacada em `biblioteca-linguagem.MD`
- [ ] Enviar mensagem de agradecimento e próximos passos

### Output

- [ ] 10 arquivos de notas no formato `_DATA/entrevista-XX-nome.MD` (ou subpasta dedicada)
- [ ] Campo de consentimento preenchido para cada entrevista
- [ ] Biblioteca de linguagem atualizada com citações chave

---

## Etapa 6 – Consolidar padrões e classificar hipóteses (0,5 dia)

Owner:
Data:

### Tarefas

- [ ] Revisar todas as notas e destacar padrões recorrentes
- [ ] Agrupar citações por hipótese e por categoria de dor/objeção
- [ ] Preencher `_DATA/analise-padroes.MD` com pelo menos 3 aprendizados
- [ ] Classificar cada hipótese em `_DATA/classificacao-hipoteses.MD`
- [ ] Adicionar justificativas e citações para cada classificação
- [ ] Atualizar `_DATA/biblioteca-linguagem.MD` com trechos mais relevantes
- [ ] Definir próximos passos (experimentar, refinar, descartar, nova rodada)
- [ ] Compartilhar resumo com stakeholders (anexar ou linkar onde ficará)

### Output

- [ ] `analise-padroes.MD` completo com síntese dos principais aprendizados
- [ ] `classificacao-hipoteses.MD` preenchido com status e evidências
- [ ] `biblioteca-linguagem.MD` atualizada com top citações categorizadas
- [ ] Lista de decisões e owners para próximas ações

---

## Checklist Final de Qualidade

- [ ] 10 entrevistas documentadas com consentimento registrado
- [ ] Briefing, roteiro e plano de recrutamento atualizados no `_DATA/`
- [ ] Tracker de convites completo com status final (compareceu, faltou, recusou)
- [ ] Padrões e aprendizados sintetizados com pelo menos 3 insights acionáveis
- [ ] Todas as hipóteses classificadas (validada/refutada/inconclusiva) com justificativas
- [ ] Biblioteca de linguagem com no mínimo 10 citações literais
- [ ] Próximos passos definidos com owner e data alvo
- [ ] Validator executado e criterios aprovados (ver [validator.MD](validator.MD))

---

## Estrutura de Arquivos Recomendadas em `_DATA/`

```
_DATA/
├── briefing-entrevistas.MD
├── roteiro-entrevista-base.MD
├── plano-recrutamento.MD
├── tracker-recrutamento.MD
├── entrevistas/
│   ├── entrevista-01-nome.MD
│   ├── entrevista-02-nome.MD
│   └── ...
├── analise-padroes.MD
├── classificacao-hipoteses.MD
└── biblioteca-linguagem.MD
```

Garanta que todos os arquivos gerados durante o processo sejam salvos nesta estrutura para facilitar revisão e auditoria.
