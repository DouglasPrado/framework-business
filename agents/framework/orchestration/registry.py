"""
Sistema de registro de plugins para orquestradores e estratégias.

Este módulo implementa um registry dinâmico que suporta descoberta automática
via setuptools entrypoints e registro programático.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Dict, List, Optional

from agents.framework.core.exceptions import StrategyNotFoundError

logger = logging.getLogger(__name__)


# =============================================================================
# Plugin Metadata
# =============================================================================


class PluginMetadata:
    """
    Metadados de um plugin registrado.

    Attributes:
        name: Nome único do plugin
        factory: Função factory para criar instâncias
        description: Descrição do plugin (opcional)
        version: Versão do plugin (opcional)
        metadata: Metadados adicionais
    """

    def __init__(
        self,
        name: str,
        factory: Callable,
        description: Optional[str] = None,
        version: Optional[str] = None,
        **metadata: Any,
    ):
        self.name = name
        self.factory = factory
        self.description = description
        self.version = version
        self.metadata = metadata

    def __repr__(self) -> str:
        version_str = f" v{self.version}" if self.version else ""
        return f"<Plugin: {self.name}{version_str}>"


# =============================================================================
# Plugin Registry
# =============================================================================


class PluginRegistry:
    """
    Registry dinâmico para plugins de orquestradores e estratégias.

    Suporta dois modos de registro:
    1. Descoberta automática via setuptools entrypoints
    2. Registro programático manual

    Examples:
        >>> registry = PluginRegistry(group="agents.orchestrators")
        >>> registry.register("my_strategy", my_strategy_factory)
        >>> factory = registry.get("my_strategy")
        >>> orchestrator = factory(context)
    """

    def __init__(self, group: Optional[str] = None):
        """
        Inicializa o registry.

        Args:
            group: Nome do grupo de entrypoints para descoberta automática
                  (ex: "agents.orchestrators", "agents.strategies")
        """
        self.group = group
        self._registry: Dict[str, PluginMetadata] = {}
        self._loaded = False

    def register(
        self,
        name: str,
        factory: Callable,
        description: Optional[str] = None,
        version: Optional[str] = None,
        override: bool = False,
        **metadata: Any,
    ) -> None:
        """
        Registra um plugin programaticamente.

        Args:
            name: Nome único do plugin
            factory: Função factory para criar instâncias
            description: Descrição do plugin (opcional)
            version: Versão do plugin (opcional)
            override: Se True, sobrescreve plugin existente
            **metadata: Metadados adicionais

        Raises:
            ValueError: Se plugin já existe e override=False

        Examples:
            >>> registry.register("zeroum", ZeroUmOrchestrator, version="1.0")
        """
        if name in self._registry and not override:
            raise ValueError(
                f"Plugin '{name}' já está registrado. Use override=True para sobrescrever."
            )

        plugin = PluginMetadata(
            name=name,
            factory=factory,
            description=description,
            version=version,
            **metadata,
        )
        self._registry[name] = plugin
        logger.debug(f"Plugin registrado: {plugin}")

    def unregister(self, name: str) -> None:
        """
        Remove um plugin do registry.

        Args:
            name: Nome do plugin

        Raises:
            KeyError: Se plugin não existe
        """
        if name not in self._registry:
            raise KeyError(f"Plugin '{name}' não encontrado no registry")

        del self._registry[name]
        logger.debug(f"Plugin removido: {name}")

    def get(self, name: str) -> Callable:
        """
        Retorna a factory de um plugin.

        Args:
            name: Nome do plugin

        Returns:
            Função factory do plugin

        Raises:
            StrategyNotFoundError: Se plugin não existe

        Examples:
            >>> factory = registry.get("zeroum")
            >>> orchestrator = factory(context, config)
        """
        self._ensure_loaded()

        if name not in self._registry:
            available = ", ".join(self.list())
            raise StrategyNotFoundError(
                f"Plugin '{name}' não encontrado. "
                f"Disponíveis: {available or 'nenhum'}"
            )

        return self._registry[name].factory

    def get_metadata(self, name: str) -> PluginMetadata:
        """
        Retorna metadados completos de um plugin.

        Args:
            name: Nome do plugin

        Returns:
            PluginMetadata do plugin

        Raises:
            StrategyNotFoundError: Se plugin não existe
        """
        self._ensure_loaded()

        if name not in self._registry:
            raise StrategyNotFoundError(f"Plugin '{name}' não encontrado")

        return self._registry[name]

    def list(self) -> List[str]:
        """
        Lista nomes de todos os plugins registrados.

        Returns:
            Lista de nomes de plugins

        Examples:
            >>> registry.list()
            ['zeroum', 'generic', 'custom_strategy']
        """
        self._ensure_loaded()
        return sorted(self._registry.keys())

    def list_all(self) -> List[PluginMetadata]:
        """
        Lista metadados de todos os plugins.

        Returns:
            Lista de PluginMetadata
        """
        self._ensure_loaded()
        return list(self._registry.values())

    def exists(self, name: str) -> bool:
        """
        Verifica se um plugin existe.

        Args:
            name: Nome do plugin

        Returns:
            True se plugin existe, False caso contrário
        """
        self._ensure_loaded()
        return name in self._registry

    def discover_plugins(self) -> int:
        """
        Descobre plugins via setuptools entrypoints.

        Returns:
            Número de plugins descobertos

        Note:
            Requer que self.group esteja definido.
            Plugins descobertos não sobrescrevem plugins já registrados.

        Examples:
            >>> registry = PluginRegistry(group="agents.orchestrators")
            >>> count = registry.discover_plugins()
            >>> print(f"Descobertos {count} plugins")
        """
        if not self.group:
            logger.warning("Nenhum grupo definido para descoberta de plugins")
            return 0

        discovered = 0

        try:
            # Tenta importar entrypoints (Python 3.10+)
            try:
                from importlib.metadata import entry_points
            except ImportError:
                # Fallback para Python 3.9
                from importlib_metadata import entry_points  # type: ignore

            # Descobre entrypoints do grupo
            eps = entry_points()

            # Compatibilidade com diferentes versões de entry_points
            if hasattr(eps, "select"):
                # Python 3.10+
                group_eps = eps.select(group=self.group)
            else:
                # Python 3.9
                group_eps = eps.get(self.group, [])

            for ep in group_eps:
                try:
                    # Carrega plugin
                    factory = ep.load()

                    # Registra apenas se não existir
                    if ep.name not in self._registry:
                        self.register(
                            name=ep.name,
                            factory=factory,
                            description=f"Plugin descoberto via entrypoint: {self.group}",
                        )
                        discovered += 1
                        logger.info(f"Plugin descoberto: {ep.name} ({self.group})")
                    else:
                        logger.debug(
                            f"Plugin {ep.name} já registrado, ignorando entrypoint"
                        )

                except Exception as exc:
                    logger.warning(
                        f"Falha ao carregar plugin {ep.name}: {exc}", exc_info=True
                    )

        except ImportError:
            logger.debug("importlib.metadata não disponível, descoberta desabilitada")
        except Exception as exc:
            logger.warning(f"Erro ao descobrir plugins: {exc}", exc_info=True)

        if discovered > 0:
            logger.info(f"Descobertos {discovered} plugin(s) no grupo {self.group}")

        return discovered

    def _ensure_loaded(self) -> None:
        """Garante que plugins foram carregados (lazy loading)."""
        if not self._loaded:
            self.discover_plugins()
            self._loaded = True

    def clear(self) -> None:
        """Limpa todos os plugins registrados."""
        self._registry.clear()
        self._loaded = False
        logger.debug("Registry limpo")


# =============================================================================
# Singleton Instances
# =============================================================================

# Registry global para orquestradores de estratégia
_strategy_registry: Optional[PluginRegistry] = None

# Registry global para orquestradores de processo
_process_registry: Optional[PluginRegistry] = None


def get_strategy_registry() -> PluginRegistry:
    """
    Retorna o registry singleton de estratégias.

    Returns:
        PluginRegistry para estratégias
    """
    global _strategy_registry
    if _strategy_registry is None:
        _strategy_registry = PluginRegistry(group="agents.strategies")
    return _strategy_registry


def get_process_registry() -> PluginRegistry:
    """
    Retorna o registry singleton de processos.

    Returns:
        PluginRegistry para processos
    """
    global _process_registry
    if _process_registry is None:
        _process_registry = PluginRegistry(group="agents.processes")
    return _process_registry


__all__ = [
    "PluginMetadata",
    "PluginRegistry",
    "get_strategy_registry",
    "get_process_registry",
]
