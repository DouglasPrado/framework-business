"""Tests for the template filler utility."""

from __future__ import annotations

from pathlib import Path
from typing import List

import pytest

from business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)


class _StubLLM:
    def __init__(self, response_text: str) -> None:
        self.response_text = response_text
        self.prompts: List[str] = []

    class _Result:
        def __init__(self, text: str) -> None:
            self.content = text

    def invoke(self, prompt: str) -> "_StubLLM._Result":
        self.prompts.append(prompt)
        return self._Result(self.response_text)


def test_fill_template_creates_file(tmp_path: Path) -> None:
    llm = _StubLLM("Template preenchido")
    filler = ProcessTemplateFiller(
        process_code="00-ProblemHypothesisExpress",
        output_dir=tmp_path,
        llm=llm,
    )

    filler.fill_templates(
        [
            TemplateTask(
                template="log-versoes-feedback.MD",
                instructions="Preencha com dados fictícios.",
                output_name="log-preenchido.MD",
            )
        ],
        context="Contexto de teste",
    )

    output_file = tmp_path / "log-preenchido.MD"
    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip() == "Template preenchido"


def test_fill_template_injects_context_in_prompt(tmp_path: Path) -> None:
    llm = _StubLLM("ok")
    filler = ProcessTemplateFiller(
        process_code="00-ProblemHypothesisExpress",
        output_dir=tmp_path,
        llm=llm,
    )

    filler.fill_templates(
        [TemplateTask(template="log-versoes-feedback.MD")],
        context="Contexto relevante ABC",
    )

    assert llm.prompts, "Esperava pelo menos uma chamada ao LLM"
    assert "Contexto relevante ABC" in llm.prompts[0]
