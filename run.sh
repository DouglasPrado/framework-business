#!/bin/bash
# Wrapper script para executar estratégias com logs em tempo real

# Ativar venv
source .venv/bin/activate

# Executar com unbuffered output
PYTHONUNBUFFERED=1 python scripts/run_strategy_agent.py "$@"
