"""Orquestrador da estratégia ZeroUm refatorado usando o framework."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from framework.core.context import AgentContext, RunConfig
from framework.orchestration.graph import OrchestrationGraph
from framework.io.workspace import WorkspaceManager
from framework.io.package import PackageService
from framework.io.knowledge import StrategyKnowledgeManager
from framework.observability import MetricsCollector, TracingManager
from framework.llm.factory import build_llm

# Importar registry de subagentes
from business.strategies.zeroum.subagents.registry import SubagentRegistry

logger = logging.getLogger(__name__)


class ZeroUmOrchestrator:
    """
    Orquestrador da estratégia ZeroUm usando o novo framework.

    Utiliza AgentContext para configuração e ProcessPipeline para execução.
    """

    strategy_name = "ZeroUm"

    def __init__(
        self,
        context_name: str,
        context_description: str = "",
        base_path: Optional[Path] = None,
    ) -> None:
        """
        Inicializa o orquestrador ZeroUm.

        Args:
            context_name: Nome do contexto de execução
            context_description: Descrição do contexto
            base_path: Caminho base (padrão: agents/)
        """
        # Criar contexto imutável
        repo_root = base_path or Path(__file__).resolve().parents[3]

        self.context = AgentContext(
            context_name=context_name,
            context_description=context_description,
            strategy_name=self.strategy_name,
            base_path=repo_root,
        )

        # Componentes do framework
        self.workspace = WorkspaceManager(self.context)
        self.package_service = PackageService(self.context)
        self.knowledge_manager = StrategyKnowledgeManager(
            base_path=repo_root,
            strategy_name=self.strategy_name
        )
        self.metrics = MetricsCollector()
        self.tracing = TracingManager()

    def run(self, config: Optional[RunConfig] = None) -> Dict[str, Any]:
        """
        Executa a estratégia ZeroUm usando OrchestrationGraph com roteamento dinâmico.

        Args:
            config: Configuração de execução (opcional)

        Returns:
            Dicionário com manifests, consolidated e archive
        """
        if config is None:
            config = RunConfig()

        # Iniciar tracing
        if self.tracing.is_enabled:
            self.tracing.start_trace(f"zeroum_strategy_{self.context.context_name}")

        self.metrics.start_timer("zeroum_strategy")

        try:
            # Criar grafo de orquestração com roteamento dinâmico
            graph = OrchestrationGraph.from_handlers({
                "collect_context": self._collect_context,
                "analyze_context": self._analyze_context,
                "execute_subagent": self._execute_subagent,
                "validate_result": self._validate_result,
            })

            # Executar grafo
            final_state = graph.execute(initial_state={})

            # Registrar métricas
            elapsed = self.metrics.stop_timer("zeroum_strategy")
            logger.info(f"Estratégia ZeroUm concluída em {elapsed:.2f}s")

            return {
                "manifests": final_state.get("manifests", []),
                "consolidated": final_state.get("consolidated", ""),
                "archive": final_state.get("archive", ""),
                "metrics": self.metrics.get_summary(),
                "selected_subagent": final_state.get("selected_subagent", ""),
                "complexity": final_state.get("complexity", ""),
            }

        finally:
            if self.tracing.is_enabled:
                self.tracing.end_trace()

    def _collect_context(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara workspace para execução da estratégia.

        Args:
            state: Estado atual da orquestração

        Returns:
            Estado atualizado
        """
        logger.info(
            "Preparando workspace para estratégia %s",
            self.strategy_name,
        )

        # Garantir que workspace existe
        self.workspace.ensure_workspace()
        pipeline_dir = self.context.workspace_root / "_pipeline"
        pipeline_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Workspace preparado em %s", self.context.workspace_root)

        return state

    def _analyze_context(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analisa o contexto da execução e seleciona o subagente apropriado.

        Args:
            state: Estado atual da orquestração

        Returns:
            Estado atualizado com subagente selecionado
        """
        logger.info("Analisando contexto para seleção de subagente...")
        logger.info("Carregando conhecimento da estratégia ZeroUm...")

        # Carregar conhecimento da estratégia usando o manager genérico
        strategy_knowledge = self.knowledge_manager.load_default_knowledge()

        # Construir prompt de análise
        prompt = f"""
Você é um especialista em metodologia ZeroUm e deve analisar o contexto abaixo para recomendar o processo mais adequado.

{strategy_knowledge}

CONTEXTO DO PROJETO:
- Nome: {self.context.context_name}
- Descrição: {self.context.context_description}

SUBAGENTES DISPONÍVEIS:
"""
        # Adicionar informações dos subagentes registrados
        for name in SubagentRegistry.list_available():
            info = SubagentRegistry.get_info(name)
            prompt += f"""
- {name}:
  Descrição: {info['description']}
  Processo: {info['process_code']}
  Complexidade: {info['complexity']}
  Duração: {info['duration']}
"""

        prompt += """
Sua tarefa:
1. Analise o contexto fornecido.
2. Classifique a complexidade (simple/moderate/complex).
3. Liste a ordem completa dos subagentes que devem ser executados (pipeline com 1+ itens).
4. Justifique brevemente o plano proposto.

Responda APENAS com um JSON válido no seguinte formato:
{
  "complexity": "simple|moderate|complex",
  "recommended_pipeline": ["problem_hypothesis_express", "client_delivery"],
  "reasoning": "Justificativa da escolha em 1-2 frases"
}
"""

        # Invocar LLM para análise
        llm = build_llm()
        logger.info("━" * 80)
        logger.info("Invocando LLM para analisar contexto e selecionar subagentes...")
        logger.info("Aguardando resposta da OpenAI (isso pode levar 10-30 segundos)...")
        logger.info("━" * 80)
        response = llm.invoke(prompt)

        logger.info("✓ Resposta recebida do LLM, processando análise...")
        # Extrair conteúdo
        if hasattr(response, 'content'):
            content = response.content
        else:
            content = str(response)

        # Parse JSON
        try:
            # Tentar extrair JSON do conteúdo (pode vir com markdown)
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                analysis = json.loads(json_match.group())
            else:
                analysis = json.loads(content)

            complexity = analysis.get("complexity", "moderate")
            pipeline = analysis.get("recommended_pipeline") or analysis.get("pipeline")
            if isinstance(pipeline, str):
                pipeline = [pipeline]
            recommended_subagent = analysis.get("recommended_subagent")
            reasoning = analysis.get("reasoning", "Análise baseada no contexto fornecido")

            pipeline = self._sanitize_pipeline(pipeline, recommended_subagent)
            if not recommended_subagent and pipeline:
                recommended_subagent = pipeline[0]

            logger.info(f"Análise concluída: {reasoning}")
            logger.info(f"Complexidade: {complexity}")
            logger.info(f"Pipeline recomendado: {pipeline}")

            # Atualizar estado
            state["complexity"] = complexity
            state["selected_subagent"] = recommended_subagent or "problem_hypothesis_express"
            state["selected_subagents"] = pipeline
            state["analysis_reasoning"] = reasoning

        except (json.JSONDecodeError, AttributeError) as e:
            logger.warning(f"Erro ao parsear resposta da análise: {e}")
            logger.warning(f"Conteúdo recebido: {content}")
            # Fallback para ProblemHypothesisExpress (mais simples)
            state["complexity"] = "simple"
            default_pipeline = self._default_pipeline()
            state["selected_subagent"] = default_pipeline[0]
            state["selected_subagents"] = default_pipeline
            state["analysis_reasoning"] = "Fallback para processo mais simples devido a erro na análise"

        return state

    def _execute_subagent(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa o subagente selecionado dinamicamente.

        Args:
            state: Estado com subagente selecionado

        Returns:
            Estado atualizado com resultados do subagente
        """
        pipeline = state.get("selected_subagents")
        if not pipeline:
            pipeline = [state.get("selected_subagent", "problem_hypothesis_express")]
        state["selected_subagents"] = pipeline

        manifests = state.get("manifests", [])

        for subagent_name in pipeline:
            manifest = self._run_single_subagent(subagent_name, state)
            manifests.append(manifest)

        state["manifests"] = manifests

        return state

    def _run_single_subagent(self, subagent_name: str, state: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("━" * 80)
        logger.info(f"🚀 EXECUTANDO SUBAGENTE: {subagent_name.upper()}")
        logger.info("━" * 80)
        try:
            SubagentClass = SubagentRegistry.get(subagent_name)

            # Obter dados de subagentes anteriores para encadeamento
            manifests = state.get("manifests", [])
            previous_results = self._extract_previous_results(manifests)

            # Handler para cada subagente implementado
            if subagent_name == "problem_hypothesis_express":
                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    idea_context=self.context.context_description,
                    target_audience=None,
                    enable_tools=True,
                )
                results = subagent.execute_express_session()

            elif subagent_name == "problem_hypothesis_definition":
                initial_hypothesis = previous_results.get("hypothesis_statement")
                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    idea_context=self.context.context_description,
                    initial_hypothesis=initial_hypothesis,
                    research_notes=None,
                    enable_tools=True,
                )
                results = subagent.execute_full_definition()

            elif subagent_name == "target_user_identification":
                hypothesis_statement = previous_results.get("hypothesis_statement", self.context.context_description)
                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    hypothesis_statement=hypothesis_statement,
                    context_notes=None,
                    enable_tools=True,
                )
                results = subagent.execute_full_identification()

            elif subagent_name == "user_interview_validation":
                hypotheses = previous_results.get("hypotheses", [self.context.context_description])
                target_profiles = previous_results.get("target_profiles", [])
                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    hypotheses=hypotheses if isinstance(hypotheses, list) else [hypotheses],
                    target_profiles=target_profiles if isinstance(target_profiles, list) else [],
                    owner=self.context.context_name,
                    timeframe="2 semanas",
                    context_notes=None,
                    enable_tools=True,
                )
                results = subagent.execute_full_validation()

            elif subagent_name == "landing_page_creation":
                from datetime import datetime, timedelta
                hypothesis_statement = previous_results.get("hypothesis_statement", self.context.context_description)
                # Calcular deadline padrão: 7 dias a partir de hoje
                default_deadline = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    product_name=self.context.context_name,
                    offer_summary=self.context.context_description,
                    primary_audience=previous_results.get("primary_audience", "PMEs"),
                    hypothesis_statement=hypothesis_statement,
                    owner=self.context.context_name,
                    publish_deadline=default_deadline,
                    proof_points=None,
                    enable_tools=True,
                )
                results = subagent.execute_full_creation()

            elif subagent_name == "checkout_setup":
                # URLs padrão para checkout
                base_url = f"https://example.com/{self.context.context_name.lower().replace(' ', '-')}"
                landing_url = f"{base_url}/landing"
                thankyou_url = f"{base_url}/obrigado"
                support_email = f"contato@{self.context.context_name.lower().replace(' ', '')}.com"

                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    product_name=self.context.context_name,
                    offer_description=self.context.context_description,
                    price="R$ 99,00",
                    owner=self.context.context_name,
                    preferred_gateway="Stripe",
                    landing_url=landing_url,
                    thankyou_url=thankyou_url,
                    support_email=support_email,
                    enable_tools=True,
                )
                results = subagent.execute_full_setup()

            elif subagent_name == "client_delivery":
                subagent = SubagentClass(
                    workspace_root=self.context.workspace_root,
                    client_name=self.context.context_name,
                    delivery_scope=self.context.context_description,
                    deadline=None,
                    enable_tools=True,
                )
                results = subagent.execute_full_delivery()

            else:
                raise ValueError(f"Subagente {subagent_name} não tem handler configurado")

            manifest = {
                "process": subagent_name,
                "status": "completed",
                "started_at": results.get("started_at", ""),
                "completed_at": results.get("completed_at", ""),
                "stages": results.get("stages", {}),
                "artifacts": results.get("artifacts", []),
                "notes": f"Subagente selecionado automaticamente. {state.get('analysis_reasoning', '')}",
            }

            logger.info("━" * 80)
            logger.info(f"✅ SUBAGENTE {subagent_name.upper()} CONCLUÍDO COM SUCESSO")
            logger.info(f"   Artefatos criados: {len(results.get('artifacts', []))}")
            logger.info("━" * 80)
            return manifest

        except Exception as exc:
            logger.error(f"Erro ao executar subagente {subagent_name}: {exc}")
            return {
                "process": subagent_name,
                "status": "failed",
                "error": str(exc),
                "notes": f"Falha na execução do subagente: {exc}",
            }

    def _extract_previous_results(self, manifests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extrai resultados de subagentes anteriores para encadeamento.

        Args:
            manifests: Lista de manifestos de execuções anteriores

        Returns:
            Dicionário com dados agregados dos processos anteriores
        """
        results = {}

        for manifest in manifests:
            process = manifest.get("process", "")
            stages = manifest.get("stages", {})

            # Extrair dados relevantes baseado no tipo de processo
            if "hypothesis" in process.lower():
                # Processos de hipótese
                for stage_data in stages.values():
                    if isinstance(stage_data, dict):
                        if "hypothesis_statement" in stage_data:
                            results["hypothesis_statement"] = stage_data["hypothesis_statement"]
                        if "hypotheses" in stage_data:
                            results["hypotheses"] = stage_data["hypotheses"]

            elif "target" in process.lower() or "user" in process.lower():
                # Processos de identificação de usuários
                for stage_data in stages.values():
                    if isinstance(stage_data, dict):
                        if "profiles" in stage_data:
                            results["target_profiles"] = stage_data["profiles"]
                        if "primary_audience" in stage_data:
                            results["primary_audience"] = stage_data["primary_audience"]

        return results

    def _default_pipeline(self) -> List[str]:
        """Retorna ordem padrão de execução baseada no registry (apenas implementados)."""
        # Todos os subagentes que têm handlers implementados no método _run_single_subagent
        IMPLEMENTED_SUBAGENTS = {
            "problem_hypothesis_express",
            "problem_hypothesis_definition",
            "target_user_identification",
            "user_interview_validation",
            "landing_page_creation",
            "checkout_setup",
            "client_delivery",
        }

        available = SubagentRegistry.list_available()
        implemented = [name for name in available if name in IMPLEMENTED_SUBAGENTS]

        return implemented if implemented else ["problem_hypothesis_express"]

    def _sanitize_pipeline(
        self,
        pipeline: Optional[List[str]],
        recommended_subagent: Optional[str] = None,
    ) -> List[str]:
        """Normaliza pipeline garantindo somente subagentes válidos E IMPLEMENTADOS."""
        # Todos os subagentes que têm handlers implementados no método _run_single_subagent
        IMPLEMENTED_SUBAGENTS = {
            "problem_hypothesis_express",
            "problem_hypothesis_definition",
            "target_user_identification",
            "user_interview_validation",
            "landing_page_creation",
            "checkout_setup",
            "client_delivery",
        }

        if not pipeline:
            pipeline = [recommended_subagent] if recommended_subagent else None
        if not pipeline:
            return self._default_pipeline()

        valid = []
        skipped = []
        registered = set(SubagentRegistry.list_available())
        for name in pipeline:
            # Verificar se está registrado E implementado
            if name in registered and name in IMPLEMENTED_SUBAGENTS and name not in valid:
                valid.append(name)
            elif name in registered and name not in IMPLEMENTED_SUBAGENTS:
                skipped.append(name)

        # Log de subagentes não implementados
        if skipped:
            logger.warning(
                f"Subagentes registrados mas NÃO IMPLEMENTADOS foram ignorados: {skipped}. "
                f"Apenas estes estão implementados: {list(IMPLEMENTED_SUBAGENTS)}"
            )

        if not valid:
            logger.info("Nenhum subagente válido no pipeline, usando pipeline padrão")
            return self._default_pipeline()
        return valid


    def _validate_result(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Valida resultados, gera consolidado e empacota artefatos.

        Args:
            state: Estado com manifests

        Returns:
            Estado final com consolidated e archive
        """
        manifests: List[Dict[str, Any]] = list(state.get("manifests", []))

        # Escrever relatório consolidado
        consolidated = self._write_consolidated(manifests)

        # Empacotar artefatos
        archive = self._package_artifacts()

        logger.info("Consolidado salvo em %s", consolidated)
        logger.info("Pacote final gerado em %s", archive)

        return {
            "manifests": manifests,
            "consolidated": str(consolidated),
            "archive": str(archive),
        }

    def _write_consolidated(self, manifests: List[Dict[str, Any]]) -> Path:
        """
        Escreve relatório consolidado.

        Args:
            manifests: Lista de manifestos dos subagentes

        Returns:
            Caminho do arquivo consolidado
        """
        lines = [
            f"# Consolidado: {self.strategy_name}",
            f"## Contexto: {self.context.context_name}",
            "",
            self.context.context_description or "Sem descrição adicional.",
            "",
        ]

        if not manifests:
            lines.append("Nenhum processo executado nesta rodada.")
        else:
            for manifest in manifests:
                process = manifest.get("process", "desconhecido")
                status = manifest.get("status", "desconhecido")
                lines.extend([
                    f"## Processo {process}",
                    f"- Status: {status}",
                ])

                metrics = manifest.get("metrics") or {}
                if metrics:
                    duration = metrics.get("total_duration_seconds")
                    tokens = metrics.get("total_tokens")
                    cost = metrics.get("total_cost")
                    metric_lines: List[str] = []
                    if duration is not None:
                        metric_lines.append(f"{duration:.2f}s")
                    if tokens is not None:
                        metric_lines.append(f"{tokens} tokens")
                    if cost is not None:
                        metric_lines.append(f"USD {cost}")
                    if metric_lines:
                        lines.append(f"- Métricas: {', '.join(metric_lines)}")

                todos = manifest.get("todos_summary") or {}
                if todos:
                    total = todos.get("total")
                    completed = todos.get("completed")
                    pending = todos.get("pending")
                    progress = todos.get("progress_percentage")
                    summary = []
                    if completed is not None and total is not None:
                        summary.append(f"{completed}/{total} completos")
                    if pending is not None:
                        summary.append(f"{pending} pendentes")
                    if progress is not None:
                        summary.append(f"{progress:.0f}% do plano")
                    if summary:
                        lines.append(f"- TODOs: {', '.join(summary)}")

                notes = manifest.get("notes", "")
                if notes:
                    lines.append(f"- Notas: {notes}")

                artifacts = manifest.get("artifacts", [])
                if artifacts:
                    lines.append("")
                    lines.append("### Artefatos")
                    for artifact in artifacts:
                        artifact_path = Path(artifact)
                        artifact_name = artifact_path.name
                        lines.append(f"- {artifact_name}")
                        if artifact_path.exists():
                            try:
                                content = artifact_path.read_text(encoding="utf-8").strip()
                            except OSError:
                                content = ""
                            if content:
                                lines.append("")
                                lines.append(content)
                                lines.append("")
                        else:
                            lines.append(f"  (arquivo não encontrado em {artifact_path})")
                lines.append("")

        content = "\n".join(lines)

        # Usar workspace manager para escrever
        consolidated_path = self.context.workspace_root / "00-consolidado.MD"
        # Garantir que o diretório pai existe
        consolidated_path.parent.mkdir(parents=True, exist_ok=True)
        consolidated_path.write_text(content, encoding="utf-8")

        return consolidated_path

    def _package_artifacts(self) -> Path:
        """
        Empacota todos os artefatos do workspace.

        Returns:
            Caminho do arquivo ZIP
        """
        output_stem = f"{self.context.context_name}_{self.strategy_name}_outputs"
        target_path = self.context.workspace_root / output_stem

        archive_path = self.package_service.create_archive(
            source_dir=self.context.workspace_root,
            output_path=target_path,
        )

        return archive_path

