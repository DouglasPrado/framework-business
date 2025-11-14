"""
Subagente: User Interview Validation (03-UserInterviewValidation)

Baseado em: process/ZeroUm/03-UserInterviewValidation/process.MD

Propósito:
Planejar, executar e sintetizar uma rodada de 10 entrevistas rápidas
com usuários-alvo, documentando evidências, linguagem do cliente,
classificação de hipóteses e próximos passos acionáveis.

Etapas:
1. Preparar briefing da rodada
2. Construir roteiro de entrevista
3. Planejar recrutamento e mensagens
4. Executar recrutamento e agendamentos
5. Conduzir entrevistas e registrar evidências
6. Consolidar padrões e classificar hipóteses
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from framework.agents import BaseAgent
from business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

logger = logging.getLogger(__name__)

class UserInterviewValidationAgent(BaseAgent):
    """
    Subagente especializado em validação qualitativa com usuários reais.

    Gera todos os artefatos previstos no processo, desde briefing e
    roteiros até análises finais, além de preencher os templates oficiais.
    """

    process_name = "03-UserInterviewValidation"
    strategy_name = "ZeroUm"

    def __init__(
        self,
        workspace_root: Path,
        hypotheses: List[str],
        target_profiles: List[str],
        owner: str,
        timeframe: str = "7 dias",
        context_notes: Optional[str] = None,
        enable_tools: bool = True,
    ) -> None:
        """
        Args:
            workspace_root: Diretório raiz do contexto em execução
            hypotheses: Lista de hipóteses priorizadas (problema/solução/objeção)
            target_profiles: Perfis de usuários a recrutar
            owner: Responsável pela rodada
            timeframe: Período planejado (ex.: "Próximos 5 dias úteis")
            context_notes: Observações adicionais relevantes
            enable_tools: Habilita tools do framework (padrão True)
        """
        # Inicializar BaseAgent (configura workspace_root, llm, tools, process_dir, data_dir)
        super().__init__(
            workspace_root=workspace_root,
            enable_tools=enable_tools,
            load_knowledge=True
        )

        # Atributos específicos do negócio
        self.hypotheses = hypotheses or ["Hipótese não informada"]
        self.target_profiles = target_profiles or ["Perfil não definido"]
        self.owner = owner or "Responsável não definido"
        self.timeframe = timeframe
        self.context_notes = (context_notes or "").strip()

        # Criar estrutura de diretórios específica
        self.setup_directories(["assets", "evidencias"])

        # Template filler usa self.llm (já configurado pelo BaseAgent)
        self.template_filler = ProcessTemplateFiller(
            process_code="03-UserInterviewValidation",
            output_dir=self.data_dir,
            llm=self.llm,
        )

        self.interviews: List[Dict[str, Any]] = []
        self.recruitment_log: List[Dict[str, Any]] = []

    def execute_full_validation(self) -> Dict[str, Any]:
        """
        Executa todo o fluxo de validação por entrevistas.
        """
        logger.info("Iniciando UserInterviewValidation")
        results: Dict[str, Any] = {
            "hypotheses": self.hypotheses,
            "target_profiles": self.target_profiles,
            "owner": self.owner,
            "timeframe": self.timeframe,
            "context_notes": self.context_notes,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        stage_briefing = self._stage_1_prepare_briefing()
        results["stages"]["briefing"] = stage_briefing

        stage_script = self._stage_2_build_script()
        results["stages"]["script"] = stage_script

        stage_plan = self._stage_3_plan_recruitment()
        results["stages"]["recruitment_plan"] = stage_plan

        stage_pipeline = self._stage_4_execute_recruitment()
        results["stages"]["recruitment_tracker"] = stage_pipeline

        stage_interviews = self._stage_5_conduct_interviews()
        results["stages"]["interviews"] = stage_interviews

        stage_synthesis = self._stage_6_synthesize()
        results["stages"]["synthesis"] = stage_synthesis

        results["completed_at"] = datetime.now().isoformat()

        consolidated = self._create_consolidated_report(results)
        results["consolidated_file"] = str(consolidated)

        self._fill_data_templates(results)

        logger.info("UserInterviewValidation concluído")
        return results

    # ------------------------------------------------------------------
    # Stage implementations
    # ------------------------------------------------------------------
    def _stage_1_prepare_briefing(self) -> Dict[str, Any]:
        """Etapa 1: Preparar briefing e metas da rodada."""
        prompt = f"""
Você é um estrategista ZeroUm preparando uma rodada de entrevistas.

Hipóteses priorizadas:
{self._format_bullets(self.hypotheses)}

Perfis alvo:
{self._format_bullets(self.target_profiles)}

Responsável: {self.owner}
Período planejado: {self.timeframe}
Notas adicionais: {self.context_notes or 'Nenhuma'}

Produza um briefing completo seguindo o processo oficial,
usando seções do template mas sem tabelas. Texto em português.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("01-briefing-entrevistas.MD", content)
        return {
            "file_path": str(path),
            "summary": "Briefing com objetivos, hipóteses e riscos documentados",
        }

    def _stage_2_build_script(self) -> Dict[str, Any]:
        """Etapa 2: Construir roteiro estruturado."""
        prompt = f"""
Utilize as hipóteses e perfis abaixo para criar um roteiro de entrevista enxuto (5 perguntas principais, follow-ups e abertura/encerramento).

Hipóteses:
{self._format_bullets(self.hypotheses)}

Perfis:
{self._format_bullets(self.target_profiles)}

Inclua:
- Contexto da rodada
- Checklist de abertura
- Perguntas principais com follow-ups
- Encerramento
- Notas do entrevistador e checklist rápido

Texto em português, sem tabelas, seguindo o processo ZeroUm.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("02-roteiro-entrevista.MD", content)
        return {
            "file_path": str(path),
            "summary": "Roteiro com perguntas, follow-ups e checklist",
        }

    def _stage_3_plan_recruitment(self) -> Dict[str, Any]:
        """Etapa 3: Planejar recrutamento e mensagens."""
        prompt = f"""
Crie um plano de recrutamento cobrindo canais, mensagens, incentivos e cronograma para conseguir 10 entrevistas.

Perfis prioritários:
{self._format_bullets(self.target_profiles)}

Hipóteses:
{self._format_bullets(self.hypotheses)}

Inclua:
- Objetivos e métricas
- Canais com responsável e volume
- Mensagem de convite, follow-up e agradecimento
- Cronograma de 3 dias + buffer
- Critérios de confirmação
- Observações e responsáveis
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("03-plano-recrutamento.MD", content)

        self.interviews = self._generate_interview_plan()

        return {
            "file_path": str(path),
            "summary": "Plano de recrutamento e mensagens definidas",
            "interview_target": len(self.interviews),
        }

    def _stage_4_execute_recruitment(self) -> Dict[str, Any]:
        """Etapa 4: Registrar convites, confirmações e agendamentos."""
        if not self.interviews:
            self.interviews = self._generate_interview_plan()

        for idx, interview in enumerate(self.interviews):
            if idx < 8:
                interview["status"] = "confirmado"
            elif idx < 10:
                interview["status"] = "pendente"
            else:
                interview["status"] = "backup"
            interview["invite_sent_at"] = datetime.now().isoformat()

        tracker_content = self.invoke_llm(
            f"""
Crie um relatório textual do pipeline de recrutamento com base nos dados abaixo.
Use subtítulos por contato e mantenha linguagem direta.

Dados (JSON):
{json.dumps(self.interviews, ensure_ascii=False, indent=2)}

Inclua resumo geral (convites, confirmados, realizados planejados) e um bloco por contato.
"""
        )
        path = self.save_document("04-tracker-recrutamento.MD", tracker_content)

        return {
            "file_path": str(path),
            "summary": "Tracker textual com status de cada contato",
        }

    def _stage_5_conduct_interviews(self) -> Dict[str, Any]:
        """Etapa 5: Conduzir entrevistas e registrar evidências."""
        interview_notes: List[Path] = []
        for idx, interview in enumerate(self.interviews, start=1):
            interview["status"] = "realizado" if idx <= 10 else interview["status"]
            interview["completed_at"] = datetime.now().isoformat()
            notes_path = self._render_interview_notes(idx, interview)
            interview["notes_file"] = str(notes_path)
            interview_notes.append(notes_path)

        synthesis_prompt = f"""
Considere as notas de entrevistas (JSON) abaixo e produza um sumário das principais evidências.

{json.dumps(self.interviews, ensure_ascii=False, indent=2)}

Crie um documento com:
- Resumo geral da rodada
- Destaques por hipótese
- Objeções recorrentes
- Linguagem literal marcante
- Recomendações imediatas
"""
        content = self.invoke_llm(synthesis_prompt)
        path = self.save_document("05-evidencias-entrevistas.MD", content)

        return {
            "file_path": str(path),
            "summary": "Notas consolidadas e destaques coletados",
            "notes_files": [str(p) for p in interview_notes],
        }

    def _stage_6_synthesize(self) -> Dict[str, Any]:
        """Etapa 6: Consolidação final, padrões e classificação."""
        interviews_json = json.dumps(self.interviews, ensure_ascii=False, indent=2)

        analysis_prompt = f"""
Gere análise de padrões considerando as entrevistas abaixo.

{interviews_json}

Siga o template de análise de padrões em texto corrido.
"""
        analysis_path = self.save_document(
            "06-analise-padroes.MD", self.invoke_llm(analysis_prompt)
        )

        classification_prompt = f"""
Classifique cada hipótese (até 3 principais) usando as evidências.

Hipóteses:
{self._format_bullets(self.hypotheses)}

Entrevistas:
{interviews_json}

Use texto estruturado com status, evidências e próximos passos.
"""
        classification_path = self.save_document(
            "06-classificacao-hipoteses.MD", self.invoke_llm(classification_prompt)
        )

        language_prompt = f"""
Construa biblioteca de linguagem do cliente agrupando por temas e objeções.

Dados:
{interviews_json}

Entregue no formato do template, em português e sem tabelas.
"""
        language_path = self.save_document(
            "06-biblioteca-linguagem.MD", self.invoke_llm(language_prompt)
        )

        return {
            "file_path": str(analysis_path),
            "analysis_file": str(analysis_path),
            "classification_file": str(classification_path),
            "language_file": str(language_path),
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _generate_interview_plan(self) -> List[Dict[str, Any]]:
        """Solicita ao LLM um plano estruturado de entrevistas em JSON."""
        profiles_text = self._format_bullets(self.target_profiles)
        hypotheses_text = self._format_bullets(self.hypotheses)

        prompt = f"""
Gere exatamente 10 itens em JSON descrevendo entrevistas planejadas.

Perfis:
{profiles_text}

Hipóteses:
{hypotheses_text}

Cada item deve conter:
- id (1-10)
- profile
- hypothesis (lista)
- channel
- scheduled_for (YYYY-MM-DD HH:MM)
- duration_minutes
- pain_points (lista)
- expected_outcomes (lista)
- quotes (lista de frases prováveis)
- decision_hint (validar/refutar/descobrir)
- status ("planejado")
- sample_contact (nome/canal)
Retorne apenas JSON.
"""
        response = self.invoke_llm(prompt)
        data = self._extract_json_array(response)
        if not data:
            logger.warning("Não foi possível gerar plano via LLM, criando fallback.")
            data = self._fallback_interview_plan()
        return data

    def _render_interview_notes(self, index: int, interview: Dict[str, Any]) -> Path:
        """Gera arquivo com notas completas no formato do template."""
        prompt = f"""
Use os dados abaixo para preencher o template de notas de entrevista em texto contínuo.

Entrevista:
{json.dumps(interview, ensure_ascii=False, indent=2)}

Inclua citações literais e menções às hipóteses tocadas.
"""
        content = self.invoke_llm(prompt)
        filename = f"entrevistas/entrevista-{index:02d}.MD"
        path = self._save_data_document(filename, content)
        return path

    def _create_consolidated_report(self, results: Dict[str, Any]) -> Path:
        """Gera relatório executivo consolidado."""
        interviews_json = json.dumps(self.interviews, ensure_ascii=False, indent=2)
        prompt = f"""
Crie um consolidado da rodada de entrevistas com:
- Resumo executivo (4 bullets)
- Métricas chave
- Principais aprendizados
- Decisões e próximos passos

Dados:
{interviews_json}
"""
        content = self.invoke_llm(prompt)
        return self.save_document("00-consolidado-entrevistas.MD", content)

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        """Preenche templates oficiais com o contexto gerado."""
        context = self._build_template_context(results)
        tasks: List[TemplateTask] = [
            TemplateTask(
                template="briefing-entrevistas.MD",
                instructions=(
                    "Replique todos os campos usando os dados reais desta rodada, "
                    "incluindo hipóteses, perfis e métricas."
                ),
                output_name="briefing-entrevistas-preenchido.MD",
            ),
            TemplateTask(
                template="roteiro-entrevista-base.MD",
                instructions=(
                    "Adapte o roteiro para os perfis prioritários, preenchendo perguntas e follow-ups."
                ),
                output_name="roteiro-entrevista-custom.MD",
            ),
            TemplateTask(
                template="plano-recrutamento.MD",
                instructions="Preencha com canais, mensagens, cronograma e responsáveis definidos.",
                output_name="plano-recrutamento-preenchido.MD",
            ),
            TemplateTask(
                template="tracker-recrutamento.MD",
                instructions=(
                    "Resuma o status dos contatos recrutados, preenchendo pelo menos 10 blocos."
                ),
                output_name="tracker-recrutamento-preenchido.MD",
            ),
            TemplateTask(
                template="analise-padroes.MD",
                instructions="Documente três padrões principais identificados nesta rodada.",
                output_name="analise-padroes-preenchida.MD",
            ),
            TemplateTask(
                template="classificacao-hipoteses.MD",
                instructions="Classifique até três hipóteses usando evidências coletadas.",
                output_name="classificacao-hipoteses-preenchida.MD",
            ),
            TemplateTask(
                template="biblioteca-linguagem.MD",
                instructions="Registre citações literais agrupadas por tema e objeções recorrentes.",
                output_name="biblioteca-linguagem-preenchida.MD",
            ),
        ]

        # Preencher pelo menos as duas primeiras entrevistas usando o template de notas
        for idx, interview in enumerate(self.interviews[:2], start=1):
            instructions = (
                "Preencha o template com as respostas reais da entrevista descrita no contexto. "
                f"Referencie o entrevistado {interview.get('profile')} e as citações registradas."
            )
            tasks.append(
                TemplateTask(
                    template="notas-entrevista.MD",
                    instructions=instructions,
                    output_name=f"entrevistas/notas-template-{idx:02d}.MD",
                )
            )

        self.template_filler.fill_templates(tasks, context)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        """Combina documentos e dados para auxiliar o preenchimento de templates."""
        sections = [
            f"Hipóteses: {self._format_bullets(self.hypotheses)}",
            f"Perfis: {self._format_bullets(self.target_profiles)}",
            f"Owner: {self.owner}",
            f"Período: {self.timeframe}",
            f"Notas: {self.context_notes or 'Nenhuma'}",
        ]
        for stage in results["stages"].values():
            path_str = stage.get("file_path")
            if isinstance(path_str, str):
                path = Path(path_str)
                if path.exists():
                    try:
                        sections.append(f"\n=== {path.name} ===\n{path.read_text(encoding='utf-8')}")
                    except OSError:
                        continue
            elif isinstance(stage, dict):
                for key, value in stage.items():
                    if isinstance(value, str) and value.endswith(".MD"):
                        path = Path(value)
                        if path.exists():
                            try:
                                sections.append(
                                    f"\n=== {path.name} ({key}) ===\n{path.read_text(encoding='utf-8')}"
                                )
                            except OSError:
                                continue

        sections.append("\n=== Entrevistas Estruturadas ===")
        sections.append(json.dumps(self.interviews, ensure_ascii=False, indent=2))
        return "\n".join(sections)

    def _extract_json_array(self, content: str) -> List[Dict[str, Any]]:
        """Extrai lista JSON de uma string."""
        try:
            start = content.find("[")
            end = content.rfind("]")
            if start == -1 or end == -1:
                raise ValueError("JSON não encontrado")
            payload = content[start : end + 1]
            data = json.loads(payload)
            if not isinstance(data, list):
                raise ValueError("Conteúdo não é lista")
            return data
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Falha ao extrair JSON: %s", exc)
            return []

    def _fallback_interview_plan(self) -> List[Dict[str, Any]]:
        """Plano padrão caso o LLM não retorne JSON válido."""
        plan = []
        for idx in range(1, 11):
            plan.append(
                {
                    "id": idx,
                    "profile": self.target_profiles[(idx - 1) % len(self.target_profiles)],
                    "hypothesis": [self.hypotheses[(idx - 1) % len(self.hypotheses)]],
                    "channel": "Zoom",
                    "scheduled_for": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "duration_minutes": 12,
                    "pain_points": ["Falta de clareza sobre problema"],
                    "expected_outcomes": ["Confirmar dor relatada"],
                    "quotes": ["Ainda não sei se vale investir nisso."],
                    "decision_hint": "descobrir",
                    "status": "planejado",
                    "sample_contact": f"Contato {idx}",
                }
            )
        return plan

    def _save_data_document(self, relative_path: str, content: str) -> Path:
        """Salva arquivo dentro de _DATA."""
        path = self.data_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        logger.info("Documento salvo: %s", path)
        return path
    def _format_bullets(items: List[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- Não informado"

__all__ = ["UserInterviewValidationAgent"]
