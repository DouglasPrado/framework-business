"""
Subagente: Landing Page Creation (04-LandingPageCreation)

Baseado em: process/ZeroUm/04-LandingPageCreation/process.MD

Propósito:
Transformar hipóteses validadas em uma landing page publicada e pronta
para tráfego em até 8 horas, cobrindo briefing, estrutura, copy,
plano de implementação, configuração de analytics e checklist de QA.

Etapas:
1. Consolidar insumos e briefing
2. Definir estrutura da página
3. Produzir copy e selecionar prova social
4. Planejar construção e implementação
5. Configurar formulário, integrações e analytics
6. Executar QA final e publicar
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from framework.llm.factory import build_llm
from framework.tools import AgentType, get_tools
from business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

logger = logging.getLogger(__name__)


class LandingPageCreationAgent:
    """
    Subagente especializado em criar landing pages alinhadas à metodologia ZeroUm.

    Gera todos os artefatos necessários para briefing, estrutura, copy,
    plano técnico, analytics e QA, além de preencher os templates oficiais.
    """

    def __init__(
        self,
        workspace_root: Path,
        product_name: str,
        offer_summary: str,
        primary_audience: str,
        hypothesis_statement: str,
        owner: str,
        publish_deadline: str,
        proof_points: Optional[List[str]] = None,
        enable_tools: bool = True,
    ) -> None:
        """
        Args:
            workspace_root: Diretório raiz do contexto (drive/<Contexto>)
            product_name: Nome do produto/oferta
            offer_summary: Descrição curta do que será ofertado na landing
            primary_audience: Perfil prioritário a ser atingido
            hypothesis_statement: Declaração de hipótese atual
            owner: Responsável pela landing
            publish_deadline: Data planejada de publicação (YYYY-MM-DD)
            proof_points: Lista de provas sociais disponíveis
            enable_tools: Habilita tools do framework (padrão True)
        """
        self.workspace_root = workspace_root
        self.product_name = product_name.strip()
        self.offer_summary = offer_summary.strip()
        self.primary_audience = primary_audience.strip()
        self.hypothesis_statement = hypothesis_statement.strip()
        self.owner = owner.strip() or "Owner não definido"
        self.publish_deadline = publish_deadline
        self.proof_points = proof_points or []
        self.llm = build_llm()

        self.tools = get_tools(AgentType.PROCESS) if enable_tools else []
        if self.tools:
            logger.info("Tools habilitadas: %s", [tool.name for tool in self.tools])

        self.process_dir = workspace_root / "04-LandingPageCreation"
        self.data_dir = self.process_dir / "_DATA"
        self._setup_directories()
        self.template_filler = ProcessTemplateFiller(
            process_code="04-LandingPageCreation",
            output_dir=self.data_dir,
            llm=self.llm,
        )

        self.section_outline: Dict[str, Any] = {}
        self.copy_blocks: Dict[str, Any] = {}

    def _setup_directories(self) -> None:
        """Cria estrutura de diretórios necessária."""
        dirs = [
            self.process_dir,
            self.data_dir,
            self.data_dir / "assets",
            self.data_dir / "evidencias",
        ]
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)

    def execute_full_creation(self) -> Dict[str, Any]:
        """
        Executa todas as etapas da criação da landing page.
        """
        logger.info("Iniciando LandingPageCreation para %s", self.product_name)
        results: Dict[str, Any] = {
            "product_name": self.product_name,
            "offer_summary": self.offer_summary,
            "primary_audience": self.primary_audience,
            "hypothesis_statement": self.hypothesis_statement,
            "owner": self.owner,
            "publish_deadline": self.publish_deadline,
            "proof_points": self.proof_points,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        stage_briefing = self._stage_1_briefing()
        results["stages"]["briefing"] = stage_briefing

        stage_structure = self._stage_2_structure()
        results["stages"]["structure"] = stage_structure

        stage_copy = self._stage_3_copy()
        results["stages"]["copy"] = stage_copy

        stage_build_plan = self._stage_4_build_plan()
        results["stages"]["build_plan"] = stage_build_plan

        stage_analytics = self._stage_5_analytics()
        results["stages"]["analytics"] = stage_analytics

        stage_qa = self._stage_6_qa_publish()
        results["stages"]["qa"] = stage_qa

        results["completed_at"] = datetime.now().isoformat()
        consolidated = self._create_consolidated_report(results)
        results["consolidated_file"] = str(consolidated)

        self._fill_data_templates(results)

        logger.info("LandingPageCreation concluído para %s", self.product_name)
        return results

    # ------------------------------------------------------------------
    # Stage implementations
    # ------------------------------------------------------------------
    def _stage_1_briefing(self) -> Dict[str, Any]:
        """Etapa 1: Consolidar insumos e briefing."""
        prompt = f"""
Você é um especialista em landing pages ZeroUm. Estruture um briefing completo usando os campos oficiais.

Produto: {self.product_name}
Oferta: {self.offer_summary}
Público prioritário: {self.primary_audience}
Hipótese: {self.hypothesis_statement}
Owner: {self.owner}
Data alvo: {self.publish_deadline}
Provas sociais: {self._format_list(self.proof_points)}

Inclua objetivos, dores, benefícios, oferta, ferramentas, métricas e pendências.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("01-briefing-landing.MD", content)
        return {
            "file_path": str(path),
            "summary": "Briefing completo documentado",
        }

    def _stage_2_structure(self) -> Dict[str, Any]:
        """Etapa 2: Definir estrutura da página."""
        prompt = f"""
Com base no briefing da landing de {self.product_name}, defina a estrutura completa de seções.

Incluir: Hero, Problema, Solução, Prova social, Oferta, FAQ, CTA final, seções extras e assets.
Use texto corrido seguindo o template oficial, sem tabelas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("02-estrutura-secoes.MD", content)

        self.section_outline = {
            "document": content,
            "generated_at": datetime.now().isoformat(),
        }

        return {
            "file_path": str(path),
            "summary": "Estrutura de seções aprovada",
        }

    def _stage_3_copy(self) -> Dict[str, Any]:
        """Etapa 3: Produzir copy e provas sociais."""
        prompt = f"""
Você tem a estrutura da landing e precisa criar o copy completo. Utilize o template Copy Draft.

Produto: {self.product_name}
Oferta: {self.offer_summary}
Público: {self.primary_audience}
Provas sociais: {self._format_list(self.proof_points)}
Hipótese: {self.hypothesis_statement}

Entregue todas as seções (Hero, Problema, Solução, Prova, Oferta, FAQ, CTA final) em português e sem tabelas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("03-copy-draft.MD", content)

        self.copy_blocks = {
            "document": content,
            "generated_at": datetime.now().isoformat(),
        }

        return {
            "file_path": str(path),
            "summary": "Copy completo pronto para implementação",
        }

    def _stage_4_build_plan(self) -> Dict[str, Any]:
        """Etapa 4: Planejar construção na ferramenta escolhida."""
        prompt = f"""
Crie um plano operacional para construção da landing, considerando:
- Plataforma e acessos
- Passo a passo de implementação por seção
- Recursos necessários (assets, checklist de conteúdo)
- Responsáveis e prazos por etapa
- Riscos e mitigação
- Critérios de aceite antes da publicação

Formato textual com listas e subtítulos.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("04-plano-construcao.MD", content)
        return {
            "file_path": str(path),
            "summary": "Plano de implementação e responsabilidades",
        }

    def _stage_5_analytics(self) -> Dict[str, Any]:
        """Etapa 5: Configurar analytics, formulários e integrações."""
        prompt = f"""
Produza um plano completo de analytics e integrações usando o template oficial.

Inclua:
- Ferramentas (GA4, Meta Pixel, etc.)
- Eventos e conversões por plataforma
- Padrão de UTMs e campanhas planejadas
- Cronograma de monitoramento das primeiras 72h
- Planos de contingência

Use texto em português, sem tabelas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("05-plano-analytics.MD", content)
        return {
            "file_path": str(path),
            "summary": "Plano de analytics e integrações definido",
        }

    def _stage_6_qa_publish(self) -> Dict[str, Any]:
        """Etapa 6: QA final e publicação."""
        prompt = f"""
Monte um checklist de QA preenchido com foco em:
- Conteúdo
- Funcionalidades
- Responsividade
- Performance
- Analytics
- Acessibilidade
- Publicação/comunicação

Inclua resultados simulados (ex: PageSpeed), status (ok/pending) e pendências destacadas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("06-qa-publicacao.MD", content)
        return {
            "file_path": str(path),
            "summary": "QA registrado e publicado virtualmente",
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _create_consolidated_report(self, results: Dict[str, Any]) -> Path:
        """Gera resumo executivo consolidado da landing."""
        data = {
            "product": self.product_name,
            "audience": self.primary_audience,
            "owner": self.owner,
            "deadline": self.publish_deadline,
            "proof_points": self.proof_points,
            "sections": self.section_outline,
            "copy": self.copy_blocks,
        }
        prompt = f"""
Gere um consolidado executivo da criação da landing contendo:
- Resumo executivo
- Estrutura aprovada
- Destaques de copy e provas sociais
- Checklist de implementação e status
- Plano de analytics e QA
- Próximos passos pós-lançamento

Dados:
{json.dumps(data, ensure_ascii=False, indent=2)}
"""
        content = self._invoke_llm(prompt)
        return self._save_document("00-consolidado-landing.MD", content)

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        """Preenche templates oficiais usando os dados da execução."""
        context = self._build_template_context(results)
        tasks = [
            TemplateTask(
                template="briefing-landing.MD",
                instructions="Preencha todos os campos do briefing com os dados desta execução.",
                output_name="briefing-landing-preenchido.MD",
            ),
            TemplateTask(
                template="estrutura-secoes.MD",
                instructions="Reproduza a estrutura aprovada com headlines, copy e assets necessários.",
                output_name="estrutura-secoes-preenchida.MD",
            ),
            TemplateTask(
                template="copy-draft.MD",
                instructions="Preencha com a copy final aprovada, mantendo linguagem do cliente.",
                output_name="copy-draft-preenchido.MD",
            ),
            TemplateTask(
                template="plano-analytics.MD",
                instructions="Registre IDs, eventos e UTMs definidos nesta execução.",
                output_name="plano-analytics-preenchido.MD",
            ),
            TemplateTask(
                template="checklist-qa.MD",
                instructions="Marque cada item com status e inclua evidências/responsáveis.",
                output_name="checklist-qa-preenchido.MD",
            ),
        ]
        self.template_filler.fill_templates(tasks, context)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        """Monta contexto textual para auxiliar no preenchimento dos templates."""
        sections = [
            f"Produto: {self.product_name}",
            f"Oferta: {self.offer_summary}",
            f"Público: {self.primary_audience}",
            f"Hipótese: {self.hypothesis_statement}",
            f"Owner: {self.owner}",
            f"Data alvo: {self.publish_deadline}",
            "Provas sociais:",
            self._format_list(self.proof_points),
        ]
        for stage in results["stages"].values():
            path_str = stage.get("file_path")
            if not path_str:
                continue
            path = Path(path_str)
            if path.exists():
                try:
                    sections.append(f"\n=== {path.name} ===\n{path.read_text(encoding='utf-8')}")
                except OSError:
                    continue
        return "\n".join(sections)

    def _save_document(self, filename: str, content: str) -> Path:
        """Salva arquivo textual no diretório do processo."""
        path = self.process_dir / filename
        path.write_text(content.strip() + "\n", encoding="utf-8")
        logger.info("Documento salvo: %s", path)
        return path

    def _invoke_llm(self, prompt: str) -> str:
        """Invoca LLM e padroniza o retorno."""
        response = self.llm.invoke(prompt)
        content = getattr(response, "content", response)
        if isinstance(content, list):
            parts: List[str] = []
            for chunk in content:
                if isinstance(chunk, dict) and "text" in chunk:
                    parts.append(chunk["text"])
                else:
                    parts.append(str(chunk))
            normalized = "\n".join(parts)
        else:
            normalized = str(content)
        return normalized.strip()

    @staticmethod
    def _format_list(items: List[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- Não informado"


__all__ = ["LandingPageCreationAgent"]
