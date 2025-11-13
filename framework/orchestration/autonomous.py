"""
Autonomous Agent for task execution.

Provides LLM-driven autonomous execution of complex tasks using all available tools.
The agent plans, executes, validates, and recovers from errors automatically.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from framework.core.context import AgentContext
from framework.llm.factory import build_llm
from framework.tools.registry import AgentType, get_tools

logger = logging.getLogger(__name__)


@dataclass
class TaskStep:
    """Single step in task execution plan."""

    number: int
    description: str
    tools_needed: List[str]
    expected_outcome: str
    status: str = "pending"  # pending, in_progress, completed, failed
    result: Optional[str] = None
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


@dataclass
class TaskExecutionPlan:
    """Execution plan created by LLM."""

    task_description: str
    complexity: str  # simple, moderate, complex
    estimated_steps: int
    steps: List[TaskStep] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class TaskExecutionResult:
    """Result of autonomous task execution."""

    task_description: str
    success: bool
    plan: TaskExecutionPlan
    execution_log: List[str] = field(default_factory=list)
    artifacts_created: List[Path] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    started_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "task_description": self.task_description,
            "success": self.success,
            "complexity": self.plan.complexity,
            "total_steps": len(self.plan.steps),
            "completed_steps": sum(1 for s in self.plan.steps if s.status == "completed"),
            "failed_steps": sum(1 for s in self.plan.steps if s.status == "failed"),
            "artifacts_created": [str(p) for p in self.artifacts_created],
            "errors": self.errors,
            "duration_seconds": (
                (self.completed_at - self.started_at).total_seconds()
                if self.completed_at else None
            ),
        }


class AutonomousAgent:
    """
    Autonomous agent that executes tasks using LLM-driven planning and tool execution.

    The agent:
    1. Analyzes task description
    2. Creates execution plan with steps
    3. Executes each step using available tools
    4. Validates results after each step
    5. Recovers from errors automatically
    6. Returns structured result

    Example:
        >>> agent = AutonomousAgent(context, "Analyze Python files and create report")
        >>> result = agent.execute()
        >>> print(result.success)
        True
    """

    def __init__(
        self,
        context: AgentContext,
        task_description: str,
        max_iterations: int = 20,
        enable_recovery: bool = True,
    ):
        """
        Initialize autonomous agent.

        Args:
            context: Agent context with workspace information
            task_description: Natural language task description
            max_iterations: Maximum steps to execute (safety limit)
            enable_recovery: Enable automatic error recovery
        """
        self.context = context
        self.task_description = task_description
        self.max_iterations = max_iterations
        self.enable_recovery = enable_recovery

        # Initialize LLM with all tools
        self.llm = build_llm({
            "model": "gpt-4o-mini",
            "temperature": 0.3,  # Lower temp for more deterministic planning
        })

        # Get all available tools (AUTONOMOUS has access to everything)
        self.tools = get_tools(AgentType.AUTONOMOUS)
        logger.info(f"AutonomousAgent initialized with {len(self.tools)} tools")
        logger.info(f"Available tools: {[tool.name for tool in self.tools]}")

        # Execution state
        self.plan: Optional[TaskExecutionPlan] = None
        self.execution_log: List[str] = []
        self.artifacts: List[Path] = []
        self.errors: List[str] = []

    def execute(self) -> TaskExecutionResult:
        """
        Execute task autonomously.

        Returns:
            TaskExecutionResult with success status and details
        """
        started_at = datetime.now()
        logger.info(f"Starting autonomous execution: {self.task_description}")

        try:
            # Step 1: Analyze task and create plan
            self._log("Analyzing task...")
            self.plan = self._analyze_and_plan()
            self._log(f"Plan created with {len(self.plan.steps)} steps")

            # Step 2: Execute plan step by step
            self._log("Executing plan...")
            success = self._execute_plan()

            # Step 3: Create result
            result = TaskExecutionResult(
                task_description=self.task_description,
                success=success,
                plan=self.plan,
                execution_log=self.execution_log,
                artifacts_created=self.artifacts,
                errors=self.errors,
                started_at=started_at,
                completed_at=datetime.now(),
            )

            logger.info(f"Execution completed: success={success}")
            return result

        except Exception as e:
            logger.error(f"Fatal error during execution: {e}", exc_info=True)
            self.errors.append(f"Fatal error: {str(e)}")

            return TaskExecutionResult(
                task_description=self.task_description,
                success=False,
                plan=self.plan or self._create_empty_plan(),
                execution_log=self.execution_log,
                artifacts_created=self.artifacts,
                errors=self.errors,
                started_at=started_at,
                completed_at=datetime.now(),
            )

    def _analyze_and_plan(self) -> TaskExecutionPlan:
        """
        Analyze task and create execution plan using LLM.

        Returns:
            TaskExecutionPlan with steps
        """
        available_tools = [tool.name for tool in self.tools]

        prompt = f"""You are an autonomous agent tasked with planning and executing: {self.task_description}

Available tools:
{chr(10).join(f"- {tool}" for tool in available_tools)}

Analyze the task and create a detailed execution plan.

Respond ONLY with a JSON object in this format:
{{
  "complexity": "simple|moderate|complex",
  "estimated_steps": 5,
  "steps": [
    {{
      "number": 1,
      "description": "Step description",
      "tools_needed": ["tool1", "tool2"],
      "expected_outcome": "What should result from this step"
    }}
  ]
}}

Be specific and actionable. Each step should be concrete.
"""

        response = self.llm.invoke(prompt)
        response_text = response.content if hasattr(response, "content") else str(response)

        # Parse JSON response
        try:
            # Extract JSON from response (handle markdown code blocks)
            json_text = response_text
            if "```json" in json_text:
                json_text = json_text.split("```json")[1].split("```")[0]
            elif "```" in json_text:
                json_text = json_text.split("```")[1].split("```")[0]

            plan_data = json.loads(json_text.strip())

            # Create TaskStep objects
            steps = [
                TaskStep(
                    number=step["number"],
                    description=step["description"],
                    tools_needed=step.get("tools_needed", []),
                    expected_outcome=step.get("expected_outcome", ""),
                )
                for step in plan_data.get("steps", [])
            ]

            plan = TaskExecutionPlan(
                task_description=self.task_description,
                complexity=plan_data.get("complexity", "moderate"),
                estimated_steps=plan_data.get("estimated_steps", len(steps)),
                steps=steps,
            )

            logger.info(f"Plan created: {plan.complexity} complexity, {len(steps)} steps")
            return plan

        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to parse plan from LLM: {e}")
            logger.debug(f"LLM response: {response_text}")

            # Fallback: create simple plan
            return TaskExecutionPlan(
                task_description=self.task_description,
                complexity="simple",
                estimated_steps=1,
                steps=[
                    TaskStep(
                        number=1,
                        description=self.task_description,
                        tools_needed=[],
                        expected_outcome="Task completed",
                    )
                ],
            )

    def _execute_plan(self) -> bool:
        """
        Execute plan step by step.

        Returns:
            True if all steps completed successfully
        """
        if not self.plan:
            self.errors.append("No plan to execute")
            return False

        for step in self.plan.steps:
            if len(self.execution_log) >= self.max_iterations:
                self._log(f"Reached max iterations ({self.max_iterations}), stopping")
                self.errors.append("Exceeded maximum iterations")
                return False

            self._log(f"Step {step.number}/{len(self.plan.steps)}: {step.description}")

            try:
                step.status = "in_progress"
                step.started_at = datetime.now()

                # Execute step using LLM with tools
                result = self._execute_step(step)

                step.status = "completed"
                step.result = result
                step.completed_at = datetime.now()

                self._log(f"  ✓ Step {step.number} completed")

            except Exception as e:
                logger.error(f"Step {step.number} failed: {e}", exc_info=True)
                step.status = "failed"
                step.error = str(e)
                step.completed_at = datetime.now()

                self._log(f"  ✗ Step {step.number} failed: {e}")
                self.errors.append(f"Step {step.number} failed: {e}")

                # Try to recover if enabled
                if self.enable_recovery:
                    self._log(f"  Attempting recovery...")
                    if not self._attempt_recovery(step):
                        self._log(f"  Recovery failed, stopping execution")
                        return False
                else:
                    return False

        # Check if all steps completed
        completed = sum(1 for s in self.plan.steps if s.status == "completed")
        total = len(self.plan.steps)

        return completed == total

    def _execute_step(self, step: TaskStep) -> str:
        """
        Execute single step using LLM with tools.

        Args:
            step: Step to execute

        Returns:
            Step result as string
        """
        # Build context from previous steps
        previous_results = []
        for i, prev_step in enumerate(self.plan.steps[:step.number - 1]):
            if prev_step.status == "completed":
                previous_results.append(
                    f"Step {prev_step.number}: {prev_step.description}\n"
                    f"Result: {prev_step.result}"
                )

        context_text = "\n\n".join(previous_results) if previous_results else "No previous steps"

        prompt = f"""You are executing step {step.number} of a task plan.

Task: {self.task_description}

Current Step:
Description: {step.description}
Tools needed: {', '.join(step.tools_needed) if step.tools_needed else 'Any available tools'}
Expected outcome: {step.expected_outcome}

Previous steps results:
{context_text}

Execute this step using the available tools. Be specific and thorough.
Return a summary of what was done and the result.
"""

        # Bind tools to LLM
        llm_with_tools = self.llm.bind_tools(self.tools)
        response = llm_with_tools.invoke(prompt)

        result_text = response.content if hasattr(response, "content") else str(response)

        # Check if tools were called
        if hasattr(response, "tool_calls") and response.tool_calls:
            self._log(f"  Tools called: {[tc.get('name') for tc in response.tool_calls]}")

        return result_text

    def _attempt_recovery(self, failed_step: TaskStep) -> bool:
        """
        Attempt to recover from failed step.

        Args:
            failed_step: Step that failed

        Returns:
            True if recovery succeeded
        """
        logger.info(f"Attempting recovery for step {failed_step.number}")

        prompt = f"""Step {failed_step.number} failed with error: {failed_step.error}

Step description: {failed_step.description}
Expected outcome: {failed_step.expected_outcome}

Analyze the error and suggest a recovery action. Can this step be:
1. Retried with different parameters?
2. Skipped (if not critical)?
3. Replaced with an alternative approach?

Respond with JSON:
{{
  "can_recover": true/false,
  "action": "retry|skip|alternative",
  "reasoning": "explanation"
}}
"""

        try:
            response = self.llm.invoke(prompt)
            response_text = response.content if hasattr(response, "content") else str(response)

            # Parse recovery decision
            if "```json" in response_text:
                json_text = response_text.split("```json")[1].split("```")[0]
            else:
                json_text = response_text

            recovery_data = json.loads(json_text.strip())

            if recovery_data.get("can_recover"):
                action = recovery_data.get("action")
                reasoning = recovery_data.get("reasoning", "No reasoning provided")

                self._log(f"  Recovery action: {action} - {reasoning}")

                if action == "skip":
                    failed_step.status = "skipped"
                    return True
                elif action in ["retry", "alternative"]:
                    # Try executing step again
                    try:
                        result = self._execute_step(failed_step)
                        failed_step.status = "completed"
                        failed_step.result = result
                        failed_step.error = None
                        self._log(f"  Recovery successful!")
                        return True
                    except Exception as e:
                        logger.error(f"Recovery attempt failed: {e}")
                        return False

            return False

        except Exception as e:
            logger.error(f"Recovery analysis failed: {e}")
            return False

    def _log(self, message: str):
        """Add message to execution log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.execution_log.append(log_entry)
        logger.info(message)

    def _create_empty_plan(self) -> TaskExecutionPlan:
        """Create empty plan for error cases."""
        return TaskExecutionPlan(
            task_description=self.task_description,
            complexity="unknown",
            estimated_steps=0,
            steps=[],
        )


__all__ = [
    "AutonomousAgent",
    "TaskStep",
    "TaskExecutionPlan",
    "TaskExecutionResult",
]
