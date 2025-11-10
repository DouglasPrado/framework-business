"""Utilitário para ler processos em process/<Estratégia>/<NN-Nome>."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass
class ProcessDefinition:
    code: str
    root: Path
    files: Dict[str, str]


def load_process(process_dir: Path) -> ProcessDefinition:
    """Retorna os arquivos essenciais do processo."""

    if not process_dir.exists():
        raise FileNotFoundError(f"Processo não encontrado em {process_dir}")

    data: Dict[str, str] = {}
    for filename in ["process.MD", "knowledge.MD", "tasks.MD", "validator.MD"]:
        file_path = process_dir / filename
        data[filename] = file_path.read_text(encoding="utf-8") if file_path.exists() else ""

    return ProcessDefinition(code=process_dir.name, root=process_dir, files=data)
