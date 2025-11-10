from __future__ import annotations

import os
import unittest

os.environ["AGENTS_DISABLE_CONTEXT_AI"] = "1"

from agents.utils.context import normalize_context_name


class NormalizeContextNameTests(unittest.TestCase):
    def test_preserves_existing_camel_case(self) -> None:
        self.assertEqual(normalize_context_name("AutomarticlesAutomacaoBlog"), "AutomarticlesAutomacaoBlog")

    def test_collapses_sentence_to_three_words(self) -> None:
        raw = "Automarticles ferramenta de automacao de blog"
        self.assertEqual(normalize_context_name(raw), "AutomarticlesFerramentaDe")

    def test_handles_hyphenated_and_underscored_names(self) -> None:
        raw = "mega_projeto-super complexo"
        self.assertEqual(normalize_context_name(raw), "MegaProjetoSuper")

    def test_returns_default_when_empty(self) -> None:
        self.assertEqual(normalize_context_name(""), "Contexto")


if __name__ == "__main__":
    unittest.main()
