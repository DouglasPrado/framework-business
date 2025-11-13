"""
Security controls for autonomous agent operations.

Provides validators, rate limiters, and safety checks for:
- Command execution
- File system operations
- Path access
- Resource usage
"""

from __future__ import annotations

import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class SecurityConfig:
    """
    Security configuration for autonomous operations.

    Attributes:
        allowed_commands: Whitelist of allowed command prefixes
        dangerous_patterns: Blacklist of dangerous command patterns
        blocked_paths: Paths that cannot be accessed
        require_confirmation_patterns: Patterns requiring user confirmation
        max_commands_per_minute: Rate limit for command execution
        enable_audit_log: Enable comprehensive audit logging
    """

    allowed_commands: Set[str] = field(default_factory=lambda: {
        "git", "ls", "cat", "head", "tail", "wc", "find", "grep",
        "python", "python3", "pip", "pytest", "npm", "node", "make", "docker"
    })

    dangerous_patterns: List[str] = field(default_factory=lambda: [
        "rm -rf /",
        "rm -rf *",
        ":(){ :|:& };:",  # Fork bomb
        "dd if=",
        "mkfs",
        "format",
        "> /dev/",
        "wget",
        "curl",
        "chmod 777",
        "chown",
        "sudo",
        "su -",
    ])

    blocked_paths: Set[str] = field(default_factory=lambda: {
        "/", "/etc", "/usr", "/bin", "/sbin", "/var", "/boot",
        "/sys", "/proc", "/dev", "/root"
    })

    require_confirmation_patterns: List[str] = field(default_factory=lambda: [
        "rm -rf",
        "git push --force",
        "git push -f",
        "DROP TABLE",
        "DELETE FROM",
    ])

    max_commands_per_minute: int = 30
    enable_audit_log: bool = True
    audit_log_path: Optional[Path] = None


class CommandValidator:
    """
    Validates shell commands against security policies.

    Example:
        >>> validator = CommandValidator(config)
        >>> is_safe, reason = validator.validate("git status")
        >>> print(is_safe)
        True
    """

    def __init__(self, config: Optional[SecurityConfig] = None):
        """
        Initialize validator.

        Args:
            config: Security configuration (default: SecurityConfig())
        """
        self.config = config or SecurityConfig()
        self.audit_entries: List[Dict[str, str]] = []

    def validate(self, command: str) -> tuple[bool, str]:
        """
        Validate command against security policy.

        Args:
            command: Shell command to validate

        Returns:
            Tuple of (is_safe, reason)
        """
        command_lower = command.lower().strip()

        # Check for dangerous patterns
        for pattern in self.config.dangerous_patterns:
            if pattern.lower() in command_lower:
                reason = f"Comando contém padrão perigoso: {pattern}"
                self._audit("BLOCKED", command, reason)
                return False, reason

        # Check if command starts with allowed prefix
        command_first_word = command_lower.split()[0] if command_lower.split() else ""

        for allowed in self.config.allowed_commands:
            if command_first_word == allowed or command_lower.startswith(allowed + " "):
                self._audit("ALLOWED", command, "Command in whitelist")
                return True, "Comando permitido"

        # Command not in whitelist
        allowed_list = ", ".join(sorted(self.config.allowed_commands))
        reason = f"Comando não está na whitelist. Permitidos: {allowed_list}"
        self._audit("BLOCKED", command, reason)
        return False, reason

    def requires_confirmation(self, command: str) -> bool:
        """
        Check if command requires user confirmation.

        Args:
            command: Shell command

        Returns:
            True if confirmation required
        """
        command_lower = command.lower()

        for pattern in self.config.require_confirmation_patterns:
            if pattern.lower() in command_lower:
                self._audit("CONFIRMATION_REQUIRED", command, f"Matches pattern: {pattern}")
                return True

        return False

    def _audit(self, action: str, command: str, reason: str):
        """Record audit entry."""
        if self.config.enable_audit_log:
            entry = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "action": action,
                "command": command,
                "reason": reason,
            }
            self.audit_entries.append(entry)
            logger.info(f"[AUDIT] {action}: {command} - {reason}")

            # Write to audit file if configured
            if self.config.audit_log_path:
                try:
                    with open(self.config.audit_log_path, "a", encoding="utf-8") as f:
                        f.write(f"{entry['timestamp']} | {action} | {command} | {reason}\n")
                except Exception as e:
                    logger.error(f"Failed to write audit log: {e}")

    def get_audit_log(self) -> List[Dict[str, str]]:
        """Get all audit entries."""
        return self.audit_entries.copy()


class PathValidator:
    """
    Validates file system paths against security policies.

    Example:
        >>> validator = PathValidator(config)
        >>> is_safe, reason = validator.validate("/home/user/file.txt")
        >>> print(is_safe)
        True
    """

    def __init__(self, config: Optional[SecurityConfig] = None):
        """
        Initialize validator.

        Args:
            config: Security configuration
        """
        self.config = config or SecurityConfig()

    def validate(self, path: str) -> tuple[bool, str]:
        """
        Validate path against security policy.

        Args:
            path: File system path to validate

        Returns:
            Tuple of (is_safe, reason)
        """
        try:
            path_obj = Path(path).resolve()
        except Exception as e:
            return False, f"Invalid path: {e}"

        # Check if path is in blocked list
        for blocked in self.config.blocked_paths:
            blocked_path = Path(blocked).resolve()

            # Check exact match or parent match
            if path_obj == blocked_path or blocked_path in path_obj.parents:
                return False, f"Path is blocked: {blocked}"

        # Additional check: prevent accessing system directories
        path_str = str(path_obj)
        if path_str.startswith(("/etc/", "/usr/", "/bin/", "/sbin/")):
            return False, f"System directory access blocked: {path_str}"

        return True, "Path allowed"

    def validate_write(self, path: str) -> tuple[bool, str]:
        """
        Validate path for write operations (stricter).

        Args:
            path: Path to write to

        Returns:
            Tuple of (is_safe, reason)
        """
        # First, check basic validation
        is_safe, reason = self.validate(path)
        if not is_safe:
            return is_safe, reason

        try:
            path_obj = Path(path).resolve()

            # Check if trying to write to root or system dirs
            if path_obj.parent == Path("/"):
                return False, "Cannot write to root directory"

            # Check if path exists and is a directory
            if path_obj.exists() and path_obj.is_dir():
                return False, "Cannot write to existing directory (specify file path)"

            return True, "Path safe for writing"

        except Exception as e:
            return False, f"Path validation error: {e}"

    def validate_delete(self, path: str, recursive: bool = False) -> tuple[bool, str]:
        """
        Validate path for delete operations (strictest).

        Args:
            path: Path to delete
            recursive: Whether deletion is recursive

        Returns:
            Tuple of (is_safe, reason)
        """
        # Basic validation
        is_safe, reason = self.validate(path)
        if not is_safe:
            return is_safe, reason

        try:
            path_obj = Path(path).resolve()

            # Prevent deleting important directories even if not in blocked list
            important_dirs = [
                ".git",
                "node_modules",
                ".env",
                "venv",
                ".venv",
            ]

            if path_obj.name in important_dirs:
                return False, f"Cannot delete important directory: {path_obj.name}"

            # If recursive deletion, be extra careful
            if recursive:
                # Prevent deleting entire project roots
                markers = [".git", "package.json", "pyproject.toml", "setup.py"]
                if any((path_obj / marker).exists() for marker in markers):
                    return False, "Cannot recursively delete project root"

                # Warn about large recursive deletions
                logger.warning(f"Recursive deletion requested for: {path}")

            return True, "Path safe for deletion"

        except Exception as e:
            return False, f"Path validation error: {e}"


class RateLimiter:
    """
    Rate limiter for command execution and resource usage.

    Example:
        >>> limiter = RateLimiter(max_per_minute=30)
        >>> if limiter.check_and_record("command_execution"):
        ...     execute_command()
        ... else:
        ...     print("Rate limit exceeded")
    """

    def __init__(self, max_per_minute: int = 30):
        """
        Initialize rate limiter.

        Args:
            max_per_minute: Maximum operations per minute
        """
        self.max_per_minute = max_per_minute
        self.operations: Dict[str, List[float]] = defaultdict(list)

    def check_and_record(self, operation_type: str) -> bool:
        """
        Check if operation is within rate limit and record it.

        Args:
            operation_type: Type of operation (e.g., "command_execution")

        Returns:
            True if within limit, False if exceeded
        """
        now = time.time()
        cutoff = now - 60  # 60 seconds ago

        # Remove old operations
        self.operations[operation_type] = [
            ts for ts in self.operations[operation_type]
            if ts > cutoff
        ]

        # Check if limit exceeded
        if len(self.operations[operation_type]) >= self.max_per_minute:
            logger.warning(
                f"Rate limit exceeded for {operation_type}: "
                f"{len(self.operations[operation_type])}/{self.max_per_minute} per minute"
            )
            return False

        # Record new operation
        self.operations[operation_type].append(now)
        return True

    def get_current_rate(self, operation_type: str) -> int:
        """
        Get current operation count in last minute.

        Args:
            operation_type: Type of operation

        Returns:
            Number of operations in last 60 seconds
        """
        now = time.time()
        cutoff = now - 60

        self.operations[operation_type] = [
            ts for ts in self.operations[operation_type]
            if ts > cutoff
        ]

        return len(self.operations[operation_type])

    def reset(self, operation_type: Optional[str] = None):
        """
        Reset rate limiter.

        Args:
            operation_type: Specific operation to reset, or None for all
        """
        if operation_type:
            self.operations[operation_type] = []
        else:
            self.operations.clear()


# Global default instances
_default_command_validator = None
_default_path_validator = None
_default_rate_limiter = None


def get_command_validator() -> CommandValidator:
    """Get global default command validator."""
    global _default_command_validator
    if _default_command_validator is None:
        _default_command_validator = CommandValidator()
    return _default_command_validator


def get_path_validator() -> PathValidator:
    """Get global default path validator."""
    global _default_path_validator
    if _default_path_validator is None:
        _default_path_validator = PathValidator()
    return _default_path_validator


def get_rate_limiter() -> RateLimiter:
    """Get global default rate limiter."""
    global _default_rate_limiter
    if _default_rate_limiter is None:
        _default_rate_limiter = RateLimiter()
    return _default_rate_limiter


__all__ = [
    "SecurityConfig",
    "CommandValidator",
    "PathValidator",
    "RateLimiter",
    "get_command_validator",
    "get_path_validator",
    "get_rate_limiter",
]
