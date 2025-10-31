# CLAUDE.MD - Instruções Específicas para Claude Code

## Propósito

Este documento complementa o [AGENTS.MD](AGENTS.MD) com instruções específicas para quando você (Claude Code) estiver trabalhando neste framework business. Todas as instruções do AGENTS.MD se aplicam, e este documento adiciona considerações específicas para a integração com Claude Code.

## Contexto de Execução

Você está operando dentro de um framework de processos de negócio estruturado que prioriza:
- Consistência e reutilização
- Documentação em português (pt-BR)
- Processos acionáveis e executáveis
- Templates e artefatos compartilhados

## Artefatos Compartilhados (`process/_SHARED/`)

### Princípio Central: DRY (Don't Repeat Yourself)

Antes de criar qualquer template ou artefato, **sempre verifique primeiro** se já existe uma versão compartilhada em `process/_SHARED/`.

### Fluxo de Verificação Obrigatório

Quando solicitado a criar um processo:

1. **Leia primeiro**: `process/_SHARED/README.MD`
2. **Verifique**: `process/_SHARED/templates/` para templates existentes
3. **Procure**: Templates similares em outros processos
4. **Decida**:
   - Se encontrou em `_SHARED/`: **Referencie**, não duplique
   - Se encontrou em outro processo: Considere mover para `_SHARED/`
   - Se não encontrou: Crie no `_DATA/` local, mas sinalize se pode ser útil para outros processos

### Critérios para Artefatos Compartilhados

Um artefato deve estar em `process/_SHARED/` quando:
- É usado por **2 ou mais processos**
- Representa uma **prática padrão** do framework
- A **consistência entre processos é crítica**
- Pode ser **útil para futuros processos**

### Como Referenciar Artefatos Compartilhados

#### Em process.MD:
```markdown
**Use o template compartilhado**: [Nome do Template](../_SHARED/templates/nome-template.md)
```

#### Em tasks.MD:
```markdown
**Template**: Utilize o artefato compartilhado em `../_SHARED/templates/nome-template.md`
```

#### Em knowledge.MD:
```markdown
## Materiais de Apoio
- [Nome do Template](../_SHARED/templates/nome-template.md) - Template padrão do framework
```

### Quando Criar Novo Artefato Compartilhado

Se você identificar que está criando um template que:
1. Já existe em outro processo (duplicação)
2. Poderia ser útil para múltiplos processos
3. Representa uma prática padrão

**Ação**:
1. Crie em `process/_SHARED/templates/` ou `process/_SHARED/references/`
2. Adicione entrada no `process/_SHARED/README.MD` documentando:
   - Nome do artefato
   - Processos que utilizam
   - Descrição breve do propósito
3. Atualize processos existentes para referenciar a versão compartilhada

## Estrutura de Pastas Esperada

```
framework-business/
├── AGENTS.MD (instruções gerais para todos os agentes)
├── CLAUDE.MD (este arquivo - específico para Claude Code)
├── README.MD (visão geral do sistema)
│
├── process/
│   ├── README.MD (padrões de estrutura de processo)
│   │
│   ├── _SHARED/ (artefatos compartilhados - VERIFICAR PRIMEIRO)
│   │   ├── README.MD (documentação de artefatos compartilhados)
│   │   ├── templates/ (templates usados por 2+ processos)
│   │   │   └── declaracao-hipotese.md
│   │   └── references/ (referências compartilhadas)
│   │
│   ├── ProcessoA/
│   │   ├── process.MD
│   │   ├── tasks.MD
│   │   ├── knowledge.MD
│   │   ├── validator.MD
│   │   └── _DATA/ (artefatos específicos deste processo)
│   │
│   └── ProcessoB/
│       ├── process.MD (pode referenciar _SHARED)
│       ├── tasks.MD (pode referenciar _SHARED)
│       ├── knowledge.MD
│       ├── validator.MD
│       └── _DATA/
│
├── models/ (templates base para criar novos processos)
│   └── process/
│
├── strategies/ (estratégias que usam processos)
│
└── tools/ (catálogo de ferramentas aprovadas)
```

## Workflow de Criação de Processo (Atualizado)

### Passo a Passo Obrigatório

1. **Leitura inicial**:
   ```
   - README.MD
   - process/README.MD
   - models/process/README.MD
   - process/_SHARED/README.MD ⭐ NOVO
   ```

2. **Verificação de artefatos compartilhados**:
   ```
   - Listar conteúdo de process/_SHARED/templates/
   - Identificar templates relevantes para o novo processo
   - Decidir quais artefatos reutilizar
   ```

3. **Pesquisa de processos similares**:
   ```
   - Buscar processos com escopo similar
   - Identificar padrões de tarefas
   - Verificar se há tarefas duplicadas
   ```

4. **Criação**:
   ```
   - Criar pasta process/NovoProcesso/
   - Criar pasta process/NovoProcesso/_DATA/
   - Copiar models: process.MD, tasks.MD, knowledge.MD, validator.MD
   - Customizar conteúdo
   - REFERENCIAR artefatos de _SHARED/ (não copiar)
   ```

5. **Validação**:
   ```
   - Verificar que não há duplicação desnecessária
   - Confirmar que artefatos compartilhados estão referenciados
   - Verificar consistência entre arquivos
   - Se criou template usado por 2+ processos, adicionar a _SHARED/
   ```

## Artefatos Compartilhados Existentes

### 1. Declaração de Hipótese
- **Arquivo**: `process/_SHARED/templates/declaracao-hipotese.md`
- **Usado por**:
  - ProblemHypothesisDefinition (processo completo)
  - TargetUserIdentification (versão rápida)
- **Propósito**: Template padrão para criar hipóteses no formato "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"
- **Quando usar**: Sempre que um processo precisar criar ou validar declaração de hipótese

## Checklist de Qualidade (Atualizado)

Antes de considerar qualquer trabalho completo:

- [ ] Li `process/_SHARED/README.MD` primeiro
- [ ] Verifiquei `process/_SHARED/templates/` para artefatos existentes
- [ ] Se encontrei artefato compartilhado relevante, referenciei ao invés de duplicar
- [ ] Se criei template usado por 2+ processos, adicionei a `_SHARED/` e documentei
- [ ] Atualizei `process/_SHARED/README.MD` se adicionei novo artefato compartilhado
- [ ] Todos os arquivos obrigatórios criados (process.MD, tasks.MD, knowledge.MD, validator.MD)
- [ ] Pasta `_DATA/` criada para artefatos específicos do processo
- [ ] Conteúdo em português (pt-BR)
- [ ] Sem tabelas markdown (usar listas)
- [ ] Sem emojis
- [ ] Links relativos funcionando
- [ ] Consistência entre process.MD ↔ tasks.MD ↔ validator.MD

## Cenários Comuns

### Cenário 1: "Criar processo de validação de mercado"

❌ **ERRADO**:
```
1. Criar process/MarketValidation/
2. Criar _DATA/template-hipotese.md (duplicando template)
3. Documentar processo
```

✅ **CORRETO**:
```
1. Verificar process/_SHARED/README.MD
2. Identificar que existe template-declaracao-hipotese.md
3. Criar process/MarketValidation/
4. Em process.MD, referenciar: [Template de Hipótese](../_SHARED/templates/declaracao-hipotese.md)
5. Criar apenas artefatos específicos em _DATA/
```

### Cenário 2: "Encontrei template duplicado em 2 processos"

✅ **AÇÃO CORRETA**:
```
1. Criar versão generalizada em process/_SHARED/templates/
2. Documentar em process/_SHARED/README.MD
3. Atualizar os 2 processos para referenciar _SHARED/
4. (Opcional) Remover duplicatas de _DATA/ locais
```

### Cenário 3: "Preciso customizar template compartilhado"

✅ **AÇÃO CORRETA**:
```
1. Referenciar template base de _SHARED/ no knowledge.MD
2. Criar versão customizada em _DATA/ se absolutamente necessário
3. Documentar em knowledge.MD que usa template compartilhado como base
4. Explicar razão da customização
```

## Comandos Úteis

### Verificar artefatos compartilhados existentes:
```bash
ls -la process/_SHARED/templates/
ls -la process/_SHARED/references/
```

### Procurar templates duplicados:
```bash
find process -name "*template*.md" -type f
find process -name "*checklist*.md" -type f
```

### Ver processos que referenciam _SHARED:
```bash
grep -r "_SHARED" process/*/process.MD
grep -r "_SHARED" process/*/tasks.MD
```

## Princípios de Governança

### Você DEVE:
- Sempre verificar `_SHARED/` antes de criar templates
- Referenciar artefatos compartilhados ao invés de copiar
- Documentar novos artefatos compartilhados no README
- Manter backward compatibility ao atualizar artefatos compartilhados
- Sinalizar quando identificar duplicação que pode ser consolidada

### Você NÃO DEVE:
- Copiar templates de `_SHARED/` para `_DATA/` local
- Criar templates duplicados quando versão compartilhada existe
- Modificar artefatos compartilhados sem verificar impacto
- Adicionar artefatos a `_SHARED/` que são específicos de um processo

## Exceções e Casos Especiais

### Quando é OK duplicar ao invés de compartilhar:
1. Template precisa de customização pesada e específica
2. Artefato está em experimentação e pode mudar significativamente
3. Processo é temporário ou experimental
4. Compartilhar quebraria a clareza ou usabilidade do processo

**Importante**: Mesmo nesses casos, documente no `knowledge.MD` que o template foi baseado em versão compartilhada.

## Integração com TodoWrite

Ao usar TodoWrite para planejar criação de processo, **sempre inclua**:
```
- [ ] Ler process/_SHARED/README.MD
- [ ] Verificar templates compartilhados existentes
- [ ] Identificar artefatos reutilizáveis
- [ ] Referenciar _SHARED/ ao invés de duplicar
- [ ] (Se aplicável) Adicionar novo artefato a _SHARED/
```

## Perguntas Frequentes

**P: Quando devo adicionar um artefato a `_SHARED/`?**
R: Quando for usado por 2 ou mais processos, ou quando representar uma prática padrão do framework.

**P: Posso modificar um artefato em `_SHARED/`?**
R: Sim, mas documente a mudança, atualize a data, e verifique impacto em processos que o utilizam.

**P: E se eu precisar de versão customizada de template compartilhado?**
R: Referencie o template base de `_SHARED/` no knowledge.MD e crie versão customizada em `_DATA/` local, documentando a razão.

**P: Como sei quais processos usam um artefato compartilhado?**
R: Está documentado no cabeçalho do próprio artefato e no `process/_SHARED/README.MD`.

## Conclusão

O sistema de artefatos compartilhados existe para:
- **Reduzir duplicação** de esforço e documentação
- **Aumentar consistência** entre processos
- **Facilitar manutenção** e evolução do framework
- **Acelerar criação** de novos processos

Sempre que você identificar duplicação ou oportunidade de compartilhamento, **aja proativamente** para consolidar em `_SHARED/`.

---

**Última atualização**: 2025-10-31
**Mantido por**: Framework Business Team
**Complementa**: [AGENTS.MD](AGENTS.MD)
