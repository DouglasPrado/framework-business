"""
Execution tools for autonomous agent operations.

Provides shell command execution, git operations, and file system operations
with security controls and audit logging.
"""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from typing import List, Optional

from langchain_core.tools import StructuredTool

logger = logging.getLogger(__name__)

# Security: Whitelist of allowed commands
ALLOWED_COMMANDS = {
    # Git operations
    "git status",
    "git diff",
    "git add",
    "git commit",
    "git log",
    "git branch",
    "git checkout",
    # File operations
    "ls",
    "cat",
    "head",
    "tail",
    "wc",
    "find",
    "grep",
    # Python operations
    "python",
    "python3",
    "pip",
    "pytest",
    # Node operations
    "npm",
    "node",
    # Build tools
    "make",
    "docker",
}

# Security: Blacklist of dangerous command patterns
DANGEROUS_PATTERNS = [
    "rm -rf /",
    "rm -rf *",
    ":(){ :|:& };:",  # Fork bomb
    "dd if=",
    "mkfs",
    "format",
    "> /dev/",
    "wget",
    "curl",
]


def _is_command_safe(command: str) -> tuple[bool, str]:
    """
    Check if command is safe to execute.

    Args:
        command: Shell command to validate

    Returns:
        Tuple of (is_safe, reason)
    """
    command_lower = command.lower().strip()

    # Check for dangerous patterns
    for pattern in DANGEROUS_PATTERNS:
        if pattern in command_lower:
            return False, f"Comando contém padrão perigoso: {pattern}"

    # Check if command starts with allowed prefix
    for allowed in ALLOWED_COMMANDS:
        if command_lower.startswith(allowed):
            return True, "Comando permitido"

    return False, f"Comando não está na whitelist. Permitidos: {', '.join(sorted(ALLOWED_COMMANDS))}"


def _run_command(
    command: str,
    cwd: Optional[str] = None,
    timeout: int = 30,
    check: bool = False,
) -> str:
    """
    Execute shell command with safety controls.

    Args:
        command: Command to execute
        cwd: Working directory (default: current)
        timeout: Timeout in seconds (default: 30)
        check: Raise exception on non-zero exit (default: False)

    Returns:
        Command output (stdout + stderr)

    Raises:
        ValueError: If command is not safe
        subprocess.TimeoutExpired: If command times out
        subprocess.CalledProcessError: If check=True and command fails
    """
    # Security check
    is_safe, reason = _is_command_safe(command)
    if not is_safe:
        raise ValueError(f"Comando bloqueado por segurança: {reason}")

    # Audit log
    logger.info(f"Executando comando: {command}")
    if cwd:
        logger.info(f"  Diretório: {cwd}")

    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=check,
        )

        output = result.stdout
        if result.stderr:
            output += f"\n[STDERR]\n{result.stderr}"

        logger.info(f"Comando concluído (exit code: {result.returncode})")
        return output

    except subprocess.TimeoutExpired as e:
        logger.error(f"Comando excedeu timeout de {timeout}s")
        raise
    except subprocess.CalledProcessError as e:
        logger.error(f"Comando falhou com exit code {e.returncode}")
        raise
    except Exception as e:
        logger.error(f"Erro ao executar comando: {e}")
        raise


def _git_status(cwd: Optional[str] = None) -> str:
    """
    Get git repository status.

    Args:
        cwd: Repository directory (default: current)

    Returns:
        Git status output
    """
    return _run_command("git status", cwd=cwd)


def _git_diff(file: Optional[str] = None, cwd: Optional[str] = None) -> str:
    """
    Show git diff.

    Args:
        file: Specific file to diff (default: all changes)
        cwd: Repository directory (default: current)

    Returns:
        Git diff output
    """
    command = f"git diff {file}" if file else "git diff"
    return _run_command(command, cwd=cwd)


def _git_add(files: List[str], cwd: Optional[str] = None) -> str:
    """
    Add files to git staging area.

    Args:
        files: List of file paths to add
        cwd: Repository directory (default: current)

    Returns:
        Command output
    """
    files_str = " ".join(files)
    return _run_command(f"git add {files_str}", cwd=cwd)


def _git_commit(message: str, cwd: Optional[str] = None) -> str:
    """
    Create git commit.

    Args:
        message: Commit message
        cwd: Repository directory (default: current)

    Returns:
        Commit output
    """
    # Escape quotes in message
    safe_message = message.replace('"', '\\"')
    return _run_command(f'git commit -m "{safe_message}"', cwd=cwd)


def _git_log(limit: int = 10, cwd: Optional[str] = None) -> str:
    """
    Show git commit log.

    Args:
        limit: Number of commits to show (default: 10)
        cwd: Repository directory (default: current)

    Returns:
        Git log output
    """
    return _run_command(f"git log --oneline -n {limit}", cwd=cwd)


def _mkdir(path: str, parents: bool = True) -> str:
    """
    Create directory.

    Args:
        path: Directory path to create
        parents: Create parent directories if needed (default: True)

    Returns:
        Success message
    """
    path_obj = Path(path)

    if path_obj.exists():
        return f"Diretório já existe: {path}"

    try:
        path_obj.mkdir(parents=parents, exist_ok=True)
        logger.info(f"Diretório criado: {path}")
        return f"Diretório criado com sucesso: {path}"
    except Exception as e:
        logger.error(f"Erro ao criar diretório {path}: {e}")
        raise ValueError(f"Erro ao criar diretório: {e}")


def _rm(path: str, recursive: bool = False, force: bool = False) -> str:
    """
    Remove file or directory.

    Args:
        path: Path to remove
        recursive: Remove directories recursively (default: False)
        force: Force removal without confirmation (default: False)

    Returns:
        Success message

    Raises:
        ValueError: If trying to remove dangerous paths
    """
    path_obj = Path(path).resolve()

    # Security: prevent removing system directories
    dangerous_paths = ["/", "/etc", "/usr", "/var", "/bin", "/sbin", "/home"]
    if str(path_obj) in dangerous_paths or path_obj.parent in [Path(p) for p in dangerous_paths]:
        raise ValueError(f"Bloqueado: não é permitido remover path do sistema: {path}")

    if not path_obj.exists():
        return f"Path não existe: {path}"

    # Confirmation required for recursive removal
    if recursive and not force:
        raise ValueError(
            f"Remoção recursiva requer confirmação explícita (force=True): {path}"
        )

    try:
        if path_obj.is_file():
            path_obj.unlink()
            logger.info(f"Arquivo removido: {path}")
            return f"Arquivo removido: {path}"
        elif path_obj.is_dir() and recursive:
            import shutil
            shutil.rmtree(path_obj)
            logger.info(f"Diretório removido recursivamente: {path}")
            return f"Diretório removido recursivamente: {path}"
        else:
            raise ValueError(f"Path é diretório, use recursive=True: {path}")
    except Exception as e:
        logger.error(f"Erro ao remover {path}: {e}")
        raise ValueError(f"Erro ao remover: {e}")


def _mv(source: str, dest: str) -> str:
    """
    Move or rename file/directory.

    Args:
        source: Source path
        dest: Destination path

    Returns:
        Success message
    """
    source_path = Path(source)
    dest_path = Path(dest)

    if not source_path.exists():
        raise ValueError(f"Path de origem não existe: {source}")

    try:
        source_path.rename(dest_path)
        logger.info(f"Movido: {source} -> {dest}")
        return f"Movido com sucesso: {source} -> {dest}"
    except Exception as e:
        logger.error(f"Erro ao mover {source} para {dest}: {e}")
        raise ValueError(f"Erro ao mover: {e}")


def _run_python(script_path: str, args: Optional[str] = None, cwd: Optional[str] = None) -> str:
    """
    Execute Python script.

    Args:
        script_path: Path to Python script
        args: Command-line arguments (default: None)
        cwd: Working directory (default: current)

    Returns:
        Script output
    """
    command = f"python3 {script_path}"
    if args:
        command += f" {args}"
    return _run_command(command, cwd=cwd, timeout=60)


def _run_tests(test_path: Optional[str] = None, cwd: Optional[str] = None) -> str:
    """
    Run pytest tests.

    Args:
        test_path: Specific test file/directory (default: all tests)
        cwd: Working directory (default: current)

    Returns:
        Test output
    """
    command = f"pytest {test_path}" if test_path else "pytest"
    return _run_command(command, cwd=cwd, timeout=120)


# Create LangChain tools
run_command_tool = StructuredTool.from_function(
    _run_command,
    name="run_command",
    description="""Execute shell command with safety controls.

    Use this to run allowed shell commands. Commands must be in whitelist:
    git, ls, cat, head, tail, wc, find, grep, python, pytest, npm, make, docker.

    Examples:
    - run_command("git status")
    - run_command("ls -la", cwd="/path/to/dir")
    - run_command("python3 script.py", timeout=60)

    Returns command output (stdout + stderr).
    """
)

git_status_tool = StructuredTool.from_function(
    _git_status,
    name="git_status",
    description="Get current git repository status. Shows modified files, staged changes, and branch info."
)

git_diff_tool = StructuredTool.from_function(
    _git_diff,
    name="git_diff",
    description="Show git diff. Pass file path to see changes in specific file, or omit to see all changes."
)

git_add_tool = StructuredTool.from_function(
    _git_add,
    name="git_add",
    description="Add files to git staging area. Pass list of file paths. Example: git_add(['file1.py', 'file2.py'])"
)

git_commit_tool = StructuredTool.from_function(
    _git_commit,
    name="git_commit",
    description="Create git commit with message. Example: git_commit('Add new feature')"
)

git_log_tool = StructuredTool.from_function(
    _git_log,
    name="git_log",
    description="Show git commit history. Specify limit for number of commits to show (default: 10)."
)

mkdir_tool = StructuredTool.from_function(
    _mkdir,
    name="mkdir",
    description="Create directory. Pass path and optionally parents=True to create parent dirs."
)

rm_tool = StructuredTool.from_function(
    _rm,
    name="rm",
    description="""Remove file or directory.

    IMPORTANT: Recursive removal requires force=True for safety.
    Examples:
    - rm('file.txt')  # Remove file
    - rm('dir/', recursive=True, force=True)  # Remove directory

    Dangerous paths (/, /etc, /usr, etc) are blocked.
    """
)

mv_tool = StructuredTool.from_function(
    _mv,
    name="mv",
    description="Move or rename file/directory. Example: mv('old_name.txt', 'new_name.txt')"
)

run_python_tool = StructuredTool.from_function(
    _run_python,
    name="run_python",
    description="Execute Python script. Example: run_python('script.py', args='--verbose', cwd='/path')"
)

run_tests_tool = StructuredTool.from_function(
    _run_tests,
    name="run_tests",
    description="Run pytest tests. Specify test_path for specific file/dir, or omit to run all tests."
)


# Export all execution tools
EXECUTION_TOOLS = [
    run_command_tool,
    git_status_tool,
    git_diff_tool,
    git_add_tool,
    git_commit_tool,
    git_log_tool,
    mkdir_tool,
    rm_tool,
    mv_tool,
    run_python_tool,
    run_tests_tool,
]


__all__ = [
    "EXECUTION_TOOLS",
    "run_command_tool",
    "git_status_tool",
    "git_diff_tool",
    "git_add_tool",
    "git_commit_tool",
    "git_log_tool",
    "mkdir_tool",
    "rm_tool",
    "mv_tool",
    "run_python_tool",
    "run_tests_tool",
]
