#!/bin/bash
# Script auxiliar para executar agents facilmente

set -e

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Framework Business - Agents Runner${NC}"
echo ""

# Verificar se está no diretório correto
if [ ! -f "scripts/run_strategy_agent.py" ]; then
    echo -e "${RED}❌ Erro: Execute este script de dentro do diretório agents/${NC}"
    echo "Comando correto: cd agents && ./RUN.sh"
    exit 1
fi

# Verificar .env
if [ ! -f ".env" ]; then
    echo -e "${RED}⚠️  Arquivo .env não encontrado!${NC}"
    echo "Copiando .env.example para .env..."
    cp .env.example .env
    echo -e "${BLUE}📝 Edite o arquivo .env e adicione sua OPENAI_API_KEY${NC}"
    exit 1
fi

# Carregar .env
export $(cat .env | grep -v '^#' | xargs)

# Verificar API Key
if [ -z "$OPENAI_API_KEY" ] && [ "$AGENTS_SKIP_SECRET_CHECK" != "true" ]; then
    echo -e "${RED}❌ OPENAI_API_KEY não configurada no .env${NC}"
    echo "Adicione sua chave ou use AGENTS_SKIP_SECRET_CHECK=true para testes"
    exit 1
fi

# Exibir menu se não houver argumentos
if [ $# -eq 0 ]; then
    echo "Uso: $0 <estratégia> <contexto> [descrição]"
    echo ""
    echo "Estratégias disponíveis:"
    echo "  - ZeroUm       : Validação de problema/hipótese"
    echo "  - Branding     : Estratégia de branding"
    echo "  - MVPBuilder   : Construção de MVP"
    echo "  - Naming       : Estratégia de naming"
    echo ""
    echo "Exemplos:"
    echo "  $0 ZeroUm MeuProjeto 'Descrição do projeto'"
    echo "  $0 MVPBuilder TesteSaaS 'Plataforma SaaS para gestão'"
    exit 0
fi

# Parâmetros
STRATEGY=$1
CONTEXT=$2
DESCRIPTION=${3:-"Contexto de execução"}

echo -e "${GREEN}✅ Configuração:${NC}"
echo "  Estratégia: $STRATEGY"
echo "  Contexto: $CONTEXT"
echo "  Descrição: $DESCRIPTION"
echo "  Modelo: ${AGENTS_LLM_MODEL:-gpt-4o-mini}"
echo ""

# Executar
echo -e "${BLUE}🚀 Executando...${NC}"
python3 scripts/run_strategy_agent.py "$STRATEGY" "$CONTEXT" -d "$DESCRIPTION"

echo ""
echo -e "${GREEN}✅ Concluído!${NC}"
echo "Verifique os resultados em: ../drive/$CONTEXT/"
