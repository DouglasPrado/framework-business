"""Funções auxiliares para normalizar nomes de contexto."""

from __future__ import annotations

import logging
import os
import re
from typing import Optional

logger = logging.getLogger(__name__)

try:  # pragma: no cover
    from deepagents import create_deep_agent
except ImportError:  # pragma: no cover
    try:
        from ..deepagents import create_deep_agent  # type: ignore
    except ImportError:  # pragma: no cover
        create_deep_agent = None

AI_DISABLED = os.getenv("AGENTS_DISABLE_CONTEXT_AI", "").lower() in {"1", "true", "yes"}
HAS_MODEL_KEY = bool(os.getenv("OPENAI_API_KEY"))
_PROMPT = (
    "Você recebe descrições de iniciativas e precisa gerar o nome da pasta em CamelCase "
    "com no máximo {max_words} palavras. Responda SOMENTE com o nome sugerido, sem comentários, "
    "sem pontos e sem espaços."
)


def normalize_context_name(raw_name: str, max_words: int = 3) -> str:
    """Gera um nome CamelCase para o contexto usando IA quando disponível."""
    raw = (raw_name or "").strip()
    if not raw:
        return "Contexto"

    use_ai = not AI_DISABLED and create_deep_agent is not None and HAS_MODEL_KEY
    if use_ai:
        ai_name = _ask_agent_for_name(raw, max_words)
        if ai_name:
            return ai_name

    return _heuristic_name(raw, max_words)


def _ask_agent_for_name(raw: str, max_words: int) -> Optional[str]:
    try:
        agent = create_deep_agent(system_prompt=_PROMPT.format(max_words=max_words), tools=[])
    except Exception as exc:  # pragma: no cover - erros de instância não devem travar
        logger.warning("Falha ao criar agente para nome de contexto: %s", exc)
        return None

    instructions = (
        f"Descrição do projeto: {raw}\n"
        f"Crie um nome de pasta CamelCase com até {max_words} palavras."
    )
    try:
        response = agent.run(instructions)
    except Exception as exc:  # pragma: no cover
        logger.warning("Falha ao solicitar nome ao agente: %s", exc)
        return None

    cleaned = _sanitize(response, max_words)
    if not cleaned:
        logger.warning("Agente devolveu nome inválido para o contexto '%s': %s", raw, response)
    return cleaned


def _sanitize(text: str, max_words: int) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    letters = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", text)
    if not letters:
        return ""
    words = letters[:max_words]
    return "".join(word[:1].upper() + word[1:] for word in words)


def _heuristic_name(raw: str, max_words: int) -> str:
    needs_normalization = bool(re.search(r"[\s_-]", raw))
    if not needs_normalization:
        return raw

    sanitized = raw.replace("_", " ").replace("-", " ")
    raw_words = re.findall(r"\w+", sanitized, flags=re.UNICODE)
    words = []
    for word in raw_words:
        words.append(word)
        if len(words) == max_words:
            break

    if not words:
        return "Contexto"

    return "".join(word.capitalize() for word in words)
