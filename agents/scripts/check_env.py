"""Script utilitário para validar variáveis sensíveis antes de executar agentes."""

from __future__ import annotations

import sys

from agents.utils.env_validation import validate_sensitive_environment


def main() -> int:
    try:
        validate_sensitive_environment()
    except EnvironmentError as exc:  # pragma: no cover - caminho principal testado indiretamente
        print(str(exc), file=sys.stderr)
        return 1
    else:
        print("Variáveis sensíveis configuradas corretamente.")
        return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
