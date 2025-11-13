#!/usr/bin/env python3
"""
Exemplo de uso do Orquestrador Dinâmico ZeroUm.

Este exemplo demonstra como o orquestrador analisa o contexto
e seleciona automaticamente o subagente mais apropriado.

Uso:
    python3 agents/business/examples/dynamic_orchestrator_example.py
"""

import sys
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Adicionar root ao path
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator


def test_simple_context():
    """Testa orquestrador com contexto simples (deve selecionar ProblemHypothesisExpress)."""
    print("=" * 80)
    print("Teste 1: Contexto Simples - Validação de Ideia")
    print("=" * 80)
    print()

    orchestrator = ZeroUmOrchestrator(
        context_name="ValidacaoIdeiaRapida",
        context_description="""
        Tenho uma ideia de criar uma plataforma de automação de validação de ideias
        para founders de startups. Preciso validar se isso resolve um problema real
        antes de começar a desenvolver.
        """,
    )

    print("Executando orquestrador com análise automática de contexto...")
    print()

    try:
        results = orchestrator.run()

        print()
        print("=" * 80)
        print("RESULTADO DA EXECUÇÃO")
        print("=" * 80)
        print()
        print(f"Complexidade detectada: {results['complexity']}")
        print(f"Subagente selecionado: {results['selected_subagent']}")
        print(f"Consolidado: {results['consolidated']}")
        print(f"Pacote: {results['archive']}")
        print()

        if results['manifests']:
            manifest = results['manifests'][0]
            print("Detalhes do processo:")
            print(f"  Status: {manifest['status']}")
            print(f"  Notas: {manifest.get('notes', 'N/A')}")
            print()

        return 0

    except Exception as e:
        print(f"Erro ao executar orquestrador: {e}")
        import traceback
        traceback.print_exc()
        return 1


def test_complex_context():
    """Testa orquestrador com contexto complexo (deve selecionar ClientDelivery)."""
    print()
    print("=" * 80)
    print("Teste 2: Contexto Complexo - Entrega ao Cliente")
    print("=" * 80)
    print()

    orchestrator = ZeroUmOrchestrator(
        context_name="EntregaProjetoCompleto",
        context_description="""
        Preciso realizar a entrega completa de um projeto para o cliente XYZ.
        Isso inclui: handoff da venda, onboarding do cliente, planejamento detalhado,
        produção dos entregáveis, entrega final e acompanhamento pós-entrega.
        O projeto tem escopo de 3 meses e múltiplos stakeholders envolvidos.
        """,
    )

    print("Executando orquestrador com análise automática de contexto...")
    print()

    try:
        results = orchestrator.run()

        print()
        print("=" * 80)
        print("RESULTADO DA EXECUÇÃO")
        print("=" * 80)
        print()
        print(f"Complexidade detectada: {results['complexity']}")
        print(f"Subagente selecionado: {results['selected_subagent']}")
        print(f"Consolidado: {results['consolidated']}")
        print(f"Pacote: {results['archive']}")
        print()

        if results['manifests']:
            manifest = results['manifests'][0]
            print("Detalhes do processo:")
            print(f"  Status: {manifest['status']}")
            print(f"  Notas: {manifest.get('notes', 'N/A')}")
            print()

        return 0

    except Exception as e:
        print(f"Erro ao executar orquestrador: {e}")
        import traceback
        traceback.print_exc()
        return 1


def main():
    """Executa os testes do orquestrador dinâmico."""
    print()
    print("=" * 80)
    print("TESTES DO ORQUESTRADOR DINÂMICO ZEROUM")
    print("=" * 80)
    print()
    print("O orquestrador irá:")
    print("1. Analisar o contexto usando LLM")
    print("2. Classificar a complexidade")
    print("3. Selecionar o subagente mais apropriado")
    print("4. Executar o subagente dinamicamente")
    print("5. Gerar consolidado e pacote final")
    print()

    # Executar teste 1 (contexto simples)
    result1 = test_simple_context()

    # Executar teste 2 (contexto complexo)
    result2 = test_complex_context()

    # Resumo final
    print()
    print("=" * 80)
    print("RESUMO DOS TESTES")
    print("=" * 80)
    print()
    print(f"Teste 1 (Contexto Simples): {'OK' if result1 == 0 else 'FALHOU'}")
    print(f"Teste 2 (Contexto Complexo): {'OK' if result2 == 0 else 'FALHOU'}")
    print()

    if result1 == 0 and result2 == 0:
        print("Todos os testes passaram!")
        print()
        print("Próximos passos:")
        print("1. Verificar os workspaces gerados em drive/")
        print("2. Revisar os documentos consolidados")
        print("3. Validar se os subagentes foram selecionados corretamente")
        return 0
    else:
        print("Alguns testes falharam. Verifique os erros acima.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
