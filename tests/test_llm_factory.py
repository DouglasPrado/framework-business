from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from agents.llm_factory import build_llm


class BuildLLMTests(unittest.TestCase):
    @patch("agents.llm_factory.ChatOpenAI")
    def test_build_llm_uses_configured_model(self, mock_chat) -> None:
        instance = MagicMock()
        mock_chat.return_value = instance

        llm = build_llm({"model": "gpt-test", "temperature": 0.1, "max_tokens": 512})

        self.assertIs(llm, instance)
        mock_chat.assert_called_once()
        kwargs = mock_chat.call_args.kwargs
        self.assertEqual(kwargs["model"], "gpt-test")
        self.assertEqual(kwargs["temperature"], 0.1)
        self.assertEqual(kwargs["max_tokens"], 512)

    @patch("agents.llm_factory.LangSmithCallbackHandler")
    @patch("agents.llm_factory.LangChainTracer")
    @patch("agents.llm_factory.ChatOpenAI")
    def test_build_llm_combines_callbacks(self, mock_chat, mock_tracer, mock_langsmith) -> None:
        tracer_instance = MagicMock(name="tracer")
        mock_tracer.return_value = tracer_instance
        smith_instance = MagicMock(name="langsmith")
        mock_langsmith.return_value = smith_instance

        build_llm(
            {
                "model": "gpt-test",
                "observability": {
                    "langchain_tracer": {"project_name": "framework"},
                    "langsmith": {"project_name": "framework", "tags": ["dev"]},
                },
                "callbacks": ["existing"],
            }
        )

        mock_tracer.assert_called_once_with(project_name="framework")
        mock_langsmith.assert_called_once_with(project_name="framework", tags=["dev"])
        callbacks = mock_chat.call_args.kwargs["callbacks"]
        self.assertIn("existing", callbacks)
        self.assertIn(tracer_instance, callbacks)
        self.assertIn(smith_instance, callbacks)

    def test_unknown_provider_raises(self) -> None:
        with self.assertRaises(ValueError):
            build_llm({"provider": "custom"})


if __name__ == "__main__":
    unittest.main()
