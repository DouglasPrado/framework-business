# KnowledgeLoader - Exemplos de Uso

Este documento demonstra as diferentes formas de usar o `KnowledgeLoader` e `StrategyKnowledgeManager` para carregar conhecimento de estratégias.

## 1. Uso Básico - StrategyKnowledgeManager (Recomendado)

Para estratégias que seguem a estrutura padrão:

```python
from framework.io.knowledge import StrategyKnowledgeManager

# Inicializar manager
manager = StrategyKnowledgeManager(
    base_path=Path("/caminho/do/repo"),
    strategy_name="ZeroUm"
)

# Carregar arquivos padrão (knowledge.MD, README.MD, etc)
knowledge = manager.load_default_knowledge()

# Usar no prompt do LLM
prompt = f"""
Você é um especialista na estratégia...

{knowledge}

CONTEXTO DO PROJETO:
...
"""
```

## 2. Arquivos Customizados - StrategyKnowledgeManager

Para carregar apenas arquivos específicos:

```python
from framework.io.knowledge import StrategyKnowledgeManager

manager = StrategyKnowledgeManager(
    base_path=Path("/caminho/do/repo"),
    strategy_name="MinhaEstrategia"
)

# Opção 1: Lista simples
knowledge = manager.load_specific_files(
    "knowledge.MD",
    "tasks.MD"
)

# Opção 2: Dicionário com títulos customizados
knowledge = manager.load_custom_knowledge({
    "knowledge.MD": "Base de Conhecimento",
    "process.MD": "Definição de Processos",
    "examples.MD": "Exemplos Práticos"
})
```

## 3. Uso Avançado - KnowledgeLoader

Para casos mais complexos com caminhos arbitrários:

```python
from framework.io.knowledge import KnowledgeLoader
from pathlib import Path

# Carregar de um diretório específico
loader = KnowledgeLoader(base_path=Path("/caminho/base"))

# Carregar arquivo único
content = loader.load_file("subdir/arquivo.MD", title="Meu Arquivo")

# Carregar múltiplos arquivos
knowledge = loader.load_files({
    "doc1.MD": "Documentação 1",
    "doc2.MD": "Documentação 2",
    "subdir/doc3.MD": "Documentação 3"
})
```

## 4. Caminhos Absolutos - Método Estático

Quando você tem caminhos completos:

```python
from framework.io.knowledge import KnowledgeLoader
from pathlib import Path

# Carregar arquivos com caminhos absolutos
knowledge = KnowledgeLoader.load_from_paths(
    files=[
        Path("/caminho/completo/knowledge.MD"),
        Path("/outro/caminho/process.MD")
    ],
    titles=["Conhecimento", "Processos"]
)
```

## 5. Integração em Orquestradores

Exemplo completo de como usar em um orquestrador:

```python
from pathlib import Path
from typing import Dict, Any
from framework.io.knowledge import StrategyKnowledgeManager
from framework.core.context import AgentContext
from framework.llm.factory import build_llm

class MeuOrchestrator:

    def __init__(self, context_name: str, context_description: str):
        repo_root = Path(__file__).resolve().parents[3]

        self.context = AgentContext(
            context_name=context_name,
            context_description=context_description,
            strategy_name="MinhaEstrategia",
            base_path=repo_root
        )

        # Inicializar knowledge manager
        self.knowledge_manager = StrategyKnowledgeManager(
            base_path=repo_root,
            strategy_name="MinhaEstrategia"
        )

    def _analyze_context(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa contexto com conhecimento da estratégia."""

        # Carregar conhecimento
        knowledge = self.knowledge_manager.load_default_knowledge()

        # Criar prompt com conhecimento
        prompt = f"""
        Você é um especialista...

        {knowledge}

        CONTEXTO DO PROJETO:
        - Nome: {self.context.context_name}
        - Descrição: {self.context.context_description}

        Sua tarefa: ...
        """

        # Invocar LLM
        llm = build_llm()
        response = llm.invoke(prompt)

        return state
```

## 6. Carregar Conhecimento de Múltiplas Estratégias

Para combinar conhecimento de diferentes estratégias:

```python
from framework.io.knowledge import StrategyKnowledgeManager
from pathlib import Path

base_path = Path("/caminho/do/repo")

# Carregar de ZeroUm
manager_zeroum = StrategyKnowledgeManager(base_path, "ZeroUm")
knowledge_zeroum = manager_zeroum.load_specific_files("knowledge.MD")

# Carregar de outra estratégia
manager_generic = StrategyKnowledgeManager(base_path, "Generic")
knowledge_generic = manager_generic.load_specific_files("knowledge.MD")

# Combinar
combined_knowledge = f"""
# CONHECIMENTO COMBINADO

## Da Estratégia ZeroUm
{knowledge_zeroum}

## Da Estratégia Generic
{knowledge_generic}
"""
```

## 7. Tratamento de Erros

O KnowledgeLoader lida graciosamente com arquivos ausentes:

```python
from framework.io.knowledge import StrategyKnowledgeManager

manager = StrategyKnowledgeManager(base_path, "MinhaEstrategia")

# Arquivos ausentes geram apenas warnings no log, não exceptions
knowledge = manager.load_custom_knowledge({
    "existente.MD": "Arquivo que existe",
    "nao_existe.MD": "Arquivo que não existe"  # Warning no log
})

# knowledge conterá apenas o conteúdo de "existente.MD"
```

## 8. Customização Completa

Exemplo de uso totalmente customizado:

```python
from framework.io.knowledge import KnowledgeLoader
from pathlib import Path

# Criar loader para diretório customizado
loader = KnowledgeLoader(
    base_path=Path("/caminho/custom/docs")
)

# Carregar com estrutura própria
knowledge = loader.load_files({
    "intro/overview.md": "Visão Geral",
    "concepts/core.md": "Conceitos Fundamentais",
    "guides/quickstart.md": "Início Rápido",
    "api/reference.md": "Referência da API"
})

# Usar no seu sistema
print(knowledge)
```

## 9. Formato do Output

O conhecimento é retornado formatado assim:

```markdown
# CONHECIMENTO DA ESTRATÉGIA

## Base de Conhecimento (knowledge.MD)

[Conteúdo do arquivo knowledge.MD]

================================================================================

## Análise de Processos (process-analysis.md)

[Conteúdo do arquivo process-analysis.md]

================================================================================

...
```

## Observações

1. **Logs Automáticos**: Todos os carregamentos são logados automaticamente
2. **Encoding UTF-8**: Todos os arquivos são lidos com UTF-8
3. **Paths Relativos**: Paths podem ser relativos ao `base_path`
4. **Paths Absolutos**: Paths absolutos também são suportados
5. **Graceful Degradation**: Arquivos ausentes geram warnings, não erros
6. **Títulos Opcionais**: Se não fornecer título, usa o nome do arquivo

## Estrutura Padrão de Conhecimento

A estrutura padrão esperada é:

```
strategies/
└── NomeDaEstrategia/
    ├── knowledge.MD          # Base de conhecimento
    ├── process-analysis.md   # Análise de processos
    ├── README.MD             # Visão geral
    └── tasks.MD              # Checklist operacional
```

Mas você pode usar qualquer estrutura customizada com os métodos apropriados.
