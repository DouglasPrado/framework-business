#!/bin/bash
# Script para encerrar processos iniciados pelo run.sh (sem confirmação)
# Útil para automação e scripts

echo "🔍 Procurando processos do Framework Business..."

# Encontrar processos relacionados ao run_strategy_agent.py
PIDS=$(ps aux | grep "python.*run_strategy_agent.py" | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo "✅ Nenhum processo encontrado em execução."
    exit 0
fi

# Contar processos
COUNT=$(echo "$PIDS" | wc -l | tr -d ' ')
echo "📊 Encerrando $COUNT processo(s)..."

# Encerrar cada processo silenciosamente
KILLED=0
FAILED=0

for PID in $PIDS; do
    if kill $PID 2>/dev/null; then
        KILLED=$((KILLED + 1))
    else
        if kill -9 $PID 2>/dev/null; then
            KILLED=$((KILLED + 1))
        else
            FAILED=$((FAILED + 1))
        fi
    fi
done

echo "✅ $KILLED processo(s) encerrado(s)"
if [ $FAILED -gt 0 ]; then
    echo "⚠️  $FAILED processo(s) não puderam ser encerrados"
    exit 1
fi

exit 0
