# Artefatos Compartilhados - _SHARED

## Propósito

Esta pasta contém artefatos, templates e referências que são utilizados por **múltiplos processos** dentro do framework. O objetivo é:

1. **Evitar duplicação**: Não repetir o mesmo template ou artefato em vários processos
2. **Manter consistência**: Garantir que todos os processos usem a mesma versão de templates críticos
3. **Facilitar manutenção**: Atualizar um template compartilhado atualiza todos os processos que o utilizam
4. **Promover reutilização**: Incentivar uso de artefatos já validados e testados

## Estrutura

```
_SHARED/
├── README.MD (este arquivo)
├── templates/
│   └── [Templates compartilhados entre processos]
└── references/
    └── [Materiais de referência comuns]
```

## Quando Usar Artefatos Compartilhados

### Use artefatos de _SHARED quando:
- O template é usado por 2 ou mais processos
- O artefato representa uma prática padrão do framework
- A consistência entre processos é crítica
- O template pode ser útil para futuros processos

### Mantenha no processo local (_DATA/) quando:
- O artefato é específico de um único processo
- Customizações são necessárias para contexto específico
- O template é experimental ou em validação

## Templates Disponíveis

### 1. Declaração de Hipótese
**Arquivo**: `templates/declaracao-hipotese.md`
**Usado por**:
- [ProblemHypothesisDefinition](../ProblemHypothesisDefinition/process.MD)
- [TargetUserIdentification](../TargetUserIdentification/process.MD)

**Descrição**: Template padrão para criar declarações de hipótese no formato "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]" com validação rápida e completa.

## Referências Disponíveis

(Seção a ser expandida conforme novos materiais de referência forem adicionados)

## Como Adicionar Novos Artefatos Compartilhados

### Critérios para tornar um artefato compartilhado:

1. **Usado por 2+ processos**: Identifique duplicação entre processos existentes
2. **Generalização possível**: O template pode ser usado sem customização pesada
3. **Valor para futuros processos**: Outros processos poderiam se beneficiar deste artefato
4. **Mantém qualidade**: Não perde qualidade ao ser generalizado

### Processo para adicionar:

1. Identifique o artefato duplicado nos processos
2. Crie versão generalizada em `_SHARED/templates/` ou `_SHARED/references/`
3. Documente no README.MD (este arquivo) qual template e quem usa
4. Atualize os processos que usam o artefato para referenciar `_SHARED/`
5. Remova versões duplicadas dos `_DATA/` locais (opcional, mas recomendado)

### Convenções de nomenclatura:

- Use nomes descritivos em kebab-case: `declaracao-hipotese.md`
- Prefira português para conteúdo interno
- Inclua cabeçalho indicando que é artefato compartilhado
- Liste processos que utilizam no topo do arquivo

## Como Referenciar Artefatos Compartilhados

### Em process.MD:
```markdown
Use o template compartilhado: [Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md)
```

### Em tasks.MD:
```markdown
**Template**: Utilize o artefato compartilhado em `../_SHARED/templates/declaracao-hipotese.md`
```

### Em knowledge.MD:
```markdown
## Materiais de Apoio
- [Template de Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md) - Template padrão do framework
```

## Versionamento

Artefatos compartilhados devem incluir:
- Data da última atualização
- Indicação de quais processos utilizam
- Tipo: "Artefato Compartilhado"

## Governança

### Quem pode modificar artefatos compartilhados?
- Product Owners
- Process Managers
- Equipe de governança do framework

### Processo de atualização:
1. Propor mudança documentando impacto
2. Revisar com processos que utilizam o artefato
3. Atualizar artefato compartilhado
4. Validar que processos dependentes continuam funcionando
5. Documentar mudança e data de atualização

### Backward compatibility:
- Evite quebrar compatibilidade com processos existentes
- Se mudança for breaking, considere criar nova versão do template
- Notifique owners dos processos afetados antes de mudanças significativas

## Princípios

1. **DRY (Don't Repeat Yourself)**: Não duplique artefatos desnecessariamente
2. **Single Source of Truth**: Um template, múltiplos usos
3. **Evolução gradual**: Adicione artefatos compartilhados conforme identificar duplicação
4. **Documentação clara**: Sempre documente quem usa e para quê
5. **Referência, não cópia**: Processos devem referenciar `_SHARED/`, não copiar

## Exemplos de Uso

### Exemplo 1: Processo novo precisa de declaração de hipótese
❌ **Errado**: Criar novo template em `MeuProcesso/_DATA/template-hipotese.md`
✅ **Correto**: Referenciar `../_SHARED/templates/declaracao-hipotese.md`

### Exemplo 2: Template precisa de customização específica
✅ **Correto**:
1. Referenciar template base de `_SHARED/`
2. Criar versão customizada em `_DATA/` se necessário
3. Documentar em `knowledge.MD` que usa template compartilhado como base

### Exemplo 3: Identificou template usado por 3 processos
✅ **Correto**:
1. Criar versão compartilhada em `_SHARED/templates/`
2. Atualizar os 3 processos para referenciar versão compartilhada
3. Documentar neste README.MD

## Manutenção

Este README.MD deve ser atualizado sempre que:
- Novo artefato compartilhado é adicionado
- Novo processo começa a usar artefato existente
- Artefato compartilhado é removido ou substituído
- Estrutura da pasta `_SHARED/` muda

---

**Última atualização**: 2025-10-31
**Mantido por**: Framework Business Team
**Versão**: 1.0
