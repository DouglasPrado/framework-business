# Framework Agents

Classes base genéricas e reutilizáveis para criação de agentes e subagentes.

## 📋 Visão Geral

Este módulo fornece a classe `BaseAgent`, que oferece funcionalidade comum para todos os agentes do framework:

- ✅ Carregamento automático de conhecimento do processo
- ✅ LLM pré-configurado com monitoramento automático
- ✅ Integração com sistema de ferramentas
- ✅ Utilitários para gerenciamento de arquivos e diretórios
- ✅ Métodos helpers para prompts e documentos

## 🚀 Uso Básico

### Criar um Agente Simples

```python
from framework.agents import BaseAgent
from pathlib import Path

class MyAnalysisAgent(BaseAgent):
    process_name = "01-DataAnalysis"
    strategy_name = "DataScience"

# Instanciar
agent = MyAnalysisAgent(
    workspace_root=Path("drive/MyProject")
)

# Usar
agent.setup_directories(["outputs", "charts"])
result = agent.invoke_llm("Analyze this dataset...")
agent.save_document("analysis.MD", result)
```

### Herdar em Estratégias Específicas

```python
from framework.agents import BaseAgent
from framework.tools import AgentType

class ZeroUmSubagent(BaseAgent):
    """Base para todos os subagentes da estratégia ZeroUm."""

    strategy_name: str = "ZeroUm"

    def __init__(self, workspace_root, **kwargs):
        super().__init__(
            workspace_root=workspace_root,
            strategy_name=self.strategy_name,
            agent_type=AgentType.PROCESS,
            **kwargs
        )

# Depois, subagentes específicos herdam de ZeroUmSubagent
class ProblemHypothesisAgent(ZeroUmSubagent):
    process_name = "00-ProblemHypothesisExpress"

    def execute(self):
        # Conhecimento já carregado automaticamente
        prompt = self.get_enhanced_prompt("""
            Crie uma declaração de hipótese para o problema.
        """)

        result = self.invoke_llm(prompt)
        self.save_document("01-hipotese.MD", result)
```

## 🎯 Funcionalidades Principais

### 1. Carregamento Automático de Conhecimento

O `BaseAgent` carrega automaticamente conhecimento do processo de:
- `process/<strategy>/<process>/process.MD`
- `process/<strategy>/<process>/knowledge.MD`
- `process/<strategy>/<process>/tasks.MD`
- `process/<strategy>/<process>/validator.MD`

```python
agent = MyAgent(
    workspace_root=Path("drive/Project"),
    load_knowledge=True  # padrão
)

# Acesso ao conhecimento carregado
knowledge = agent.process_knowledge
print(knowledge)  # Conteúdo consolidado de todos os arquivos .MD
```

### 2. LLM com Monitoramento Automático

```python
# LLM já vem configurado com monitoramento
response = agent.invoke_llm("Analyze this...")

# Ou usar diretamente
response = agent.llm.invoke("Custom prompt...")

# Customizar configuração do LLM
agent = MyAgent(
    workspace_root=Path("drive/Project"),
    llm_config={
        "model": "gpt-4",
        "temperature": 0.8,
        "max_tokens": 4000
    }
)
```

### 3. Enriquecimento Automático de Prompts

```python
# Prompt básico
base_prompt = """
Analise os seguintes dados:
- Receita: $100k
- Despesas: $80k
"""

# Enriquecer com conhecimento do processo
enhanced = agent.get_enhanced_prompt(base_prompt)

# O prompt agora contém:
# 1. Todo o conhecimento do processo
# 2. Separador visual
# 3. O prompt original
```

### 4. Gerenciamento de Diretórios

```python
# Criar estrutura de diretórios
agent.setup_directories([
    "outputs",
    "assets",
    "charts",
    "reports"
])

# Estrutura criada:
# drive/Project/01-MyProcess/
# drive/Project/01-MyProcess/_DATA/
# drive/Project/01-MyProcess/_DATA/outputs/
# drive/Project/01-MyProcess/_DATA/assets/
# drive/Project/01-MyProcess/_DATA/charts/
# drive/Project/01-MyProcess/_DATA/reports/
```

### 5. Salvar e Ler Documentos

```python
# Salvar na raiz do processo
path = agent.save_document(
    "01-resultado.MD",
    "# Análise Completa\n\n..."
)
# Salvo em: drive/Project/01-MyProcess/01-resultado.MD

# Salvar em _DATA
path = agent.save_document(
    "raw_data.json",
    json.dumps(data),
    in_data_dir=True
)
# Salvo em: drive/Project/01-MyProcess/_DATA/raw_data.json

# Ler documento
content = agent.read_document(path)
```

### 6. Helpers Úteis

```python
# Formatar lista para prompts
items = ["feature1", "feature2", "feature3"]
formatted = agent.format_list(items)
# "feature1, feature2, feature3"

formatted = agent.format_list(items, separator="\n- ")
# "feature1
# - feature2
# - feature3"
```

## 🔧 Configuração Avançada

### Tipos de Agente (Permissões)

```python
from framework.tools import AgentType

# PROCESS: Apenas leitura/escrita de arquivos
agent = BaseAgent(
    workspace_root=Path("drive/Project"),
    agent_type=AgentType.PROCESS
)

# STRATEGY: + comandos git básicos
agent = BaseAgent(
    workspace_root=Path("drive/Project"),
    agent_type=AgentType.STRATEGY
)

# ORCHESTRATOR: + comandos git avançados
agent = BaseAgent(
    workspace_root=Path("drive/Project"),
    agent_type=AgentType.ORCHESTRATOR
)

# AUTONOMOUS: Todas as ferramentas
agent = BaseAgent(
    workspace_root=Path("drive/Project"),
    agent_type=AgentType.AUTONOMOUS
)
```

### Desabilitar Funcionalidades

```python
# Sem ferramentas
agent = BaseAgent(
    workspace_root=Path("drive/Project"),
    enable_tools=False
)
# agent.tools == []

# Sem carregamento de conhecimento
agent = BaseAgent(
    workspace_root=Path("drive/Project"),
    load_knowledge=False
)
# agent.process_knowledge == ""
```

### Sobrescrever Nomes Dinamicamente

```python
# Nomes definidos na classe
class MyAgent(BaseAgent):
    process_name = "01-Default"
    strategy_name = "DefaultStrategy"

# Sobrescrever na instância
agent = MyAgent(
    workspace_root=Path("drive/Project"),
    process_name="02-Custom",
    strategy_name="CustomStrategy"
)

print(agent.process_name)  # "02-Custom"
print(agent.strategy_name)  # "CustomStrategy"
```

## 📐 Arquitetura

### Hierarquia de Classes

```
BaseAgent (framework/agents/base.py)
├── Genérico e reutilizável
├── Sem dependência de estratégia específica
└── Fornece funcionalidade comum

    └── SubagentBase (business/strategies/zeroum/subagents/base.py)
        ├── Herda de BaseAgent
        ├── Configura strategy_name = "ZeroUm"
        └── Simplifica uso em subagentes ZeroUm

            └── ProblemHypothesisAgent, CheckoutSetupAgent, etc.
                ├── Herdam de SubagentBase
                ├── Definem process_name específico
                └── Implementam lógica de negócio
```

### Separação Framework vs Business

```
framework/agents/
└── base.py          # BaseAgent genérico (75% framework)
    ├── Sem conhecimento de negócio
    ├── Reutilizável para qualquer estratégia
    └── Mantido no framework/

business/strategies/zeroum/subagents/
└── base.py          # SubagentBase específico (25% business)
    ├── Herda de BaseAgent
    ├── Configura strategy_name = "ZeroUm"
    └── Mantido em business/
```

## 🔍 Exemplos Completos

### Exemplo 1: Agente de Análise de Dados

```python
from framework.agents import BaseAgent
from pathlib import Path
import json

class DataAnalysisAgent(BaseAgent):
    process_name = "01-DataAnalysis"
    strategy_name = "DataScience"

    def analyze_dataset(self, data: dict) -> str:
        """Analisa um dataset e retorna insights."""

        # Salvar dados brutos
        self.setup_directories(["raw", "processed"])
        raw_path = self.data_dir / "raw" / "input.json"
        raw_path.write_text(json.dumps(data, indent=2))

        # Criar prompt com conhecimento do processo
        prompt = f"""
        Analise o seguinte dataset:

        {json.dumps(data, indent=2)}

        Forneça:
        1. Estatísticas descritivas
        2. Insights principais
        3. Recomendações
        """

        # Invocar LLM (conhecimento adicionado automaticamente)
        analysis = self.invoke_llm(prompt, enhance_with_knowledge=True)

        # Salvar resultado
        self.save_document("01-analise.MD", analysis)

        return analysis

# Usar
agent = DataAnalysisAgent(workspace_root=Path("drive/MyProject"))
result = agent.analyze_dataset({
    "revenue": [100, 120, 150],
    "expenses": [80, 90, 100]
})
```

### Exemplo 2: Agente Validador

```python
from framework.agents import BaseAgent
from pathlib import Path
from typing import List, Dict

class ValidationAgent(BaseAgent):
    process_name = "02-Validation"
    strategy_name = "QualityAssurance"

    def validate_documents(self, doc_paths: List[Path]) -> Dict[str, bool]:
        """Valida múltiplos documentos."""

        results = {}

        for doc_path in doc_paths:
            # Ler documento
            content = self.read_document(doc_path)

            # Criar prompt de validação
            prompt = f"""
            Valide o seguinte documento:

            {content}

            Critérios:
            - Estrutura correta
            - Conteúdo completo
            - Formatação adequada

            Responda APENAS "VÁLIDO" ou "INVÁLIDO" seguido de justificativa.
            """

            # Invocar LLM
            response = self.invoke_llm(prompt)

            # Processar resposta
            is_valid = response.startswith("VÁLIDO")
            results[str(doc_path)] = is_valid

            # Salvar relatório
            report = f"# Validação: {doc_path.name}\n\n{response}\n"
            self.save_document(
                f"validation_{doc_path.stem}.MD",
                report,
                in_data_dir=True
            )

        # Consolidar resultados
        summary = self._generate_summary(results)
        self.save_document("00-validation-summary.MD", summary)

        return results

    def _generate_summary(self, results: Dict[str, bool]) -> str:
        """Gera resumo de validações."""
        valid = sum(1 for v in results.values() if v)
        total = len(results)

        summary = f"""# Resumo de Validações

Total de documentos: {total}
Válidos: {valid}
Inválidos: {total - valid}

## Detalhes

"""
        for doc, is_valid in results.items():
            status = "✓ VÁLIDO" if is_valid else "✗ INVÁLIDO"
            summary += f"- {status}: {doc}\n"

        return summary

# Usar
agent = ValidationAgent(workspace_root=Path("drive/QA"))
docs = [
    Path("drive/QA/doc1.MD"),
    Path("drive/QA/doc2.MD")
]
results = agent.validate_documents(docs)
```

## 🎓 Boas Práticas

1. **Use herança para estratégias específicas**:
   ```python
   # Bom: Criar classe base para estratégia
   class MyStrategyAgent(BaseAgent):
       strategy_name = "MyStrategy"

   # Depois herdar para subagentes específicos
   class ProcessAgent(MyStrategyAgent):
       process_name = "01-Process"
   ```

2. **Sempre defina process_name e strategy_name**:
   ```python
   # Bom
   class MyAgent(BaseAgent):
       process_name = "01-Analysis"
       strategy_name = "DataScience"

   # Ruim (nomes vazios)
   class MyAgent(BaseAgent):
       pass  # Sem definição
   ```

3. **Use invoke_llm para prompts automáticos**:
   ```python
   # Bom: Conhecimento adicionado automaticamente
   result = agent.invoke_llm("Analyze...")

   # Também funciona: Controle manual
   enhanced = agent.get_enhanced_prompt("Analyze...")
   result = agent.llm.invoke(enhanced)
   ```

4. **Estruture diretórios no início**:
   ```python
   def __init__(self, workspace_root, **kwargs):
       super().__init__(workspace_root, **kwargs)
       self.setup_directories(["outputs", "temp"])
   ```

5. **Separe lógica de negócio de infraestrutura**:
   ```python
   # BaseAgent: infraestrutura (framework/)
   # MyStrategyAgent: configuração da estratégia (business/)
   # ProcessAgent: lógica de negócio (business/)
   ```

## 📝 Licença

Este módulo é parte do Framework Business.
