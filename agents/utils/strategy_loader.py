"""Carregador de estratégias definido em strategies/<nome>."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class StrategyDefinition:
    name: str
    root: Path
    prompt: str
    processes: List[Dict[str, str]]


def load_strategy(strategy_dir: Path) -> StrategyDefinition:
    """Lê metadados básicos da estratégia a partir da pasta strategies."""

    if not strategy_dir.exists():
        raise FileNotFoundError(f"Estratégia não encontrada em {strategy_dir}")

    repo_root = strategy_dir.parents[1]
    strategy_name = strategy_dir.name
    process_root = repo_root / "process" / strategy_name
    processes: List[Dict[str, str]] = []

    if process_root.exists():
        for process_dir in sorted(p for p in process_root.iterdir() if p.is_dir()):
            processes.append(
                {
                    "code": process_dir.name,
                    "path": str(process_dir),
                    "manifest": f"{process_dir.name}-manifest.json",
                }
            )

    prompt_file = strategy_dir / "process.MD"
    prompt_text = prompt_file.read_text(encoding="utf-8") if prompt_file.exists() else ""

    return StrategyDefinition(
        name=strategy_name,
        root=strategy_dir,
        prompt=prompt_text,
        processes=processes,
    )
