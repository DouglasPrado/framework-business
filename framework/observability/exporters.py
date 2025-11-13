"""
Exportadores de dados de monitoramento.

Fornece funções para exportar dados coletados em diferentes formatos:
- JSON estruturado
- CSV para análise em planilhas
- Métricas agregadas
- Relatórios de resumo
"""

import csv
import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .monitoring import MonitoringManager


def export_to_json(
    filepath: Path,
    monitoring_manager: Optional[MonitoringManager] = None,
    pretty: bool = True,
) -> Path:
    """
    Exporta dados de monitoramento para arquivo JSON.

    Args:
        filepath: Caminho do arquivo de destino
        monitoring_manager: Instância do MonitoringManager (padrão: singleton)
        pretty: Se True, formata JSON com indentação

    Returns:
        Path do arquivo criado
    """
    if monitoring_manager is None:
        monitoring_manager = MonitoringManager.get_instance()

    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "exported_at": datetime.utcnow().isoformat() + "Z",
        "summary": monitoring_manager.get_metrics_summary(),
        "events": [asdict(e) for e in monitoring_manager.events],
    }

    indent = 2 if pretty else None
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

    return filepath


def export_to_csv(
    directory: Path,
    monitoring_manager: Optional[MonitoringManager] = None,
) -> Dict[str, Path]:
    """
    Exporta dados de monitoramento para arquivos CSV separados por tipo.

    Cria 3 arquivos:
    - llm_calls.csv: Chamadas LLM
    - tool_calls.csv: Execuções de ferramentas
    - agent_executions.csv: Execuções de agentes

    Args:
        directory: Diretório de destino
        monitoring_manager: Instância do MonitoringManager (padrão: singleton)

    Returns:
        Dicionário mapeando tipo de evento para Path do arquivo criado
    """
    if monitoring_manager is None:
        monitoring_manager = MonitoringManager.get_instance()

    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    files_created = {}

    # Exportar LLM calls
    llm_calls = monitoring_manager.get_events("llm_call")
    if llm_calls:
        llm_csv = directory / "llm_calls.csv"
        _export_llm_calls_csv(llm_calls, llm_csv)
        files_created["llm_calls"] = llm_csv

    # Exportar Tool calls
    tool_calls = monitoring_manager.get_events("tool_call")
    if tool_calls:
        tool_csv = directory / "tool_calls.csv"
        _export_tool_calls_csv(tool_calls, tool_csv)
        files_created["tool_calls"] = tool_csv

    # Exportar Agent executions
    agent_execs = monitoring_manager.get_events("agent_execution")
    if agent_execs:
        agent_csv = directory / "agent_executions.csv"
        _export_agent_executions_csv(agent_execs, agent_csv)
        files_created["agent_executions"] = agent_csv

    return files_created


def _export_llm_calls_csv(events: List[Any], filepath: Path):
    """Exporta LLM calls para CSV."""
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            "timestamp",
            "call_id",
            "context_name",
            "strategy_name",
            "process_code",
            "subagent",
            "model",
            "temperature",
            "input_tokens",
            "output_tokens",
            "total_tokens",
            "cost_usd",
            "latency_ms",
            "tokens_per_second",
            "tools_available",
            "tools_called",
            "tool_call_count",
        ])

        # Rows
        for event in events:
            writer.writerow([
                event.timestamp,
                event.call_id,
                event.agent_context.get("context_name", ""),
                event.agent_context.get("strategy_name", ""),
                event.agent_context.get("process_code", ""),
                event.agent_context.get("subagent", ""),
                event.llm_config.get("model", ""),
                event.llm_config.get("temperature", ""),
                event.usage.get("input_tokens", 0),
                event.usage.get("output_tokens", 0),
                event.usage.get("total_tokens", 0),
                event.usage.get("cost_usd", 0.0),
                event.performance.get("latency_ms", 0.0),
                event.performance.get("tokens_per_second", 0.0),
                "|".join(event.tools.get("tools_available", [])),
                "|".join(event.tools.get("tools_called", [])),
                event.tools.get("tool_call_count", 0),
            ])


def _export_tool_calls_csv(events: List[Any], filepath: Path):
    """Exporta tool calls para CSV."""
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            "timestamp",
            "call_id",
            "parent_llm_call_id",
            "context_name",
            "tool_name",
            "success",
            "execution_ms",
            "error",
        ])

        # Rows
        for event in events:
            writer.writerow([
                event.timestamp,
                event.call_id,
                event.parent_llm_call_id or "",
                event.agent_context.get("context_name", ""),
                event.tool.get("name", ""),
                event.tool.get("success", True),
                event.performance.get("execution_ms", 0.0),
                event.tool.get("error", ""),
            ])


def _export_agent_executions_csv(events: List[Any], filepath: Path):
    """Exporta agent executions para CSV."""
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            "timestamp",
            "execution_id",
            "agent_type",
            "agent_name",
            "context_name",
            "started_at",
            "completed_at",
            "duration_seconds",
            "status",
            "total_llm_calls",
            "total_tool_calls",
            "total_tokens",
            "total_cost_usd",
        ])

        # Rows
        for event in events:
            writer.writerow([
                event.timestamp,
                event.execution_id,
                event.agent_type,
                event.agent_name,
                event.context.get("context_name", ""),
                event.execution.get("started_at", ""),
                event.execution.get("completed_at", ""),
                event.execution.get("duration_seconds", 0),
                event.execution.get("status", ""),
                event.metrics.get("total_llm_calls", 0),
                event.metrics.get("total_tool_calls", 0),
                event.metrics.get("total_tokens", 0),
                event.metrics.get("total_cost_usd", 0.0),
            ])


def export_summary_report(
    filepath: Path,
    monitoring_manager: Optional[MonitoringManager] = None,
) -> Path:
    """
    Exporta relatório resumido de métricas.

    Args:
        filepath: Caminho do arquivo de destino (formato texto)
        monitoring_manager: Instância do MonitoringManager (padrão: singleton)

    Returns:
        Path do arquivo criado
    """
    if monitoring_manager is None:
        monitoring_manager = MonitoringManager.get_instance()

    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    summary = monitoring_manager.get_metrics_summary()

    lines = [
        "=" * 80,
        "RELATÓRIO DE MONITORAMENTO - AGENTES",
        "=" * 80,
        "",
        f"Gerado em: {datetime.utcnow().isoformat()}Z",
        "",
        "RESUMO GERAL",
        "-" * 80,
        f"Total de eventos: {summary['total_events']}",
        "",
        "CHAMADAS LLM",
        "-" * 80,
        f"  Quantidade: {summary['llm_calls']['count']}",
        f"  Tokens input: {summary['llm_calls']['total_input_tokens']:,}",
        f"  Tokens output: {summary['llm_calls']['total_output_tokens']:,}",
        f"  Tokens total: {summary['llm_calls']['total_tokens']:,}",
        f"  Custo total: ${summary['llm_calls']['total_cost_usd']:.4f}",
        f"  Latência média: {summary['llm_calls']['avg_latency_ms']:.2f}ms",
        "",
        "EXECUÇÕES DE FERRAMENTAS",
        "-" * 80,
        f"  Quantidade: {summary['tool_calls']['count']}",
        f"  Tempo médio: {summary['tool_calls']['avg_execution_ms']:.2f}ms",
        "",
        "  Top 10 ferramentas mais usadas:",
    ]

    # Top tools
    tool_usage = summary['tool_calls']['tool_usage']
    sorted_tools = sorted(tool_usage.items(), key=lambda x: x[1], reverse=True)[:10]
    for tool_name, count in sorted_tools:
        lines.append(f"    - {tool_name}: {count} vezes")

    lines.extend([
        "",
        "EXECUÇÕES DE AGENTES",
        "-" * 80,
        f"  Quantidade: {summary['agent_executions']['count']}",
        "",
        "=" * 80,
    ])

    content = "\n".join(lines)
    filepath.write_text(content, encoding='utf-8')

    return filepath


def export_all(
    base_directory: Path,
    monitoring_manager: Optional[MonitoringManager] = None,
    formats: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Exporta dados de monitoramento em todos os formatos disponíveis.

    Args:
        base_directory: Diretório base para exportação
        monitoring_manager: Instância do MonitoringManager (padrão: singleton)
        formats: Lista de formatos desejados ['json', 'csv', 'summary'] (padrão: todos)

    Returns:
        Dicionário com paths dos arquivos criados
    """
    if monitoring_manager is None:
        monitoring_manager = MonitoringManager.get_instance()

    if formats is None:
        formats = ['json', 'csv', 'summary']

    base_directory = Path(base_directory)
    base_directory.mkdir(parents=True, exist_ok=True)

    files_created = {}

    if 'json' in formats:
        json_file = export_to_json(
            base_directory / "monitoring_data.json",
            monitoring_manager
        )
        files_created['json'] = str(json_file)

    if 'csv' in formats:
        csv_files = export_to_csv(
            base_directory / "csv",
            monitoring_manager
        )
        files_created['csv'] = {k: str(v) for k, v in csv_files.items()}

    if 'summary' in formats:
        summary_file = export_summary_report(
            base_directory / "summary.txt",
            monitoring_manager
        )
        files_created['summary'] = str(summary_file)

    return files_created


__all__ = [
    "export_to_json",
    "export_to_csv",
    "export_summary_report",
    "export_all",
]
