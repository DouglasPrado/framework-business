#!/usr/bin/env python3
"""
Script para migrar subagentes para usar SubagentBase.

Automatiza as mudanças necessárias:
1. Substituir imports
2. Adicionar herança de SubagentBase
3. Adicionar process_name e strategy_name
4. Refatorar __init__
"""

import re
from pathlib import Path

# Mapeamento de subagentes para seus process_name
SUBAGENT_MAPPING = {
    "problem_hypothesis_definition.py": "01-ProblemHypothesisDefinition",
    "target_user_identification.py": "02-TargetUserIdentification",
    "user_interview_validation.py": "03-UserInterviewValidation",
    "client_delivery.py": "10-ClientDelivery",
    "problem_hypothesis_express.py": "00-ProblemHypothesisExpress",
}


def migrate_subagent(file_path: Path, process_name: str) -> bool:
    """
    Migra um subagente para usar SubagentBase.

    Args:
        file_path: Caminho do arquivo do subagente
        process_name: Nome do processo (ex: "01-ProblemHypothesisDefinition")

    Returns:
        True se migração foi bem-sucedida
    """
    print(f"\n🔄 Migrando {file_path.name}...")

    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # 1. Substituir imports
        print("  ├─ Substituindo imports...")
        content = re.sub(
            r'from framework\.llm\.factory import build_llm\nfrom framework\.tools import AgentType, get_tools',
            'from business.strategies.zeroum.subagents.base import SubagentBase',
            content
        )

        # Se não encontrou o padrão exato, tentar pattern mais flexível
        if content == original_content:
            content = re.sub(
                r'from framework\.llm\.factory import build_llm\n.*from framework\.tools import.*',
                'from business.strategies.zeroum.subagents.base import SubagentBase',
                content,
                flags=re.MULTILINE
            )

        # 2. Extrair nome da classe
        class_match = re.search(r'class (\w+Agent):', content)
        if not class_match:
            print(f"  ✗ Erro: Não encontrou nome da classe")
            return False

        class_name = class_match.group(1)
        print(f"  ├─ Classe encontrada: {class_name}")

        # 3. Adicionar herança de SubagentBase
        print("  ├─ Adicionando herança de SubagentBase...")
        content = re.sub(
            rf'class {class_name}:',
            f'class {class_name}(SubagentBase):',
            content
        )

        # 4. Adicionar process_name e strategy_name logo após o docstring da classe
        print(f"  ├─ Adicionando process_name = {process_name}...")

        # Encontrar final do docstring da classe
        class_pattern = rf'(class {class_name}\(SubagentBase\):\n\s+"""(?:.*?)""")'
        match = re.search(class_pattern, content, re.DOTALL)

        if match:
            docstring_end = match.end()
            before = content[:docstring_end]
            after = content[docstring_end:]

            # Adicionar process_name e strategy_name
            new_attrs = f'\n\n    process_name = "{process_name}"\n    strategy_name = "ZeroUm"'
            content = before + new_attrs + after

        # 5. Refatorar __init__
        print("  ├─ Refatorando __init__...")

        # Encontrar __init__
        init_pattern = r'(def __init__\((?:.*?)\) -> None:\n\s+"""(?:.*?)""")'
        init_match = re.search(init_pattern, content, re.DOTALL)

        if init_match:
            init_end = init_match.end()
            before_init = content[:init_end]
            after_init = content[init_end:]

            # Encontrar as linhas com self.llm e self.tools
            # Substituir por chamada ao super().__init__()

            # Remover self.llm = build_llm()
            after_init = re.sub(
                r'\n\s+self\.llm = build_llm\(\).*\n',
                '\n',
                after_init
            )

            # Remover self.tools = get_tools(...)
            after_init = re.sub(
                r'\n\s+self\.tools = get_tools\(AgentType\.PROCESS\) if enable_tools else \[\].*\n',
                '\n',
                after_init
            )

            # Encontrar primeira linha de atribuição (ex: self.workspace_root = ...)
            first_attr_match = re.search(r'\n(\s+)(self\.\w+ = )', after_init)

            if first_attr_match:
                indent = first_attr_match.group(1)
                pos = first_attr_match.start()

                # Inserir super().__init__() antes da primeira atribuição
                super_call = f'\n{indent}# Inicializar base (LLM, tools, conhecimento)\n'
                super_call += f'{indent}super().__init__(\n'
                super_call += f'{indent}    workspace_root=workspace_root,\n'
                super_call += f'{indent}    enable_tools=enable_tools,\n'
                super_call += f'{indent}    load_knowledge=True\n'
                super_call += f'{indent})\n\n'
                super_call += f'{indent}# Atributos específicos\n'

                after_init = after_init[:pos] + super_call + after_init[pos:]

            content = before_init + after_init

        # 6. Salvar
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print(f"  ✓ {file_path.name} migrado com sucesso!")
            return True
        else:
            print(f"  ⚠ Nenhuma mudança detectada")
            return False

    except Exception as e:
        print(f"  ✗ Erro ao migrar: {e}")
        return False


def main():
    """Executa migração de todos os subagentes."""
    print("="*80)
    print("MIGRAÇÃO DE SUBAGENTES PARA SUBAGENTBASE")
    print("="*80)

    base_dir = Path(__file__).parent / "business" / "strategies" / "zeroum" / "subagents"

    success_count = 0
    total = len(SUBAGENT_MAPPING)

    for filename, process_name in SUBAGENT_MAPPING.items():
        file_path = base_dir / filename

        if not file_path.exists():
            print(f"\n⚠ Arquivo não encontrado: {filename}")
            continue

        if migrate_subagent(file_path, process_name):
            success_count += 1

    print("\n" + "="*80)
    print(f"RESUMO: {success_count}/{total} subagentes migrados com sucesso")
    print("="*80)


if __name__ == "__main__":
    main()
