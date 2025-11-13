#!/usr/bin/env python3
"""
CLI para execução autônoma de tarefas usando LLM.

Este script permite executar tarefas complexas de forma autônoma, onde o LLM:
1. Analisa a tarefa e cria um plano
2. Executa o plano usando todas as tools disponíveis
3. Valida resultados e recupera de erros
4. Gera relatório consolidado

Exemplo de uso:
    python agents/scripts/run_autonomous_task.py \\
        --task "Analyze all Python files in agents/business and create complexity report" \\
        --context "CodeAnalysis"
"""

import argparse
import logging
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from business.strategies.task_execution.orchestrator import TaskExecutionOrchestrator


def configure_logging(verbose: bool = False):
    """
    Configure logging for CLI.

    Args:
        verbose: Enable verbose (DEBUG) logging
    """
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)-40s | %(message)s",
        datefmt="%H:%M:%S",
    )

    # Suppress noisy loggers
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def print_header():
    """Print CLI header."""
    print("=" * 80)
    print("Framework Business - Autonomous Task Execution".center(80))
    print("=" * 80)
    print()


def print_result_summary(result: dict):
    """
    Print formatted result summary.

    Args:
        result: Execution result dictionary
    """
    print()
    print("=" * 80)
    print("EXECUTION SUMMARY".center(80))
    print("=" * 80)
    print()

    # Status
    status = "✓ SUCCESS" if result["success"] else "✗ FAILED"
    print(f"Status: {status}")
    print()

    # Task info
    print(f"Task: {result['task_description']}")
    print(f"Complexity: {result.get('complexity', 'unknown')}")
    print()

    # Plan summary
    if "plan_summary" in result:
        summary = result["plan_summary"]
        print("Plan Execution:")
        print(f"  Total steps: {summary.get('total_steps', 0)}")
        print(f"  Completed: {summary.get('completed', 0)}")
        print(f"  Failed: {summary.get('failed', 0)}")
        print(f"  Skipped: {summary.get('skipped', 0)}")
        print()

    # Artifacts
    if result.get("artifacts"):
        print(f"Artifacts created: {len(result['artifacts'])}")
        for artifact in result["artifacts"][:5]:  # Show first 5
            print(f"  - {artifact}")
        if len(result["artifacts"]) > 5:
            print(f"  ... and {len(result['artifacts']) - 5} more")
        print()

    # Files
    if result.get("consolidated"):
        print(f"Consolidated report: {result['consolidated']}")
    if result.get("archive"):
        print(f"Archive: {result['archive']}")
    print()

    # Errors
    if result.get("errors"):
        print("Errors:")
        for error in result["errors"]:
            print(f"  ! {error}")
        print()

    # Metrics
    if result.get("metrics"):
        metrics = result["metrics"]
        if "total_execution" in metrics:
            total_time = metrics["total_execution"].get("total", 0)
            print(f"Total execution time: {total_time:.2f}s")
        print()

    print("=" * 80)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Execute tasks autonomously using LLM-driven planning and execution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze code complexity
  python agents/scripts/run_autonomous_task.py \\
      --task "Analyze all Python files in agents/business and create complexity report" \\
      --context "CodeAnalysis"

  # Generate documentation
  python agents/scripts/run_autonomous_task.py \\
      --task "Read all markdown files in docs/ and create a table of contents" \\
      --context "DocsTOC"

  # Run tests and analyze results
  python agents/scripts/run_autonomous_task.py \\
      --task "Run pytest tests and summarize failures" \\
      --context "TestAnalysis" \\
      --max-iterations 30
        """,
    )

    parser.add_argument(
        "--task",
        "-t",
        required=True,
        help="Natural language description of task to execute",
    )

    parser.add_argument(
        "--context",
        "-c",
        required=True,
        help="Context name for workspace (CamelCase, e.g., 'CodeAnalysis')",
    )

    parser.add_argument(
        "--max-iterations",
        "-m",
        type=int,
        default=20,
        help="Maximum execution steps (default: 20)",
    )

    parser.add_argument(
        "--no-recovery",
        action="store_true",
        help="Disable automatic error recovery",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    parser.add_argument(
        "--base-path",
        "-b",
        type=Path,
        default=None,
        help="Base path for workspace (default: drive/)",
    )

    args = parser.parse_args()

    # Configure logging
    configure_logging(args.verbose)

    # Print header
    print_header()

    # Show configuration
    logger = logging.getLogger(__name__)
    logger.info(f"Task: {args.task}")
    logger.info(f"Context: {args.context}")
    logger.info(f"Max iterations: {args.max_iterations}")
    logger.info(f"Recovery: {'disabled' if args.no_recovery else 'enabled'}")
    print()

    try:
        # Create orchestrator
        orchestrator = TaskExecutionOrchestrator(
            context_name=args.context,
            task_description=args.task,
            base_path=args.base_path,
            max_iterations=args.max_iterations,
            enable_recovery=not args.no_recovery,
        )

        # Execute
        logger.info("Starting autonomous execution...")
        result = orchestrator.run()

        # Print summary
        print_result_summary(result)

        # Exit with appropriate code
        sys.exit(0 if result["success"] else 1)

    except KeyboardInterrupt:
        print()
        logger.warning("Execution interrupted by user")
        sys.exit(130)

    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        print()
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
