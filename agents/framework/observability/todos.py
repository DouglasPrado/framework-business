"""Sistema de gerenciamento de TODOs para agentes."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from agents.framework.config import get_settings
from agents.framework.core.protocols import TodoProvider


class TodoManager:
    """Gerenciador de lista de tarefas (TODOs) para processos de agentes."""

    def __init__(
        self,
        process_code: str,
        context_name: str,
        pipeline_dir: Path,
    ):
        """
        Inicializa o gerenciador de TODOs.

        Args:
            process_code: Código do processo (ex: 00-ProblemHypothesisExpress)
            context_name: Nome do contexto de execução
            pipeline_dir: Diretório do pipeline onde salvar TODOs
        """
        self.process_code = process_code
        self.context_name = context_name
        self.pipeline_dir = pipeline_dir
        self.todos: List[Dict[str, Any]] = []
        self.enabled = self._is_enabled()
        self._load_existing()

    def _is_enabled(self) -> bool:
        """Verifica se o sistema de TODOs está habilitado."""
        settings = get_settings(validate=False)
        return settings.enable_todos

    def _get_todo_path(self) -> Path:
        """Retorna o caminho do arquivo de TODOs."""
        return self.pipeline_dir / f"{self.process_code}-todos.json"

    def _load_existing(self) -> None:
        """Carrega TODOs existentes se o arquivo já existe."""
        if not self.enabled:
            return

        todo_path = self._get_todo_path()
        if todo_path.exists():
            try:
                with open(todo_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.todos = data.get("todos", [])
            except (json.JSONDecodeError, IOError):
                self.todos = []

    def _save(self) -> None:
        """Salva TODOs no arquivo JSON."""
        if not self.enabled:
            return

        self.pipeline_dir.mkdir(parents=True, exist_ok=True)
        todo_path = self._get_todo_path()

        data = {
            "process": self.process_code,
            "context": self.context_name,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "todos": self.todos,
            "summary": {
                "total": len(self.todos),
                "pending": len([t for t in self.todos if t["status"] == "pending"]),
                "in_progress": len([t for t in self.todos if t["status"] == "in_progress"]),
                "completed": len([t for t in self.todos if t["status"] == "completed"]),
                "failed": len([t for t in self.todos if t["status"] == "failed"]),
            }
        }

        with open(todo_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_todo(
        self,
        task: str,
        todo_id: Optional[str] = None,
        status: str = "pending",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Adiciona uma nova tarefa à lista.

        Args:
            task: Descrição da tarefa
            todo_id: ID único (gerado automaticamente se não fornecido)
            status: Status inicial (pending, in_progress, completed, failed)
            metadata: Metadados adicionais

        Returns:
            ID do TODO criado
        """
        if not self.enabled:
            return ""

        if todo_id is None:
            todo_id = f"todo-{len(self.todos) + 1:03d}"

        todo_item = {
            "id": todo_id,
            "task": task,
            "status": status,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": None,
            "completed_at": None,
            "metadata": metadata or {},
        }

        self.todos.append(todo_item)
        self._save()

        if os.getenv("AGENTS_TODO_VERBOSE", "false").lower() in ("true", "1"):
            print(f"[TODO] Added: {todo_id} - {task}")

        return todo_id

    def update_status(
        self,
        todo_id: str,
        status: str,
        notes: Optional[str] = None,
    ) -> bool:
        """
        Atualiza o status de um TODO.

        Args:
            todo_id: ID do TODO
            status: Novo status (pending, in_progress, completed, failed)
            notes: Notas adicionais sobre a atualização

        Returns:
            True se atualizado com sucesso, False se TODO não encontrado
        """
        if not self.enabled:
            return False

        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["status"] = status
                todo["updated_at"] = datetime.now(timezone.utc).isoformat()

                if status == "completed":
                    todo["completed_at"] = datetime.now(timezone.utc).isoformat()

                if notes:
                    todo["metadata"]["notes"] = notes

                self._save()

                if os.getenv("AGENTS_TODO_VERBOSE", "false").lower() in ("true", "1"):
                    print(f"[TODO] Updated: {todo_id} → {status}")

                return True

        return False

    def mark_completed(self, todo_id: str) -> bool:
        """
        Marca um TODO como completado.

        Args:
            todo_id: ID do TODO

        Returns:
            True se marcado com sucesso
        """
        return self.update_status(todo_id, "completed")

    def mark_failed(self, todo_id: str, reason: str) -> bool:
        """
        Marca um TODO como falho.

        Args:
            todo_id: ID do TODO
            reason: Motivo da falha

        Returns:
            True se marcado com sucesso
        """
        return self.update_status(todo_id, "failed", notes=reason)

    def get_todos(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retorna lista de TODOs, opcionalmente filtrada por status.

        Args:
            status: Filtrar por status (None = todos)

        Returns:
            Lista de TODOs
        """
        if not self.enabled:
            return []

        if status is None:
            return self.todos.copy()

        return [t for t in self.todos if t["status"] == status]

    def get_summary(self) -> Dict[str, Any]:
        """
        Retorna resumo dos TODOs.

        Returns:
            Dicionário com contagens por status
        """
        if not self.enabled:
            return {"enabled": False}

        return {
            "enabled": True,
            "total": len(self.todos),
            "pending": len(self.get_todos("pending")),
            "in_progress": len(self.get_todos("in_progress")),
            "completed": len(self.get_todos("completed")),
            "failed": len(self.get_todos("failed")),
            "progress_percentage": (
                (len(self.get_todos("completed")) / len(self.todos) * 100)
                if len(self.todos) > 0
                else 0.0
            ),
        }

    def clear(self) -> None:
        """Remove todos os TODOs."""
        if not self.enabled:
            return

        self.todos = []
        self._save()

    def write_todos(self, todos: List[Dict[str, str]]) -> None:
        """
        Método auxiliar para escrever múltiplos TODOs de uma vez.

        Args:
            todos: Lista de dicionários com 'task' e opcionalmente 'status', 'id'
        """
        if not self.enabled:
            return

        for todo_data in todos:
            self.add_todo(
                task=todo_data.get("task", ""),
                todo_id=todo_data.get("id"),
                status=todo_data.get("status", "pending"),
            )
