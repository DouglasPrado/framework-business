# Template de Declaração de Hipótese de Problema

## Propósito

Este template é um artefato compartilhado usado por múltiplos processos para criar declarações claras de hipóteses de problema ou solução. Use este template sempre que precisar articular uma proposta de valor em formato testável.

## Processos que utilizam este artefato

- [ProblemHypothesisDefinition](../../ProblemHypothesisDefinition/process.MD) - Processo completo e rigoroso
- [TargetUserIdentification](../../TargetUserIdentification/process.MD) - Versão rápida para iniciar pesquisa de usuários

## Formato Padrão

```
Meu produto ajuda [QUEM] a alcançar [RESULTADO] sem [DOR].
```

### Componentes

**[QUEM]** - Usuário-alvo ou beneficiário
- Seja específico (não "empresas", mas "fundadores de startups B2B em estágio seed")
- Use profissão, contexto ou característica definidora
- Deve ser possível encontrar 10+ pessoas que correspondam

**[RESULTADO]** - Objetivo ou resultado desejado
- Foque no objetivo final, não na solução
- Deve ser mensurável ou verificável
- Algo que o usuário ativamente deseja alcançar

**[DOR]** - Principal obstáculo ou dor
- O que impede o usuário de alcançar o resultado hoje
- Deve ser significativo o suficiente para motivar ação
- Mencione custo (tempo, dinheiro, esforço, frustração)

## Variações do Template

### Variação 1 - Eliminação
```
Meu produto permite que [QUEM] consiga [RESULTADO] eliminando [DOR].
```

### Variação 2 - Direto
```
[QUEM] agora pode [RESULTADO] sem precisar [DOR].
```

### Variação 3 - Capacitação
```
Meu produto capacita [QUEM] a [RESULTADO] evitando [DOR].
```

## Checklist Rápido (15 minutos)

Use este checklist para validação básica:

- [ ] Frase tem uma linha e é clara
- [ ] Menciona explicitamente QUEM, RESULTADO e DOR
- [ ] Não menciona funcionalidades técnicas ou solução
- [ ] Foca no resultado gerado, não no produto
- [ ] Pode ser compreendida em 10 segundos
- [ ] Testada com pelo menos 1 pessoa do público-alvo
- [ ] Livre de jargões técnicos

## Validação Completa (45-60 minutos)

Para validação rigorosa com 5 critérios de qualidade, execute o processo completo:
[ProblemHypothesisDefinition](../../ProblemHypothesisDefinition/process.MD)

### Critérios de Qualidade (Validação Rigorosa)

1. **Específica**: Consegue identificar pessoas reais que correspondem ao QUEM?
2. **Valiosa**: O RESULTADO é algo que usuários ativamente desejariam?
3. **Dolorosa**: A DOR é significativa o suficiente para impulsionar ação?
4. **Testável**: Consegue validar através de conversas com usuários?
5. **Focada**: Aborda um problema claro, não múltiplos?

Meta: Passar em pelo menos 4 dos 5 critérios

## Exemplos

### Exemplo 1 - SaaS B2B
```
Meu produto ajuda fundadores de startups B2B SaaS em estágio inicial a validar
demanda real para suas ideias sem desperdiçar 3-6 meses construindo funcionalidades
que usuários não querem.
```

**QUEM**: Fundadores de startups B2B SaaS em estágio inicial
**RESULTADO**: Validar demanda real para suas ideias
**DOR**: Desperdiçar 3-6 meses construindo funcionalidades erradas

### Exemplo 2 - Freelancers
```
Meu produto ajuda designers freelancers a conseguir mais projetos de clientes
sem gastar horas em prospecção fria.
```

**QUEM**: Designers freelancers
**RESULTADO**: Conseguir mais projetos de clientes
**DOR**: Gastar horas em prospecção fria

### Exemplo 3 - Serviço Local
```
Meu produto ajuda cabeleireiros a gerenciar agendamentos de forma organizada
sem depender de mensagens de WhatsApp bagunçadas.
```

**QUEM**: Cabeleireiros
**RESULTADO**: Gerenciar agendamentos de forma organizada
**DOR**: Depender de mensagens de WhatsApp bagunçadas

## Antipadrões (Evite)

### ❌ Muito vago
"Meu produto ajuda empresas a crescer mais rápido"
- QUEM é genérico demais
- RESULTADO não é específico
- Sem DOR mencionada

### ❌ Focado em solução
"Meu produto ajuda profissionais de marketing fornecendo uma ferramenta de conteúdo com IA"
- Menciona a solução (ferramenta com IA), não o resultado
- Não deixa claro que dor está sendo resolvida

### ❌ Múltiplos problemas
"Meu produto ajuda designers a economizar tempo, colaborar melhor e gerenciar projetos com eficiência"
- Tenta resolver 3 problemas diferentes
- Falta foco

### ❌ Com jargão
"Meu produto aproveita IA para revolucionar o paradigma de soluções empresariais"
- Usa palavras da moda e jargão
- Não é claro o que realmente faz

## Quando Usar Cada Abordagem

### Use a Versão Rápida (15 min) quando:
- Você já tem clareza razoável sobre o problema
- Precisa iniciar pesquisa de usuários rapidamente
- Está em fase exploratória inicial
- Vai refinar depois com feedback real

### Use a Validação Completa (45-60 min) quando:
- Está definindo fundação estratégica do produto
- Precisa de hipótese rigorosa para validação
- Vai usar a hipótese para alinhar equipe ou investidores
- Quer garantir que todos os 3 componentes estão bem definidos

## Próximos Passos

Após criar sua declaração de hipótese:

1. **Se usou versão rápida**: Documente em arquivo de texto e prossiga para pesquisa de usuários
2. **Se usou validação completa**: Execute processo de [Identificação de Usuários-Alvo](../../TargetUserIdentification/process.MD)
3. **Sempre**: Teste a hipótese com usuários reais através de entrevistas de validação

## Armazenamento

Salve sua declaração de hipótese validada em:
- `process/[SeuProcesso]/_DATA/declaracao-hipotese.txt`

Ou se for um projeto específico:
- `projects/[NomeDoProjeto]/declaracao-hipotese.txt`

---

**Última atualização**: 2025-10-31
**Mantido por**: Framework Business
**Tipo**: Artefato Compartilhado
