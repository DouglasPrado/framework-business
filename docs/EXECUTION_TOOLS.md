# Execution Tools - Referência Completa

## Visão Geral

As Execution Tools são ferramentas que permitem ao LLM executar comandos shell, operações Git, e manipulação de arquivos de forma segura e controlada.

**Total: 11 tools**

## Shell Command Execution

### run_command

Executa comandos shell com controles de segurança.

**Assinatura:**
```python
run_command(command: str, cwd: Optional[str] = None, timeout: int = 30, check: bool = False) -> str
```

**Parâmetros:**
- `command`: Comando shell a executar
- `cwd`: Diretório de trabalho (opcional)
- `timeout`: Timeout em segundos (default: 30)
- `check`: Lançar exceção se comando falhar (default: False)

**Retorno:**
- String com output do comando (stdout + stderr)

**Segurança:**
- Apenas comandos na whitelist são permitidos
- Padrões perigosos são bloqueados
- Timeout obrigatório
- Audit logging de todos os comandos

**Exemplos:**
```python
# Listar arquivos
output = run_command("ls -la")

# Executar em diretório específico
output = run_command("ls", cwd="/home/user/project")

# Com timeout customizado
output = run_command("python script.py", timeout=60)
```

**Comandos Permitidos:**
```
git, ls, cat, head, tail, wc, find, grep,
python, python3, pip, pytest, npm, node, make, docker
```

**Padrões Bloqueados:**
```
rm -rf /, rm -rf *, fork bombs, dd, mkfs, format,
> /dev/, wget, curl, chmod 777, chown, sudo
```

## Git Operations

### git_status

Obtém status do repositório Git.

**Assinatura:**
```python
git_status(cwd: Optional[str] = None) -> str
```

**Exemplos:**
```python
# Status do repositório atual
status = git_status()

# Status de repositório específico
status = git_status(cwd="/path/to/repo")
```

**Output:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   file1.py
  modified:   file2.py

Untracked files:
  newfile.py
```

---

### git_diff

Mostra diferenças em arquivos.

**Assinatura:**
```python
git_diff(file: Optional[str] = None, cwd: Optional[str] = None) -> str
```

**Parâmetros:**
- `file`: Arquivo específico para diff (opcional)
- `cwd`: Diretório do repositório (opcional)

**Exemplos:**
```python
# Diff de todas as mudanças
diff = git_diff()

# Diff de arquivo específico
diff = git_diff(file="agents/framework/tools/registry.py")
```

**Output:**
```diff
diff --git a/file.py b/file.py
index 1234567..89abcdef 100644
--- a/file.py
+++ b/file.py
@@ -10,3 +10,4 @@
 def function():
     pass
+    print("new line")
```

---

### git_add

Adiciona arquivos ao staging area.

**Assinatura:**
```python
git_add(files: List[str], cwd: Optional[str] = None) -> str
```

**Parâmetros:**
- `files`: Lista de paths de arquivos
- `cwd`: Diretório do repositório (opcional)

**Exemplos:**
```python
# Adicionar arquivo único
git_add(["file.py"])

# Adicionar múltiplos arquivos
git_add(["file1.py", "file2.py", "file3.py"])

# Adicionar todos os arquivos de uma vez
git_add(["."])
```

---

### git_commit

Cria commit com mensagem.

**Assinatura:**
```python
git_commit(message: str, cwd: Optional[str] = None) -> str
```

**Parâmetros:**
- `message`: Mensagem do commit
- `cwd`: Diretório do repositório (opcional)

**Exemplos:**
```python
# Commit simples
git_commit("Add new feature")

# Commit com mensagem multi-linha
git_commit("""Add autonomous execution

- Implement AutonomousAgent
- Add security controls
- Create execution tools""")
```

**Output:**
```
[main abc1234] Add new feature
 2 files changed, 50 insertions(+), 10 deletions(-)
```

---

### git_log

Mostra histórico de commits.

**Assinatura:**
```python
git_log(limit: int = 10, cwd: Optional[str] = None) -> str
```

**Parâmetros:**
- `limit`: Número de commits a mostrar (default: 10)
- `cwd`: Diretório do repositório (opcional)

**Exemplos:**
```python
# Últimos 10 commits
log = git_log()

# Últimos 5 commits
log = git_log(limit=5)
```

**Output:**
```
abc1234 Add new feature
def5678 Fix bug in parser
ghi9012 Update documentation
jkl3456 Refactor validation
mno7890 Add tests
```

## File System Operations

### mkdir

Cria diretório.

**Assinatura:**
```python
mkdir(path: str, parents: bool = True) -> str
```

**Parâmetros:**
- `path`: Path do diretório a criar
- `parents`: Criar diretórios pais se necessário (default: True)

**Retorno:**
- Mensagem de sucesso

**Exemplos:**
```python
# Criar diretório simples
mkdir("/tmp/testdir")

# Criar diretórios aninhados
mkdir("/tmp/parent/child/grandchild")

# Sem criar pais (falha se pai não existir)
mkdir("/tmp/existing/newdir", parents=False)
```

**Output:**
```
Diretório criado com sucesso: /tmp/testdir
```

---

### rm

Remove arquivo ou diretório.

**Assinatura:**
```python
rm(path: str, recursive: bool = False, force: bool = False) -> str
```

**Parâmetros:**
- `path`: Path a remover
- `recursive`: Remover diretórios recursivamente (default: False)
- `force`: Forçar remoção sem confirmação (default: False)

**Retorno:**
- Mensagem de sucesso

**Segurança:**
- Remoção recursiva requer `force=True`
- Paths de sistema são bloqueados (/, /etc, /usr, etc)
- Diretórios importantes (.git, node_modules) são protegidos

**Exemplos:**
```python
# Remover arquivo
rm("/tmp/file.txt")

# Remover diretório vazio
rm("/tmp/emptydir")

# Remover diretório recursivamente (REQUER force=True)
rm("/tmp/directory", recursive=True, force=True)
```

**Output:**
```
Arquivo removido: /tmp/file.txt
```

**Erros:**
```python
# Sem force=True
rm("/tmp/dir", recursive=True)
# ValueError: Remoção recursiva requer confirmação explícita (force=True)

# Path perigoso
rm("/etc/config")
# ValueError: Bloqueado: não é permitido remover path do sistema
```

---

### mv

Move ou renomeia arquivo/diretório.

**Assinatura:**
```python
mv(source: str, dest: str) -> str
```

**Parâmetros:**
- `source`: Path de origem
- `dest`: Path de destino

**Retorno:**
- Mensagem de sucesso

**Exemplos:**
```python
# Renomear arquivo
mv("/tmp/old_name.txt", "/tmp/new_name.txt")

# Mover arquivo para outro diretório
mv("/tmp/file.txt", "/home/user/file.txt")

# Renomear diretório
mv("/tmp/olddir", "/tmp/newdir")
```

**Output:**
```
Movido com sucesso: /tmp/old_name.txt -> /tmp/new_name.txt
```

## Python Execution

### run_python

Executa script Python.

**Assinatura:**
```python
run_python(script_path: str, args: Optional[str] = None, cwd: Optional[str] = None) -> str
```

**Parâmetros:**
- `script_path`: Path do script Python
- `args`: Argumentos de linha de comando (opcional)
- `cwd`: Diretório de trabalho (opcional)

**Retorno:**
- Output do script (stdout + stderr)

**Timeout:**
- Default: 60 segundos

**Exemplos:**
```python
# Executar script simples
output = run_python("script.py")

# Com argumentos
output = run_python("analyze.py", args="--input data.csv --output report.txt")

# Em diretório específico
output = run_python("script.py", cwd="/home/user/project")
```

## Test Execution

### run_tests

Executa testes com pytest.

**Assinatura:**
```python
run_tests(test_path: Optional[str] = None, cwd: Optional[str] = None) -> str
```

**Parâmetros:**
- `test_path`: Arquivo/diretório de teste específico (opcional)
- `cwd`: Diretório de trabalho (opcional)

**Retorno:**
- Output completo do pytest

**Timeout:**
- Default: 120 segundos

**Exemplos:**
```python
# Executar todos os testes
output = run_tests()

# Executar teste específico
output = run_tests(test_path="tests/test_execution.py")

# Executar diretório específico
output = run_tests(test_path="tests/unit/")
```

**Output:**
```
============================= test session starts ==============================
collected 45 items

tests/test_execution.py ........                                         [ 17%]
tests/test_security.py .............                                     [ 46%]
tests/test_autonomous.py ....................                            [100%]

============================== 45 passed in 2.35s ===============================
```

## Uso com LLM

### Como o LLM Usa as Tools

O LLM recebe as tools como funções disponíveis e decide quando e como usá-las:

**Exemplo de Task:**
> "Check git status and list recent commits"

**LLM Planning:**
```json
{
  "steps": [
    {
      "number": 1,
      "description": "Check git repository status",
      "tools_needed": ["git_status"],
      "expected_outcome": "Current status of repo"
    },
    {
      "number": 2,
      "description": "List recent commits",
      "tools_needed": ["git_log"],
      "expected_outcome": "Last 10 commits"
    }
  ]
}
```

**LLM Execution:**
```python
# Step 1
status = git_status()
# LLM reads output and understands current state

# Step 2
log = git_log(limit=10)
# LLM reads commits and prepares summary
```

### Tool Chaining

O LLM pode encadear tools para tarefas complexas:

**Task:**
> "Find all Python files, count their lines, and create report"

**LLM Execution:**
```python
# 1. Find files
files = glob("**/*.py")

# 2. Read each file
results = []
for file in files:
    content = read_file(file)
    lines = len(content.split('\n'))
    results.append(f"{file}: {lines} lines")

# 3. Create report
report = "\n".join(results)
write_file("line_count_report.txt", report)
```

## Error Handling

### Tipos de Erros

**ValueError:**
- Comando não permitido pela whitelist
- Path bloqueado por segurança
- Parâmetros inválidos

**subprocess.TimeoutExpired:**
- Comando excedeu timeout

**subprocess.CalledProcessError:**
- Comando retornou exit code não-zero (com `check=True`)

**FileNotFoundError:**
- Arquivo ou diretório não existe

### Tratamento de Erros

```python
from agents.framework.tools.builtin.execution import run_command

try:
    output = run_command("git status")
except ValueError as e:
    # Comando bloqueado ou inválido
    print(f"Security error: {e}")
except subprocess.TimeoutExpired:
    # Comando muito lento
    print("Command timed out")
except Exception as e:
    # Erro genérico
    print(f"Error: {e}")
```

### Recovery Automático

Quando `enable_recovery=True` no `AutonomousAgent`:

```python
# Step fails
try:
    run_command("invalid_command")
except ValueError as e:
    # LLM analyzes error
    # Decides recovery strategy
    # Retries with different approach
```

## Best Practices

### 1. Sempre Use Timeouts

```python
# ✓ Good
run_command("python long_script.py", timeout=300)

# ✗ Bad (uses default 30s, may fail)
run_command("python long_script.py")
```

### 2. Valide Paths

```python
from agents.framework.security.controls import PathValidator

validator = PathValidator()
is_safe, reason = validator.validate(user_path)

if is_safe:
    content = read_file(user_path)
```

### 3. Use Working Directory

```python
# ✓ Good (explicit cwd)
run_command("ls -la", cwd="/home/user/project")

# ~ OK but less clear
run_command("ls -la /home/user/project")
```

### 4. Handle Errors Gracefully

```python
try:
    output = run_tests(test_path="tests/")
except Exception as e:
    # Don't crash, log and continue
    logger.error(f"Tests failed: {e}")
    output = f"Tests could not run: {e}"
```

### 5. Audit Critical Operations

```python
from agents.framework.security.controls import get_command_validator

validator = get_command_validator()

# Audit log is automatically maintained
validator.validate("rm -rf important_dir")

# Review audit later
for entry in validator.get_audit_log():
    print(entry)
```

## Referências

- [AUTONOMOUS_EXECUTION.md](AUTONOMOUS_EXECUTION.md) - Guia completo de execução autônoma
- [SECURITY_CONTROLS.md](SECURITY_CONTROLS.md) - Controles de segurança detalhados
- [agents/framework/tools/builtin/execution.py](../agents/framework/tools/builtin/execution.py) - Código fonte
