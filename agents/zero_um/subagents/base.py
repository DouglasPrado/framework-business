"""Subagentes especializados na estratégia ZeroUm."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict, Optional

from ... import BASE_PATH
from ...base import ProcessAgent
from ...utils.drive_writer import ensure_process_folder, write_artifact
from ...utils.manifest import ManifestHandler
from ...utils.process_loader import ProcessDefinition, load_process
from ...utils.todos import TodoManager

if TYPE_CHECKING:  # pragma: no cover - usado apenas para type checking
    from deepagents import DeepAgent

logger = logging.getLogger(__name__)


class ZeroUmProcessAgent(ProcessAgent):
    strategy_name = "ZeroUm"

    def __init__(
        self,
        process_code: str,
        context_name: str,
        context_description: str,
        pipeline_dir: Path,
        prompt: Optional[str] = None,
        base_path: Optional[Path] = None,
    ) -> None:
        self.pipeline_dir = pipeline_dir
        super().__init__(
            process_code=process_code,
            strategy_name=self.strategy_name,
            context_name=context_name,
            context_description=context_description,
            prompt=prompt,
            base_path=base_path or BASE_PATH,
        )
        self.definition: ProcessDefinition = load_process(self.process_dir)
        self.manifest_handler = ManifestHandler(pipeline_dir)
        self.todo_manager = TodoManager(
            process_code=process_code,
            context_name=context_name,
            pipeline_dir=pipeline_dir,
        )
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
        folder = ensure_process_folder(
            self.context_name,
            self.process_code,
            base_path=self.base_path,
        )
        artifact_path = write_artifact(folder, slug, content, extension)
        logger.info(
            "[%s] Artefato salvo em %s",
            self.process_code,
            artifact_path,
        )
        return artifact_path

    def publish_manifest(self, payload: Dict[str, Any]) -> Path:
        # Incluir resumo de TODOs no manifesto
        if self.todo_manager.enabled:
            payload["todos_summary"] = self.todo_manager.get_summary()

        manifest_name = f"{self.process_code}-manifest.json"
        manifest_path = self.manifest_handler.write(manifest_name, payload)
        logger.info(
            "[%s] Manifesto publicado em %s com status %s",
            self.process_code,
            manifest_path,
            payload.get("status", "desconhecido"),
        )
        return manifest_path

    def write_todos(self, todos: List[Dict[str, str]]) -> None:
        """
        Método auxiliar para criar múltiplos TODOs de uma vez.

        Args:
            todos: Lista de dicionários com 'task' e opcionalmente 'status', 'id'

        Exemplo:
            self.write_todos([
                {"task": "Carregar validator.MD", "status": "pending"},
                {"task": "Gerar rascunho inicial", "status": "pending"},
            ])
        """
        self.todo_manager.write_todos(todos)
