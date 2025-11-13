"""
Task Execution Orchestrator.

Orchestrates autonomous task execution using AutonomousAgent with comprehensive
observability and result packaging.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from agents.framework.core.context import AgentContext
from agents.framework.io.package import PackageService
from agents.framework.io.workspace import WorkspaceManager
from agents.framework.observability.metrics import MetricsCollector
from agents.framework.orchestration.autonomous import AutonomousAgent, TaskExecutionResult
from agents.framework.orchestration.graph import OrchestrationGraph

logger = logging.getLogger(__name__)


class TaskExecutionOrchestrator:
    """
    Orchestrator for autonomous task execution.

    Provides high-level orchestration of task execution with:
    - Task analysis and classification
    - Plan creation and validation
    - Autonomous execution with monitoring
    - Result validation and packaging
    - Comprehensive reporting

    Example:
        >>> orchestrator = TaskExecutionOrchestrator(
        ...     context_name="CodeAnalysis",
        ...     task_description="Analyze all Python files and create complexity report"
        ... )
        >>> result = orchestrator.run()
        >>> print(result['success'])
        True
    """

    def __init__(
        self,
        context_name: str,
        task_description: str,
        base_path: Optional[Path] = None,
        max_iterations: int = 20,
        enable_recovery: bool = True,
    ):
        """
        Initialize orchestrator.

        Args:
            context_name: Name for workspace (CamelCase)
            task_description: Natural language task description
            base_path: Base path for workspace (default: drive/)
            max_iterations: Maximum execution steps
            enable_recovery: Enable automatic error recovery
        """
        self.context_name = context_name
        self.task_description = task_description
        self.max_iterations = max_iterations
        self.enable_recovery = enable_recovery

        # Create context
        if base_path is None:
            base_path = Path.cwd() / "drive"

        self.context = AgentContext(
            context_name=context_name,
            context_description=task_description,
            strategy_name="TaskExecution",
            process_code=None,
            base_path=base_path,
            metadata={
                "task": task_description,
                "created_at": datetime.now().isoformat(),
            },
        )

        # Initialize services
        self.workspace = WorkspaceManager(self.context)
        self.package_service = PackageService(self.context)
        self.metrics = MetricsCollector()

        logger.info(f"TaskExecutionOrchestrator initialized: {context_name}")
        logger.info(f"Task: {task_description}")

    def run(self) -> Dict[str, Any]:
        """
        Execute task orchestration.

        Returns:
            Dictionary with results:
                - success: bool
                - task_description: str
                - complexity: str
                - plan_summary: dict
                - execution_log: list
                - artifacts: list
                - consolidated: str (path)
                - archive: str (path)
                - metrics: dict
        """
        logger.info("Starting task execution orchestration...")
        self.metrics.start_timer("total_execution")

        # Create orchestration graph
        graph = OrchestrationGraph.from_handlers({
            "analyze_task": self._analyze_task,
            "execute_task": self._execute_task,
            "validate_result": self._validate_result,
            "package_results": self._package_results,
        })

        # Add edges (linear flow)
        graph.add_edge("analyze_task", "execute_task")
        graph.add_edge("execute_task", "validate_result")
        graph.add_edge("validate_result", "package_results")

        # Execute graph
        initial_state = {
            "context": self.context,
            "task_description": self.task_description,
        }

        try:
            final_state = graph.execute(initial_state)

            self.metrics.stop_timer("total_execution")

            # Build result
            result = {
                "success": final_state.get("success", False),
                "task_description": self.task_description,
                "complexity": final_state.get("complexity", "unknown"),
                "plan_summary": final_state.get("plan_summary", {}),
                "execution_log": final_state.get("execution_log", []),
                "artifacts": final_state.get("artifacts", []),
                "consolidated": final_state.get("consolidated"),
                "archive": final_state.get("archive"),
                "metrics": self.metrics.get_summary(),
                "errors": final_state.get("errors", []),
            }

            logger.info(f"Orchestration completed: success={result['success']}")
            return result

        except Exception as e:
            logger.error(f"Orchestration failed: {e}", exc_info=True)
            self.metrics.stop_timer("total_execution")

            return {
                "success": False,
                "task_description": self.task_description,
                "error": str(e),
                "metrics": self.metrics.get_summary(),
            }

    def _analyze_task(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze task and classify complexity.

        Args:
            state: Current execution state

        Returns:
            Updated state with analysis
        """
        logger.info("Analyzing task...")
        self.metrics.start_timer("task_analysis")

        # For now, we let the AutonomousAgent do the analysis
        # This handler just logs and prepares workspace

        workspace_root = self.workspace.ensure_workspace_root()
        logger.info(f"Workspace created: {workspace_root}")

        state["workspace_root"] = workspace_root
        state["analysis_complete"] = True

        self.metrics.stop_timer("task_analysis")
        return state

    def _execute_task(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute task using AutonomousAgent.

        Args:
            state: Current execution state

        Returns:
            Updated state with execution results
        """
        logger.info("Executing task autonomously...")
        self.metrics.start_timer("task_execution")

        # Create autonomous agent
        agent = AutonomousAgent(
            context=self.context,
            task_description=self.task_description,
            max_iterations=self.max_iterations,
            enable_recovery=self.enable_recovery,
        )

        # Execute
        result: TaskExecutionResult = agent.execute()

        # Store results in state
        state["execution_result"] = result
        state["success"] = result.success
        state["complexity"] = result.plan.complexity if result.plan else "unknown"
        state["execution_log"] = result.execution_log
        state["artifacts"] = [str(p) for p in result.artifacts_created]
        state["errors"] = result.errors

        # Store plan summary
        if result.plan:
            state["plan_summary"] = {
                "total_steps": len(result.plan.steps),
                "completed": sum(1 for s in result.plan.steps if s.status == "completed"),
                "failed": sum(1 for s in result.plan.steps if s.status == "failed"),
                "skipped": sum(1 for s in result.plan.steps if s.status == "skipped"),
            }

        logger.info(f"Task execution completed: success={result.success}")
        self.metrics.stop_timer("task_execution")

        return state

    def _validate_result(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate execution results.

        Args:
            state: Current execution state

        Returns:
            Updated state with validation
        """
        logger.info("Validating results...")
        self.metrics.start_timer("validation")

        result: TaskExecutionResult = state.get("execution_result")

        if not result:
            state["validation_passed"] = False
            state["validation_errors"] = ["No execution result found"]
            self.metrics.stop_timer("validation")
            return state

        validation_errors = []

        # Check if execution succeeded
        if not result.success:
            validation_errors.append("Execution failed")

        # Check if errors occurred
        if result.errors:
            validation_errors.extend(result.errors)

        # Check if plan had steps
        if result.plan and len(result.plan.steps) == 0:
            validation_errors.append("Plan had no steps")

        # Check if any steps failed
        if result.plan:
            failed_steps = [s for s in result.plan.steps if s.status == "failed"]
            if failed_steps:
                validation_errors.append(
                    f"{len(failed_steps)} steps failed: "
                    + ", ".join(f"Step {s.number}" for s in failed_steps)
                )

        state["validation_passed"] = len(validation_errors) == 0
        state["validation_errors"] = validation_errors

        if state["validation_passed"]:
            logger.info("Validation passed ✓")
        else:
            logger.warning(f"Validation failed: {validation_errors}")

        self.metrics.stop_timer("validation")
        return state

    def _package_results(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Package results into consolidated report and archive.

        Args:
            state: Current execution state

        Returns:
            Updated state with packaged results
        """
        logger.info("Packaging results...")
        self.metrics.start_timer("packaging")

        result: TaskExecutionResult = state.get("execution_result")

        if not result:
            logger.warning("No execution result to package")
            self.metrics.stop_timer("packaging")
            return state

        # Create consolidated report
        consolidated_path = self._write_consolidated_report(result)
        state["consolidated"] = str(consolidated_path)
        logger.info(f"Consolidated report: {consolidated_path}")

        # Create archive
        try:
            archive_path = self.package_service.package_strategy_artifacts(
                output_name=f"{self.context_name}_TaskExecution_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )
            state["archive"] = str(archive_path)
            logger.info(f"Archive created: {archive_path}")
        except Exception as e:
            logger.error(f"Failed to create archive: {e}")
            state["archive"] = None

        self.metrics.stop_timer("packaging")
        return state

    def _write_consolidated_report(self, result: TaskExecutionResult) -> Path:
        """
        Write consolidated execution report.

        Args:
            result: Task execution result

        Returns:
            Path to consolidated report
        """
        report_lines = [
            f"# Task Execution Report - {self.context_name}",
            "",
            f"**Task:** {result.task_description}",
            f"**Status:** {'✓ Success' if result.success else '✗ Failed'}",
            f"**Started:** {result.started_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Completed:** {result.completed_at.strftime('%Y-%m-%d %H:%M:%S') if result.completed_at else 'N/A'}",
            "",
        ]

        # Add duration
        if result.completed_at:
            duration = (result.completed_at - result.started_at).total_seconds()
            report_lines.append(f"**Duration:** {duration:.1f} seconds")
            report_lines.append("")

        # Add plan summary
        if result.plan:
            report_lines.extend([
                "## Execution Plan",
                "",
                f"**Complexity:** {result.plan.complexity}",
                f"**Total Steps:** {len(result.plan.steps)}",
                f"**Completed:** {sum(1 for s in result.plan.steps if s.status == 'completed')}",
                f"**Failed:** {sum(1 for s in result.plan.steps if s.status == 'failed')}",
                "",
                "### Steps",
                "",
            ])

            for step in result.plan.steps:
                status_icon = {
                    "completed": "✓",
                    "failed": "✗",
                    "skipped": "⊘",
                    "pending": "○",
                }[step.status]

                report_lines.append(f"{step.number}. [{status_icon}] {step.description}")
                if step.tools_needed:
                    report_lines.append(f"   Tools: {', '.join(step.tools_needed)}")
                if step.error:
                    report_lines.append(f"   Error: {step.error}")
                report_lines.append("")

        # Add execution log
        if result.execution_log:
            report_lines.extend([
                "## Execution Log",
                "",
                "```",
                *result.execution_log,
                "```",
                "",
            ])

        # Add errors
        if result.errors:
            report_lines.extend([
                "## Errors",
                "",
                *[f"- {error}" for error in result.errors],
                "",
            ])

        # Add artifacts
        if result.artifacts_created:
            report_lines.extend([
                "## Artifacts Created",
                "",
                *[f"- {artifact}" for artifact in result.artifacts_created],
                "",
            ])

        # Write report
        report_content = "\n".join(report_lines)
        report_path = self.workspace.ensure_workspace_root() / "00-execution-report.MD"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report_content, encoding="utf-8")

        return report_path


__all__ = ["TaskExecutionOrchestrator"]
