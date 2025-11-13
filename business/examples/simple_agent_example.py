"""
Exemplo completo: Como criar um agente do zero usando o framework.

Este exemplo mostra como construir um agente personalizado sem depender
de regras de negócio existentes, utilizando apenas os componentes do framework.
"""

import logging
import sys
from pathlib import Path
from typing import Any, Dict, Optional

# Garantir que o pacote agents esteja acessível mesmo quando o script roda a partir de subpastas
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from framework.core.context import AgentContext, RunConfig
from framework.core.decorators import handle_agent_errors, log_execution
from framework.io.workspace import WorkspaceManager
from framework.io.manifest import ManifestStore
from framework.observability import MetricsCollector, TodoManager, TracingManager
from framework.llm.factory import build_llm


class SimpleCustomAgent:
    """
    Exemplo de agente customizado construído com o framework.

    Este agente demonstra como usar os componentes básicos para criar
    um agente que processa contexto e gera artefatos.
    """

    def __init__(
        self,
        context_name: str,
        context_description: str = "",
        base_path: Optional[Path] = None,
    ):
        """
        Inicializa o agente customizado.

        Args:
            context_name: Nome do contexto de execução
            context_description: Descrição detalhada do contexto
            base_path: Caminho base (padrão: diretório agents/)
        """
        # 1. Criar contexto imutável
        self.context = AgentContext(
            context_name=context_name,
            context_description=context_description,
            strategy_name="CustomStrategy",
            process_code="01-CustomProcess",
            base_path=base_path or Path(__file__).parent.parent.parent.parent,
        )

        # 2. Inicializar componentes do framework
        self.workspace = WorkspaceManager(self.context)
        self.manifest_store = ManifestStore.from_context(self.context)
        self.metrics = MetricsCollector()
        self.tracing = TracingManager()

        # 3. Inicializar sistema de TODOs
        pipeline_dir = self.context.workspace_root / "_pipeline"
        self.todo_manager = TodoManager(
            process_code=self.context.process_code or "custom",
            context_name=self.context.context_name,
            pipeline_dir=pipeline_dir,
        )

        # 4. Construir LLM usando factory (opcional - pode ser None se sem lang chain)
        try:
            self.llm = build_llm()
        except RuntimeError:
            self.llm = None  # LLM não disponível
        except Exception as exc:  # noqa: BLE001 - fallback explícito
            logging.warning("LLM indisponível: %s", exc)
            self.llm = None

    @handle_agent_errors(reraise=True)
    @log_execution(level=logging.INFO)
    def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
        """
        Executa o agente customizado.

        Args:
            config: Configuração de execução (opcional)

        Returns:
            Dicionário com resultados da execução
        """
        if config is None:
            config = RunConfig()

        # Iniciar tracing
        if self.tracing.is_enabled:
            self.tracing.start_trace("simple_custom_agent")

        # Iniciar timer
        self.metrics.start_timer("execution")

        try:
            # Preparar workspace
            self._setup_workspace()

            # Executar processamento
            result = self._process()

            # Gerar artefatos
            artifacts = self._generate_artifacts(result)

            # Publicar manifesto
            manifest = self._publish_manifest(artifacts, "completed")

            # Registrar métricas
            elapsed = self.metrics.stop_timer("execution")

            return {
                "status": "success",
                "manifest": manifest,
                "artifacts": artifacts,
                "execution_time": elapsed,
                "metrics": self.metrics.get_summary(),
            }

        finally:
            if self.tracing.is_enabled:
                self.tracing.end_trace()

    def _setup_workspace(self) -> None:
        """Prepara workspace e estrutura de diretórios."""
        # Garantir que workspace existe
        self.workspace.ensure_workspace()

        # Criar diretório de pipeline
        pipeline_dir = self.context.workspace_root / "_pipeline"
        pipeline_dir.mkdir(parents=True, exist_ok=True)

        # Criar TODOs para tracking
        if self.todo_manager.enabled:
            self.todo_manager.add_todo("Preparar workspace", status="completed")
            self.todo_manager.add_todo("Processar contexto", status="pending")
            self.todo_manager.add_todo("Gerar artefatos", status="pending")
            self.todo_manager.add_todo("Publicar manifesto", status="pending")

    def _process(self) -> Dict[str, Any]:
        """
        Processa o contexto usando LLM.

        Returns:
            Resultado do processamento
        """
        if self.todo_manager.enabled:
            self.todo_manager.update_status("todo-002", "in_progress")

        # Construir prompt
        prompt = self._build_prompt()

        response: Optional[Any] = None

        # Invocar LLM (ou usar fallback se não disponível)
        if self.llm is not None:
            self.metrics.start_timer("llm_call")
            response = self.llm.invoke(prompt)
            llm_time = self.metrics.stop_timer("llm_call")

            # Registrar uso de tokens (exemplo - ajustar conforme response real)
            if hasattr(response, "usage_metadata"):
                usage = response.usage_metadata
                self.metrics.record_token_usage(
                    input_tokens=getattr(usage, "input_tokens", 0),
                    output_tokens=getattr(usage, "output_tokens", 0),
                    cost_per_1k_input=0.01,  # Ajustar conforme modelo
                    cost_per_1k_output=0.03,
                )

            # Extrair conteúdo
            content = response.content if hasattr(response, "content") else str(response)
        else:
            # Fallback sem LLM
            llm_time = 0.0
            content = f"# Processamento Mock\n\n{prompt}\n\n---\n\n(LLM não disponível - usando fallback mock)"
            response = None

        if self.todo_manager.enabled:
            self.todo_manager.mark_completed("todo-002")

        return {
            "content": content,
            "llm_time": llm_time,
            "raw_response": response,
        }

    def _build_prompt(self) -> str:
        """
        Constrói prompt para o LLM.

        Returns:
            Prompt formatado
        """
        return f"""
# Contexto
{self.context.context_description or "Nenhuma descrição fornecida"}

# Tarefa
Analise o contexto acima e gere um relatório estruturado com:
1. Principais pontos identificados
2. Análise crítica
3. Recomendações de ação

# Formato
Use markdown para formatação. Seja objetivo e claro.
"""

    def _generate_artifacts(self, result: Dict[str, Any]) -> list[Path]:
        """
        Gera e salva artefatos no workspace.

        Args:
            result: Resultado do processamento

        Returns:
            Lista de caminhos dos artefatos gerados
        """
        if self.todo_manager.enabled:
            self.todo_manager.update_status("todo-003", "in_progress")

        artifacts: list[Path] = []

        # Salvar resultado principal
        content = result.get("content", "")
        artifact_path = self.workspace.write_artifact(
            folder=self.context.workspace_root / (self.context.process_code or "custom"),
            slug="resultado-processamento",
            content=content,
            extension=".MD",
        )
        artifacts.append(artifact_path)

        if self.todo_manager.enabled:
            self.todo_manager.mark_completed("todo-003")

        return artifacts

    def _publish_manifest(
        self, artifacts: list[Path], status: str
    ) -> Dict[str, Any]:
        """
        Publica manifesto com resultados da execução.

        Args:
            artifacts: Lista de artefatos gerados
            status: Status da execução

        Returns:
            Manifesto publicado
        """
        if self.todo_manager.enabled:
            self.todo_manager.update_status("todo-004", "in_progress")

        manifest = {
            "process": self.context.process_code or "custom",
            "strategy": self.context.strategy_name,
            "context": self.context.context_name,
            "status": status,
            "artifacts": [str(p) for p in artifacts],
            "metrics": self.metrics.get_summary(),
        }

        # Incluir resumo de TODOs se habilitado
        if self.todo_manager.enabled:
            manifest["todos_summary"] = self.todo_manager.get_summary()

        # Salvar manifesto
        manifest_name = f"{self.context.process_code or 'custom'}-manifest.json"
        self.manifest_store.write(manifest_name, manifest)

        if self.todo_manager.enabled:
            self.todo_manager.mark_completed("todo-004")

        return manifest


# =============================================================================
# Exemplo de uso
# =============================================================================

def main():
    """Função principal demonstrando uso do agente."""
    # Criar agente
    agent = SimpleCustomAgent(
        context_name="ExemploFramework",
        context_description=(
            "Este é um exemplo de contexto para demonstrar o uso do framework. "
            "O agente deve analisar este contexto e gerar um relatório estruturado."
        ),
    )

    # Executar agente
    result = agent.run()

    # Exibir resultados
    print("\n" + "=" * 80)
    print("EXECUÇÃO CONCLUÍDA")
    print("=" * 80)
    print(f"Status: {result['status']}")
    print(f"Tempo de execução: {result['execution_time']:.2f}s")
    print(f"Artefatos gerados: {len(result['artifacts'])}")
    print(f"\nArtefatos:")
    for artifact in result["artifacts"]:
        print(f"  - {artifact}")
    print("\nMétricas:")
    metrics = result["metrics"]
    print(f"  - Total de métricas: {metrics['total_metrics']}")
    print(f"  - Total de tokens: {metrics['tokens']['total_tokens']}")
    print(f"  - Custo total: ${metrics['tokens']['total_cost']:.4f}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
