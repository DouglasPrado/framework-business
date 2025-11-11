"""Fundamentos reutilizáveis para orquestradores e subagentes."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import BASE_PATH
from .utils.manifest import ManifestHandler
from .utils.strategy_loader import StrategyDefinition, load_strategy

try:  # pragma: no cover - dependência externa obrigatória em tempo de execução
    from .deepagents import DeepAgent, create_deep_agent
except ImportError as exc:  # pragma: no cover - falha explícita quando ausente
    raise ImportError(
        "O pacote 'deepagents' é obrigatório para executar os agentes. "
        "Instale-o com 'pip install deepagents'."
    ) from exc


@dataclass
class StrategyAgent:
    """Agente responsável por executar uma estratégia ponta a ponta."""

    strategy_name: str
    context_name: str
    context_description: str = ""
    orchestrator_prompt: Optional[str] = None
    base_path: Path = BASE_PATH
    processes: List[Dict[str, Any]] = field(default_factory=list)
    llm_config: Optional[Dict[str, Any]] = None

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

    def build_orchestrator(self) -> DeepAgent:
        """Instancia o agente de linguagem responsável pela coordenação."""
        if self.orchestrator_agent is not None:
            return self.orchestrator_agent
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
        return create_deep_agent(system_prompt=prompt, tools=tools, llm_config=self.llm_config)

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
    llm_config: Optional[Dict[str, Any]] = None
    language_agent: Optional[DeepAgent] = field(default=None, init=False)

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

    def build_agent(self) -> DeepAgent:
        if self.language_agent is not None:
            return self.language_agent
        self.language_agent = create_deep_agent(system_prompt=self.prompt or "", tools=[
            "ls",
            "read_file",
            "write_file",
            "edit_file",
            "glob",
        ], llm_config=self.llm_config)
        return self.language_agent

    def run(self) -> Dict[str, Any]:
        """Executa o processo e devolve um manifesto com os principais artefatos."""
        raise NotImplementedError("Subagentes precisam implementar run().")
