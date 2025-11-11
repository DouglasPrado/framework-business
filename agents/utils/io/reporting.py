"""
Funções compartilhadas para geração de relatórios e consolidação.

Este módulo contém funções reutilizáveis para gerar relatórios consolidados
de execução de estratégias.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


def write_consolidated_report(
    strategy_name: str,
    context_name: str,
    context_description: str,
    manifests: List[Dict[str, Any]],
    output_path: Path,
    additional_notes: str = "",
) -> Path:
    """
    Escreve relatório consolidado de execução de estratégia.

    Args:
        strategy_name: Nome da estratégia executada
        context_name: Nome do contexto de execução
        context_description: Descrição do contexto
        manifests: Lista de manifestos dos processos executados
        output_path: Caminho onde salvar o relatório
        additional_notes: Notas adicionais para incluir no relatório

    Returns:
        Path do arquivo gerado

    Example:
        >>> manifests = [{"process": "01-Test", "status": "completed"}]
        >>> write_consolidated_report(
        ...     "ZeroUm",
        ...     "MyProject",
        ...     "Project description",
        ...     manifests,
        ...     Path("output/00-consolidado.MD")
        ... )
    """
    lines = [
        f"# Execução da estratégia {strategy_name}",
        "",
        f"Contexto: {context_name}",
        f"Descrição: {context_description}",
        "",
    ]

    # Seção de processos executados
    if manifests:
        lines.append("## Processos executados")
        lines.append("")
        for manifest in manifests:
            process_name = manifest.get("process", "desconhecido")
            status = manifest.get("status", "desconhecido")
            lines.append(f"- {process_name}: {status}")
        lines.append("")

    # Seção de notas adicionais
    if additional_notes:
        lines.append("## Notas")
        lines.append("")
        lines.append(additional_notes)
        lines.append("")

    # Rodapé com timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append("---")
    lines.append(f"Gerado em: {timestamp}")

    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def format_process_summary(manifests: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """
    Formata manifestos em resumo de processos completados/pendentes.

    Args:
        manifests: Lista de manifestos de processos

    Returns:
        Dicionário com listas 'completed' e 'pending'

    Example:
        >>> manifests = [
        ...     {"process": "01-Test", "status": "completed"},
        ...     {"process": "02-Review", "status": "pending"}
        ... ]
        >>> format_process_summary(manifests)
        {'completed': ['01-Test'], 'pending': ['02-Review']}
    """
    summary: Dict[str, List[str]] = {
        "completed": [],
        "pending": [],
    }

    for manifest in manifests:
        process_name = manifest.get("process", "unknown")
        status = manifest.get("status", "pending")

        if status == "completed":
            summary["completed"].append(process_name)
        else:
            summary["pending"].append(process_name)

    return summary


__all__ = [
    "write_consolidated_report",
    "format_process_summary",
]
