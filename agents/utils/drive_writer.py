"""Helpers para manter o padrão de arquivos dentro de drive/."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from .. import BASE_PATH


def ensure_strategy_folder(context_name: str, strategy_name: str, base_path: Path = BASE_PATH) -> Path:
    """Garante que drive/<Contexto>/<Estratégia>/ exista."""
    target = base_path / "drive" / context_name / strategy_name
    target.mkdir(parents=True, exist_ok=True)
    return target


def ensure_process_folder(context_name: str, process_code: str, base_path: Path = BASE_PATH) -> Path:
    """Cria a pasta drive/<Contexto>/<Processo>/ quando necessário."""
    target = base_path / "drive" / context_name / process_code
    target.mkdir(parents=True, exist_ok=True)
    return target


def next_prefixed_name(folder: Path, slug: str, extension: str = ".MD") -> Path:
    """Calcula o próximo nome numerado (01-, 02-, etc.) dentro da pasta."""
    ensure_folder = folder
    ensure_folder.mkdir(parents=True, exist_ok=True)

    pattern = re.compile(r"^(\d{2})-", re.IGNORECASE)
    highest = 0
    for item in folder.iterdir():
        match = pattern.match(item.name)
        if match:
            highest = max(highest, int(match.group(1)))

    slugified = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
    next_index = highest + 1
    filename = f"{next_index:02d}-{slugified}{extension}"
    return folder / filename


def write_artifact(folder: Path, slug: str, content: str, extension: str = ".MD") -> Path:
    """Escreve o arquivo numerado e retorna o caminho gerado."""
    target = next_prefixed_name(folder, slug, extension)
    target.write_text(content, encoding="utf-8")
    return target


def get_pipeline_folder(context_name: str, base_path: Path = BASE_PATH) -> Path:
    pipeline = base_path / "drive" / context_name / "_pipeline"
    pipeline.mkdir(parents=True, exist_ok=True)
    return pipeline
