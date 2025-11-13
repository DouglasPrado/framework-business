"""
Grafo de orquestração com suporte dual-mode (declarativo + programático).

Este módulo permite definir fluxos de orquestração tanto via arquivos
declarativos (YAML/JSON) quanto via código Python.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


# =============================================================================
# Node and Edge Classes
# =============================================================================


@dataclass
class GraphNode:
    """
    Nó do grafo de orquestração.

    Attributes:
        id: Identificador único do nó
        handler: Função handler a ser executada
        name: Nome legível do nó (opcional)
        metadata: Metadados adicionais
    """

    id: str
    handler: Callable
    name: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.name is None:
            self.name = self.id


@dataclass
class GraphEdge:
    """
    Aresta do grafo de orquestração.

    Attributes:
        from_node: ID do nó de origem
        to_node: ID do nó de destino
        condition: Condição para seguir a aresta (opcional)
        metadata: Metadados adicionais
    """

    from_node: str
    to_node: str
    condition: Optional[Callable[[Dict[str, Any]], bool]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


# =============================================================================
# Orchestration Graph
# =============================================================================


class OrchestrationGraph:
    """
    Grafo de orquestração com suporte dual-mode.

    Permite definir fluxos de execução tanto declarativamente
    (via YAML/JSON) quanto programaticamente (via código Python).

    Examples:
        # Modo programático
        >>> graph = OrchestrationGraph()
        >>> graph.add_node("collect", collect_handler)
        >>> graph.add_node("generate", generate_handler)
        >>> graph.add_edge("collect", "generate")
        >>> result = graph.execute(state)

        # Modo declarativo
        >>> graph = OrchestrationGraph.from_yaml("workflow.yaml")
        >>> result = graph.execute(state)
    """

    def __init__(self):
        """Inicializa um grafo vazio."""
        self.nodes: Dict[str, GraphNode] = {}
        self.edges: List[GraphEdge] = []
        self.start_node: Optional[str] = None
        self.end_nodes: List[str] = []

    def add_node(
        self,
        node_id: str,
        handler: Callable,
        name: Optional[str] = None,
        **metadata: Any,
    ) -> None:
        """
        Adiciona um nó ao grafo.

        Args:
            node_id: Identificador único do nó
            handler: Função handler para executar
            name: Nome legível (opcional)
            **metadata: Metadados adicionais
        """
        node = GraphNode(id=node_id, handler=handler, name=name, metadata=metadata)
        self.nodes[node_id] = node
        logger.debug(f"Nó adicionado: {node_id}")

        # Primeiro nó é o start por padrão
        if self.start_node is None:
            self.start_node = node_id

    def add_edge(
        self,
        from_node: str,
        to_node: str,
        condition: Optional[Callable[[Dict[str, Any]], bool]] = None,
        **metadata: Any,
    ) -> None:
        """
        Adiciona uma aresta ao grafo.

        Args:
            from_node: ID do nó de origem
            to_node: ID do nó de destino
            condition: Condição para seguir aresta (opcional)
            **metadata: Metadados adicionais

        Raises:
            ValueError: Se nós não existem
        """
        if from_node not in self.nodes:
            raise ValueError(f"Nó de origem '{from_node}' não existe")
        if to_node not in self.nodes:
            raise ValueError(f"Nó de destino '{to_node}' não existe")

        edge = GraphEdge(
            from_node=from_node, to_node=to_node, condition=condition, metadata=metadata
        )
        self.edges.append(edge)
        logger.debug(f"Aresta adicionada: {from_node} → {to_node}")

    def set_start_node(self, node_id: str) -> None:
        """
        Define o nó inicial do grafo.

        Args:
            node_id: ID do nó inicial

        Raises:
            ValueError: Se nó não existe
        """
        if node_id not in self.nodes:
            raise ValueError(f"Nó '{node_id}' não existe")
        self.start_node = node_id

    def add_end_node(self, node_id: str) -> None:
        """
        Adiciona um nó final ao grafo.

        Args:
            node_id: ID do nó final

        Raises:
            ValueError: Se nó não existe
        """
        if node_id not in self.nodes:
            raise ValueError(f"Nó '{node_id}' não existe")
        if node_id not in self.end_nodes:
            self.end_nodes.append(node_id)

    def execute(self, initial_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Executa o grafo de orquestração.

        Args:
            initial_state: Estado inicial (opcional)

        Returns:
            Estado final após execução

        Raises:
            ValueError: Se grafo estiver inválido
        """
        if not self.start_node:
            raise ValueError("Grafo não tem nó inicial definido")

        state = initial_state or {}
        current_node = self.start_node

        logger.info(f"Iniciando execução do grafo a partir de '{current_node}'")

        visited = set()

        while current_node:
            # Previne loops infinitos
            if current_node in visited:
                logger.warning(f"Ciclo detectado no nó '{current_node}'")
                break

            visited.add(current_node)

            # Executa handler do nó
            node = self.nodes[current_node]
            logger.debug(f"Executando nó: {node.name or node.id}")

            try:
                state = node.handler(state)
            except Exception as exc:
                logger.error(
                    f"Erro ao executar nó '{node.name}': {exc}", exc_info=True
                )
                state["_error"] = exc
                break

            # Se é nó final, termina
            if current_node in self.end_nodes:
                logger.info(f"Nó final alcançado: {current_node}")
                break

            # Encontra próximo nó
            next_node = self._find_next_node(current_node, state)
            if next_node is None:
                logger.info(f"Nenhum próximo nó encontrado para '{current_node}'")
                break

            current_node = next_node

        logger.info(f"Execução do grafo concluída. Visitados {len(visited)} nós.")
        return state

    def _find_next_node(
        self, current_node: str, state: Dict[str, Any]
    ) -> Optional[str]:
        """Encontra o próximo nó a executar."""
        for edge in self.edges:
            if edge.from_node == current_node:
                # Se tem condição, verifica
                if edge.condition and not edge.condition(state):
                    continue
                return edge.to_node
        return None

    @classmethod
    def from_dict(cls, config: Dict[str, Any], handlers: Dict[str, Callable]) -> OrchestrationGraph:
        """
        Cria grafo a partir de dicionário de configuração.

        Args:
            config: Configuração do grafo com estrutura:
                {
                    "nodes": [{"id": "node1", "handler": "handler1"}],
                    "edges": [{"from": "node1", "to": "node2"}],
                    "start": "node1",
                    "end": ["node2"]
                }
            handlers: Mapeamento de nomes de handlers para funções

        Returns:
            OrchestrationGraph configurado

        Examples:
            >>> handlers = {"collect": collect_fn, "generate": generate_fn}
            >>> graph = OrchestrationGraph.from_dict(config, handlers)
        """
        graph = cls()

        # Adiciona nós
        for node_config in config.get("nodes", []):
            node_id = node_config["id"]
            handler_name = node_config.get("handler", node_id)

            if handler_name not in handlers:
                raise ValueError(f"Handler '{handler_name}' não encontrado")

            graph.add_node(
                node_id=node_id,
                handler=handlers[handler_name],
                name=node_config.get("name"),
            )

        # Adiciona arestas
        for edge_config in config.get("edges", []):
            graph.add_edge(
                from_node=edge_config["from"],
                to_node=edge_config["to"],
            )

        # Define nó inicial
        if "start" in config:
            graph.set_start_node(config["start"])

        # Define nós finais
        for end_node in config.get("end", []):
            graph.add_end_node(end_node)

        return graph

    @classmethod
    def from_yaml(cls, yaml_path: Path, handlers: Dict[str, Callable]) -> OrchestrationGraph:
        """
        Cria grafo a partir de arquivo YAML.

        Args:
            yaml_path: Caminho para arquivo YAML
            handlers: Mapeamento de handlers

        Returns:
            OrchestrationGraph configurado

        Raises:
            ImportError: Se PyYAML não estiver instalado
        """
        try:
            import yaml
        except ImportError:
            raise ImportError(
                "PyYAML é necessário para carregar YAML. " "Instale com: pip install pyyaml"
            )

        config = yaml.safe_load(yaml_path.read_text())
        return cls.from_dict(config, handlers)

    @classmethod
    def from_json(cls, json_path: Path, handlers: Dict[str, Callable]) -> OrchestrationGraph:
        """
        Cria grafo a partir de arquivo JSON.

        Args:
            json_path: Caminho para arquivo JSON
            handlers: Mapeamento de handlers

        Returns:
            OrchestrationGraph configurado
        """
        config = json.loads(json_path.read_text())
        return cls.from_dict(config, handlers)

    @classmethod
    def from_handlers(cls, handlers: Dict[str, Callable]) -> OrchestrationGraph:
        """
        Cria grafo simples sequencial a partir de handlers.

        Args:
            handlers: Dicionário ordenado de handlers

        Returns:
            OrchestrationGraph com nós em sequência

        Examples:
            >>> handlers = {"collect": collect_fn, "generate": generate_fn}
            >>> graph = OrchestrationGraph.from_handlers(handlers)
        """
        graph = cls()

        handler_ids = list(handlers.keys())

        # Adiciona nós
        for handler_id in handler_ids:
            graph.add_node(handler_id, handlers[handler_id])

        # Adiciona arestas sequenciais
        for i in range(len(handler_ids) - 1):
            graph.add_edge(handler_ids[i], handler_ids[i + 1])

        # Define nós inicial e final
        if handler_ids:
            graph.set_start_node(handler_ids[0])
            graph.add_end_node(handler_ids[-1])

        return graph


__all__ = [
    "GraphNode",
    "GraphEdge",
    "OrchestrationGraph",
]
