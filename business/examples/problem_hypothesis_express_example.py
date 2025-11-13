#!/usr/bin/env python3
"""
Exemplo de uso do ProblemHypothesisExpressAgent.

Este exemplo demonstra como usar o subagente ProblemHypothesisExpress
para gerar uma proposta de valor clara em 30 minutos.

Uso:
    python3 agents/business/examples/problem_hypothesis_express_example.py
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

from business.strategies.zeroum.subagents.problem_hypothesis_express import ProblemHypothesisExpressAgent


def main():
    """Exemplo de execução do ProblemHypothesisExpressAgent."""

    print("=" * 80)
    print("Exemplo: Problem Hypothesis Express Agent")
    print("=" * 80)
    print()

    # Configurar contexto da ideia
    idea_context = """
    Estou criando uma plataforma que automatiza a validação de ideias de produto
    para founders de startups. O problema é que founders gastam 3-6 meses
    construindo produtos que ninguém quer, porque não têm metodologia prática
    para validar rapidamente. Minha solução oferece um framework passo a passo
    que gera validação real em 30 dias, em vez de meses de tentativa e erro.
    """

    target_audience = "Founders de startups B2B em estágio seed"
    workspace = Path("drive") / "ExemploProblemHypothesis"

    print("Contexto da ideia:")
    print(idea_context.strip())
    print()
    print(f"Público-alvo sugerido: {target_audience}")
    print(f"Workspace: {workspace}")
    print()

    # Criar subagente
    print("Criando ProblemHypothesisExpressAgent...")
    agent = ProblemHypothesisExpressAgent(
        workspace_root=workspace,
        idea_context=idea_context,
        target_audience=target_audience,
    )
    print("✅ Subagente criado")
    print()

    # Executar sessão express (30 min simulados)
    print("Executando sessão express (5 etapas - 30 minutos simulados)...")
    print("Isso vai gerar ~6 documentos usando LLM...")
    print()

    try:
        results = agent.execute_express_session()

        print()
        print("=" * 80)
        print("✅ SESSÃO EXPRESS CONCLUÍDA!")
        print("=" * 80)
        print()

        print("Resumo:")
        print(f"  Início: {results['started_at']}")
        print(f"  Fim: {results['completed_at']}")
        print(f"  Duração target: 30 minutos")
        print()

        print("Etapas executadas:")
        for stage_name, stage_data in results["stages"].items():
            duration = stage_data.get("duration_target", "N/A")
            status_emoji = "✅" if stage_data["status"] == "completed" else "⚠️"
            print(f"  {status_emoji} {stage_name}: {stage_data['status']} ({duration})")
        print()

        print("Arquivos gerados:")
        print(f"  📁 {workspace}/00-ProblemHypothesisExpress/")
        print(f"  📄 00-sessao-consolidada.MD")
        print(f"  📁 _DATA/ (6 documentos)")
        print()

        print("Próximos passos CRÍTICOS:")
        print("  ⚠️  A frase só está pronta APÓS validação real!")
        print()
        print("  1. Abrir 05-guia-validacao.MD")
        print("  2. Seguir roteiro de validação (3 min)")
        print("  3. Documentar feedback no log")
        print("  4. Ajustar frase final")
        print()

        print("Documentos gerados:")
        print("  1. 01-foco-sessao.MD - Contexto e objetivos")
        print("  2. 02-usuarios-alvo.MD - 3-5 perfis mapeados")
        print("  3. 03-dor-central.MD - Análise da dor")
        print("  4. 04-variacoes-proposta.MD - 3 variações da frase")
        print("  5. 05-guia-validacao.MD - Roteiro de validação")
        print("  6. 06-log-versoes-feedback.MD - Template de log")
        print()

        print(f"📖 Veja o resumo completo em:")
        print(f"   {workspace}/00-ProblemHypothesisExpress/00-sessao-consolidada.MD")
        print()

        print("Template da frase (após validação):")
        print("  \"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]\"")
        print()

    except Exception as e:
        print(f"❌ Erro ao executar sessão: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
