"""Utility tools exposed to DeepAgents and LangChain graphs."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, List, Sequence

from .... import BASE_PATH

try:  # pragma: no cover - optional dependency during runtime
    from langchain.tools import Tool as LangChainTool  # type: ignore
except ImportError:  # pragma: no cover - fallback used in tests
    LangChainTool = None  # type: ignore


@dataclass
class SimpleTool:
    """Small wrapper mimicking ``langchain.tools.Tool`` when the library is absent."""

    name: str
    description: str
    func: Callable[[str], str]

    def __call__(self, argument: str) -> str:
        return self.func(argument)


ToolLike = SimpleTool  # default alias for type checkers
if LangChainTool is not None:  # pragma: no cover - executed when LangChain is installed
    ToolLike = LangChainTool  # type: ignore


def _build_tool(name: str, description: str, func: Callable[[str], str]) -> ToolLike:
    if LangChainTool is not None:  # pragma: no cover - depends on runtime installation
        return LangChainTool(name=name, description=description, func=func)  # type: ignore[arg-type]
    return SimpleTool(name=name, description=description, func=func)


def _iter_markdown_files(base_path: Path) -> Iterable[Path]:
    for relative_root in ("process", "strategies", "drive"):
        folder = base_path / relative_root
        if not folder.exists():
            continue
        for path in sorted(folder.rglob("*.MD")):
            if path.is_file():
                yield path


def _extract_snippet(text: str, query: str, margin: int = 120) -> str:
    lowered = text.lower()
    index = lowered.find(query.lower())
    if index < 0:
        return ""
    start = max(0, index - margin)
    end = min(len(text), index + len(query) + margin)
    snippet = " ".join(text[start:end].split())
    return snippet


def search_internal_base(query: str, base_path: Path = BASE_PATH, max_results: int = 5) -> str:
    query = (query or "").strip()
    if not query:
        return "Forneça um termo de busca válido."

    results: List[str] = []
    for path in _iter_markdown_files(base_path):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:  # pragma: no cover - arquivos inacessíveis não devem interromper a busca
            continue
        snippet = _extract_snippet(text, query)
        if snippet:
            relative = path.relative_to(base_path)
            results.append(f"{relative}: {snippet}")
        if len(results) >= max_results:
            break

    if not results:
        return f"Nenhum resultado encontrado para '{query}'."
    return "\n".join(results)


def summarize_markdown(content: str, max_sentences: int = 3) -> str:
    text = " ".join((content or "").split())
    if not text:
        return "Conteúdo vazio informado para sumarização."
    sentences = re.split(r"(?<=[.!?])\s+", text)
    summary = " ".join(sentences[:max_sentences]).strip()
    return summary or text[:280]


def create_internal_search_tool(base_path: Path = BASE_PATH, max_results: int = 5) -> ToolLike:
    description = (
        "Busca termos dentro dos artefatos internos (process/, strategies/ e drive/). "
        "Retorna até {max_results} correspondências com trechos relevantes."
    ).format(max_results=max_results)

    def _search(query: str) -> str:
        return search_internal_base(query, base_path=base_path, max_results=max_results)

    return _build_tool("internal_base_search", description, _search)


def create_markdown_summary_tool(max_sentences: int = 3) -> ToolLike:
    description = (
        "Produz um resumo heurístico em português com até {max_sentences} frases a partir do texto informado."
    ).format(max_sentences=max_sentences)

    def _summarize(markdown: str) -> str:
        return summarize_markdown(markdown, max_sentences=max_sentences)

    return _build_tool("markdown_summarizer", description, _summarize)


def list_default_operations() -> Sequence[str]:
    return (
        "internal_base_search",
        "markdown_summarizer",
    )


def get_default_tools(base_path: Path = BASE_PATH) -> List[ToolLike]:
    return [
        create_internal_search_tool(base_path=base_path),
        create_markdown_summary_tool(),
    ]


__all__ = [
    "SimpleTool",
    "ToolLike",
    "create_internal_search_tool",
    "create_markdown_summary_tool",
    "get_default_tools",
    "list_default_operations",
    "search_internal_base",
    "summarize_markdown",
]
