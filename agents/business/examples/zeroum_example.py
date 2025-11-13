#!/usr/bin/env python3
"""
Exemplo de uso da estratégia ZeroUm.

Este exemplo mostra como usar o ZeroUmOrchestrator para executar
a estratégia completa.
"""

import sys
from pathlib import Path

# Garantir que o pacote agents esteja acessível
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator


def main():
    """Exemplo de execução da estratégia ZeroUm."""

    print("="*80)
    print("EXEMPLO: Estratégia ZeroUm")
    print("="*80)

    # 1. Definir contexto
    context_name = "ExemploAutomarticles"
    context_description = """
    Automarticles é uma plataforma que automatiza blogs para PMEs usando IA.

    Objetivo: Validar hipótese de problema e criar MVP.
    Target: PMEs que precisam de conteúdo mas não tem tempo/recursos.
    """

    print(f"\nContexto: {context_name}")
    print(f"Descrição: {context_description.strip()}")

    # 2. Criar orchestrator
    print("\n1. Criando ZeroUmOrchestrator...")
    orchestrator = ZeroUmOrchestrator(
        context_name=context_name,
        context_description=context_description,
    )

    print(f"   ✓ Workspace: {orchestrator.context.workspace_root}")
    print(f"   ✓ Strategy: {orchestrator.context.strategy_name}")

    # 3. Executar estratégia
    print("\n2. Executando estratégia ZeroUm...")
    result = orchestrator.run()

    # 4. Mostrar resultados
    print("\n3. Resultados:")
    print(f"   ✓ Consolidado: {result['consolidated']}")
    print(f"   ✓ Archive: {result['archive']}")

    metrics = result.get('metrics', {})
    if metrics:
        print("\n4. Métricas:")
        for key, value in metrics.items():
            print(f"   - {key}: {value}")

    print("\n" + "="*80)
    print("ESTRATÉGIA CONCLUÍDA!")
    print("="*80)

    print(f"\nArquivos gerados em: {orchestrator.context.workspace_root}")
    print("\nPróximos passos:")
    print("1. Revisar o consolidado gerado")
    print("2. Extrair o ZIP para ver todos os artefatos")
    print("3. Implementar lógica customizada em _gerar_hipotese()")


if __name__ == "__main__":
    main()
