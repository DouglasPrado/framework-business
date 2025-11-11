"""Fundamentos reutilizáveis para orquestradores e subagentes."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import BASE_PATH
from .config import get_settings
from .tools import get_tools_for_agent


def _compose_llm_config(base_config: Optional[Dict[str, Any]], project_hint: str) -> Dict[str, Any]:
    settings = get_settings(validate=False)
    config = dict(base_config or {})
    observability = dict(config.get("observability") or {})
    if settings.langchain_tracing and "langchain_tracer" not in observability:
        observability["langchain_tracer"] = {
            "project_name": settings.langchain_project or project_hint,
        }
    if settings.langchain_api_key and "langsmith" not in observability:
        observability["langsmith"] = {
            "project_name": settings.langchain_project or project_hint,
        }
    if observability:
        config["observability"] = observability
    return config
from .utils import ManifestHandler, StrategyDefinition, load_strategy

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
    orchestrator_agent: Optional[DeepAgent] = None

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
        tools = get_tools_for_agent("strategy")
        self.orchestrator_agent = create_deep_agent(
            system_prompt=prompt,
            tools=tools,
            llm_config=_compose_llm_config(self.llm_config, self.strategy_name),
        )
        return self.orchestrator_agent

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
    language_agent: Optional[DeepAgent] = None

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
        tools = get_tools_for_agent("process")
        self.language_agent = create_deep_agent(
            system_prompt=self.prompt or "",
            tools=tools,
            llm_config=_compose_llm_config(self.llm_config, f"{self.strategy_name}-{self.process_code}"),
        )
        return self.language_agent

    def run(self) -> Dict[str, Any]:
        """Executa o processo e devolve um manifesto com os principais artefatos."""
        raise NotImplementedError("Subagentes precisam implementar run().")
