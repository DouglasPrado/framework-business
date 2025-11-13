"""
Exceções customizadas para o framework de agents.

Este módulo define uma hierarquia de exceções específicas para o sistema,
facilitando tratamento de erros e debugging.
"""

from __future__ import annotations

from typing import Any, Optional


class AgentError(Exception):
    """
    Exceção base para todos os erros relacionados aos agents.

    Todas as exceções específicas do framework devem herdar desta classe.
    """

    def __init__(self, message: str, details: Optional[dict[str, Any]] = None) -> None:
        """
        Inicializa a exceção com mensagem e detalhes opcionais.

        Args:
            message: Mensagem descritiva do erro
            details: Dicionário com informações adicionais sobre o erro
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        """Retorna representação string da exceção."""
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} ({details_str})"
        return self.message


# ============================================================================
# Configuration Errors
# ============================================================================


class ConfigurationError(AgentError):
    """Erro relacionado a configurações inválidas ou ausentes."""

    pass


class MissingConfigError(ConfigurationError):
    """Configuração obrigatória está ausente."""

    def __init__(self, config_name: str, hint: Optional[str] = None) -> None:
        message = f"Configuração obrigatória ausente: {config_name}"
        if hint:
            message += f". {hint}"
        super().__init__(message, {"config_name": config_name})


class InvalidConfigError(ConfigurationError):
    """Configuração possui valor inválido."""

    def __init__(
        self, config_name: str, value: Any, reason: Optional[str] = None
    ) -> None:
        message = f"Configuração inválida: {config_name}={value}"
        if reason:
            message += f". Razão: {reason}"
        super().__init__(
            message, {"config_name": config_name, "value": value, "reason": reason}
        )


# ============================================================================
# LLM Errors
# ============================================================================


class LLMError(AgentError):
    """Erro base para problemas relacionados a LLMs."""

    pass


class LLMInvocationError(LLMError):
    """Erro ao invocar o LLM."""

    def __init__(
        self,
        message: str,
        model: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        details = {}
        if model:
            details["model"] = model
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(message, details)
        self.original_error = original_error


class LLMResponseError(LLMError):
    """Resposta do LLM está em formato inválido ou inesperado."""

    def __init__(
        self, message: str, response: Optional[str] = None, expected: Optional[str] = None
    ) -> None:
        details = {}
        if response:
            # Limita o tamanho da resposta para não poluir logs
            details["response"] = response[:200] + "..." if len(response) > 200 else response
        if expected:
            details["expected"] = expected
        super().__init__(message, details)


# ============================================================================
# Process Errors
# ============================================================================


class ProcessError(AgentError):
    """Erro base para problemas na execução de processos."""

    pass


class ProcessNotFoundError(ProcessError):
    """Processo solicitado não foi encontrado."""

    def __init__(self, process_code: str, strategy: Optional[str] = None) -> None:
        message = f"Processo não encontrado: {process_code}"
        if strategy:
            message += f" na estratégia {strategy}"
        super().__init__(message, {"process_code": process_code, "strategy": strategy})


class ProcessExecutionError(ProcessError):
    """Erro durante a execução de um processo."""

    def __init__(
        self,
        process_code: str,
        message: str,
        stage: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        full_message = f"Erro ao executar processo {process_code}: {message}"
        details = {"process_code": process_code}
        if stage:
            details["stage"] = stage
            full_message += f" (stage: {stage})"
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(full_message, details)
        self.original_error = original_error


class ProcessValidationError(ProcessError):
    """Validação de processo falhou."""

    def __init__(
        self, process_code: str, validation_errors: list[str]
    ) -> None:
        message = f"Validação falhou para processo {process_code}"
        super().__init__(
            message,
            {"process_code": process_code, "validation_errors": validation_errors},
        )


# ============================================================================
# Strategy Errors
# ============================================================================


class StrategyError(AgentError):
    """Erro base para problemas relacionados a estratégias."""

    pass


class StrategyNotFoundError(StrategyError):
    """Estratégia solicitada não foi encontrada."""

    def __init__(self, strategy_name: str) -> None:
        message = f"Estratégia não encontrada: {strategy_name}"
        super().__init__(message, {"strategy_name": strategy_name})


class StrategyExecutionError(StrategyError):
    """Erro durante a execução de uma estratégia."""

    def __init__(
        self,
        strategy_name: str,
        message: str,
        original_error: Optional[Exception] = None,
    ) -> None:
        full_message = f"Erro ao executar estratégia {strategy_name}: {message}"
        details = {"strategy_name": strategy_name}
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(full_message, details)
        self.original_error = original_error


# ============================================================================
# File/IO Errors
# ============================================================================


class FileOperationError(AgentError):
    """Erro em operações de arquivo."""

    def __init__(
        self,
        operation: str,
        path: str,
        reason: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        message = f"Erro na operação '{operation}' no arquivo {path}"
        if reason:
            message += f": {reason}"
        details = {"operation": operation, "path": path}
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(message, details)
        self.original_error = original_error


# ============================================================================
# Tool Errors
# ============================================================================


class ToolError(AgentError):
    """Erro base para problemas com ferramentas (tools)."""

    pass


class ToolNotFoundError(ToolError):
    """Ferramenta solicitada não existe."""

    def __init__(self, tool_name: str, available_tools: Optional[list[str]] = None) -> None:
        message = f"Ferramenta não encontrada: {tool_name}"
        details = {"tool_name": tool_name}
        if available_tools:
            message += f". Ferramentas disponíveis: {', '.join(available_tools)}"
            details["available_tools"] = available_tools
        super().__init__(message, details)


class ToolExecutionError(ToolError):
    """Erro ao executar uma ferramenta."""

    def __init__(
        self,
        tool_name: str,
        message: str,
        original_error: Optional[Exception] = None,
    ) -> None:
        full_message = f"Erro ao executar ferramenta {tool_name}: {message}"
        details = {"tool_name": tool_name}
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(full_message, details)
        self.original_error = original_error


__all__ = [
    # Base
    "AgentError",
    # Configuration
    "ConfigurationError",
    "MissingConfigError",
    "InvalidConfigError",
    # LLM
    "LLMError",
    "LLMInvocationError",
    "LLMResponseError",
    # Process
    "ProcessError",
    "ProcessNotFoundError",
    "ProcessExecutionError",
    "ProcessValidationError",
    # Strategy
    "StrategyError",
    "StrategyNotFoundError",
    "StrategyExecutionError",
    # File/IO
    "FileOperationError",
    # Tools
    "ToolError",
    "ToolNotFoundError",
    "ToolExecutionError",
]
