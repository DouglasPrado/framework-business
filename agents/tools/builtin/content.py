"""Ferramentas de manipulação de conteúdo."""

from __future__ import annotations

from typing import Optional

from langchain_core.tools import StructuredTool

from ...llm_factory import build_llm


def _summarize_markdown(content: str, max_items: int = 5, instructions: Optional[str] = None) -> str:
    llm = build_llm({"max_tokens": 512, "temperature": 0.2})
    prompt = (
        "Resuma o conteúdo a seguir em até {items} bullet points claros."
        "\nSiga instruções extras se existirem.\n\nConteúdo:\n{body}"
    ).format(items=max_items, body=content)
    if instructions:
        prompt += f"\n\nInstruções adicionais: {instructions}"
    response = llm.invoke(prompt)
    content_attr = getattr(response, "content", None)
    if isinstance(content_attr, list):
        return "\n".join(part.get("text", "") for part in content_attr if isinstance(part, dict))
    if isinstance(content_attr, str):
        return content_attr
    return str(response)


MARKDOWN_SUMMARIZER_TOOL = StructuredTool.from_function(
    _summarize_markdown,
    name="markdown_summarizer",
    description="Resuma conteúdo markdown em poucos bullet points.",
)

CONTENT_TOOLS = [MARKDOWN_SUMMARIZER_TOOL]
