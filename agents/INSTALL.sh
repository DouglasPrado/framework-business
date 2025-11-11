#!/bin/bash
# Script de instalação completa do Framework Business Agents

set -e

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Framework Business - Instalação${NC}"
echo ""

# Verificar Python
echo -e "${YELLOW}Verificando Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ Python encontrado: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python 3 não encontrado!${NC}"
    echo "Instale Python 3.9+ e tente novamente"
    exit 1
fi

# Criar ambiente virtual
echo -e "${YELLOW}Criando ambiente virtual...${NC}"
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo -e "${GREEN}✅ Ambiente virtual criado${NC}"
else
    echo -e "${GREEN}✅ Ambiente virtual já existe${NC}"
fi

# Ativar ambiente virtual
echo -e "${YELLOW}Ativando ambiente virtual...${NC}"
source .venv/bin/activate

# Atualizar pip
echo -e "${YELLOW}Atualizando pip...${NC}"
pip install --upgrade pip wheel setuptools

# Instalar dependências
echo -e "${YELLOW}Instalando dependências...${NC}"
pip install langchain langchain-openai langgraph openai

# Instalar dependências de desenvolvimento (opcional)
read -p "Instalar dependências de desenvolvimento (ruff, mypy, pytest)? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Instalando dev dependencies...${NC}"
    pip install ruff mypy pytest pytest-cov black pre-commit
    echo -e "${GREEN}✅ Dev dependencies instaladas${NC}"
fi

# Configurar .env
echo -e "${YELLOW}Configurando .env...${NC}"
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✅ Arquivo .env criado${NC}"
    echo -e "${YELLOW}⚠️  IMPORTANTE: Edite .env e adicione sua OPENAI_API_KEY${NC}"
else
    echo -e "${GREEN}✅ Arquivo .env já existe${NC}"
fi

# Dar permissão aos scripts
echo -e "${YELLOW}Configurando permissões...${NC}"
chmod +x agents/RUN.sh
chmod +x INSTALL.sh
echo -e "${GREEN}✅ Permissões configuradas${NC}"

# Testar instalação
echo -e "${YELLOW}Testando instalação...${NC}"
if python3 -c "from agents.registry import STRATEGY_REGISTRY; print('Import OK')" 2>/dev/null; then
    echo -e "${GREEN}✅ Imports funcionando!${NC}"
else
    echo -e "${RED}❌ Erro nos imports${NC}"
    echo "Tente: pip install -e ."
fi

echo ""
echo -e "${GREEN}🎉 Instalação concluída!${NC}"
echo ""
echo -e "${BLUE}Próximos passos:${NC}"
echo "1. Edite .env e adicione sua OPENAI_API_KEY"
echo "2. Execute: ./agents/RUN.sh ZeroUm \"TesteProjeto\" \"Teste de instalação\""
echo ""
echo -e "${YELLOW}Comandos úteis:${NC}"
echo "  - Ver estratégias: python3 -c \"from agents.registry import STRATEGY_REGISTRY; print(list(STRATEGY_REGISTRY.keys()))\""
echo "  - Verificar env: python3 agents/scripts/check_env.py"
echo "  - Executar: ./agents/RUN.sh <estratégia> <contexto> \"<descrição>\""
echo ""
echo -e "${GREEN}Documentação:${NC}"
echo "  - README-EXECUTION.md  : Guia de execução"
echo "  - COMANDOS-RAPIDOS.md  : Comandos prontos"
echo "  - agents/QUICKSTART.md : Guia completo"
echo ""
