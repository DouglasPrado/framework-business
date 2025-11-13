# Scripts Atualizados - Framework Business

## Status: ✅ CONCLUÍDO

Data: 2025-11-12

## Resumo

Scripts obsoletos foram removidos e substituídos por versões modernas compatíveis com o novo framework.

## Scripts Removidos

### 1. agents/INSTALL.sh (REMOVIDO)
- **Status**: ❌ Removido
- **Motivo**: Referenciava `agents.registry` (não existe mais)
- **Substituído por**: `install.sh` (na raiz)

### 2. agents/RUN.sh (REMOVIDO)
- **Status**: ❌ Removido
- **Motivo**: Usava código antigo
- **Substituído por**: `agents/scripts/run_strategy_agent.py` (atualizado)

## Novos Scripts

### 1. install.sh (Raiz do Projeto)

**Localização**: `/install.sh`

**Funcionalidade**:
- Verifica Python 3
- Cria ambiente virtual em `agents/.venv`
- Instala dependências (langchain, langgraph, openai)
- Opção para instalar dev dependencies (pytest, ruff, mypy)
- Configura .env
- Testa instalação

**Uso**:
```bash
./install.sh
```

**Output esperado**:
```
🚀 Framework Business - Instalação
✅ Python encontrado: Python 3.13.5
✅ Ambiente virtual criado
✅ Dependências instaladas
✅ Framework funcionando!
🎉 Instalação concluída!
```

### 2. agents/scripts/run_strategy_agent.py (Atualizado)

**Localização**: `agents/scripts/run_strategy_agent.py`

**Funcionalidade**:
- CLI moderno para executar estratégias
- Suporta estratégias: `zeroum`, `generic`
- Logging configurável
- Output JSON opcional
- Usa apenas framework novo (zero código legacy)

**Uso**:

```bash
# Ver ajuda
python3 agents/scripts/run_strategy_agent.py --help

# Executar ZeroUm
python3 agents/scripts/run_strategy_agent.py zeroum MeuProjeto \
  -d "Descrição do projeto"

# Executar Generic
python3 agents/scripts/run_strategy_agent.py generic MinhaEstrategia \
  -s NomeDaEstrategia -d "Descrição"

# Modo silencioso + salvar JSON
python3 agents/scripts/run_strategy_agent.py zeroum Teste \
  -d "Teste" -q -o resultado.json
```

**Argumentos**:
- `strategy`: Nome da estratégia (`zeroum` ou `generic`)
- `context`: Nome do contexto
- `-d, --description`: Descrição detalhada
- `-s, --strategy-name`: Nome da estratégia (apenas para `generic`)
- `-q, --quiet`: Modo silencioso
- `-o, --output`: Salvar resultado em arquivo JSON

**Output esperado**:
```
================================================================================
Framework Business - Executor de Estratégias
================================================================================
Estratégia: zeroum
Contexto: MeuProjeto
Descrição: Descrição do projeto
================================================================================
Preparando workspace para estratégia ZeroUm
Workspace preparado em drive/MeuProjeto
Processando hipóteses para estratégia ZeroUm
Consolidado salvo em drive/MeuProjeto/00-consolidado.MD
Pacote final gerado em drive/MeuProjeto/MeuProjeto_ZeroUm_outputs.zip
Estratégia ZeroUm concluída em 0.01s

================================================================================
EXECUÇÃO CONCLUÍDA
================================================================================
Consolidado: drive/MeuProjeto/00-consolidado.MD
Archive: drive/MeuProjeto/MeuProjeto_ZeroUm_outputs.zip

Métricas:
  total_metrics: 1
  tokens: {...}
  ...
```

## Comparação

### Antes (Scripts Antigos)

```bash
# INSTALL.sh (agents/)
# ❌ Usava agents.registry (removido)
from agents.registry import STRATEGY_REGISTRY  # Não existe!

# RUN.sh (agents/)
# ❌ Executava script desatualizado
python3 scripts/run_strategy_agent.py "$STRATEGY" "$CONTEXT"
```

### Depois (Scripts Novos)

```bash
# install.sh (raiz)
# ✅ Testa framework novo
python3 -c "from agents.framework.core.context import AgentContext"

# run_strategy_agent.py
# ✅ Usa estratégias diretamente
from agents.business.strategies.zeroum.orchestrator import ZeroUmOrchestrator
from agents.business.strategies.generic.orchestrator import GenericStrategyOrchestrator
```

## Exemplo de Uso Completo

### 1. Instalação

```bash
# Clonar projeto
git clone <repo>
cd framework-business

# Executar instalação
./install.sh

# Ativar ambiente
source agents/.venv/bin/activate

# Configurar .env (se necessário)
echo "OPENAI_API_KEY=sk-..." > agents/.env
```

### 2. Executar Estratégia

```bash
# Via CLI
python3 agents/scripts/run_strategy_agent.py zeroum AutomarticlesDemo \
  -d "Plataforma de automação de blogs com IA"

# Via exemplo Python
python3 agents/business/examples/zeroum_example.py

# Verificar resultados
ls drive/AutomarticlesDemo/
# - 00-consolidado.MD
# - AutomarticlesDemo_ZeroUm_outputs.zip
# - _pipeline/
```

### 3. Executar Testes

```bash
# Teste de validação final
python3 test_final_cleanup.py

# Resultado esperado:
# ✅ PASSOU: Framework Imports
# ✅ PASSOU: Legacy Code Removed
# ✅ PASSOU: Orchestrators Clean
# ✅ PASSOU: AgentContext Works
# ✅ PASSOU: Examples Work
#
# RESULTADO FINAL: 5/5 testes passaram
```

## Estrutura de Arquivos

```
framework-business/
├── install.sh                          # ✅ NOVO (raiz)
├── agents/
│   ├── scripts/
│   │   ├── run_strategy_agent.py      # ✅ ATUALIZADO
│   │   └── check_env.py               # ✅ Mantido
│   │
│   ├── business/examples/
│   │   ├── zeroum_example.py          # ✅ Exemplo Python
│   │   └── simple_agent_example.py    # ✅ Exemplo básico
│   │
│   ├── INSTALL.sh                     # ❌ REMOVIDO
│   └── RUN.sh                         # ❌ REMOVIDO
│
└── test_final_cleanup.py              # ✅ Teste de validação
```

## Validação

### Teste do CLI

```bash
# Teste 1: Help
$ python3 agents/scripts/run_strategy_agent.py --help
# ✅ Exibe ajuda com estratégias disponíveis

# Teste 2: Execução rápida
$ python3 agents/scripts/run_strategy_agent.py zeroum TesteCLI -d "Teste"
# ✅ Executou em 0.00s
# ✅ Criou consolidado em drive/TesteCLI/00-consolidado.MD
# ✅ Criou archive em drive/TesteCLI/TesteCLI_ZeroUm_outputs.zip

# Teste 3: Output JSON
$ python3 agents/scripts/run_strategy_agent.py zeroum Teste -d "Teste" -q -o result.json
# ✅ Salvou resultado em result.json
```

### Teste da Instalação

```bash
$ ./install.sh
# ✅ Python encontrado: Python 3.13.5
# ✅ Ambiente virtual criado em agents/.venv
# ✅ Dependências instaladas
# ✅ Framework funcionando!
# 🎉 Instalação concluída!
```

## Dependências

### Produção (Obrigatórias)
- Python 3.9+
- langchain
- langchain-openai
- langgraph
- openai

### Desenvolvimento (Opcionais)
- pytest
- pytest-cov
- ruff
- mypy
- black

## Configuração

### Variáveis de Ambiente (.env)

```bash
# Obrigatório para usar LLMs
OPENAI_API_KEY=sk-...

# Opcional - modelo LLM (default: gpt-4o-mini)
AGENTS_LLM_MODEL=gpt-4o-mini

# Opcional - tracing (LangSmith)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=framework-business

# Opcional - modo de raciocínio
AGENTS_REASONING_MODE=simple
```

## Documentação Relacionada

- [PROJECT_STATUS.md](PROJECT_STATUS.md) - Status completo do projeto
- [FINAL_STRUCTURE.md](FINAL_STRUCTURE.md) - Estrutura final
- [agents/MIGRATION_GUIDE.md](agents/MIGRATION_GUIDE.md) - Guia de migração
- [agents/business/examples/README.md](agents/business/examples/README.md) - Guia de exemplos

## Changelog

### Removido
- ❌ `agents/INSTALL.sh` - Script obsoleto
- ❌ `agents/RUN.sh` - Script obsoleto
- ❌ Referências a `agents.registry` (não existe mais)
- ❌ Referências a `agents.utils` (movido/removido)

### Adicionado
- ✅ `install.sh` (raiz) - Script moderno de instalação
- ✅ CLI atualizado com novo framework
- ✅ Suporte a output JSON
- ✅ Logging configurável
- ✅ Documentação completa

### Melhorado
- ✅ `agents/scripts/run_strategy_agent.py` - Completamente reescrito
- ✅ Usa apenas framework novo (zero legacy)
- ✅ Melhor UX (help, exemplos, erro handling)
- ✅ Código limpo e documentado

## Conclusão

✅ **Scripts atualizados com sucesso**
✅ **100% compatível com novo framework**
✅ **Zero código legacy**
✅ **CLI moderno e funcional**
✅ **Instalação simplificada**
✅ **Documentação completa**

Os scripts estão prontos para uso em produção! 🎉

---

**Data**: 2025-11-12
**Status**: ✅ PRODUÇÃO
**Testes**: CLI validado e funcionando
