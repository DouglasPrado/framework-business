"""CLI simples para acionar um orquestrador de estratégia."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from agents.registry import STRATEGY_REGISTRY  # noqa: E402
from agents.utils.context import normalize_context_name  # noqa: E402

LOGGER_NAME = "agents.cli"


def configure_logging(verbose: bool = True) -> None:
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )


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
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Reduz o nível de log para avisos apenas.",
    )
    args = parser.parse_args()

    configure_logging(verbose=not args.quiet)
    logger = logging.getLogger(LOGGER_NAME)

    context_name = normalize_context_name(args.context)
    if context_name != args.context:
        logger.info("Contexto normalizado de '%s' para '%s'", args.context, context_name)

    description = args.context_description or args.context
    logger.info("Iniciando estratégia %s para o contexto %s", args.strategy, context_name)
    logger.info("Descrição resumida do contexto: %s", description)

    factory = STRATEGY_REGISTRY[args.strategy]
    orchestrator = factory(context_name, description)
    result = orchestrator.run()

    logger.info("Execução concluída. Consolidado disponível em %s", result["consolidated"])
    logger.info("Artefatos compactados em %s", result["archive"])
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
