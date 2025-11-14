# Subagentes ZeroUm

Este diretório contém os subagentes da estratégia ZeroUm, todos usando **BaseAgent do framework** com suporte a carregamento automático de conhecimento dos processos.

## 📚 Arquitetura

Todos os subagentes herdam **diretamente** de `framework.agents.BaseAgent`:

```
framework.agents.BaseAgent (genérico e reutilizável)
├── ProblemHypothesisExpressAgent
├── ProblemHypothesisDefinitionAgent
├── TargetUserIdentificationAgent
├── UserInterviewValidationAgent
├── LandingPageCreationAgent
├── CheckoutSetupAgent
└── ClientDeliveryAgent
```

### Recursos Herdados de BaseAgent

Todos os subagentes têm acesso a:

✅ **Carregamento automático de conhecimento** do processo
✅ **LLM pré-configurado** com monitoramento automático
✅ **Ferramentas do framework** automaticamente disponíveis
✅ **Métodos helpers** para gerenciamento de arquivos e prompts

## 🚀 Início Rápido

### Criar Novo Subagente ZeroUm

```python
from pathlib import Path
from framework.agents import BaseAgent

class MeuNovoSubagente(BaseAgent):
    """Descrição do meu subagente."""

    # Definir processo e estratégia
    process_name = "XX-MeuProcesso"  # Nome da pasta em process/ZeroUm/
    strategy_name = "ZeroUm"

    def __init__(self, workspace_root: Path, **kwargs):
        # Inicializar BaseAgent (LLM, tools, conhecimento)
        super().__init__(
            workspace_root=workspace_root,
            enable_tools=True,
            load_knowledge=True
        )

        # Seus atributos específicos de negócio
        self.meu_param = kwargs.get('meu_param')

    def execute(self):
        """Executa o subagente."""

        # Usar LLM com conhecimento automático
        result = self.invoke_llm("""
            Sua tarefa aqui...

            Siga as melhores práticas do processo.
        """, enhance_with_knowledge=True)

        return result
```

### Como Funciona

1. **Definir `process_name`**: Nome da pasta do processo (ex: "05-CheckoutSetup")
2. **Chamar `super().__init__()`**: Carrega conhecimento automaticamente
3. **Usar `invoke_llm()`**: Prompts são enriquecidos com conhecimento do processo

## 📖 Conhecimento Disponível

Quando você define `process_name`, o sistema carrega automaticamente:

```
process/ZeroUm/<process_name>/
├── knowledge.MD    → Base de conhecimento do processo
├── process.MD      → Definição detalhada do processo
├── tasks.MD        → Checklist operacional
├── validator.MD    → Critérios de validação
└── README.MD       → Visão geral
```

Todo esse conteúdo fica disponível em `self.process_knowledge`.

## 🛠️ Métodos Disponíveis

### invoke_llm()

Invoca o LLM com prompt enriquecido automaticamente:

```python
# Com conhecimento (padrão recomendado)
result = self.invoke_llm(
    "Configure checkout...",
    enhance_with_knowledge=True  # Adiciona conhecimento ao prompt
)

# Sem conhecimento (para prompts específicos)
result = self.invoke_llm(
    "Resuma em uma frase...",
    enhance_with_knowledge=False
)
```

### get_enhanced_prompt()

Enriquece um prompt manualmente:

```python
base_prompt = "Sua tarefa: configurar gateway"
enhanced = self.get_enhanced_prompt(base_prompt)

# enhanced agora tem o conhecimento + base_prompt
response = self.llm.invoke(enhanced)
```

### process_knowledge (property)

Acessa o conhecimento carregado diretamente:

```python
if self.process_knowledge:
    print(f"Conhecimento: {len(self.process_knowledge)} caracteres")

    # Salvar para debug
    debug_file = self.data_dir / "knowledge.txt"
    debug_file.write_text(self.process_knowledge)
```

## 📂 Estrutura de Arquivos

```
business/strategies/zeroum/subagents/
├── base.py                      # Classe base com conhecimento
├── example_with_knowledge.py    # Exemplo completo de uso
├── MIGRATION_GUIDE.md           # Guia de migração de subagentes existentes
├── README.md                    # Este arquivo
├── registry.py                  # Registro de subagentes
├── template_filler.py           # Preenchimento de templates
│
├── checkout_setup.py            # Subagentes existentes
├── landing_page_creation.py
├── problem_hypothesis_definition.py
├── target_user_identification.py
├── user_interview_validation.py
└── problem_hypothesis_express.py
```

## 📝 Exemplos Práticos

### Exemplo 1: Subagente Simples

```python
class CheckoutSetupAgent(SubagentBase):
    process_name = "05-CheckoutSetup"
    strategy_name = "ZeroUm"

    def __init__(self, workspace_root: Path, gateway: str):
        super().__init__(workspace_root=workspace_root)
        self.gateway = gateway

    def configure(self):
        return self.invoke_llm(f"""
            Configure checkout para gateway: {self.gateway}

            Use as melhores práticas do processo.
        """, enhance_with_knowledge=True)
```

### Exemplo 2: Sem Conhecimento Automático

Se seu subagente não tem processo correspondente:

```python
class UtilityAgent(SubagentBase):
    process_name = ""  # Vazio = sem processo

    def __init__(self, workspace_root: Path):
        super().__init__(
            workspace_root=workspace_root,
            load_knowledge=False  # Desabilitar carregamento
        )
```

### Exemplo 3: Conhecimento Customizado

Carregar apenas arquivos específicos:

```python
from framework.io.knowledge import ProcessKnowledgeManager

class CustomAgent(SubagentBase):
    process_name = "05-CheckoutSetup"

    def __init__(self, workspace_root: Path):
        super().__init__(
            workspace_root=workspace_root,
            load_knowledge=False  # Desabilitar carregamento padrão
        )

        # Carregar manualmente
        manager = ProcessKnowledgeManager(
            base_path=self.workspace_root.parents[1],
            strategy_name="ZeroUm",
            process_name=self.process_name
        )

        # Apenas alguns arquivos
        self._process_knowledge = manager.load_specific_files(
            "knowledge.MD",
            "validator.MD"
        )
```

## 🔄 Migrando Subagentes Existentes

Para migrar subagentes que já existem para usar `SubagentBase`:

1. **Ler o guia**: [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
2. **Ver exemplo**: [example_with_knowledge.py](example_with_knowledge.py)
3. **Testar**: Executar e verificar logs de carregamento

### Checklist Rápida

- [ ] Importar `SubagentBase`
- [ ] Definir `process_name` e `strategy_name`
- [ ] Atualizar `__init__` para chamar `super().__init__()`
- [ ] Remover `self.llm = build_llm()`
- [ ] Remover `self.tools = get_tools(...)`
- [ ] Substituir `self.llm.invoke()` por `self.invoke_llm()`
- [ ] Testar execução e verificar logs

## 📊 Logs de Conhecimento

Quando um subagente carrega conhecimento, você verá nos logs:

```
INFO | framework.io.knowledge | Carregado conhecimento de knowledge.MD
INFO | framework.io.knowledge | Carregado conhecimento de process.MD
INFO | framework.io.knowledge | Carregado conhecimento de tasks.MD
INFO | framework.io.knowledge | Carregado conhecimento de validator.MD
INFO | framework.io.knowledge | Carregado conhecimento de README.MD
INFO | business.strategies.zeroum.subagents.checkout_setup | Conhecimento do processo 05-CheckoutSetup carregado com sucesso
```

## 🔗 Recursos Relacionados

### Framework
- [framework/io/knowledge.py](../../../framework/io/knowledge.py) - Implementação do carregador
- [framework/io/KNOWLEDGE_EXAMPLES.md](../../../framework/io/KNOWLEDGE_EXAMPLES.md) - Exemplos de uso

### Documentação
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Guia de migração completo
- [example_with_knowledge.py](example_with_knowledge.py) - Exemplo executável

### Processos
- [process/ZeroUm/](../../../process/ZeroUm/) - Processos disponíveis

## ❓ FAQ

### P: Todo subagente precisa herdar de SubagentBase?

**R:** Não! É opcional. Use se quiser carregamento automático de conhecimento. Subagentes existentes continuam funcionando normalmente.

### P: O que acontece se o processo não existir?

**R:** O sistema gera um warning no log mas não falha. `self.process_knowledge` ficará vazio.

### P: Posso desabilitar o carregamento de conhecimento?

**R:** Sim! Passe `load_knowledge=False` no `super().__init__()` ou deixe `process_name = ""`.

### P: Como verificar se o conhecimento foi carregado?

**R:** Verifique os logs ou use `if self.process_knowledge:` no código.

### P: O conhecimento deixa o prompt muito grande?

**R:** Use `enhance_with_knowledge=False` em prompts específicos. Ou carregue apenas arquivos específicos com `ProcessKnowledgeManager`.

## 🚀 Próximos Passos

1. **Leia**: [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
2. **Veja**: [example_with_knowledge.py](example_with_knowledge.py)
3. **Teste**: Crie um subagente simples herdando de `SubagentBase`
4. **Migre**: Adapte subagentes existentes (opcional)

## 📞 Suporte

Para dúvidas sobre o sistema de conhecimento:
- Ver exemplos em [framework/io/KNOWLEDGE_EXAMPLES.md](../../../framework/io/KNOWLEDGE_EXAMPLES.md)
- Consultar código em [base.py](base.py)
- Verificar implementação em [framework/io/knowledge.py](../../../framework/io/knowledge.py)
