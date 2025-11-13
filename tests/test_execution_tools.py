"""
Tests for execution tools.

Tests security controls and tool functionality.
"""

import pytest
from pathlib import Path

from framework.security.controls import (
    SecurityConfig,
    CommandValidator,
    PathValidator,
    RateLimiter,
)


class TestSecurityConfig:
    """Tests for SecurityConfig."""

    def test_default_config(self):
        """Test default security configuration."""
        config = SecurityConfig()

        assert len(config.allowed_commands) > 0
        assert "git" in config.allowed_commands
        assert "python" in config.allowed_commands
        assert len(config.dangerous_patterns) > 0
        assert "rm -rf /" in config.dangerous_patterns
        assert len(config.blocked_paths) > 0
        assert "/" in config.blocked_paths

    def test_custom_config(self):
        """Test custom security configuration."""
        config = SecurityConfig(
            allowed_commands={"git", "ls"},
            max_commands_per_minute=10,
        )

        assert len(config.allowed_commands) == 2
        assert config.max_commands_per_minute == 10


class TestCommandValidator:
    """Tests for CommandValidator."""

    def test_validate_allowed_command(self):
        """Test validating allowed command."""
        validator = CommandValidator()

        is_safe, reason = validator.validate("git status")
        assert is_safe is True
        assert "permitido" in reason.lower()

    def test_validate_dangerous_command(self):
        """Test blocking dangerous command."""
        validator = CommandValidator()

        is_safe, reason = validator.validate("rm -rf /")
        assert is_safe is False
        assert "perigoso" in reason.lower()

    def test_validate_non_whitelisted_command(self):
        """Test blocking non-whitelisted command."""
        validator = CommandValidator()

        is_safe, reason = validator.validate("curl http://example.com")
        assert is_safe is False
        assert "whitelist" in reason.lower()

    def test_requires_confirmation(self):
        """Test confirmation requirement check."""
        validator = CommandValidator()

        assert validator.requires_confirmation("rm -rf somedir") is True
        assert validator.requires_confirmation("git push --force") is True
        assert validator.requires_confirmation("git status") is False

    def test_audit_log(self):
        """Test audit logging."""
        validator = CommandValidator()

        validator.validate("git status")
        validator.validate("rm -rf /")

        audit_log = validator.get_audit_log()
        assert len(audit_log) == 2
        assert audit_log[0]["action"] == "ALLOWED"
        assert audit_log[1]["action"] == "BLOCKED"


class TestPathValidator:
    """Tests for PathValidator."""

    def test_validate_safe_path(self):
        """Test validating safe path."""
        validator = PathValidator()

        is_safe, reason = validator.validate("/tmp/test.txt")
        assert is_safe is True

    def test_validate_blocked_path(self):
        """Test blocking system paths."""
        validator = PathValidator()

        is_safe, reason = validator.validate("/etc/passwd")
        assert is_safe is False
        assert "blocked" in reason.lower() or "system" in reason.lower()

    def test_validate_write_to_directory(self):
        """Test validating write operation."""
        validator = PathValidator()

        # Writing to non-existent file should be safe
        is_safe, reason = validator.validate_write("/tmp/new_file.txt")
        assert is_safe is True

        # Writing to system directory should fail
        is_safe, reason = validator.validate_write("/etc/test.txt")
        assert is_safe is False

    def test_validate_delete_important_directory(self):
        """Test blocking deletion of important directories."""
        validator = PathValidator()

        # Deleting .git should be blocked
        is_safe, reason = validator.validate_delete("/tmp/project/.git", recursive=True)
        assert is_safe is False
        assert "important" in reason.lower()


class TestRateLimiter:
    """Tests for RateLimiter."""

    def test_rate_limit_within_limit(self):
        """Test operations within rate limit."""
        limiter = RateLimiter(max_per_minute=5)

        for i in range(5):
            assert limiter.check_and_record("test_operation") is True

    def test_rate_limit_exceeded(self):
        """Test rate limit exceeded."""
        limiter = RateLimiter(max_per_minute=3)

        # First 3 should pass
        for i in range(3):
            assert limiter.check_and_record("test_operation") is True

        # 4th should fail
        assert limiter.check_and_record("test_operation") is False

    def test_get_current_rate(self):
        """Test getting current rate."""
        limiter = RateLimiter(max_per_minute=10)

        limiter.check_and_record("test")
        limiter.check_and_record("test")

        assert limiter.get_current_rate("test") == 2

    def test_reset_limiter(self):
        """Test resetting rate limiter."""
        limiter = RateLimiter(max_per_minute=3)

        for i in range(3):
            limiter.check_and_record("test")

        # Should be at limit
        assert limiter.check_and_record("test") is False

        # Reset
        limiter.reset("test")

        # Should work again
        assert limiter.check_and_record("test") is True

    def test_different_operation_types(self):
        """Test different operation types have separate limits."""
        limiter = RateLimiter(max_per_minute=2)

        limiter.check_and_record("operation_a")
        limiter.check_and_record("operation_a")

        # operation_a is at limit
        assert limiter.check_and_record("operation_a") is False

        # operation_b still has capacity
        assert limiter.check_and_record("operation_b") is True


class TestExecutionTools:
    """Tests for execution tools."""

    @pytest.mark.skip(reason="Requires actual command execution")
    def test_git_status_tool(self):
        """Integration test for git_status tool."""
        from framework.tools.builtin.execution import _git_status

        # Only run if in a git repository
        if Path(".git").exists():
            result = _git_status()
            assert isinstance(result, str)
            assert len(result) > 0

    @pytest.mark.skip(reason="Requires actual file system")
    def test_mkdir_tool(self):
        """Integration test for mkdir tool."""
        from framework.tools.builtin.execution import _mkdir

        test_dir = Path("/tmp/test_mkdir_tool")

        if test_dir.exists():
            import shutil
            shutil.rmtree(test_dir)

        result = _mkdir(str(test_dir))
        assert "sucesso" in result.lower()
        assert test_dir.exists()

        # Cleanup
        test_dir.rmdir()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
