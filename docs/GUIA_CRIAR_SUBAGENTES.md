# Guia: Como Criar Subagentes no ZeroUm

**Data**: 2025-11-12
**Framework**: 2.0.1

---

## 📖 Índice

1. [Conceito de Subagentes](#conceito-de-subagentes)
2. [Abordagem 1: Nodes no OrchestrationGraph (Recomendado)](#abordagem-1-nodes-no-orchestrationgraph)
3. [Abordagem 2: Classes Dedicadas](#abordagem-2-classes-dedicadas)
4. [Exemplo Completo: Subagente de Validação](#exemplo-completo)
5. [Boas Práticas](#boas-práticas)

---

## Conceito de Subagentes

**Subagentes** são componentes especializados que executam tarefas específicas dentro de uma estratégia maior.

### No Framework Atual

O framework usa **Nodes** (nós) no `OrchestrationGraph` em vez de classes de subagentes:

```python
graph = OrchestrationGraph.from_handlers({
    "coletar_contexto": self._coletar_contexto,      # Node 1
    "gerar_hipotese": self._gerar_hipotese,          # Node 2
    "validar_resultado": self._validar_resultado,    # Node 3
})
```

Cada node é uma **função** que:
1. Recebe `state: Dict[str, Any]`
2. Executa uma tarefa específica
3. Retorna `state` atualizado

---

## Abordagem 1: Nodes no OrchestrationGraph

**Esta é a abordagem recomendada** - usa o framework moderno sem criar classes extras.

### Passo 1: Criar Método no Orchestrator

```python
# agents/business/strategies/zeroum/orchestrator.py

def _validar_perfis_usuarios(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Subagente: Valida os perfis de usuários-alvo.

    Args:
        state: Estado contendo hypothesis

    Returns:
        Estado com perfis validados
    """
    logger.info("Validando perfis de usuários")

    from agents.framework.llm.factory import build_llm

    # Obter hipótese do estado
    hypothesis = state.get('hypothesis', '')

    # Criar LLM
    llm = build_llm()

    # Prompt específico para validação
    prompt = f"""
    Analise os perfis de usuários na hipótese abaixo e valide se:
    1. São específicos e mensuráveis
    2. Têm canais de aquisição claros
    3. Estão priorizados corretamente

    Hipótese:
    {hypothesis}

    Retorne uma análise estruturada com:
    - Perfis válidos (lista)
    - Perfis que precisam refinamento (lista com sugestões)
    - Recomendações de priorização
    """

    # Invocar LLM
    response = llm.invoke(prompt)
    validation = response.content if hasattr(response, 'content') else str(response)

    # Salvar resultado
    validation_file = self.context.workspace_root / "00-ProblemHypothesisExpress" / "03-validacao-perfis.MD"
    validation_file.write_text(validation, encoding='utf-8')

    logger.info(f"Validação salva em {validation_file}")

    # Atualizar estado
    state['profile_validation'] = validation

    return state
```

### Passo 2: Adicionar ao Graph

```python
def run(self, config: Optional[RunConfig] = None) -> dict:
    """Executa estratégia ZeroUm."""

    # Criar grafo com NOVO node
    graph = OrchestrationGraph.from_handlers({
        "coletar_contexto": self._coletar_contexto,
        "gerar_hipotese": self._gerar_hipotese,
        "validar_perfis": self._validar_perfis_usuarios,  # ← NOVO
        "validar_resultado": self._validar_resultado,
    })

    # Executar grafo (nodes executam em ordem)
    final_state = graph.execute(initial_state={})

    return {
        "manifests": final_state.get("manifests", []),
        "consolidated": final_state.get("consolidated", ""),
        "archive": final_state.get("archive", ""),
        "profile_validation": final_state.get("profile_validation", ""),  # ← NOVO
        "metrics": self.metrics.get_summary(),
    }
```

### Vantagens desta Abordagem

✅ Usa framework moderno (OrchestrationGraph)
✅ Não cria classes extras
✅ Fácil de testar
✅ Estado compartilhado automaticamente
✅ Observabilidade built-in

---

## Abordagem 2: Classes Dedicadas

Se você **realmente precisa** de uma classe separada (para lógica muito complexa):

### Passo 1: Criar Classe do Subagente

```python
# agents/business/strategies/zeroum/subagents/profile_validator.py

from typing import Any, Dict
from pathlib import Path
from agents.framework.llm.factory import build_llm
import logging

logger = logging.getLogger(__name__)


class ProfileValidator:
    """
    Subagente especializado em validar perfis de usuários-alvo.
    """

    def __init__(self, workspace_root: Path):
        """
        Args:
            workspace_root: Diretório raiz do workspace
        """
        self.workspace_root = workspace_root
        self.llm = build_llm()

    def validate(self, hypothesis: str) -> Dict[str, Any]:
        """
        Valida perfis de usuários na hipótese.

        Args:
            hypothesis: Texto da hipótese contendo perfis

        Returns:
            Dicionário com validação
        """
        logger.info("Iniciando validação de perfis")

        # Prompt específico
        prompt = self._build_validation_prompt(hypothesis)

        # Invocar LLM
        response = self.llm.invoke(prompt)
        validation = response.content if hasattr(response, 'content') else str(response)

        # Salvar resultado
        self._save_validation(validation)

        return {
            'validation_text': validation,
            'status': 'completed',
        }

    def _build_validation_prompt(self, hypothesis: str) -> str:
        """Constrói prompt de validação."""
        return f"""
        Analise os perfis de usuários na hipótese abaixo...

        {hypothesis}
        """

    def _save_validation(self, validation: str) -> None:
        """Salva resultado da validação."""
        output_dir = self.workspace_root / "00-ProblemHypothesisExpress"
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "03-validacao-perfis.MD"
        output_file.write_text(validation, encoding='utf-8')

        logger.info(f"Validação salva em {output_file}")
```

### Passo 2: Usar no Orchestrator

```python
# agents/business/strategies/zeroum/orchestrator.py

from agents.business.strategies.zeroum.subagents.profile_validator import ProfileValidator

class ZeroUmOrchestrator:

    def _validar_perfis_usuarios(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Wrapper para subagente ProfileValidator."""

        # Criar subagente
        validator = ProfileValidator(self.context.workspace_root)

        # Executar validação
        result = validator.validate(state.get('hypothesis', ''))

        # Atualizar estado
        state['profile_validation'] = result['validation_text']

        return state
```

### Estrutura de Diretórios

```
agents/business/strategies/zeroum/
├── __init__.py
├── orchestrator.py                  # Orchestrator principal
└── subagents/                       # Subagentes dedicados
    ├── __init__.py
    ├── profile_validator.py         # Validação de perfis
    ├── hypothesis_refiner.py        # Refinamento de hipótese
    └── evidence_collector.py        # Coleta de evidências
```

---

## Exemplo Completo

Vou criar um exemplo completo de subagente que refina a hipótese:

### 1. Criar Arquivo do Subagente

```python
# agents/business/strategies/zeroum/subagents/hypothesis_refiner.py

"""
Subagente especializado em refinar hipóteses com feedback iterativo.
"""

from typing import Any, Dict, List
from pathlib import Path
from agents.framework.llm.factory import build_llm
import logging

logger = logging.getLogger(__name__)


class HypothesisRefiner:
    """
    Refina hipóteses usando feedback estruturado.
    """

    def __init__(self, workspace_root: Path, max_iterations: int = 3):
        """
        Args:
            workspace_root: Diretório raiz do workspace
            max_iterations: Máximo de iterações de refinamento
        """
        self.workspace_root = workspace_root
        self.max_iterations = max_iterations
        self.llm = build_llm()
        self.iterations: List[Dict[str, str]] = []

    def refine(self, initial_hypothesis: str) -> Dict[str, Any]:
        """
        Refina hipótese iterativamente.

        Args:
            initial_hypothesis: Hipótese inicial

        Returns:
            Dicionário com hipótese refinada e histórico
        """
        logger.info("Iniciando refinamento de hipótese")

        current_hypothesis = initial_hypothesis

        for i in range(self.max_iterations):
            logger.info(f"Iteração {i+1}/{self.max_iterations}")

            # Gerar feedback
            feedback = self._generate_feedback(current_hypothesis)

            # Aplicar refinamento
            refined = self._apply_refinement(current_hypothesis, feedback)

            # Registrar iteração
            self.iterations.append({
                'iteration': i + 1,
                'hypothesis': current_hypothesis,
                'feedback': feedback,
                'refined': refined,
            })

            # Verificar se atingiu qualidade desejada
            if self._is_good_enough(refined):
                logger.info(f"Qualidade atingida na iteração {i+1}")
                current_hypothesis = refined
                break

            current_hypothesis = refined

        # Salvar histórico
        self._save_refinement_log()

        return {
            'final_hypothesis': current_hypothesis,
            'iterations': len(self.iterations),
            'history': self.iterations,
        }

    def _generate_feedback(self, hypothesis: str) -> str:
        """Gera feedback estruturado sobre a hipótese."""
        prompt = f"""
        Analise a seguinte hipótese e forneça feedback estruturado:

        {hypothesis}

        Avalie:
        1. Clareza: Os perfis estão bem definidos?
        2. Especificidade: A dor é mensurável?
        3. Evidências: Há dados concretos?
        4. Proposta de valor: Está diferenciada?

        Forneça 3 sugestões de melhoria específicas.
        """

        response = self.llm.invoke(prompt)
        return response.content if hasattr(response, 'content') else str(response)

    def _apply_refinement(self, hypothesis: str, feedback: str) -> str:
        """Aplica refinamento baseado no feedback."""
        prompt = f"""
        Refine a seguinte hipótese baseado no feedback:

        HIPÓTESE ATUAL:
        {hypothesis}

        FEEDBACK:
        {feedback}

        Retorne a hipótese refinada mantendo o formato original.
        """

        response = self.llm.invoke(prompt)
        return response.content if hasattr(response, 'content') else str(response)

    def _is_good_enough(self, hypothesis: str) -> bool:
        """Verifica se a hipótese atingiu qualidade suficiente."""
        # Critérios simples - pode ser expandido
        return len(hypothesis) > 1000 and "evidência" in hypothesis.lower()

    def _save_refinement_log(self) -> None:
        """Salva log de refinamento."""
        output_dir = self.workspace_root / "00-ProblemHypothesisExpress"
        output_dir.mkdir(parents=True, exist_ok=True)

        log_file = output_dir / "04-refinamento-log.MD"

        content = "# Log de Refinamento de Hipótese\n\n"

        for iteration in self.iterations:
            content += f"## Iteração {iteration['iteration']}\n\n"
            content += f"### Hipótese\n{iteration['hypothesis']}\n\n"
            content += f"### Feedback\n{iteration['feedback']}\n\n"
            content += f"### Refinada\n{iteration['refined']}\n\n"
            content += "---\n\n"

        log_file.write_text(content, encoding='utf-8')
        logger.info(f"Log salvo em {log_file}")
```

### 2. Integrar no Orchestrator

```python
# agents/business/strategies/zeroum/orchestrator.py

from agents.business.strategies.zeroum.subagents.hypothesis_refiner import HypothesisRefiner

class ZeroUmOrchestrator:

    def _refinar_hipotese(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Node: Refina hipótese usando feedback iterativo.
        """
        logger.info("Refinando hipótese")

        # Criar subagente
        refiner = HypothesisRefiner(
            workspace_root=self.context.workspace_root,
            max_iterations=3
        )

        # Executar refinamento
        result = refiner.refine(state.get('hypothesis', ''))

        # Atualizar estado
        state['hypothesis'] = result['final_hypothesis']
        state['refinement_iterations'] = result['iterations']
        state['refinement_history'] = result['history']

        logger.info(f"Hipótese refinada em {result['iterations']} iterações")

        return state

    def run(self, config: Optional[RunConfig] = None) -> dict:
        """Executa estratégia ZeroUm com refinamento."""

        graph = OrchestrationGraph.from_handlers({
            "coletar_contexto": self._coletar_contexto,
            "gerar_hipotese": self._gerar_hipotese,
            "refinar_hipotese": self._refinar_hipotese,      # ← NOVO
            "validar_resultado": self._validar_resultado,
        })

        final_state = graph.execute(initial_state={})

        return {
            "manifests": final_state.get("manifests", []),
            "consolidated": final_state.get("consolidated", ""),
            "archive": final_state.get("archive", ""),
            "refinement_iterations": final_state.get("refinement_iterations", 0),
            "metrics": self.metrics.get_summary(),
        }
```

---

## Boas Práticas

### 1. Escolha a Abordagem Certa

**Use Nodes (Abordagem 1) quando:**
- Lógica é simples (< 50 linhas)
- Não precisa reutilizar em outras estratégias
- Quer aproveitar OrchestrationGraph

**Use Classes (Abordagem 2) quando:**
- Lógica é complexa (> 50 linhas)
- Precisa reutilizar em múltiplas estratégias
- Precisa manter estado interno complexo
- Quer testar isoladamente

### 2. Estrutura de Estado

Sempre use o padrão:

```python
def _meu_subagente(self, state: Dict[str, Any]) -> Dict[str, Any]:
    # 1. Ler do estado
    input_data = state.get('input_key', default_value)

    # 2. Processar
    result = self._process(input_data)

    # 3. Atualizar estado
    state['output_key'] = result

    # 4. Retornar estado
    return state
```

### 3. Logging

Use logging estruturado:

```python
logger.info("Iniciando validação de perfis")
logger.info(f"Processados {count} perfis")
logger.warning(f"Perfil {name} precisa refinamento")
logger.error(f"Erro ao validar: {error}")
```

### 4. Salvamento de Artefatos

Sempre salve resultados intermediários:

```python
output_dir = self.context.workspace_root / "00-ProblemHypothesisExpress"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / f"{step_number:02d}-{artifact_name}.MD"
output_file.write_text(content, encoding='utf-8')
```

### 5. Testes

Teste subagentes isoladamente:

```python
# tests/test_hypothesis_refiner.py

def test_hypothesis_refiner():
    workspace = Path("/tmp/test_workspace")
    workspace.mkdir(exist_ok=True)

    refiner = HypothesisRefiner(workspace)
    result = refiner.refine("Hipótese inicial")

    assert result['final_hypothesis']
    assert result['iterations'] > 0
```

---

## Resumo

### Criar Subagente Simples (Recomendado)

```python
# No orchestrator.py
def _meu_subagente(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """Subagente: faz alguma coisa."""
    # ... lógica ...
    state['resultado'] = valor
    return state

# Adicionar ao graph
graph = OrchestrationGraph.from_handlers({
    "meu_subagente": self._meu_subagente,
})
```

### Criar Subagente Complexo

```python
# subagents/meu_subagente.py
class MeuSubagente:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.llm = build_llm()

    def executar(self, input_data: Any) -> Dict[str, Any]:
        # ... lógica complexa ...
        return resultado

# No orchestrator.py
def _meu_subagente(self, state: Dict[str, Any]) -> Dict[str, Any]:
    subagente = MeuSubagente(self.context.workspace_root)
    result = subagente.executar(state['input'])
    state['output'] = result
    return state
```

---

**Próximos Passos:**
1. Decida qual abordagem usar
2. Implemente o subagente
3. Adicione ao OrchestrationGraph
4. Teste isoladamente
5. Valide integração completa

**Documentação:**
- [agents/framework/orchestration/graph.py](agents/framework/orchestration/graph.py) - OrchestrationGraph
- [agents/framework/llm/factory.py](agents/framework/llm/factory.py) - LLM Factory
- [PROJETO_FINALIZADO.md](PROJETO_FINALIZADO.md) - Arquitetura do framework

---

**Data**: 2025-11-12
**Versão**: 2.0.1
**Status**: Guia Completo
