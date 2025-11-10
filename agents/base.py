"""Fundamentos reutilizáveis para orquestradores e subagentes."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import BASE_PATH
from .utils.manifest import ManifestHandler
from .utils.strategy_loader import StrategyDefinition, load_strategy

try:  # pragma: no cover - dependência externa opcional durante o setup
    from deepagents import create_deep_agent
except ImportError:  # pragma: no cover - fallback para stub local dentro de agents/
    try:
        from .deepagents import create_deep_agent  # type: ignore
    except ImportError:
        create_deep_agent = None


@dataclass
class StrategyAgent:
    """Agente responsável por executar uma estratégia ponta a ponta."""

    strategy_name: str
    context_name: str
    context_description: str = ""
    orchestrator_prompt: Optional[str] = None
    base_path: Path = BASE_PATH
    processes: List[Dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.strategy_dir = self.base_path / "strategies" / self.strategy_name
        self.drive_dir = self.base_path / "drive" / self.context_name / self.strategy_name
        self.pipeline_dir = self.base_path / "drive" / self.context_name / "_pipeline"
        self.manifest_handler = ManifestHandler(self.pipeline_dir)
        self.definition: Optional[StrategyDefinition] = None

    def bootstrap(self) -> None:
        """Prepara diretórios e carrega metadados da estratégia."""
        self.drive_dir.mkdir(parents=True, exist_ok=True)
        self.pipeline_dir.mkdir(parents=True, exist_ok=True)
        self.definition = load_strategy(self.strategy_dir)
        self.processes = self.definition.processes if self.definition else []

    def build_orchestrator(self) -> Any:
        """Instancia o agente de linguagem responsável pela coordenação."""
        if create_deep_agent is None:
            raise RuntimeError(
                "deepagents não está instalado. Instale antes de executar o orquestrador."
            )
        prompt = self.orchestrator_prompt or (
            self.definition.prompt if self.definition else ""
        )
        tools = [
            "ls",
            "read_file",
            "write_file",
            "glob",
            "edit_file",
            "grep",
        ]
        return create_deep_agent(system_prompt=prompt, tools=tools)

    def run(self) -> None:
        """Executa a estratégia completa, chamando cada subagente definido."""
        raise NotImplementedError("Estratégias precisam implementar o método run().")


@dataclass
class ProcessAgent:
    """Agente dedicado a um único processo operacional."""

    process_code: str
    strategy_name: str
    context_name: str
    context_description: str = ""
    base_path: Path = BASE_PATH
    prompt: Optional[str] = None

    def __post_init__(self) -> None:
        self.process_dir = (
            self.base_path
            / "process"
            / self.strategy_name
            / self.process_code
        )
        self.context_dir = (
            self.base_path
            / "drive"
            / self.context_name
            / self.process_dir.name
        )
        self.context_dir.mkdir(parents=True, exist_ok=True)

    def build_agent(self) -> Any:
        if create_deep_agent is None:
            raise RuntimeError(
                "deepagents não está instalado. Instale antes de executar subagentes."
            )
        return create_deep_agent(system_prompt=self.prompt or "", tools=[
            "ls",
            "read_file",
            "write_file",
            "edit_file",
            "glob",
        ])

    def run(self) -> Dict[str, Any]:
        """Executa o processo e devolve um manifesto com os principais artefatos."""
        raise NotImplementedError("Subagentes precisam implementar run().")
