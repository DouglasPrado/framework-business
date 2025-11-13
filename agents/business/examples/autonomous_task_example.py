"""
Example: Autonomous Task Execution

Demonstrates how to use the autonomous task execution system to perform
complex tasks using LLM-driven planning and execution.
"""

import logging
from pathlib import Path

from agents.business.strategies.task_execution.orchestrator import TaskExecutionOrchestrator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)


def example_1_simple_file_analysis():
    """Example 1: Simple file analysis task."""
    print("\n" + "=" * 80)
    print("Example 1: Analyze Python files in framework/tools")
    print("=" * 80 + "\n")

    orchestrator = TaskExecutionOrchestrator(
        context_name="ToolsAnalysis",
        task_description="Read all Python files in agents/framework/tools and list their main functions",
        max_iterations=10,
    )

    result = orchestrator.run()

    print(f"\nSuccess: {result['success']}")
    print(f"Complexity: {result['complexity']}")
    print(f"Steps executed: {result['plan_summary']['total_steps']}")
    print(f"Report: {result['consolidated']}")


def example_2_git_operations():
    """Example 2: Git operations task."""
    print("\n" + "=" * 80)
    print("Example 2: Git repository analysis")
    print("=" * 80 + "\n")

    orchestrator = TaskExecutionOrchestrator(
        context_name="GitAnalysis",
        task_description="Check git status, show last 5 commits, and summarize recent changes",
        max_iterations=15,
    )

    result = orchestrator.run()

    print(f"\nSuccess: {result['success']}")
    print(f"Execution log entries: {len(result['execution_log'])}")

    if result['execution_log']:
        print("\nExecution Log (last 10 entries):")
        for entry in result['execution_log'][-10:]:
            print(f"  {entry}")


def example_3_directory_exploration():
    """Example 3: Directory structure exploration."""
    print("\n" + "=" * 80)
    print("Example 3: Explore and document directory structure")
    print("=" * 80 + "\n")

    orchestrator = TaskExecutionOrchestrator(
        context_name="DirectoryExploration",
        task_description=(
            "Explore the agents/framework directory structure, "
            "identify all modules, and create a summary of the architecture"
        ),
        max_iterations=20,
    )

    result = orchestrator.run()

    print(f"\nSuccess: {result['success']}")
    print(f"Artifacts created: {len(result.get('artifacts', []))}")

    if result.get('artifacts'):
        print("\nArtifacts:")
        for artifact in result['artifacts']:
            print(f"  - {artifact}")


def example_4_with_error_recovery():
    """Example 4: Task with intentional error to demonstrate recovery."""
    print("\n" + "=" * 80)
    print("Example 4: Task with error recovery")
    print("=" * 80 + "\n")

    orchestrator = TaskExecutionOrchestrator(
        context_name="ErrorRecoveryDemo",
        task_description=(
            "Try to read a file that doesn't exist (nonexistent.txt), "
            "then recover by listing available files instead"
        ),
        max_iterations=10,
        enable_recovery=True,
    )

    result = orchestrator.run()

    print(f"\nSuccess: {result['success']}")
    print(f"Errors encountered: {len(result.get('errors', []))}")

    if result.get('errors'):
        print("\nErrors:")
        for error in result['errors']:
            print(f"  ! {error}")

    print(f"\nRecovery {'successful' if result['success'] else 'failed'}")


if __name__ == "__main__":
    print("\nAutonomous Task Execution Examples")
    print("=" * 80)

    # Run examples
    # Note: Uncomment the examples you want to run

    # example_1_simple_file_analysis()
    # example_2_git_operations()
    # example_3_directory_exploration()
    # example_4_with_error_recovery()

    print("\nTo run examples, uncomment the function calls in __main__")
    print("Or run individual functions directly:")
    print("  python -c 'from autonomous_task_example import example_1_simple_file_analysis; example_1_simple_file_analysis()'")
