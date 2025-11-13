# Security Controls - Documentação Completa

## Visão Geral

O sistema de segurança fornece múltiplas camadas de proteção para execução autônoma de tarefas:

1. **CommandValidator**: Valida comandos shell antes de executar
2. **PathValidator**: Valida acessos a arquivos e diretórios
3. **RateLimiter**: Limita taxa de operações
4. **Audit Logging**: Registra todas as operações críticas

## SecurityConfig

Configuração centralizada de segurança.

### Estrutura

```python
@dataclass
class SecurityConfig:
    allowed_commands: Set[str]            # Whitelist de comandos
    dangerous_patterns: List[str]         # Blacklist de padrões
    blocked_paths: Set[str]              # Paths bloqueados
    require_confirmation_patterns: List[str]  # Padrões que requerem confirmação
    max_commands_per_minute: int         # Rate limit
    enable_audit_log: bool               # Habilitar audit log
    audit_log_path: Optional[Path]       # Path para arquivo de audit
```

### Valores Padrão

**Comandos Permitidos:**
```python
{
    "git", "ls", "cat", "head", "tail", "wc", "find", "grep",
    "python", "python3", "pip", "pytest", "npm", "node", "make", "docker"
}
```

**Padrões Perigosos:**
```python
[
    "rm -rf /",
    "rm -rf *",
    ":(){ :|:& };:",  # Fork bomb
    "dd if=",
    "mkfs",
    "format",
    "> /dev/",
    "wget",
    "curl",
    "chmod 777",
    "chown",
    "sudo",
    "su -",
]
```

**Paths Bloqueados:**
```python
{
    "/", "/etc", "/usr", "/bin", "/sbin", "/var", "/boot",
    "/sys", "/proc", "/dev", "/root"
}
```

**Padrões que Requerem Confirmação:**
```python
[
    "rm -rf",
    "git push --force",
    "git push -f",
    "DROP TABLE",
    "DELETE FROM",
]
```

### Uso

```python
from agents.framework.security.controls import SecurityConfig

# Usar configuração padrão
config = SecurityConfig()

# Configuração customizada
config = SecurityConfig(
    allowed_commands={"git", "ls", "python"},
    max_commands_per_minute=10,
    enable_audit_log=True,
    audit_log_path=Path("security_audit.log")
)
```

## CommandValidator

Valida comandos shell contra políticas de segurança.

### Métodos

#### validate(command: str) -> tuple[bool, str]

Valida se comando é seguro para executar.

**Retorno:**
- `(True, "Comando permitido")` - Comando seguro
- `(False, "Razão do bloqueio")` - Comando bloqueado

**Exemplos:**

```python
from agents.framework.security.controls import CommandValidator

validator = CommandValidator()

# Comando seguro
is_safe, reason = validator.validate("git status")
print(is_safe)  # True
print(reason)   # "Comando permitido"

# Comando perigoso
is_safe, reason = validator.validate("rm -rf /")
print(is_safe)  # False
print(reason)   # "Comando contém padrão perigoso: rm -rf /"

# Comando não na whitelist
is_safe, reason = validator.validate("curl http://example.com")
print(is_safe)  # False
print(reason)   # "Comando não está na whitelist..."
```

#### requires_confirmation(command: str) -> bool

Verifica se comando requer confirmação do usuário.

**Exemplos:**

```python
validator = CommandValidator()

# Operações destrutivas requerem confirmação
print(validator.requires_confirmation("rm -rf mydir"))  # True
print(validator.requires_confirmation("git push --force"))  # True

# Operações normais não requerem
print(validator.requires_confirmation("git status"))  # False
print(validator.requires_confirmation("ls -la"))  # False
```

#### get_audit_log() -> List[Dict[str, str]]

Retorna todas as entradas do audit log.

**Exemplo:**

```python
validator = CommandValidator(
    SecurityConfig(enable_audit_log=True)
)

validator.validate("git status")
validator.validate("rm -rf /")

for entry in validator.get_audit_log():
    print(f"{entry['timestamp']} | {entry['action']} | {entry['command']}")

# Output:
# 2025-01-15 16:30:00 | ALLOWED | git status
# 2025-01-15 16:30:01 | BLOCKED | rm -rf /
```

### Integração com Execution Tools

As execution tools usam `CommandValidator` automaticamente:

```python
# Em agents/framework/tools/builtin/execution.py

def _run_command(command: str, ...):
    # Validação automática
    is_safe, reason = _is_command_safe(command)
    if not is_safe:
        raise ValueError(f"Comando bloqueado por segurança: {reason}")

    # Executa apenas se seguro
    result = subprocess.run(...)
```

### Audit Logging

Todas as validações são automaticamente auditadas:

**Formato do Log:**
```
timestamp | action | command | reason
```

**Ações:**
- `ALLOWED`: Comando permitido e executado
- `BLOCKED`: Comando bloqueado por segurança
- `CONFIRMATION_REQUIRED`: Comando requer confirmação

**Exemplo de Arquivo de Audit:**
```
2025-01-15 16:30:00 | ALLOWED | git status | Command in whitelist
2025-01-15 16:30:01 | BLOCKED | rm -rf / | Comando contém padrão perigoso: rm -rf /
2025-01-15 16:30:02 | CONFIRMATION_REQUIRED | git push --force | Matches pattern: git push --force
2025-01-15 16:30:03 | ALLOWED | python script.py | Command in whitelist
```

## PathValidator

Valida acessos a arquivos e diretórios.

### Métodos

#### validate(path: str) -> tuple[bool, str]

Validação básica de path (leitura).

**Exemplos:**

```python
from agents.framework.security.controls import PathValidator

validator = PathValidator()

# Path seguro
is_safe, reason = validator.validate("/home/user/file.txt")
print(is_safe)  # True

# Path de sistema bloqueado
is_safe, reason = validator.validate("/etc/passwd")
print(is_safe)  # False
print(reason)   # "Path is blocked: /etc"

# Path em diretório de sistema
is_safe, reason = validator.validate("/usr/local/bin/script")
print(is_safe)  # False
print(reason)   # "System directory access blocked: /usr/local/bin/script"
```

#### validate_write(path: str) -> tuple[bool, str]

Validação para operações de escrita (mais restritiva).

**Exemplos:**

```python
validator = PathValidator()

# Escrita em user space OK
is_safe, reason = validator.validate_write("/home/user/output.txt")
print(is_safe)  # True

# Escrita em root bloqueada
is_safe, reason = validator.validate_write("/newfile.txt")
print(is_safe)  # False
print(reason)   # "Cannot write to root directory"

# Escrita em diretório existente
is_safe, reason = validator.validate_write("/home/user/existing_dir")
print(is_safe)  # False (se existing_dir é um diretório)
print(reason)   # "Cannot write to existing directory (specify file path)"
```

#### validate_delete(path: str, recursive: bool = False) -> tuple[bool, str]

Validação para operações de deleção (mais restritiva ainda).

**Exemplos:**

```python
validator = PathValidator()

# Deleção de arquivo simples OK
is_safe, reason = validator.validate_delete("/tmp/file.txt")
print(is_safe)  # True

# Deleção de diretório importante bloqueada
is_safe, reason = validator.validate_delete("/project/.git", recursive=True)
print(is_safe)  # False
print(reason)   # "Cannot delete important directory: .git"

# Deleção recursiva de project root bloqueada
is_safe, reason = validator.validate_delete("/project", recursive=True)
print(is_safe)  # False (se /project contém .git ou package.json)
print(reason)   # "Cannot recursively delete project root"
```

### Diretórios Protegidos

**System Directories:**
```python
["/", "/etc", "/usr", "/bin", "/sbin", "/var", "/boot", "/sys", "/proc", "/dev", "/root"]
```

**Important Directories:**
```python
[".git", "node_modules", ".env", "venv", ".venv"]
```

**Project Root Markers:**
```python
[".git", "package.json", "pyproject.toml", "setup.py"]
```

### Uso em Execution Tools

```python
# Em agents/framework/tools/builtin/execution.py

def _write_file(path: str, content: str):
    validator = PathValidator()
    is_safe, reason = validator.validate_write(path)

    if not is_safe:
        raise ValueError(f"Write blocked: {reason}")

    # Escrita permitida
    Path(path).write_text(content)

def _rm(path: str, recursive: bool, force: bool):
    validator = PathValidator()
    is_safe, reason = validator.validate_delete(path, recursive)

    if not is_safe:
        raise ValueError(f"Delete blocked: {reason}")

    if recursive and not force:
        raise ValueError("Remoção recursiva requer confirmação explícita (force=True)")

    # Deleção permitida
    ...
```

## RateLimiter

Limita taxa de operações para prevenir abuso.

### Métodos

#### check_and_record(operation_type: str) -> bool

Verifica se operação está dentro do limite e registra.

**Retorno:**
- `True`: Operação permitida
- `False`: Rate limit excedido

**Exemplos:**

```python
from agents.framework.security.controls import RateLimiter

# Criar limiter (30 ops/minuto)
limiter = RateLimiter(max_per_minute=30)

# Verificar e registrar operação
if limiter.check_and_record("command_execution"):
    execute_command()
else:
    print("Rate limit exceeded, please wait")
```

#### get_current_rate(operation_type: str) -> int

Retorna quantidade de operações no último minuto.

**Exemplo:**

```python
limiter = RateLimiter(max_per_minute=30)

for i in range(10):
    limiter.check_and_record("test_op")

print(limiter.get_current_rate("test_op"))  # 10
```

#### reset(operation_type: Optional[str] = None)

Reseta o limiter.

**Exemplos:**

```python
limiter = RateLimiter(max_per_minute=5)

# Atingir limite
for i in range(5):
    limiter.check_and_record("op")

# Não pode mais executar
print(limiter.check_and_record("op"))  # False

# Resetar operação específica
limiter.reset("op")

# Pode executar novamente
print(limiter.check_and_record("op"))  # True

# Resetar tudo
limiter.reset()
```

### Tipos de Operação

Você pode ter limites diferentes para tipos diferentes:

```python
limiter = RateLimiter(max_per_minute=30)

# Diferentes operações têm contadores separados
limiter.check_and_record("command_execution")  # Contador 1
limiter.check_and_record("file_write")         # Contador 2
limiter.check_and_record("api_call")           # Contador 3

# Cada uma pode atingir limite independentemente
```

### Uso no Framework

```python
# No AutonomousAgent

class AutonomousAgent:
    def __init__(self, ...):
        self.rate_limiter = RateLimiter(max_per_minute=30)

    def _execute_step(self, step):
        # Verificar rate limit antes de executar
        if not self.rate_limiter.check_and_record("step_execution"):
            raise RuntimeError("Rate limit exceeded")

        # Executar step
        ...
```

## Funções Globais

### get_command_validator() -> CommandValidator

Retorna instância global de `CommandValidator`.

```python
from agents.framework.security.controls import get_command_validator

validator = get_command_validator()
is_safe, reason = validator.validate("git status")
```

### get_path_validator() -> PathValidator

Retorna instância global de `PathValidator`.

```python
from agents.framework.security.controls import get_path_validator

validator = get_path_validator()
is_safe, reason = validator.validate("/tmp/file.txt")
```

### get_rate_limiter() -> RateLimiter

Retorna instância global de `RateLimiter`.

```python
from agents.framework.security.controls import get_rate_limiter

limiter = get_rate_limiter()
if limiter.check_and_record("operation"):
    perform_operation()
```

## Configuração Customizada

### Exemplo 1: Whitelist Restrita

```python
from agents.framework.security.controls import SecurityConfig, CommandValidator

# Apenas git e python
config = SecurityConfig(
    allowed_commands={"git", "python3"},
    max_commands_per_minute=10
)

validator = CommandValidator(config)

# git OK
print(validator.validate("git status"))  # (True, ...)

# npm bloqueado
print(validator.validate("npm install"))  # (False, ...)
```

### Exemplo 2: Audit Log em Arquivo

```python
from pathlib import Path
from agents.framework.security.controls import SecurityConfig, CommandValidator

config = SecurityConfig(
    enable_audit_log=True,
    audit_log_path=Path("security_audit.log")
)

validator = CommandValidator(config)

# Todas as validações são escritas em security_audit.log
validator.validate("git status")
validator.validate("ls -la")
```

### Exemplo 3: Rate Limit Agressivo

```python
from agents.framework.security.controls import RateLimiter

# Apenas 5 operações por minuto
limiter = RateLimiter(max_per_minute=5)

for i in range(10):
    if limiter.check_and_record("api_call"):
        print(f"Call {i+1} allowed")
    else:
        print(f"Call {i+1} BLOCKED (rate limit)")

# Output:
# Call 1 allowed
# Call 2 allowed
# Call 3 allowed
# Call 4 allowed
# Call 5 allowed
# Call 6 BLOCKED (rate limit)
# Call 7 BLOCKED (rate limit)
# ...
```

## Best Practices

### 1. Use Instâncias Globais

```python
# ✓ Good - compartilha audit log e rate limits
from agents.framework.security.controls import get_command_validator

validator = get_command_validator()

# ✗ Bad - cria nova instância sem histórico
validator = CommandValidator()
```

### 2. Sempre Valide Antes de Executar

```python
# ✓ Good
validator = get_command_validator()
is_safe, reason = validator.validate(user_command)

if is_safe:
    execute(user_command)
else:
    log_security_violation(reason)

# ✗ Bad - executa sem validar
execute(user_command)
```

### 3. Monitore Audit Logs

```python
# Periodicamente revise audit logs
validator = get_command_validator()

blocked_commands = [
    entry for entry in validator.get_audit_log()
    if entry['action'] == 'BLOCKED'
]

if len(blocked_commands) > 10:
    alert_security_team(blocked_commands)
```

### 4. Ajuste Rate Limits Conforme Necessidade

```python
# Para desenvolvimento: liberal
dev_limiter = RateLimiter(max_per_minute=100)

# Para produção: conservador
prod_limiter = RateLimiter(max_per_minute=30)

# Para APIs externas: muito conservador
api_limiter = RateLimiter(max_per_minute=5)
```

### 5. Custom Paths Blocked

```python
config = SecurityConfig(
    blocked_paths={
        "/", "/etc", "/usr",  # System
        "/home/user/secrets",  # Custom
        "/var/www/production",  # Production
    }
)

validator = PathValidator(config)
```

## Integração com AutonomousAgent

O `AutonomousAgent` usa todos os security controls automaticamente:

```python
class AutonomousAgent:
    def __init__(self, ...):
        # Security controls são usados pelas execution tools
        # que o agent tem acesso
        self.tools = get_tools(AgentType.AUTONOMOUS)

        # Execution tools usam:
        # - CommandValidator para validar comandos
        # - PathValidator para validar paths
        # - RateLimiter para limitar taxa
        # - Audit logging para registrar operações

    def execute(self):
        # Durante execução, todas as operações são validadas
        # automaticamente pelas tools
        ...
```

## Troubleshooting

### Comando Bloqueado Incorretamente

**Problema:** Comando legítimo está sendo bloqueado

**Solução:** Adicione à whitelist

```python
config = SecurityConfig(
    allowed_commands=SecurityConfig().allowed_commands | {"your_command"}
)

validator = CommandValidator(config)
```

### Path Bloqueado Incorretamente

**Problema:** Path legítimo está sendo bloqueado

**Solução:** Remova da blacklist ou adicione exceção

```python
config = SecurityConfig(
    blocked_paths=SecurityConfig().blocked_paths - {"/your/path"}
)

validator = PathValidator(config)
```

### Rate Limit Muito Restritivo

**Problema:** Operações legítimas atingindo rate limit

**Solução:** Aumente o limite

```python
limiter = RateLimiter(max_per_minute=100)  # Aumentado de 30
```

### Audit Log Muito Grande

**Problema:** Arquivo de audit crescendo muito

**Solução:** Rotação de logs

```python
# Use logrotate ou implemente rotação manual
import shutil
from pathlib import Path

audit_path = Path("security_audit.log")

if audit_path.stat().st_size > 10_000_000:  # 10MB
    # Rotacionar
    shutil.move(audit_path, f"{audit_path}.{time.time()}")
```

## Referências

- [AUTONOMOUS_EXECUTION.md](AUTONOMOUS_EXECUTION.md) - Guia de execução autônoma
- [EXECUTION_TOOLS.md](EXECUTION_TOOLS.md) - Documentação das tools
- [agents/framework/security/controls.py](../agents/framework/security/controls.py) - Código fonte
