#!/usr/bin/env python3
"""Teste final após remoção do código legacy."""

from __future__ import annotations

import sys
from pathlib import Path


def test_framework_imports() -> bool:
    """Testa se todos os imports do framework funcionam."""
    print("\n" + "="*80)
    print("TESTE 1: Imports do Framework")
    print("="*80)

    try:
        # Core
        from framework.core.context import AgentContext, RunConfig
        from framework.core.protocols import PipelineStage
        from framework.core.exceptions import AgentError
        from framework.core.decorators import handle_agent_errors

        # IO
        from framework.io.workspace import WorkspaceManager
        from framework.io.manifest import ManifestStore
        from framework.io.package import PackageService

        # Observability
        from framework.observability import TodoManager, MetricsCollector, TracingManager

        # Orchestration
        from framework.orchestration.pipeline import ProcessPipeline
        from framework.orchestration.graph import OrchestrationGraph
        from framework.orchestration.registry import PluginRegistry

        # LLM
        from framework.llm.factory import build_llm

        # Config
        from framework.config import get_settings

        print("✅ Todos os imports do framework funcionaram")
        return True
    except Exception as e:
        print(f"❌ Erro nos imports: {e}")
        return False


def test_no_legacy_code() -> bool:
    """Verifica que código legacy foi removido."""
    print("\n" + "="*80)
    print("TESTE 2: Código Legacy Removido")
    print("="*80)

    base_path = Path(__file__).parent / "agents"

    # Verificar que diretórios legacy não existem
    removed_dirs = [
        "business/legacy",
        "business/strategies/zeroum/subagents",
    ]

    for dir_path in removed_dirs:
        full_path = base_path / dir_path
        if full_path.exists():
            print(f"❌ Diretório não removido: {dir_path}")
            return False

    print("✅ Todo código legacy foi removido")
    return True


def test_orchestrators_clean() -> bool:
    """Verifica que orchestrators estão limpos."""
    print("\n" + "="*80)
    print("TESTE 3: Orchestrators Limpos")
    print("="*80)

    try:
        from business.strategies.zeroum.orchestrator import ZeroUmOrchestrator

        # Verificar que orchestrator não tem referências a subagents
        orch = ZeroUmOrchestrator(context_name="Test", context_description="Test")

        # Verificar que não tem atributo subagents
        if hasattr(orch, 'subagents'):
            print("❌ Orchestrator ainda tem atributo 'subagents'")
            return False

        # Verificar que tem componentes do framework
        assert hasattr(orch, 'workspace')
        assert hasattr(orch, 'package_service')
        assert hasattr(orch, 'metrics')
        assert hasattr(orch, 'tracing')

        print("✅ Orchestrators estão limpos e usando framework")
        return True
    except Exception as e:
        print(f"❌ Erro ao validar orchestrator: {e}")
        return False


def test_agent_context_works() -> bool:
    """Testa que AgentContext funciona corretamente."""
    print("\n" + "="*80)
    print("TESTE 4: AgentContext Funcional")
    print("="*80)

    try:
        from framework.core.context import AgentContext
        from framework.io.workspace import WorkspaceManager

        # Criar contexto (context_description é obrigatório)
        context = AgentContext(
            context_name="TestContext",
            context_description="Test description",
            strategy_name="TestStrategy",
        )

        # Verificar imutabilidade
        try:
            context.context_name = "Changed"  # type: ignore
            print("❌ AgentContext não é imutável!")
            return False
        except (AttributeError, TypeError, Exception):
            pass  # Esperado - frozen dataclass impede modificação

        # Criar workspace manager
        workspace = WorkspaceManager(context)

        # Verificar paths (TestStrategy não aparece no workspace_root)
        assert context.workspace_root.name == "TestContext"
        # workspace_root é drive/<context_name>, não inclui strategy

        print("✅ AgentContext funciona corretamente")
        return True
    except Exception as e:
        import traceback
        print(f"❌ Erro ao testar AgentContext: {e}")
        traceback.print_exc()
        return False


def test_examples_work() -> bool:
    """Verifica que exemplos ainda funcionam."""
    print("\n" + "="*80)
    print("TESTE 5: Exemplos Funcionam")
    print("="*80)

    try:
        from business.examples.simple_agent_example import SimpleCustomAgent

        # Criar agente (process_code não é parâmetro, context_description sim)
        agent = SimpleCustomAgent(
            context_name="TestExample",
            context_description="Test example",
        )

        assert agent.context.context_name == "TestExample"
        assert agent.context.strategy_name == "CustomStrategy"

        print("✅ Exemplos funcionam corretamente")
        return True
    except Exception as e:
        print(f"❌ Erro ao testar exemplos: {e}")
        return False


def main() -> int:
    """Executa todos os testes."""
    print("🔍" * 40)
    print("TESTES FINAIS - REMOÇÃO DE CÓDIGO LEGACY")
    print("🔍" * 40)

    tests = [
        test_framework_imports,
        test_no_legacy_code,
        test_orchestrators_clean,
        test_agent_context_works,
        test_examples_work,
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ ERRO FATAL: {e}")
            results.append(False)

    print("\n" + "="*80)
    print("RESUMO DOS TESTES")
    print("="*80)

    test_names = [
        "Framework Imports",
        "Legacy Code Removed",
        "Orchestrators Clean",
        "AgentContext Works",
        "Examples Work",
    ]

    for name, result in zip(test_names, results):
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status}: {name}")

    passed = sum(results)
    total = len(results)

    print("\n" + "="*80)
    print(f"RESULTADO FINAL: {passed}/{total} testes passaram")
    print("="*80)

    if passed == total:
        print("\n🎉 TODOS OS TESTES PASSARAM! Código legacy removido com sucesso.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} teste(s) falharam.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
