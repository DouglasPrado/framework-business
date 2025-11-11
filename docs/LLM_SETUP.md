# Configuração de LLM

1. **Python / Ambiente**
   - Use Python 3.11+ e crie um virtualenv dedicado (`python3.11 -m venv .venv`).
   - Instale as dependências do módulo `agents/` com `pip install -r agents/requirements.txt` seguido de `pip install "deepagents @ git+https://github.com/langchain-ai/deepagents.git"`.

2. **Variáveis obrigatórias**
   ```bash
   export OPENAI_API_KEY="sua-chave"
   export AGENTS_LLM_MODEL="gpt-4o-mini"
   export AGENTS_LLM_TEMPERATURE="0.4"
   ```

3. **Razão/reflexão**
   ```bash
   export AGENTS_REASONING_MODE="reflection"    # ou simple
   export AGENTS_REASONING_MODEL="gpt-4o"
   ```

4. **Observabilidade (LangSmith)**
   ```bash
   export LANGCHAIN_TRACING_V2=true
   export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   export LANGCHAIN_API_KEY="sua-chave-langsmith"
   export LANGCHAIN_PROJECT="framework-business"
   ```

5. **Execução**
   ```bash
   cd agents
   source .venv/bin/activate
   ./RUN.sh ZeroUm "MeuProjeto" "Descrição"
   ```

Essas configurações garantem que o DeepAgent oficial funcione com reflexão, ferramentas reais e observabilidade integrada.
