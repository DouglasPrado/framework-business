# Base de Conhecimento - Definição de Escopo de MVP

## Propósito deste Documento

Este documento fornece contexto teórico, referências, boas práticas e respostas a perguntas frequentes sobre o processo de Definição de Escopo de MVP. Use como material de apoio durante a execução do processo.

## Fundamentos Teóricos

### O que é um MVP

MVP (Minimum Viable Product) é a versão mais simples de um produto que permite validar uma hipótese principal com usuários reais, coletando máximo aprendizado com mínimo esforço de desenvolvimento.

**Características de um bom MVP:**
- Foca em UMA funcionalidade principal que valida a hipótese
- É funcional, não apenas um protótipo ou mockup
- Pode ser lançado e usado por usuários reais
- Gera dados mensuráveis de validação
- É construído em semanas, não meses

**O que MVP NÃO é:**
- Produto completo com features reduzidas
- Versão beta de produto final
- Protótipo não funcional ou clickable mockup
- Desculpa para lançar produto de baixa qualidade

### Diferença entre MVP, MLP e Prototype

**MVP (Minimum Viable Product):**
- Produto funcional mínimo
- Validação de hipótese de negócio
- Usuários reais utilizam
- Gera aprendizado de mercado

**MLP (Minimum Lovable Product):**
- Produto mínimo que usuários amam
- Foco em experiência além da funcionalidade
- Validação de engajamento emocional
- Próximo passo após MVP validado

**Prototype:**
- Simulação não funcional
- Validação de conceito ou usabilidade
- Usuários testam em ambiente controlado
- Não gera validação de mercado real

### Framework de Hipótese

O formato "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]" é baseado em Jobs-to-be-Done e força clareza em três elementos críticos:

**QUEM:** Beneficiário específico da solução
- Evite "pessoas" ou "usuários genéricos"
- Seja específico: profissão, contexto, características definidoras
- Você deve conseguir encontrar 10+ pessoas que correspondam

**RESULTADO:** Objetivo ou resultado desejado
- Foque no objetivo, não na solução
- Descreva o estado final alcançado
- Deve ser mensurável sempre que possível

**DOR:** Principal obstáculo ou fricção
- O que impede o resultado hoje
- Descreva a solução inadequada atual
- Quantifique se possível (tempo, dinheiro, esforço)

### Priorização de Funcionalidades

#### Framework: "MVP funciona sem isso?"

Para cada funcionalidade secundária proposta, faça a pergunta:
"Se removermos essa funcionalidade, o MVP ainda valida a hipótese principal?"

**Se SIM:** Funcionalidade NÃO é crítica → Vai para backlog futuro
**Se NÃO:** Funcionalidade é crítica → Candidata a funcionalidade secundária

#### Regra das 3 Funcionalidades Secundárias

MVP deve ter:
- 1 funcionalidade principal (core) que valida hipótese
- Máximo 3 funcionalidades secundárias críticas
- Total: 4 funcionalidades no máximo

Se você identificou mais de 3 secundárias, repriorize usando critérios:
1. Sem essa funcionalidade, o produto é inutilizável?
2. Sem essa funcionalidade, não conseguimos testar a hipótese?
3. Sem essa funcionalidade, o produto não pode ser monetizado?

Se nenhum dos critérios acima for verdadeiro, a funcionalidade NÃO é crítica.

### Scope Negativo

Tão importante quanto definir o que entra no MVP é documentar explicitamente o que NÃO entra.

**Benefícios do Scope Negativo:**
- Evita scope creep durante desenvolvimento
- Alinha expectativas de stakeholders
- Facilita tomada de decisão ("isso está no scope negativo")
- Documenta promessas para futura consideração

**Como documentar Scope Negativo:**
Para cada feature excluída, registre:
- Nome da funcionalidade
- Razão da exclusão (complexidade, tempo, não valida hipótese)
- Quando considerar no futuro (pós-validação, após X usuários, versão 2.0)

## Boas Práticas

### Durante Análise de Documentação

**Faça:**
- Leia todos os documentos disponíveis antes de tirar conclusões
- Anote contradições e gaps explicitamente
- Destaque citações diretas de usuários em pesquisas
- Prepare perguntas específicas para stakeholders
- Crie síntese consolidada de todas as fontes

**Não faça:**
- Pular documentos considerados "não importantes"
- Assumir que contradições serão resolvidas sozinhas
- Confiar apenas em um documento (ex: apenas o briefing)
- Seguir em frente com gaps críticos de informação

### Durante Definição de Hipótese

**Faça:**
- Use o formato padrão: "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"
- Valide que a hipótese é mensurável
- Teste se você consegue imaginar como invalidar a hipótese
- Documente hipóteses secundárias para referência

**Não faça:**
- Criar hipótese vaga ou genérica
- Incluir múltiplas hipóteses em uma única frase
- Formular hipótese que não pode ser testada
- Ignorar validação com stakeholders

### Durante Definição de Funcionalidades

**Faça:**
- Comece sempre pela pergunta: "Se tivéssemos apenas 1 funcionalidade..."
- Descreva fluxo de usuário completo da funcionalidade core
- Aplique rigorosamente o critério "MVP funciona sem isso?"
- Documente scope negativo explicitamente
- Explique conexão entre funcionalidade core e hipótese

**Não faça:**
- Selecionar mais de 3 funcionalidades secundárias
- Adicionar funcionalidades "porque são fáceis de fazer"
- Confundir funcionalidade de suporte (autenticação) com funcionalidade core
- Deixar funcionalidades excluídas sem documentação

### Durante Criação do Briefing

**Faça:**
- Preencha todas as seções do template
- Use linguagem clara e objetiva
- Defina métricas com valores quantitativos
- Documente riscos e mitigações
- Obtenha aprovação formal documentada

**Não faça:**
- Pular seções do template
- Usar linguagem vaga ("melhorar", "otimizar")
- Definir métricas genéricas ("usuários satisfeitos")
- Ignorar riscos óbvios
- Considerar aprovação verbal como suficiente

## Materiais de Apoio

### Templates

- [Template de Briefing de MVP](_DATA/template-briefing-mvp.md) - Template completo para consolidar toda análise
- [Template de Funcionalidades](_DATA/template-funcionalidades.md) - Template para mapear funcionalidades em detalhes
- [Template de Declaração de Hipótese](../../_SHARED/templates/declaracao-hipotese.md) - Template compartilhado do framework

### Referências Externas

**Livros recomendados:**
- "The Lean Startup" - Eric Ries (metodologia MVP)
- "Running Lean" - Ash Maurya (canvas e validação)
- "Sprint" - Jake Knapp (decisões rápidas de produto)
- "The Mom Test" - Rob Fitzpatrick (validação de hipóteses)

**Artigos e recursos:**
- Y Combinator: "How to Build an MVP"
- First Round Review: "The Minimum Viable Testing Process"
- Product Coalition: "MVP vs MLP vs MMP"

### Ferramentas Recomendadas

**Para documentação:**
- Google Docs (colaborativo)
- Notion (estruturado)
- Confluence (empresarial)

**Para análise e priorização:**
- Miro ou Mural (workshops colaborativos)
- Planilhas Google (priorização)
- Excalidraw ou Figma (fluxos de usuário)

## Perguntas Frequentes

### Sobre Processo

**P: Quanto tempo deve levar para completar este processo?**
R: 4-5 dias em média. Se levar mais de 1 semana, provavelmente há indecisão ou falta de informação crítica.

**P: Preciso completar todas as tarefas na ordem exata?**
R: A ordem é recomendada, mas algumas tarefas podem ser paralelizadas (ex: Tarefa 2 e 3 podem ocorrer simultaneamente).

**P: E se não houver documentação existente para analisar?**
R: Considere executar processos anteriores primeiro: ProblemHypothesisDefinition ou TargetUserIdentification. Ou realize discovery rápido com stakeholders antes de iniciar.

**P: Posso pular a aprovação formal se stakeholders já concordaram verbalmente?**
R: Não recomendado. Aprovação documentada evita mal-entendidos futuros e serve como contrato de escopo.

### Sobre Hipótese

**P: E se houver múltiplas hipóteses igualmente importantes?**
R: Escolha UMA como principal para o MVP. Documente as outras como secundárias e considere MVPs sequenciais para validá-las.

**P: A hipótese pode mudar durante o desenvolvimento?**
R: Mudanças na hipótese requerem revisão completa do Briefing e aprovação de stakeholders. Evite mudanças após início do desenvolvimento.

**P: Como saber se a hipótese é mensurável?**
R: Pergunte-se: "Como eu saberei se validei ou invalidei essa hipótese?" Se consegue imaginar métricas específicas, ela é mensurável.

### Sobre Funcionalidades

**P: Autenticação e pagamento contam como funcionalidades secundárias?**
R: Não. São funcionalidades de suporte essenciais. As 3 funcionalidades secundárias são específicas do produto.

**P: E se a funcionalidade core for muito complexa?**
R: Provavelmente você está descrevendo múltiplas funcionalidades. Quebre e identifique qual é o núcleo mínimo que valida a hipótese.

**P: Posso adicionar funcionalidades durante o desenvolvimento?**
R: Apenas se crítico para viabilidade. Novas funcionalidades requerem aprovação formal e podem afetar timeline.

**P: Como lidar com stakeholder que insiste em funcionalidade não crítica?**
R: Use o scope negativo: documente a funcionalidade, justifique exclusão, prometa considerar pós-validação. Se impasse, escalone para decisor final.

### Sobre Métricas

**P: Quais são valores realistas para métricas de validação?**
R: Depende do produto, mas referências típicas:
- Cadastros (4 semanas): 20-100 usuários
- Taxa de ativação: 40-60%
- Taxa de conversão para pagamento: 5-10%
- Retenção semana 2: 30-40%
- NPS: 30-50

**P: Preciso definir todas as métricas agora?**
R: Sim, ao menos as principais (cadastros, ativação, conversão, retenção). Métricas orientam decisão pós-lançamento.

**P: E se não bater nenhuma das métricas definidas?**
R: Use critérios de decisão (validado/não validado/perseverar). Analise quais métricas falharam e por quê. Considere pivotar.

### Sobre Timeline e Orçamento

**P: 6-8 semanas é realista para qualquer MVP?**
R: Para MVP com 1 funcionalidade core + até 3 secundárias, usando stack padrão, sim. Se estimar mais, revise escopo.

**P: E se o orçamento aprovado for insuficiente?**
R: Reavalie hosting e providers. Muitos têm free tiers generosos. Se ainda insuficiente, discuta com stakeholders antes de prosseguir.

**P: Posso estender o prazo durante desenvolvimento?**
R: Extensões requerem aprovação formal. Prefira cortar funcionalidades secundárias a estender timeline significativamente.

### Sobre Riscos

**P: Quantos riscos devo identificar?**
R: 3-5 riscos principais. Mais que isso dificulta gestão. Foque nos mais prováveis ou de maior impacto.

**P: E se um risco identificado se materializar?**
R: Execute a mitigação planejada. Se mitigação falhar, reavalie viabilidade do MVP com stakeholders.

## Checkpoints de Qualidade

### Checkpoint 1: Após Análise de Documentação (Etapa 1)
- Todos os documentos disponíveis foram lidos?
- Existe síntese consolidada de informações?
- Contradições foram identificadas e registradas?
- Lista de perguntas para stakeholders está preparada?

### Checkpoint 2: Após Definição de Hipótese (Etapa 2)
- Hipótese está no formato padrão?
- QUEM, RESULTADO e DOR estão claramente definidos?
- A hipótese é mensurável?
- Stakeholders validaram e aprovaram a hipótese?

### Checkpoint 3: Após Definição de Funcionalidades (Etapa 3)
- Funcionalidade core está descrita em detalhes?
- Existem no máximo 3 funcionalidades secundárias?
- Scope negativo foi documentado?
- Stakeholders aprovaram funcionalidades e scope negativo?

### Checkpoint 4: Após Criação do Briefing (Etapa 4)
- Todas as seções do template estão preenchidas?
- Métricas de validação são quantitativas?
- Timeline é de 6-8 semanas?
- Orçamento está dentro do aprovado?
- Riscos principais foram identificados com mitigações?

### Checkpoint 5: Após Aprovação (Etapa 5)
- Aprovação formal foi documentada?
- Briefing foi compartilhado com todo o time?
- Todos têm acesso ao documento?
- Briefing é reconhecido como referência oficial?

## Sinais de Alerta

### Sinais de que o escopo está muito grande:
- Mais de 3 funcionalidades secundárias identificadas
- Timeline estimada acima de 8 semanas
- Funcionalidade core tem mais de 5 etapas no fluxo de usuário
- Múltiplas hipóteses sendo testadas simultaneamente

**Ação:** Revisar priorização. Aplicar rigorosamente "MVP funciona sem isso?". Considerar dividir em múltiplos MVPs sequenciais.

### Sinais de que a hipótese está vaga:
- QUEM é descrito como "pessoas" ou "usuários"
- RESULTADO usa verbos vagos ("melhorar", "facilitar")
- DOR não é específica ou mensurável
- Você não consegue imaginar como medir validação

**Ação:** Refazer Etapa 2. Consultar documentação de pesquisas. Realizar sessão de discovery com stakeholders.

### Sinais de falta de alinhamento com stakeholders:
- Múltiplas rodadas de revisão sem convergência
- Feedback contraditório entre stakeholders
- Solicitações de funcionalidades adicionais constantes
- Resistência em documentar scope negativo

**Ação:** Facilitar workshop de alinhamento. Usar técnicas de priorização objetiva. Escalonar para decisor final se necessário.

### Sinais de falta de informação crítica:
- Muitas perguntas sem resposta após análise de documentação
- Público-alvo não está claro
- Problema não foi validado com usuários
- Não há dados de pesquisa ou entrevistas

**Ação:** Pausar processo. Executar discovery adicional (entrevistas, pesquisas). Considerar processos anteriores: ProblemHypothesisDefinition ou TargetUserIdentification.

## Glossário

**MVP (Minimum Viable Product):** Produto mínimo viável que valida hipótese com usuários reais.

**Hipótese Principal:** Suposição crítica sobre valor do produto que precisa ser testada.

**Funcionalidade Core:** Funcionalidade principal que valida a hipótese.

**Funcionalidades Secundárias:** Funcionalidades críticas para MVP funcionar mas não são o diferencial.

**Scope Negativo:** Documentação explícita do que NÃO entra no MVP.

**Métricas de Validação:** Indicadores quantitativos que determinam se hipótese foi validada.

**Stack Técnica:** Conjunto de tecnologias usadas para construir o MVP.

**Briefing de MVP:** Documento consolidado que serve como referência para todo desenvolvimento.

**Stakeholders:** Pessoas com interesse ou autoridade sobre o projeto (fundadores, investidores, líderes).

**Scope Creep:** Crescimento não controlado do escopo durante desenvolvimento.

**Early Adopters:** Primeiros usuários que testam o MVP após lançamento.

---

**Última atualização:** 2025-11-05
**Mantido por:** Framework Business Team
**Versão:** 1.0
