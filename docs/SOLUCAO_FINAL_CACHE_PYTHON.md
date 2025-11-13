# Solução Final - Problema de Cache Python

## Problema Identificado

O erro persistente de importação do `langchain_openai`:

```
RuntimeError: Dependência langchain_openai não encontrada. Instale langchain-openai para usar ChatOpenAI.
```

Ocorria mesmo com a dependência corretamente instalada porque o Python estava usando **bytecode em cache** compilado em um momento anterior quando a dependência não estava disponível.

## Root Cause

1. Durante o desenvolvimento, o módulo `agents/framework/llm/factory.py` foi importado quando `langchain-openai` NÃO estava instalado
2. Python compilou o bytecode com `ChatOpenAI = None` e armazenou em `__pycache__/factory.cpython-313.pyc`
3. Mesmo após instalar `langchain-openai`, Python continuou usando o bytecode em cache
4. O bytecode em cache mantinha a variável `ChatOpenAI = None`, causando o erro na função `_resolve_chat_openai()`

## Verificação do Problema

### Teste 1: Import direto funcionava
```bash
$ python3 -c "from langchain_openai import ChatOpenAI; print('Import OK')"
Import OK
<class 'langchain_openai.chat_models.base.ChatOpenAI'>
```

### Teste 2: Import via factory falhava
```python
from agents.framework.llm.factory import build_llm
llm = build_llm()  # RuntimeError: Dependência langchain_openai não encontrada
```

Isso confirmou que o problema estava no cache, não na instalação.

## Solução Aplicada

### Passo 1: Remover TODO o cache Python
```bash
# Remover diretórios __pycache__
find /Users/douglasprado/www/framework-business -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

# Remover arquivos .pyc
find /Users/douglasprado/www/framework-business -type f -name "*.pyc" -delete
```

### Passo 2: Executar sem gerar novo cache (opcional)
```bash
PYTHONDONTWRITEBYTECODE=1 python3 agents/scripts/run_strategy_agent.py ...
```

## Resultado

Após limpar o cache, o orquestrador executou perfeitamente:

```
16:57:21 | INFO     | Framework Business - Executor de Estratégias
16:57:21 | INFO     | Estratégia: zeroum
16:57:21 | INFO     | Contexto: Automarticles
16:57:22 | INFO     | Workspace criado: drive/Automarticles
16:57:22 | INFO     | Pipeline dinâmico criado: 4 nós registrados
16:57:22 | INFO     | Executando nó: coletar_contexto
16:57:22 | INFO     | Executando nó: analisar_contexto
16:57:22 | INFO     | Analisando contexto para seleção de subagente...
16:57:22 | INFO     | Criando ChatOpenAI com modelo: gpt-4o-mini  ✓ FUNCIONOU
16:57:23 | INFO     | Decisão do orquestrador:
16:57:23 | INFO     |   Complexidade: simple
16:57:23 | INFO     |   Subagente selecionado: problem_hypothesis_express
...
16:57:51 | INFO     | EXECUÇÃO CONCLUÍDA COM SUCESSO
```

## Prevenção Futura

### Para desenvolvedores

1. **Sempre limpar cache após instalar novas dependências**:
   ```bash
   find agents -type d -name "__pycache__" -exec rm -rf {} +
   ```

2. **Usar variável de ambiente durante desenvolvimento**:
   ```bash
   export PYTHONDONTWRITEBYTECODE=1
   ```
   Adicionar ao `.env` ou `.bashrc`

3. **Adicionar ao .gitignore**:
   ```
   __pycache__/
   *.pyc
   *.pyo
   ```

### Para CI/CD

Adicionar step de limpeza de cache antes dos testes:
```yaml
- name: Clean Python cache
  run: |
    find . -type d -name "__pycache__" -exec rm -rf {} + || true
    find . -type f -name "*.pyc" -delete || true
```

## Script de Limpeza

Criar `agents/scripts/clean_cache.sh`:

```bash
#!/bin/bash
# Limpa todo o cache Python do projeto

echo "Limpando cache Python..."

# Remover __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
echo "  ✓ Diretórios __pycache__ removidos"

# Remover .pyc
find . -type f -name "*.pyc" -delete 2>/dev/null || true
echo "  ✓ Arquivos .pyc removidos"

# Remover .pyo (Python 2 legacy)
find . -type f -name "*.pyo" -delete 2>/dev/null || true
echo "  ✓ Arquivos .pyo removidos"

echo "Cache limpo com sucesso!"
```

Tornar executável:
```bash
chmod +x agents/scripts/clean_cache.sh
```

Uso:
```bash
./agents/scripts/clean_cache.sh
```

## Comando Final Funcionando

```bash
source agents/.venv/bin/activate && \
python3 agents/scripts/run_strategy_agent.py zeroum "Automarticles" \
  -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS"
```

**Status**: ✓ Funcionando perfeitamente após limpeza de cache

## Lições Aprendidas

1. **Cache Python pode mascarar problemas**: Mesmo com dependências corretas, bytecode antigo pode causar erros
2. **Importações opcionais requerem cuidado**: O padrão `try/except ImportError` com fallback para `None` é comum em bibliotecas, mas cria armadilhas de cache
3. **Teste de importação direta != teste de uso real**: Import direto funcionava, mas uso via módulos falhava devido ao cache
4. **Limpeza de cache deve ser parte do workflow**: Especialmente após mudanças em dependências

## Referências

- Python Bytecode: https://docs.python.org/3/glossary.html#term-bytecode
- `__pycache__`: https://peps.python.org/pep-3147/
- `PYTHONDONTWRITEBYTECODE`: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
