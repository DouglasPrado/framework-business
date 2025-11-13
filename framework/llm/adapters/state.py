"""State and memory helpers shared between DeepAgents and LangGraph nodes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

try:  # pragma: no cover - optional runtime dependency
    from langchain.memory import ConversationBufferMemory  # type: ignore
except ImportError:  # pragma: no cover - fallback used in tests
    ConversationBufferMemory = None  # type: ignore


class _SimpleMessage:
    """Lightweight fallback representation for chat messages."""

    def __init__(self, message_type: str, content: str) -> None:
        self.type = message_type
        self.content = content

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"_SimpleMessage(type={self.type!r}, content={self.content!r})"


class _SimpleChatMemory:
    """Mimics the subset of LangChain's chat memory interface we rely on."""

    def __init__(self) -> None:
        self.messages: List[_SimpleMessage] = []

    def add_user_message(self, content: str) -> None:
        self.messages.append(_SimpleMessage("human", content))

    def add_ai_message(self, content: str) -> None:
        self.messages.append(_SimpleMessage("ai", content))


class _SimpleConversationBufferMemory:
    """Fallback implementation for environments without LangChain installed."""

    def __init__(self, return_messages: bool = True, memory_key: str = "chat_history", input_key: str = "input") -> None:
        self.return_messages = return_messages
        self.memory_key = memory_key
        self.input_key = input_key
        self.chat_memory = _SimpleChatMemory()

    def load_memory_variables(self, _: Dict[str, Any]) -> Dict[str, Any]:
        if self.return_messages:
            return {self.memory_key: list(self.chat_memory.messages)}
        return {
            self.memory_key: "\n".join(message.content for message in self.chat_memory.messages)
        }

    def save_context(self, inputs: Dict[str, Any], outputs: Union[Dict[str, Any], str]) -> None:
        incoming = inputs.get(self.input_key)
        if incoming:
            self.chat_memory.add_user_message(str(incoming))
        if isinstance(outputs, dict):
            outgoing = outputs.get("output") or outputs.get("response")
        else:
            outgoing = outputs
        if outgoing:
            self.chat_memory.add_ai_message(str(outgoing))

    def clear(self) -> None:
        self.chat_memory = _SimpleChatMemory()


def _build_memory() -> Any:
    if ConversationBufferMemory is None:  # pragma: no cover - exercised in tests
        return _SimpleConversationBufferMemory(return_messages=True)
    return ConversationBufferMemory(return_messages=True, memory_key="chat_history", input_key="input")


def _add_message(memory: Any, role: str, content: str) -> None:
    chat_memory = getattr(memory, "chat_memory", None)
    if chat_memory is None:
        return
    if role == "user":
        add_method = getattr(chat_memory, "add_user_message", None)
    else:
        add_method = getattr(chat_memory, "add_ai_message", None)
    if callable(add_method):
        add_method(content)


@dataclass
class AgentStateStore:
    """Centralizes conversation history and node-level state."""

    memory: Optional[Any] = None
    node_state: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.memory is None:
            self.memory = _build_memory()

    def add_user_message(self, content: str) -> None:
        _add_message(self.memory, "user", content)

    def add_ai_message(self, content: str) -> None:
        _add_message(self.memory, "ai", content)

    def update_node_state(self, node_id: str, **data: Any) -> None:
        state = self.node_state.setdefault(node_id, {})
        state.update(data)

    def get_node_state(self, node_id: str) -> Dict[str, Any]:
        return dict(self.node_state.get(node_id, {}))

    def get_state_for_node(self, node_id: str) -> Dict[str, Any]:
        snapshot = self.get_node_state(node_id)
        loader = getattr(self.memory, "load_memory_variables", None)
        memory_key = getattr(self.memory, "memory_key", "chat_history")
        if callable(loader):
            snapshot[memory_key] = loader({}).get(memory_key, [])
        else:  # pragma: no cover - defensive fallback
            snapshot[memory_key] = []
        return snapshot

    def as_graph_state(self) -> Dict[str, Any]:
        return {"memory": self.memory, "nodes": dict(self.node_state)}
