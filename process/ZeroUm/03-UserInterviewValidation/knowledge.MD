# Base de Conhecimento - UserInterviewValidation

## Visão Geral

Entrevistas de validação são conversas estruturadas com usuários reais usadas para confirmar ou refutar hipóteses críticas antes de investir em construção de produto, marketing ou operações. Este documento reúne princípios, boas práticas, materiais de apoio e FAQs para conduzir entrevistas rápidas (5-15 minutos) com alto rigor e aproveitamento de insights.

## Objetivo Central

Extrair evidências qualitativas confiáveis que orientem decisões estratégicas imediatas, garantindo que cada entrevista gere aprendizado sobre:
- Intensidade real das dores
- Soluções alternativas já utilizadas
- Objeções e barreiras à adoção
- Linguagem literal que descreve o problema ou o desejo

## Princípios Fundamentais

1. **Perguntas abertas primeiro** – comece com histórias e exemplos antes de aprofundar hipóteses específicas.
2. **Escuta ativa acima de vendas** – não defenda a solução; investigue a realidade do usuário.
3. **Evidência antes de opinião** – foque em comportamentos observados, não em intenções futuras.
4. **Velocidade com qualidade** – entrevistas curtas exigem preparação precisa para extrair insights profundos rapidamente.
5. **Documentação instantânea** – notas completas durante a conversa evitam perda de contexto ou viés posterior.

## Conceitos-Chave

### Hipótese a validar
Declaração específica sobre problema, solução ou adoção que será testada na entrevista. Deve seguir o formato padrão da [Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md).

### Pergunta aberta vs. fechada
Perguntas abertas exploram contexto e histórias (“Conte sobre a última vez que…”). Fechadas confirmam entendimento ou coletam métricas (“Quantas vezes por semana isso ocorre?”). Use abertas como base e fechadas apenas para validar detalhes.

### Saturação
Momento em que novas entrevistas não trazem aprendizados relevantes adicionais. Se, após 8-10 entrevistas, padrões continuam se repetindo, há sinal de saturação suficiente para decisão.

### Linguagem do cliente
Palavras e expressões exatas usadas pelos usuários. Essenciais para copy, pitch e priorização de dores. Devem ser registradas com fonte e contexto.

### Objeções crônicas
Barreiras recorrentes que aparecem em múltiplas entrevistas (ex: falta de tempo, confiança, orçamento). Documente com citações literais para tratativas futuras.

## Como Estruturar Perguntas

1. **Abertura contextual** – “Conte um pouco sobre como você [executa trabalho relacionado] hoje.”
2. **Exploração do problema** – “Qual foi a última vez que isso aconteceu? O que tornou essa situação difícil?”
3. **Soluções atuais** – “O que você faz hoje para lidar com isso? Já tentou outras abordagens?”
4. **Impacto e urgência** – “Qual é o impacto quando isso acontece? Quanto tempo/dinheiro se perde?”
5. **Encerramento e próximos passos** – “Existe algo que tornaria uma nova solução impossível para você?”

## Perguntas Frequentes

### Quantas entrevistas são suficientes?
Para hipóteses específicas de problema, 8-10 entrevistas normalmente revelam padrões. Continue até confirmar padrões robustos ou até a evidência ser claramente inconclusiva.

### Posso adaptar o roteiro no meio?
Sim, desde que registre o motivo da mudança e ajuste oficialmente o roteiro após revisar aprendizados das primeiras entrevistas.

### O que fazer se ninguém responde aos convites?
Revise os canais, a proposta de valor do convite e considere incentivos. Refaça mensagens focando no benefício para o entrevistado e adicionando provas sociais ou urgência.

### Como lidar com respostas superficiais?
Use follow-ups focados em exemplos concretos: “Pode me contar como isso aconteceu da última vez?”, “O que você fez a seguir?”.

### É necessário gravar?
Recomendado, mas não obrigatório. Sempre peça consentimento explícito. Se a pessoa recusar, faça notas detalhadas em tempo real usando `_DATA/notas-entrevista.MD`.

### Quando definir hipótese como validada?
Quando houver evidência consistente de que pelo menos 70% dos perfis priorizados confirmam a dor ou comportamento investigado, com exemplos concretos e linguagem similar.

## Checkpoints de Qualidade

1. **Antes de recrutar** – Briefing completo com hipóteses, perfis e métricas (template `_DATA/briefing-entrevistas.MD`).
2. **Antes da primeira entrevista** – Roteiro revisado por outra pessoa, perguntas abertas e sem viés.
3. **Após 3 entrevistas** – Ajustar perguntas que não geraram insights ou eram repetitivas.
4. **Após 6 entrevistas** – Revisar se padrões começam a aparecer; reforçar pontos ainda inconclusivos.
5. **Ao final** – Classificar hipóteses com justificativas baseadas em evidências e citações.

## Boas Práticas de Condução

- Agende blocos com buffer de 5 minutos entre entrevistas para atualizar notas.
- Confirme consentimento para gravação antes de iniciar as perguntas.
- Peça exemplos específicos (“Quando foi a última vez?”, “Como você resolveu?”).
- Evite vender a solução; mantenha o foco em entender o problema do entrevistado.
- Registre emoções observadas (tom de voz, velocidade, hesitações) nas notas.
- Finalize agradecendo, informando próximos passos e pedindo indicação de outras pessoas.

## Documentação Recomendada

- **Briefing de validação** – `_DATA/briefing-entrevistas.MD`
- **Roteiro padrão** – [`../_SHARED/templates/script-entrevista.MD`](../_SHARED/templates/script-entrevista.MD) (duplicar para `_DATA/roteiro-entrevista-base.MD`)
- **Plano de recrutamento** – `_DATA/plano-recrutamento.MD`
- **Controle de convites** – `_DATA/tracker-recrutamento.MD`
- **Notas por entrevista** – `_DATA/notas-entrevista.MD`
- **Síntese de padrões** – `_DATA/analise-padroes.MD`
- **Classificação de hipóteses** – `_DATA/classificacao-hipoteses.MD`
- **Biblioteca de linguagem** – `_DATA/biblioteca-linguagem.MD`

## Ferramentas Recomendadas (verificar em `tools/`)

- Videoconferência: Zoom, Google Meet, Whereby
- Agendamento: Calendly, SavvyCal ou Google Calendar
- Registro de notas: Google Docs, Notion, Coda (garantir acesso compartilhado)
- Transcrição automática: ferramentas aprovadas no catálogo `tools/` quando disponíveis

## Materiais de Apoio

- Livro “The Mom Test” (perguntas que evitam viés de validação)
- Guia “Lean Customer Development” (estrutura de entrevistas com foco em problema)
- Conceitos de Jobs To Be Done (entender contexto e motivadores)
- Artigos sobre entrevistas de validação disponíveis na base interna (referenciar quando adicionados)

## Riscos e Mitigações

### Risco: Pipeline vazio
- **Sintoma:** poucas entrevistas agendadas ou cancelamentos frequentes
- **Mitigação:** iniciar com 150% da meta, diversificar canais e agendar lembretes automáticos

### Risco: Hipóteses mal definidas
- **Sintoma:** entrevistas sem foco, aprendizados dispersos
- **Mitigação:** investir tempo suficiente no briefing e alinhar hipóteses com o time

### Risco: Entrevistas virando pitch
- **Sintoma:** entrevistado mais ouvindo que falando
- **Mitigação:** limitar pitches a 30 segundos apenas para contexto e voltar às perguntas abertas

### Risco: Análise superficial
- **Sintoma:** conclusões baseadas em impressões individuais
- **Mitigação:** usar `_DATA/analise-padroes.MD` para sintetizar evidências antes de decidir

### Risco: Falta de rastreabilidade
- **Sintoma:** citações sem referência ou notas em locais diferentes
- **Mitigação:** padronizar armazenamento na pasta `_DATA/` com convenção de nomes (`entrevista-01`, `entrevista-02`, etc.)

## Integrações com Outros Processos

### Processos anteriores
- [ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD) – gera hipóteses a validar
- [TargetUserIdentification](../02-TargetUserIdentification/process.MD) – fornece perfis prioritários

### Processos posteriores
- Planejamento de MVP/protótipo
- Criação de landing page com linguagem validada
- Planejamento de campanha de aquisição ou pré-venda
- Revisão de tese em `strategies/ZeroUm`

## Próximos Passos Sugeridos Após a Validação

1. Atualizar backlog de hipóteses com status e evidências
2. Compartilhar resumo executivo das entrevistas com stakeholders
3. Priorizar experimentos (MVP, landing page, oferta piloto) com base nas hipóteses validadas
4. Revisitar processos anteriores se hipóteses forem refutadas (ex: redefinir usuário-alvo)
5. Programar nova rodada de entrevistas ou testes caso hipóteses permaneçam inconclusivas

## Referências Internas

- [process.MD](process.MD) – etapas completas e outputs esperados
- [tasks.MD](tasks.MD) – checklist operacional para execução
- [validator.MD](validator.MD) – critérios objetivos de qualidade
- `_DATA/` – templates prontos para cada etapa
-
