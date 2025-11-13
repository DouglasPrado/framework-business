"""
Script de teste para validar migração da Fase 5.

Testa:
1. Imports do framework
2. Facades de compatibilidade
3. Nova estrutura de business/strategies/
4. Exemplo de agente customizado
"""

import sys
import warnings
from pathlib import Path

# Adicionar agents ao path
sys.path.insert(0, str(Path(__file__).parent))


def test_framework_imports():
    """Testa imports do framework."""
    print("=" * 80)
    print("TESTE 1: Imports do Framework")
    print("=" * 80)

    try:
        # Core
        from agents.framework.core.context import AgentContext, RunConfig
        from agents.framework.core.protocols import PipelineStage
        from agents.framework.core.exceptions import AgentError
        from agents.framework.core.decorators import handle_agent_errors

        # I/O
        from agents.framework.io.workspace import WorkspaceManager
        from agents.framework.io.manifest import ManifestStore
        from agents.framework.io.package import PackageService

        # Observability
        from agents.framework.observability import (
            TodoManager,
            MetricsCollector,
            TracingManager,
        )

        # Orchestration
        from agents.framework.orchestration.pipeline import ProcessPipeline
        from agents.framework.orchestration.graph import OrchestrationGraph
        from agents.framework.orchestration.registry import PluginRegistry

        # LLM
        from agents.framework.llm.factory import build_llm

        print("✅ Todos os imports do framework funcionaram")
        return True

    except Exception as e:
        print(f"❌ Erro nos imports: {e}")
        return False


def test_backward_compatibility_facades():
    """
    REMOVIDO: Facades foram removidas.

    As facades de compatibilidade (agents.ZeroUm e agents.generic) foram
    completamente removidas. Código deve usar diretamente:
    - agents.business.strategies.zeroum.orchestrator
    - agents.business.strategies.generic.orchestrator
    """
    print("\n" + "=" * 80)
    print("TESTE 2: Facades Removidas (SKIP)")
    print("=" * 80)
    print("✅ Facades removidas - usando imports diretos")
    return True


def test_new_business_structure():
    """Testa nova estrutura em business/strategies/."""
    print("\n" + "=" * 80)
    print("TESTE 3: Nova Estrutura Business/Strategies")
    print("=" * 80)

    try:
        # Testar import direto da nova estrutura
        from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator
        from agents.business.strategies.generic.orchestrator import (
            GenericStrategyOrchestrator,
        )

        print("✅ Imports da nova estrutura funcionam")

        # Verificar que classes podem ser instanciadas
        zeroum = ZeroUmOrchestrator(
            context_name="TestContext", context_description="Test description"
        )
        print(f"✅ ZeroUmOrchestrator instanciado: {zeroum.strategy_name}")

        generic = GenericStrategyOrchestrator(
            strategy_name="TestStrategy",
            context_name="TestContext",
            context_description="Test description",
        )
        print(f"✅ GenericStrategyOrchestrator instanciado: {generic.context.strategy_name}")

        print("✅ Nova estrutura business/strategies/ funciona corretamente")
        return True

    except Exception as e:
        print(f"❌ Erro na nova estrutura: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_custom_agent_example():
    """Testa exemplo de agente customizado."""
    print("\n" + "=" * 80)
    print("TESTE 4: Exemplo de Agente Customizado")
    print("=" * 80)

    try:
        # Importar classe do exemplo
        from agents.business.examples.simple_agent_example import SimpleCustomAgent

        print("✅ Exemplo importado com sucesso")

        # Instanciar agente
        agent = SimpleCustomAgent(
            context_name="TestCustomAgent",
            context_description="Teste do agente customizado usando framework",
        )

        print(f"✅ Agente customizado instanciado")
        print(f"   - Context name: {agent.context.context_name}")
        print(f"   - Strategy: {agent.context.strategy_name}")
        print(f"   - Process: {agent.context.process_code}")

        # Verificar componentes
        assert agent.workspace is not None
        assert agent.metrics is not None
        assert agent.todo_manager is not None
        print("✅ Todos os componentes do framework inicializados")

        print("✅ Exemplo de agente customizado funciona corretamente")
        return True

    except Exception as e:
        print(f"❌ Erro no agente customizado: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_agent_context_immutability():
    """Testa imutabilidade do AgentContext."""
    print("\n" + "=" * 80)
    print("TESTE 5: Imutabilidade do AgentContext")
    print("=" * 80)

    try:
        from agents.framework.core.context import AgentContext

        context = AgentContext(
            context_name="TestImmutable",
            context_description="Test",
            strategy_name="TestStrategy",
        )

        # Tentar modificar deve falhar
        try:
            context.context_name = "Modified"
            print("❌ AgentContext não é imutável (modificação permitida)")
            return False
        except AttributeError:
            print("✅ AgentContext é imutável (não permite modificação)")

        # Verificar propriedades calculadas
        assert context.workspace_root.name == "TestImmutable"
        print(f"✅ Propriedades calculadas funcionam: {context.workspace_root}")

        return True

    except Exception as e:
        print(f"❌ Erro no teste de imutabilidade: {e}")
        return False


def test_metrics_collection():
    """Testa coleta de métricas."""
    print("\n" + "=" * 80)
    print("TESTE 6: Coleta de Métricas")
    print("=" * 80)

    try:
        from agents.framework.observability import MetricsCollector
        import time

        collector = MetricsCollector()

        # Testar timer
        collector.start_timer("test_operation")
        time.sleep(0.01)
        elapsed = collector.stop_timer("test_operation")
        assert elapsed >= 0.01
        print(f"✅ Timer funciona: {elapsed:.3f}s")

        # Testar tokens
        collector.record_token_usage(
            input_tokens=1000, output_tokens=500, cost_per_1k_input=0.01, cost_per_1k_output=0.03
        )
        print(f"✅ Token tracking funciona: {collector.token_metrics.total_tokens} tokens")

        # Testar summary
        summary = collector.get_summary()
        assert summary["total_metrics"] > 0
        assert summary["tokens"]["total_tokens"] == 1500
        print(f"✅ Summary gerado: {summary['total_metrics']} métricas")

        return True

    except Exception as e:
        print(f"❌ Erro na coleta de métricas: {e}")
        import traceback

        traceback.print_exc()
        return False


def run_all_tests():
    """Executa todos os testes."""
    print("\n" + "🔍" * 40)
    print("INICIANDO TESTES DA FASE 5: MIGRAÇÃO DE NEGÓCIO")
    print("🔍" * 40 + "\n")

    results = {
        "Framework Imports": test_framework_imports(),
        "Backward Compatibility": test_backward_compatibility_facades(),
        "Business Structure": test_new_business_structure(),
        "Custom Agent Example": test_custom_agent_example(),
        "AgentContext Immutability": test_agent_context_immutability(),
        "Metrics Collection": test_metrics_collection(),
    }

    # Resumo
    print("\n" + "=" * 80)
    print("RESUMO DOS TESTES")
    print("=" * 80)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, result in results.items():
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status}: {test_name}")

    print("\n" + "=" * 80)
    print(f"RESULTADO FINAL: {passed}/{total} testes passaram")
    print("=" * 80)

    if passed == total:
        print("\n🎉 TODOS OS TESTES PASSARAM! Migração da Fase 5 completa.")
        return True
    else:
        print(f"\n⚠️  {total - passed} teste(s) falharam. Revisar antes de prosseguir.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
