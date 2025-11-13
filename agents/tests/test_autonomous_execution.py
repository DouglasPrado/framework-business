"""
Tests for autonomous execution system.

Tests the AutonomousAgent and TaskExecutionOrchestrator components.
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch

from agents.framework.core.context import AgentContext
from agents.framework.orchestration.autonomous import (
    AutonomousAgent,
    TaskStep,
    TaskExecutionPlan,
    TaskExecutionResult,
)
from agents.business.strategies.task_execution.orchestrator import TaskExecutionOrchestrator


class TestTaskStep:
    """Tests for TaskStep dataclass."""

    def test_task_step_creation(self):
        """Test creating a TaskStep."""
        step = TaskStep(
            number=1,
            description="Test step",
            tools_needed=["tool1", "tool2"],
            expected_outcome="Success",
        )

        assert step.number == 1
        assert step.description == "Test step"
        assert step.tools_needed == ["tool1", "tool2"]
        assert step.expected_outcome == "Success"
        assert step.status == "pending"
        assert step.result is None
        assert step.error is None


class TestTaskExecutionPlan:
    """Tests for TaskExecutionPlan."""

    def test_plan_creation(self):
        """Test creating an execution plan."""
        steps = [
            TaskStep(1, "Step 1", [], "Outcome 1"),
            TaskStep(2, "Step 2", [], "Outcome 2"),
        ]

        plan = TaskExecutionPlan(
            task_description="Test task",
            complexity="simple",
            estimated_steps=2,
            steps=steps,
        )

        assert plan.task_description == "Test task"
        assert plan.complexity == "simple"
        assert plan.estimated_steps == 2
        assert len(plan.steps) == 2


class TestTaskExecutionResult:
    """Tests for TaskExecutionResult."""

    def test_result_creation(self):
        """Test creating an execution result."""
        plan = TaskExecutionPlan(
            task_description="Test",
            complexity="simple",
            estimated_steps=1,
            steps=[],
        )

        result = TaskExecutionResult(
            task_description="Test task",
            success=True,
            plan=plan,
        )

        assert result.task_description == "Test task"
        assert result.success is True
        assert result.plan == plan

    def test_result_to_dict(self):
        """Test converting result to dictionary."""
        plan = TaskExecutionPlan(
            task_description="Test",
            complexity="simple",
            estimated_steps=2,
            steps=[
                TaskStep(1, "Step 1", [], "Outcome 1", status="completed"),
                TaskStep(2, "Step 2", [], "Outcome 2", status="failed"),
            ],
        )

        result = TaskExecutionResult(
            task_description="Test task",
            success=False,
            plan=plan,
            artifacts_created=[Path("/tmp/test.txt")],
            errors=["Error 1"],
        )

        result_dict = result.to_dict()

        assert result_dict["task_description"] == "Test task"
        assert result_dict["success"] is False
        assert result_dict["complexity"] == "simple"
        assert result_dict["total_steps"] == 2
        assert result_dict["completed_steps"] == 1
        assert result_dict["failed_steps"] == 1
        assert len(result_dict["artifacts_created"]) == 1
        assert len(result_dict["errors"]) == 1


class TestAutonomousAgent:
    """Tests for AutonomousAgent."""

    def test_agent_creation(self):
        """Test creating an autonomous agent."""
        context = AgentContext(
            context_name="Test",
            strategy_name="TaskExecution",
            process_code=None,
            base_path=Path("/tmp"),
        )

        agent = AutonomousAgent(
            context=context,
            task_description="Test task",
            max_iterations=10,
        )

        assert agent.context == context
        assert agent.task_description == "Test task"
        assert agent.max_iterations == 10
        assert agent.enable_recovery is True
        assert len(agent.tools) > 0  # Should have tools loaded

    def test_create_empty_plan(self):
        """Test creating an empty plan."""
        context = AgentContext(
            context_name="Test",
            strategy_name="TaskExecution",
            process_code=None,
            base_path=Path("/tmp"),
        )

        agent = AutonomousAgent(context, "Test task")
        plan = agent._create_empty_plan()

        assert plan.task_description == "Test task"
        assert plan.complexity == "unknown"
        assert plan.estimated_steps == 0
        assert len(plan.steps) == 0

    def test_log_method(self):
        """Test logging method."""
        context = AgentContext(
            context_name="Test",
            strategy_name="TaskExecution",
            process_code=None,
            base_path=Path("/tmp"),
        )

        agent = AutonomousAgent(context, "Test task")
        agent._log("Test message")

        assert len(agent.execution_log) == 1
        assert "Test message" in agent.execution_log[0]


class TestTaskExecutionOrchestrator:
    """Tests for TaskExecutionOrchestrator."""

    def test_orchestrator_creation(self):
        """Test creating an orchestrator."""
        orchestrator = TaskExecutionOrchestrator(
            context_name="TestContext",
            task_description="Test task",
            base_path=Path("/tmp"),
        )

        assert orchestrator.context_name == "TestContext"
        assert orchestrator.task_description == "Test task"
        assert orchestrator.max_iterations == 20
        assert orchestrator.enable_recovery is True

    def test_analyze_task_handler(self):
        """Test analyze_task handler."""
        orchestrator = TaskExecutionOrchestrator(
            context_name="TestContext",
            task_description="Test task",
            base_path=Path("/tmp/test_workspace"),
        )

        state = {
            "context": orchestrator.context,
            "task_description": "Test task",
        }

        updated_state = orchestrator._analyze_task(state)

        assert "workspace_root" in updated_state
        assert "analysis_complete" in updated_state
        assert updated_state["analysis_complete"] is True

    @pytest.mark.skip(reason="Requires LLM API calls - integration test")
    def test_full_execution(self):
        """Integration test for full execution."""
        orchestrator = TaskExecutionOrchestrator(
            context_name="TestExecution",
            task_description="List files in current directory",
            base_path=Path("/tmp/test_full_execution"),
            max_iterations=5,
        )

        result = orchestrator.run()

        assert "success" in result
        assert "task_description" in result
        assert result["task_description"] == "List files in current directory"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
