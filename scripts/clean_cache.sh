#!/bin/bash
# Limpa todo o cache Python do projeto

echo "Limpando cache Python..."

# Voltar para o root do projeto
cd "$(dirname "$0")/../.." || exit 1

# Remover __pycache__
echo "  Removendo diretórios __pycache__..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
echo "  ✓ Diretórios __pycache__ removidos"

# Remover .pyc
echo "  Removendo arquivos .pyc..."
find . -type f -name "*.pyc" -delete 2>/dev/null || true
echo "  ✓ Arquivos .pyc removidos"

# Remover .pyo (Python 2 legacy)
echo "  Removendo arquivos .pyo..."
find . -type f -name "*.pyo" -delete 2>/dev/null || true
echo "  ✓ Arquivos .pyo removidos"

echo ""
echo "Cache limpo com sucesso!"
echo ""
echo "Dica: Para evitar gerar cache durante desenvolvimento, use:"
echo "  export PYTHONDONTWRITEBYTECODE=1"
