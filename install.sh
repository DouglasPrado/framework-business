#!/bin/bash
# Script de instalação do Framework Business Agents
set -e

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🚀 Framework Business - Instalação${NC}"
echo ""

# Verificar Python
echo -e "${YELLOW}Verificando Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 não encontrado!${NC}"
    echo "Instale Python 3.9+ e tente novamente"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✅ Python encontrado: $PYTHON_VERSION${NC}"

# Criar ambiente virtual
echo -e "${YELLOW}Criando ambiente virtual...${NC}"
if [ ! -d "agents/.venv" ]; then
    cd agents
    python3 -m venv .venv
    cd ..
    echo -e "${GREEN}✅ Ambiente virtual criado em agents/.venv${NC}"
else
    echo -e "${GREEN}✅ Ambiente virtual já existe${NC}"
fi

# Ativar e instalar dependências
echo -e "${YELLOW}Instalando dependências...${NC}"
source agents/.venv/bin/activate
pip install --upgrade pip wheel setuptools -q
pip install langchain langchain-openai langgraph openai python-dotenv -q
echo -e "${GREEN}✅ Dependências instaladas${NC}"

# Instalar dev dependencies (opcional)
read -p "Instalar dependências de desenvolvimento (pytest, ruff, mypy)? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    pip install pytest pytest-cov ruff mypy black -q
    echo -e "${GREEN}✅ Dev dependencies instaladas${NC}"
fi

# Configurar .env
echo -e "${YELLOW}Configurando ambiente...${NC}"
if [ ! -f "agents/.env" ]; then
    if [ -f "agents/.env.example" ]; then
        cp agents/.env.example agents/.env
        echo -e "${GREEN}✅ Arquivo .env criado${NC}"
        echo -e "${YELLOW}⚠️  IMPORTANTE: Edite agents/.env e adicione sua OPENAI_API_KEY${NC}"
    else
        echo -e "${YELLOW}⚠️  Arquivo .env.example não encontrado${NC}"
    fi
else
    echo -e "${GREEN}✅ Arquivo .env já existe${NC}"
fi

# Dar permissão ao script
chmod +x agents/scripts/run_strategy_agent.py

# Testar instalação
echo -e "${YELLOW}Testando instalação...${NC}"
if python3 -c "from agents.framework.core.context import AgentContext; print('✓ Framework OK')" 2>/dev/null; then
    echo -e "${GREEN}✅ Framework funcionando!${NC}"
else
    echo -e "${RED}❌ Erro ao importar framework${NC}"
    exit 1
fi

deactivate

echo ""
echo -e "${GREEN}🎉 Instalação concluída!${NC}"
echo ""
echo -e "${BLUE}Próximos passos:${NC}"
echo "1. Ative o ambiente: source agents/.venv/bin/activate"
echo "2. Configure OPENAI_API_KEY em agents/.env (se necessário)"
echo "3. Execute um exemplo:"
echo "   python3 agents/business/examples/zeroum_example.py"
echo ""
echo -e "${BLUE}Ou use o CLI:${NC}"
echo "   python3 agents/scripts/run_strategy_agent.py zeroum MeuProjeto -d \"Descrição\""
echo ""
echo -e "${BLUE}Documentação:${NC}"
echo "   - PROJECT_STATUS.md        : Status do projeto"
echo "   - FINAL_STRUCTURE.md       : Estrutura completa"
echo "   - agents/MIGRATION_GUIDE.md: Guia de migração"
echo ""
