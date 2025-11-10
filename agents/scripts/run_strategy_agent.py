"""CLI simples para acionar um orquestrador de estratégia."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from agents.registry import STRATEGY_REGISTRY


def main() -> None:
    parser = argparse.ArgumentParser(description="Executa um agente de estratégia baseado em LANGCHAIN.MD")
    parser.add_argument("strategy", choices=STRATEGY_REGISTRY.keys(), help="Nome da estratégia (ZeroUm, Branding, MVPBuilder, Naming)")
    parser.add_argument("context", help="Nome CamelCase usado em drive/<Contexto>/")
    parser.add_argument(
        "--context-description",
        "-d",
        dest="context_description",
        default="",
        help="Descrição textual do projeto que servirá de base para os agentes",
    )
    args = parser.parse_args()

    factory = STRATEGY_REGISTRY[args.strategy]
    description = args.context_description or args.context
    orchestrator = factory(args.context, description)
    result = orchestrator.run()
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
