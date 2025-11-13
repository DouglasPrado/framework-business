#!/usr/bin/env python3
"""
Remove métodos duplicados dos subagentes que agora estão na SubagentBase.
"""

import re
from pathlib import Path

SUBAGENTS = [
    "landing_page_creation.py",
    "problem_hypothesis_definition.py",
    "target_user_identification.py",
    "user_interview_validation.py",
    "client_delivery.py",
    "problem_hypothesis_express.py",
]

BASE_DIR = Path("business/strategies/zeroum/subagents")

# Padrões de métodos a remover
METHODS_TO_REMOVE = [
    r'\n\s+def _setup_directories\(self\).*?(?=\n\s+def |\n\nclass |\n__all__|$)',
    r'\n\s+def _save_document\(self,.*?(?=\n\s+def |\n\nclass |\n__all__|$)',
    r'\n\s+def _invoke_llm\(self,.*?(?=\n\s+def |\n\nclass |\n__all__|$)',
    r'\n\s+def _format_list\(self,.*?(?=\n\s+def |\n\nclass |\n__all__|$)',
]


def remove_methods(filepath: Path) -> bool:
    """Remove métodos duplicados de um arquivo."""
    print(f"\n🔄 Processando {filepath.name}...")

    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content
        removed_count = 0

        for pattern in METHODS_TO_REMOVE:
            matches = list(re.finditer(pattern, content, re.DOTALL))
            if matches:
                # Remover da última ocorrência para a primeira (para não afetar índices)
                for match in reversed(matches):
                    method_name = re.search(r'def (_\w+)\(', match.group())
                    if method_name:
                        print(f"   ├─ Removendo {method_name.group(1)}()")
                        content = content[:match.start()] + content[match.end():]
                        removed_count += 1

        if content != original_content:
            # Limpar linhas vazias consecutivas
            content = re.sub(r'\n\n\n+', '\n\n', content)
            filepath.write_text(content, encoding='utf-8')
            print(f"   ✅ {removed_count} método(s) removido(s)")
            return True
        else:
            print(f"   ⚠️  Nenhum método duplicado encontrado")
            return False

    except Exception as e:
        print(f"   ✗ Erro: {e}")
        return False


def main():
    print("="*80)
    print("REMOÇÃO DE MÉTODOS DUPLICADOS DOS SUBAGENTES")
    print("="*80)

    success_count = 0

    for filename in SUBAGENTS:
        filepath = BASE_DIR / filename

        if not filepath.exists():
            print(f"\n⚠️  Arquivo não encontrado: {filename}")
            continue

        if remove_methods(filepath):
            success_count += 1

    print("\n" + "="*80)
    print(f"RESUMO: {success_count}/{len(SUBAGENTS)} arquivos processados com sucesso")
    print("="*80)
    print("\n💡 Próximos passos:")
    print("   1. Verificar arquivos modificados")
    print("   2. Executar testes de importação")
    print("   3. Testar execução de um subagente")


if __name__ == "__main__":
    main()
