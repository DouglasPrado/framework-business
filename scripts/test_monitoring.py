"""
Script de teste para validar o sistema de monitoramento.

Executa um teste simples do framework de monitoramento:
1. Habilita o monitoramento
2. Simula chamadas LLM e execuções de ferramentas
3. Exporta dados em múltiplos formatos
4. Exibe relatório resumido
"""

import sys
from pathlib import Path

# Adicionar path da raiz ao PYTHONPATH
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

# Import direto dos módulos de observability (sem passar pelo __init__ do framework)
import framework.observability.monitoring as monitoring_module
import framework.observability.exporters as exporters_module

MonitoringManager = monitoring_module.MonitoringManager
export_all = exporters_module.export_all
export_summary_report = exporters_module.export_summary_report


def test_monitoring_system():
    """Testa o sistema de monitoramento de ponta a ponta."""
    print("=" * 80)
    print("TESTE DO SISTEMA DE MONITORAMENTO")
    print("=" * 80)
    print()

    # 1. Verificar se monitoramento está habilitado
    print("1. Verificando status do monitoramento...")
    is_enabled = MonitoringManager.is_enabled()
    print(f"   Monitoramento habilitado: {is_enabled}")

    if not is_enabled:
        print("   Habilitando monitoramento...")
        MonitoringManager.set_enabled(True)
    print()

    # 2. Obter instância do monitoring manager
    print("2. Obtendo instância do MonitoringManager...")
    mon = MonitoringManager.get_instance()
    print(f"   Eventos atuais: {len(mon.events)}")
    print()

    # 3. Simular algumas chamadas LLM
    print("3. Simulando chamadas LLM...")
    for i in range(3):
        call_id = mon.record_llm_call(
            agent_context={
                "context_name": "TesteMonitoramento",
                "strategy_name": "Test",
                "subagent": f"test_agent_{i}",
            },
            llm_config={
                "model": "gpt-4o-mini",
                "temperature": 0.4,
            },
            input_data={
                "prompt_length": 100,
            },
            output_data={
                "content": f"Resposta de teste {i}",
                "content_length": 50,
            },
            usage={
                "input_tokens": 100,
                "output_tokens": 50,
                "total_tokens": 150,
                "cost_usd": 0.0001,
            },
            performance={
                "latency_ms": 500.0,
                "tokens_per_second": 100.0,
            },
            tools={
                "tools_available": ["ls", "read_file", "write_file"],
                "tools_called": ["read_file"] if i % 2 == 0 else [],
                "tool_call_count": 1 if i % 2 == 0 else 0,
            }
        )
        print(f"   LLM call {i+1} registrada: {call_id}")
    print()

    # 4. Simular execuções de ferramentas
    print("4. Simulando execuções de ferramentas...")
    tools = ["ls", "read_file", "write_file", "glob", "grep"]
    for i, tool in enumerate(tools):
        mon.record_tool_call(
            tool_name=tool,
            tool_args={"path": f"/test/path/{i}"},
            tool_result=f"Result from {tool}",
            success=True,
            execution_ms=10.0 + (i * 5),
            agent_context={
                "context_name": "TesteMonitoramento",
            }
        )
        print(f"   Tool call '{tool}' registrada")
    print()

    # 5. Simular execução de agente
    print("5. Simulando execução de agente...")
    exec_id = mon.record_agent_execution(
        agent_type="strategy_orchestrator",
        agent_name="ZeroUmOrchestrator",
        context={
            "context_name": "TesteMonitoramento",
            "workspace_root": "/test/workspace",
        },
        execution={
            "started_at": "2025-01-13T10:00:00Z",
            "completed_at": "2025-01-13T10:05:00Z",
            "duration_seconds": 300,
            "status": "completed",
        },
        metrics={
            "total_llm_calls": 3,
            "total_tool_calls": 5,
            "total_tokens": 450,
            "total_cost_usd": 0.0003,
        }
    )
    print(f"   Agent execution registrada: {exec_id}")
    print()

    # 6. Exibir resumo de métricas
    print("6. Resumo de métricas coletadas...")
    summary = mon.get_metrics_summary()
    print(f"   Total de eventos: {summary['total_events']}")
    print(f"   LLM calls: {summary['llm_calls']['count']}")
    print(f"   Tool calls: {summary['tool_calls']['count']}")
    print(f"   Agent executions: {summary['agent_executions']['count']}")
    print(f"   Custo total: ${summary['llm_calls']['total_cost_usd']:.4f}")
    print()

    # 7. Exportar dados
    print("7. Exportando dados de monitoramento...")
    export_dir = repo_root / "drive" / "_monitoring_test"

    files_created = export_all(
        base_directory=export_dir,
        monitoring_manager=mon,
        formats=['json', 'csv', 'summary']
    )

    print(f"   JSON: {files_created.get('json', 'N/A')}")
    if 'csv' in files_created:
        for csv_type, csv_path in files_created['csv'].items():
            print(f"   CSV ({csv_type}): {csv_path}")
    print(f"   Summary: {files_created.get('summary', 'N/A')}")
    print()

    # 8. Exibir conteúdo do relatório resumido
    print("8. Conteúdo do relatório resumido:")
    print("-" * 80)
    summary_path = Path(files_created['summary'])
    print(summary_path.read_text(encoding='utf-8'))
    print("-" * 80)
    print()

    # 9. Limpar eventos para próximo teste
    print("9. Limpando eventos...")
    mon.clear()
    print(f"   Eventos após limpeza: {len(mon.events)}")
    print()

    print("=" * 80)
    print("TESTE CONCLUÍDO COM SUCESSO!")
    print("=" * 80)
    print()
    print(f"Arquivos exportados em: {export_dir}")
    print()


if __name__ == "__main__":
    try:
        test_monitoring_system()
    except Exception as e:
        print(f"\nERRO durante teste: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
