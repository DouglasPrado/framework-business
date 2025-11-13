# Setup Rápido - ZeroUm com LLM

## ⚡ Configuração em 3 Passos

### 1. Instalar Dependências

```bash
cd /Users/douglasprado/www/framework-business
./install.sh
source agents/.venv/bin/activate
```

**Nota**: O `install.sh` já instala `langchain-openai` e `python-dotenv` automaticamente.

### 2. Configurar API Key

O arquivo `.env` já existe em `agents/.env`. Edite e adicione sua chave:

```bash
# Editar .env
nano agents/.env
```

Ou via comando:
```bash
# Substitua pela sua chave real
echo "OPENAI_API_KEY=sk-sua-chave-aqui" > agents/.env.tmp
cat agents/.env | grep -v "OPENAI_API_KEY" >> agents/.env.tmp
mv agents/.env.tmp agents/.env
```

**Importante**: O framework agora **carrega automaticamente** o `.env` - não precisa exportar manualmente!

### 3. Executar

```bash
python3 agents/scripts/run_strategy_agent.py zeroum MeuProjeto \
  -d "Descrição detalhada do projeto"
```

## ✅ Resultado Esperado

```
================================================================================
Framework Business - Executor de Estratégias
================================================================================
Estratégia: zeroum
Contexto: MeuProjeto
Descrição: Descrição detalhada do projeto
================================================================================

Preparando workspace para estratégia ZeroUm
Workspace preparado em drive/MeuProjeto
Gerando hipóteses para estratégia ZeroUm
Invocando LLM para gerar hipóteses...           # ✅ LLM sendo usado!
Artefato criado: drive/MeuProjeto/00-ProblemHypothesisExpress/01-declaracao-hipotese.MD
Artefato criado: drive/MeuProjeto/00-ProblemHypothesisExpress/02-log-versoes-feedback.MD
Hipóteses geradas e artefatos criados com sucesso
Consolidado salvo em drive/MeuProjeto/00-consolidado.MD
Pacote final gerado em drive/MeuProjeto/MeuProjeto_ZeroUm_outputs.zip

================================================================================
EXECUÇÃO CONCLUÍDA
================================================================================
✅ Consolidado: drive/MeuProjeto/00-consolidado.MD
✅ Archive: drive/MeuProjeto/MeuProjeto_ZeroUm_outputs.zip
```

## 📁 Artefatos Criados

```
drive/MeuProjeto/
├── 00-ProblemHypothesisExpress/
│   ├── 01-declaracao-hipotese.MD      # Documento completo gerado por LLM
│   └── 02-log-versoes-feedback.MD     # Log de versões
├── _pipeline/
├── 00-consolidado.MD
└── MeuProjeto_ZeroUm_outputs.zip
```

## 🔍 Conteúdo Gerado (Exemplo)

O LLM vai gerar um documento completo com:

### 01-declaracao-hipotese.MD

```markdown
# 00-ProblemHypothesisExpress - MeuProjeto

## 1. Contexto Inicial

[Análise detalhada do problema gerada pelo LLM]

## 2. Perfis de Usuários-Alvo Imediatos

- **Perfil 1**: [Descrição] - [Onde encontrar] - [Por que prioritário]
- **Perfil 2**: ...
- **Perfil 3**: ...

## 3. Dor Principal

### Solução Atual
[Como resolvem hoje]

### Custos e Frustrações
- [Custo 1]
- [Custo 2]

### Evidências
- [Evidência 1]
- [Evidência 2]

## 4. Variações da Proposta de Valor

### Variação 1
"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"

### Variação 2
"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"

### Variação 3
"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"

### Variação Selecionada
[A melhor variação com justificativa]

## 5. Próximos Passos

- [ ] Validar frase com 1 pessoa do público-alvo
- [ ] Ajustar baseado no feedback
- [ ] Documentar aprendizados
```

## ❌ Sem LLM = Erro

O framework **NÃO TEM FALLBACK**. Se LLM não estiver configurado, vai dar erro:

```
RuntimeError: Dependência langchain_openai não encontrada.
Instale langchain-openai para usar ChatOpenAI.
```

Isso é **intencional** - o framework só gera conteúdo dinâmico com LLM.

## 🔧 Configurações Adicionais (Opcional)

### Modelo LLM

```bash
# agents/.env
OPENAI_API_KEY=sk-...
AGENTS_LLM_MODEL=gpt-4o          # Padrão: gpt-4o-mini
AGENTS_LLM_TEMPERATURE=0.7       # Padrão: 0.7
```

### LangSmith (Observabilidade)

```bash
# agents/.env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_...
LANGCHAIN_PROJECT=framework-business
```

## 🎯 Exemplo Completo

```bash
# 1. Setup
cd /Users/douglasprado/www/framework-business
source agents/.venv/bin/activate
pip install langchain-openai

# 2. Configurar
cat > agents/.env << EOF
OPENAI_API_KEY=sk-sua-chave
AGENTS_LLM_MODEL=gpt-4o-mini
EOF

# 3. Executar
python3 agents/scripts/run_strategy_agent.py zeroum Automarticles \
  -d "Plataforma SaaS que automatiza criação de blogs para PMEs usando IA, gerando artigos otimizados para SEO e publicando automaticamente"

# 4. Ver resultado
cat drive/Automarticles/00-ProblemHypothesisExpress/01-declaracao-hipotese.MD
```

## 🚨 Troubleshooting

### Erro: "No module named 'langchain_openai'"

```bash
pip install langchain-openai
```

### Erro: "OPENAI_API_KEY não configurada"

```bash
echo "OPENAI_API_KEY=sk-..." >> agents/.env
```

### Erro: "Invalid API Key"

Verifique sua chave em https://platform.openai.com/api-keys

### Erro: "You exceeded your current quota"

Adicione créditos em https://platform.openai.com/account/billing

## ✨ Pronto!

Com esses 3 passos, o ZeroUm está pronto para gerar documentos completos usando LLM! 🚀

---

**Data**: 2025-11-12
**Status**: ✅ SEM FALLBACK
**LLM**: Obrigatório
**Qualidade**: Sempre dinâmico
