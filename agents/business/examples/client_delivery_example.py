#!/usr/bin/env python3
"""
Exemplo de uso do ClientDeliveryAgent.

Este exemplo demonstra como usar o subagente ClientDelivery
para gerenciar todo o processo de entrega ao cliente.

Uso:
    python3 agents/business/examples/client_delivery_example.py
"""

import sys
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Adicionar root ao path
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agents.business.strategies.zeroum.subagents.client_delivery import ClientDeliveryAgent


def main():
    """Exemplo de execução do ClientDeliveryAgent."""

    print("=" * 80)
    print("Exemplo: Client Delivery Agent")
    print("=" * 80)
    print()

    # Configurar cliente
    client_name = "Acme Corp"
    delivery_scope = "Landing page + Sistema de captação de leads + Dashboard de métricas"
    deadline = "2025-12-15"
    workspace = Path("drive") / "ExemploClientDelivery"

    print(f"Cliente: {client_name}")
    print(f"Escopo: {delivery_scope}")
    print(f"Prazo: {deadline}")
    print(f"Workspace: {workspace}")
    print()

    # Criar subagente
    print("Criando ClientDeliveryAgent...")
    agent = ClientDeliveryAgent(
        workspace_root=workspace,
        client_name=client_name,
        delivery_scope=delivery_scope,
        deadline=deadline,
    )
    print("✅ Subagente criado")
    print()

    # Executar processo completo
    print("Executando processo completo de entrega (6 etapas)...")
    print("Isso vai gerar ~10 documentos usando LLM...")
    print()

    try:
        results = agent.execute_full_delivery()

        print()
        print("=" * 80)
        print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
        print("=" * 80)
        print()

        print("Resumo:")
        print(f"  Cliente: {results['client_name']}")
        print(f"  Início: {results['started_at']}")
        print(f"  Fim: {results['completed_at']}")
        print()

        print("Etapas executadas:")
        for stage_name, stage_data in results["stages"].items():
            status_emoji = "✅" if stage_data["status"] == "completed" else "🟡"
            print(f"  {status_emoji} {stage_name}: {stage_data['status']}")
        print()

        print("Arquivos gerados:")
        print(f"  📁 {workspace}/10-ClientDelivery/")
        print(f"  📄 00-relatorio-consolidado.MD")
        print(f"  📁 _DATA/ (10 documentos)")
        print()

        print("Próximos passos manuais:")
        print("  1. Executar produção seguindo checklist")
        print("  2. Realizar QA completo")
        print("  3. Agendar reunião de entrega")
        print("  4. Enviar follow-up pós-entrega")
        print("  5. Coletar depoimento")
        print()

        print(f"📖 Veja o relatório completo em:")
        print(f"   {workspace}/10-ClientDelivery/00-relatorio-consolidado.MD")

    except Exception as e:
        print(f"❌ Erro ao executar processo: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
