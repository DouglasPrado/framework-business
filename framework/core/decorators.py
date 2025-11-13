"""
Decoradores úteis para o framework de agents.

Este módulo fornece decoradores para tratamento de erros, logging,
retry logic e outras funcionalidades cross-cutting.
"""

from __future__ import annotations

import functools
import logging
from typing import Any, Callable, Optional, Type, TypeVar

from framework.core.exceptions import AgentError, ProcessExecutionError

logger = logging.getLogger(__name__)

T = TypeVar("T")
F = TypeVar("F", bound=Callable[..., Any])


def handle_agent_errors(
    *,
    error_class: Type[AgentError] = ProcessExecutionError,
    fallback_value: Optional[Any] = None,
    reraise: bool = True,
    log_level: int = logging.ERROR,
) -> Callable[[F], F]:
    """
    Decorador para tratamento consistente de erros em métodos de agents.

    Args:
        error_class: Classe de exceção a ser levantada ao capturar erros
        fallback_value: Valor a retornar em caso de erro (se reraise=False)
        reraise: Se True, relança a exceção após logging. Se False, retorna fallback_value
        log_level: Nível de log para erros capturados

    Returns:
        Decorador configurado

    Example:
        >>> @handle_agent_errors(error_class=ProcessExecutionError, reraise=True)
        ... def run_process(self):
        ...     # código que pode falhar
        ...     pass
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except AgentError:
                # AgentErrors já são bem formatados, apenas propaga
                raise
            except Exception as exc:
                # Captura outras exceções e as envolve em AgentError
                logger.log(
                    log_level,
                    "Erro ao executar %s: %s",
                    func.__name__,
                    exc,
                    exc_info=True,
                )

                if reraise:
                    # Determina contexto do erro (process_code, etc.)
                    context = _extract_context_from_args(args, kwargs)

                    if error_class == ProcessExecutionError and "process_code" in context:
                        raise ProcessExecutionError(
                            process_code=context["process_code"],
                            message=str(exc),
                            stage=func.__name__,
                            original_error=exc,
                        ) from exc
                    else:
                        # Fallback para AgentError genérico
                        raise AgentError(
                            f"Erro em {func.__name__}: {exc}", {"original_error": str(exc)}
                        ) from exc
                else:
                    return fallback_value

        return wrapper  # type: ignore

    return decorator


def _extract_context_from_args(args: tuple, kwargs: dict) -> dict[str, Any]:
    """
    Extrai contexto útil dos argumentos de uma função.

    Procura por atributos comuns como process_code, strategy_name, etc.
    """
    context = {}

    # Tenta extrair de kwargs
    for key in ["process_code", "strategy_name", "context_name"]:
        if key in kwargs:
            context[key] = kwargs[key]

    # Tenta extrair de self (primeiro argumento)
    if args:
        self_obj = args[0]
        for attr in ["process_code", "strategy_name", "context_name"]:
            if hasattr(self_obj, attr):
                context[attr] = getattr(self_obj, attr)

    return context


def log_execution(
    *,
    level: int = logging.INFO,
    include_args: bool = False,
    include_result: bool = False,
) -> Callable[[F], F]:
    """
    Decorador para logging automático de execução de funções.

    Args:
        level: Nível de log a ser usado
        include_args: Se True, inclui argumentos no log
        include_result: Se True, inclui resultado no log

    Returns:
        Decorador configurado

    Example:
        >>> @log_execution(level=logging.DEBUG, include_args=True)
        ... def process_data(self, data):
        ...     return processed_data
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__qualname__

            # Log de início
            if include_args:
                logger.log(
                    level,
                    "Iniciando %s com args=%s, kwargs=%s",
                    func_name,
                    args[1:] if args else (),  # Pula self
                    kwargs,
                )
            else:
                logger.log(level, "Iniciando %s", func_name)

            try:
                result = func(*args, **kwargs)

                # Log de sucesso
                if include_result:
                    logger.log(level, "Concluído %s com resultado: %s", func_name, result)
                else:
                    logger.log(level, "Concluído %s com sucesso", func_name)

                return result

            except Exception as exc:
                logger.log(
                    logging.ERROR,
                    "Erro ao executar %s: %s",
                    func_name,
                    exc,
                    exc_info=True,
                )
                raise

        return wrapper  # type: ignore

    return decorator


def retry_on_failure(
    *,
    max_attempts: int = 3,
    exceptions: tuple[Type[Exception], ...] = (Exception,),
    backoff_factor: float = 1.0,
) -> Callable[[F], F]:
    """
    Decorador para retry automático em caso de falhas.

    Args:
        max_attempts: Número máximo de tentativas
        exceptions: Tupla de exceções que devem acionar retry
        backoff_factor: Fator de backoff exponencial entre tentativas

    Returns:
        Decorador configurado

    Example:
        >>> @retry_on_failure(max_attempts=3, exceptions=(ConnectionError,))
        ... def call_external_api(self):
        ...     return api_response
    """
    import time

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exception = exc
                    if attempt < max_attempts:
                        sleep_time = backoff_factor * (2 ** (attempt - 1))
                        logger.warning(
                            "Tentativa %d/%d de %s falhou: %s. Tentando novamente em %.1fs...",
                            attempt,
                            max_attempts,
                            func.__name__,
                            exc,
                            sleep_time,
                        )
                        time.sleep(sleep_time)
                    else:
                        logger.error(
                            "Todas as %d tentativas de %s falharam",
                            max_attempts,
                            func.__name__,
                        )

            # Se chegou aqui, todas as tentativas falharam
            raise last_exception  # type: ignore

        return wrapper  # type: ignore

    return decorator


__all__ = [
    "handle_agent_errors",
    "log_execution",
    "retry_on_failure",
]
