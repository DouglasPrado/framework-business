"""Empacotamento dos artefatos em drive para download."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

from .. import BASE_PATH


def package_artifacts(context_name: str, strategy_name: str, base_path: Path = BASE_PATH, output_name: Optional[str] = None) -> Path:
    """Gera um arquivo .zip na raiz da estratégia dentro de drive/."""
    strategy_folder = base_path / "drive" / context_name / strategy_name
    strategy_folder.mkdir(parents=True, exist_ok=True)

    archive_name = output_name or f"{strategy_name}AgentOutputs"
    archive_path = strategy_folder / archive_name

    if archive_path.with_suffix(".zip").exists():
        archive_path.with_suffix(".zip").unlink()

    result = shutil.make_archive(str(archive_path), "zip", root_dir=str(strategy_folder))
    return Path(result)
