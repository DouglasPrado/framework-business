"""Persistência simples para manifestos em drive/<Contexto>/_pipeline/."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class ManifestHandler:
    base_folder: Path

    def __post_init__(self) -> None:
        self.base_folder.mkdir(parents=True, exist_ok=True)

    def path_for(self, manifest_name: str) -> Path:
        return self.base_folder / manifest_name

    def write(self, manifest_name: str, payload: Dict[str, Any]) -> Path:
        target = self.path_for(manifest_name)
        target.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return target

    def read(self, manifest_name: str) -> Dict[str, Any]:
        target = self.path_for(manifest_name)
        if not target.exists():
            raise FileNotFoundError(f"Manifesto {manifest_name} não encontrado em {self.base_folder}")
        return json.loads(target.read_text(encoding="utf-8"))

    def list_manifests(self) -> List[str]:
        return sorted(p.name for p in self.base_folder.glob("*-manifest.json"))
