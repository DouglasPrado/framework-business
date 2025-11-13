#!/usr/bin/env python3 -u
"""
CLI para executar estratégias usando o novo framework.

Uso:
    python3 agents/scripts/run_strategy_agent.py zeroum MeuProjeto -d "Descrição"
    python3 agents/scripts/run_strategy_agent.py generic MinhaEstrategia -d "Descrição"
"""

import argparse
import sys

# Desabilitar buffering para logs aparecerem em tempo real
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)
import json
import logging
import sys
from pathlib import Path

# Adicionar root ao path
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Carregar variáveis de ambiente do .env ANTES de importar framework
try:
    from dotenv import load_dotenv

    env_file = REPO_ROOT / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        logging.debug(f"Carregado .env de: {env_file}")
except ImportError:
    pass  # dotenv não instalado

from business.strategies.zeroum.orchestrator import ZeroUmOrchestrator
from business.strategies.generic.orchestrator import GenericStrategyOrchestrator


# Registro de estratégias disponíveis
STRATEGIES = {
    "zeroum": {
        "class": ZeroUmOrchestrator,
        "description": "Estratégia ZeroUm para validação de problema/hipótese",
    },
    "generic": {
        "class": GenericStrategyOrchestrator,
        "description": "Estratégia genérica configurável",
    },
}


def configure_logging(verbose: bool = True) -> None:
    """Configura logging detalhado."""
    level = logging.INFO if verbose else logging.WARNING

    # Criar handler com flush automático
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)-40s | %(message)s",
        datefmt="%H:%M:%S"
    ))

    # Forçar flush imediato
    handler.flush = lambda: sys.stdout.flush()

    # Configurar root logger
    logging.basicConfig(
        level=level,
        handlers=[handler],
        force=True
    )

    # Aumentar nível de log do httpx para reduzir ruído
    logging.getLogger("httpx").setLevel(logging.WARNING)


def run_zeroum(context_name: str, context_description: str) -> dict:
    """Executa estratégia ZeroUm."""
    orchestrator = ZeroUmOrchestrator(
        context_name=context_name,
        context_description=context_description,
    )
    return orchestrator.run()


def run_generic(strategy_name: str, context_name: str, context_description: str) -> dict:
    """Executa estratégia Generic."""
    orchestrator = GenericStrategyOrchestrator(
        strategy_name=strategy_name,
        context_name=context_name,
        context_description=context_description,
    )
    return orchestrator.run()


def main() -> None:
    """Função principal do CLI."""
    parser = argparse.ArgumentParser(
        description="Executa estratégias de agentes usando o framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s zeroum MeuProjeto -d "Plataforma SaaS para PMEs"
  %(prog)s generic MinhaEstrategia Projeto -d "Descrição do projeto"

Estratégias disponíveis:
  zeroum   - Validação de problema/hipótese
  generic  - Estratégia genérica configurável
        """,
    )

    parser.add_argument(
        "strategy",
        choices=STRATEGIES.keys(),
        help="Nome da estratégia a executar",
    )

    parser.add_argument(
        "context",
        help="Nome do contexto (será usado como nome de pasta)",
    )

    parser.add_argument(
        "-d",
        "--description",
        dest="context_description",
        default="",
        help="Descrição detalhada do contexto/projeto",
    )

    parser.add_argument(
        "-s",
        "--strategy-name",
        dest="strategy_name",
        help="Nome da estratégia (apenas para 'generic')",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Modo silencioso (apenas warnings)",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Arquivo para salvar resultado JSON",
    )

    args = parser.parse_args()

    # Configurar logging
    configure_logging(verbose=not args.quiet)
    logger = logging.getLogger(__name__)

    # Validar argumentos específicos
    if args.strategy == "generic" and not args.strategy_name:
        parser.error("estratégia 'generic' requer --strategy-name")

    # Preparar contexto
    context_name = args.context
    context_description = args.context_description or args.context

    logger.info("=" * 80)
    logger.info("Framework Business - Executor de Estratégias")
    logger.info("=" * 80)
    logger.info("Estratégia: %s", args.strategy)
    logger.info("Contexto: %s", context_name)
    logger.info("Descrição: %s", context_description)
    logger.info("=" * 80)

    # Executar estratégia
    try:
        if args.strategy == "zeroum":
            result = run_zeroum(context_name, context_description)
        elif args.strategy == "generic":
            result = run_generic(
                args.strategy_name,
                context_name,
                context_description,
            )
        else:
            parser.error(f"Estratégia não implementada: {args.strategy}")

        # Exibir resultados
        logger.info("")
        logger.info("=" * 80)
        logger.info("EXECUÇÃO CONCLUÍDA COM SUCESSO")
        logger.info("=" * 80)

        # Informações do orquestrador dinâmico (se disponível)
        if "selected_subagent" in result:
            logger.info("")
            logger.info("DECISÃO DO ORQUESTRADOR:")
            logger.info("  Complexidade detectada: %s", result.get("complexity", "N/A"))
            logger.info("  Subagente selecionado: %s", result.get("selected_subagent", "N/A"))

        # Manifests dos subagentes
        manifests = result.get("manifests", [])
        if manifests:
            logger.info("")
            logger.info("SUBAGENTES EXECUTADOS:")
            for i, manifest in enumerate(manifests, 1):
                logger.info("  %d. %s", i, manifest.get("process", "desconhecido"))
                logger.info("     Status: %s", manifest.get("status", "desconhecido"))
                if "started_at" in manifest:
                    logger.info("     Início: %s", manifest.get("started_at"))
                if "completed_at" in manifest:
                    logger.info("     Fim: %s", manifest.get("completed_at"))
                if "notes" in manifest:
                    logger.info("     Notas: %s", manifest.get("notes"))

                # Estágios executados
                stages = manifest.get("stages", {})
                if stages:
                    logger.info("     Estágios executados: %d", len(stages))
                    for stage_name, stage_data in stages.items():
                        status_emoji = "✓" if stage_data.get("status") == "completed" else "✗"
                        logger.info("       %s %s", status_emoji, stage_name)

                # Artefatos gerados
                artifacts = manifest.get("artifacts", [])
                if artifacts:
                    logger.info("     Artefatos gerados: %d arquivos", len(artifacts))

        logger.info("")
        logger.info("ARQUIVOS GERADOS:")
        logger.info("  Consolidado: %s", result.get("consolidated", "N/A"))
        logger.info("  Pacote ZIP: %s", result.get("archive", "N/A"))

        metrics = result.get("metrics", {})
        if metrics:
            logger.info("")
            logger.info("MÉTRICAS:")
            for key, value in metrics.items():
                logger.info("  %s: %s", key, value)

        # Salvar resultado em arquivo se solicitado
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(
                json.dumps(result, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            logger.info("Resultado salvo em: %s", output_path)

        # Exibir resultado JSON no stdout (para scripts)
        if args.quiet:
            print(json.dumps(result, indent=2, ensure_ascii=False))

        return 0

    except Exception as e:
        logger.error("Erro na execução: %s", e, exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
