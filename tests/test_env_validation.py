from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from agents.utils.helpers.env_validation import (
    SKIP_FLAG,
    TRACE_DEPENDENCIES,
    TRACE_FLAG,
    validate_sensitive_environment,
)


class EnvValidationTests(unittest.TestCase):
    def test_missing_openai_key_returns_without_error(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            validate_sensitive_environment()

    def test_skip_flag_allows_execution(self) -> None:
        with patch.dict(os.environ, {SKIP_FLAG: "1"}, clear=True):
            # Não deve levantar exceção mesmo sem chaves definidas.
            validate_sensitive_environment()

    def test_tracing_without_dependencies_still_passes(self) -> None:
        with patch.dict(
            os.environ,
            {"OPENAI_API_KEY": "abc", TRACE_FLAG: "true"},
            clear=True,
        ):
            validate_sensitive_environment()

    def test_full_configuration_passes(self) -> None:
        env = {
            "OPENAI_API_KEY": "abc",
            TRACE_FLAG: "true",
            TRACE_DEPENDENCIES[0]: "https://api.smith.langchain.com",
            TRACE_DEPENDENCIES[1]: "token",
            TRACE_DEPENDENCIES[2]: "project-name",
        }
        with patch.dict(os.environ, env, clear=True):
            validate_sensitive_environment()


if __name__ == "__main__":
    unittest.main()
