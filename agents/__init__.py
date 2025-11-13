"""
Agents - Framework Reutilizável para Criação de Agentes AI.

Este pacote fornece um framework completo para construção de agentes AI,
separado em duas camadas principais:

1. Framework (agents/framework/) - 75%
   - Componentes reutilizáveis e extensíveis
   - Independente de regras de negócio específicas
   - Pode ser usado para qualquer tipo de agente

2. Business (agents/business/) - 25%
   - Estratégias e lógica de negócio específicas
   - Implementações concretas usando o framework
   - Exemplos de uso

Estrutura:
    agents/
    ├── framework/          # Framework reutilizável
    │   ├── core/          # Context, protocols, exceptions, decorators
    │   ├── io/            # Workspace, manifest, package
    │   ├── llm/           # LLM factory e adapters
    │   ├── orchestration/ # Pipeline, graph, registry
    │   └── observability/ # TODOs, metrics, tracing
    │
    ├── business/          # Lógica de negócio
    │   ├── strategies/    # Estratégias concretas (zeroum, generic)
    │   ├── examples/      # Exemplos de uso do framework
    │   └── legacy/        # Código não migrado (deprecated)
    │
    ├── ZeroUm/           # Facade de compatibilidade (deprecated)
    └── generic/          # Facade de compatibilidade (deprecated)

Para começar:
    - Ver exemplos em: agents/business/examples/
    - Ler documentação: agents/MIGRATION_GUIDE.md
    - Criar novo agente: usar componentes de agents/framework/

Legacy:
    - Código antigo movido para: agents/business/legacy/
    - Facades mantidas para compatibilidade: ZeroUm/, generic/
"""

from pathlib import Path

# Caminho base do projeto (framework-business/)
BASE_PATH = Path(__file__).resolve().parents[1]

__all__ = ["BASE_PATH"]
__version__ = "1.0.0"
