"""Subagentes especializados na estratégia ZeroUm."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, Callable, Dict, Optional

from ...base import ProcessAgent
from ...utils.drive_writer import ensure_process_folder, write_artifact
from ...utils.manifest import ManifestHandler
from ...utils.process_loader import ProcessDefinition, load_process

logger = logging.getLogger(__name__)


class ZeroUmProcessAgent(ProcessAgent):
    strategy_name = "ZeroUm"

    def __init__(self, process_code: str, context_name: str, context_description: str, pipeline_dir: Path, prompt: Optional[str] = None) -> None:
        self.pipeline_dir = pipeline_dir
        super().__init__(
            process_code=process_code,
            strategy_name=self.strategy_name,
            context_name=context_name,
            context_description=context_description,
            prompt=prompt,
        )
        self.definition: ProcessDefinition = load_process(self.process_dir)
        self.manifest_handler = ManifestHandler(pipeline_dir)
        self.cost_calculator = self._load_cost_calculator()

    def default_prompt(self) -> str:
        return (
            "Você é um subagente da estratégia ZeroUm. Leia os arquivos do processo, "
            "verifique _SHARED, siga AGENTS.MD e produza artefatos numerados em drive/."
        )

    def run(self) -> Dict[str, Any]:
        raise NotImplementedError

    def _load_cost_calculator(self) -> Optional[Callable[[int], float]]:
        """Gera função opcional para estimar custo com base em variáveis de ambiente."""

        raw_value = os.getenv("ZEROUM_COST_PER_1K_TOKENS") or os.getenv("LLM_COST_PER_1K_TOKENS")
        if not raw_value:
            return None
        try:
            per_thousand = float(raw_value)
        except ValueError:
            logger.warning(
                "[%s] Valor inválido em ZEROUM_COST_PER_1K_TOKENS/LLM_COST_PER_1K_TOKENS: %s",
                self.process_code,
                raw_value,
            )
            return None

        cost_per_token = per_thousand / 1000.0

        def _calculator(tokens: int) -> float:
            return round(tokens * cost_per_token, 6)

        return _calculator

    def save_artifact(self, slug: str, content: str, extension: str = ".MD") -> Path:
        folder = ensure_process_folder(self.context_name, self.process_code)
        artifact_path = write_artifact(folder, slug, content, extension)
        logger.info(
            "[%s] Artefato salvo em %s",
            self.process_code,
            artifact_path,
        )
        return artifact_path

    def publish_manifest(self, payload: Dict[str, Any]) -> Path:
        manifest_name = f"{self.process_code}-manifest.json"
        manifest_path = self.manifest_handler.write(manifest_name, payload)
        logger.info(
            "[%s] Manifesto publicado em %s com status %s",
            self.process_code,
            manifest_path,
            payload.get("status", "desconhecido"),
        )
        return manifest_path
