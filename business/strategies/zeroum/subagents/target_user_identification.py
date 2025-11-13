"""
Subagente: Target User Identification (02-TargetUserIdentification)

Baseado em: process/ZeroUm/02-TargetUserIdentification/process.MD

Propósito:
Mapear e documentar 5 perfis de usuários-alvo acionáveis,
com momentos-chave, canais de acesso, avaliação de acessibilidade
e plano de validação alinhado às diretrizes ZeroUm.

Etapas:
1. Registrar hipótese rápida do problema
2. Brainstorm de segmentos potenciais
3. Selecionar e priorizar 5 perfis
4. Pesquisar e detalhar cada perfil
5. Avaliar acessibilidade e canais prioritários
6. Documentar pacote final de perfis e próximos passos
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from business.strategies.zeroum.subagents.base import SubagentBase
from business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

logger = logging.getLogger(__name__)

class TargetUserIdentificationAgent(SubagentBase):
    """
    Subagente responsável por identificar usuários-alvo prioritários.

    Produz os artefatos completos descritos no processo,
    preenche templates oficiais e gera arquivos auxiliares
    para entrevistas e campanhas posteriores.
    """

    process_name = "02-TargetUserIdentification"
    strategy_name = "ZeroUm"

    def __init__(
        self,
        workspace_root: Path,
        hypothesis_statement: str,
        context_notes: Optional[str] = None,
        enable_tools: bool = True,
    ) -> None:
        """
        Args:
            workspace_root: Diretório raiz do contexto (ex.: drive/Projeto)
            hypothesis_statement: Declaração resumida de hipótese (1 frase)
            context_notes: Observações, pesquisas ou referências prévias
            enable_tools: Habilitar tools do framework (padrão True)
        """
        # Inicializar base (LLM, tools, conhecimento)
        super().__init__(
            workspace_root=workspace_root,
            enable_tools=enable_tools,
            load_knowledge=True
        )

        # Atributos específicos

        self.workspace_root = workspace_root
        self.hypothesis_statement = hypothesis_statement.strip()
        self.context_notes = (context_notes or "").strip()
        if self.tools:
            logger.info("Tools habilitadas: %s", [tool.name for tool in self.tools])

        self.process_dir = workspace_root / "02-TargetUserIdentification"
        self.data_dir = self.process_dir / "_DATA"
        self.setup_directories(["assets", "evidencias"])
        self.template_filler = ProcessTemplateFiller(
            process_code="02-TargetUserIdentification",
            output_dir=self.data_dir,
            llm=self.llm,
        )

        self.profiles_data: List[Dict[str, Any]] = []

    def execute_full_identification(self) -> Dict[str, Any]:
        """
        Executa o processo completo de identificação de usuários.
        """
        logger.info("Iniciando TargetUserIdentification")
        results: Dict[str, Any] = {
            "hypothesis_statement": self.hypothesis_statement,
            "context_notes": self.context_notes,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        stage_hypothesis = self._stage_1_quick_hypothesis()
        results["stages"]["hypothesis"] = stage_hypothesis

        stage_brainstorm = self._stage_2_brainstorm()
        results["stages"]["brainstorm"] = stage_brainstorm

        stage_prioritization = self._stage_3_prioritize(Path(stage_brainstorm["file_path"]))
        results["stages"]["prioritization"] = stage_prioritization

        self.profiles_data = self._build_profiles_data(
            [
                Path(stage_hypothesis["file_path"]),
                Path(stage_brainstorm["file_path"]),
                Path(stage_prioritization["file_path"]),
            ]
        )
        if not self.profiles_data:
            raise ValueError("Não foi possível gerar os dados estruturados dos perfis.")

        stage_research = self._stage_4_research_profiles()
        results["stages"]["profiles"] = stage_research

        stage_accessibility = self._stage_5_accessibility_review()
        results["stages"]["accessibility"] = stage_accessibility

        stage_final = self._stage_6_final_package()
        results["stages"]["final_package"] = stage_final

        results["completed_at"] = datetime.now().isoformat()
        consolidated = self._create_consolidated_report(results)
        results["consolidated_file"] = str(consolidated)

        self._fill_data_templates(results)
        self._create_contact_list_csv()

        logger.info("TargetUserIdentification concluído com sucesso")
        return results

    # ------------------------------------------------------------------
    # Stage implementations
    # ------------------------------------------------------------------
    def _stage_1_quick_hypothesis(self) -> Dict[str, Any]:
        """Etapa 1: Registrar hipótese rápida."""
        prompt = f"""
Você deve produzir um registro estruturado da hipótese de problema atual.

Hipótese fornecida:
{self.hypothesis_statement or 'Não informada'}

Notas adicionais:
{self.context_notes or 'Sem notas adicionais'}

Crie o documento abaixo (português, sem tabelas):

# 01 - Hipótese Rápida

## 1. Contexto resumido
## 2. Declaração principal (uma frase)
## 3. Elementos chave
- QUEM
- RESULTADO
- DOR

## 4. Evidências existentes
## 5. Premissas arriscadas
## 6. Métricas a observar

Finalize com próximos passos imediatos.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("01-hipotese-rapida.MD", content)
        return {
            "file_path": str(path),
            "summary": "Hipótese rápida estruturada",
        }

    def _stage_2_brainstorm(self) -> Dict[str, Any]:
        """Etapa 2: Brainstorm de segmentos."""
        prompt = f"""
Com base na hipótese abaixo, gere entre 8 e 15 segmentos de usuários distintos que podem viver o problema.

Hipótese:
{self.hypothesis_statement or 'Não informada'}

Notas:
{self.context_notes or 'Sem notas'}

Formato desejado:

# 02 - Brainstorm de Segmentos

Para cada segmento:
- Nome descritivo
- Profissão/função
- Motivo pelo qual vive a dor
- Canais onde pode ser encontrado

Inclua seção final com observações gerais e lacunas de conhecimento.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("02-brainstorm-segmentos.MD", content)
        return {
            "file_path": str(path),
            "summary": "Lista ampla de segmentos gerada",
        }

    def _stage_3_prioritize(self, brainstorm_file: Path) -> Dict[str, Any]:
        """Etapa 3: Priorizar 5 perfis."""
        brainstorm_text = brainstorm_file.read_text(encoding="utf-8")
        prompt = f"""
Você tem o brainstorm de segmentos abaixo.
Selecione 5 perfis de usuário distintos priorizando intensidade da dor, acessibilidade e diversidade.

Brainstorm:
{brainstorm_text}

Produza:

# 03 - Perfis Priorizados

Para cada perfil (1-5):
- Nome descritivo e profissão
- Momento-chave da dor
- Por que priorizar agora
- Canal principal de contato
- Nível de acessibilidade esperado

Finalize com tabela texto (sem usar tabela markdown) listando Prioridade, Perfil, Momento, Canal, Acessibilidade.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("03-perfis-priorizados.MD", content)
        return {
            "file_path": str(path),
            "summary": "Perfis com prioridade definida",
        }

    def _stage_4_research_profiles(self) -> Dict[str, Any]:
        """Etapa 4: Pesquisar e detalhar cada perfil."""
        json_data = json.dumps(self.profiles_data, ensure_ascii=False, indent=2)
        prompt = f"""
Transforme os perfis abaixo em um dossiê completo.

Perfis (JSON):
{json_data}

Crie o documento:

# 04 - Perfis Detalhados

Para cada perfil:
## Perfil X - Nome
- Descrição
- Profissão/Função
- Momento do problema
- Dor principal
- Objetivos
- Canais online prioritários (3+)
- Canais offline (2+)
- Comunidades/influenciadores
- Soluções atuais e limitações
- Mensagens e ganchos recomendados
- O que validaremos primeiro

Finalize com resumo comparativo destacando diversidades entre perfis.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("04-perfis-detalhados.MD", content)
        return {
            "file_path": str(path),
            "summary": "Dossiê completo dos 5 perfis",
            "profile_count": len(self.profiles_data),
        }

    def _stage_5_accessibility_review(self) -> Dict[str, Any]:
        """Etapa 5: Avaliar acessibilidade."""
        stats = self._calculate_accessibility_stats()
        prompt = f"""
Com base nos dados de perfis e nas estatísticas abaixo, produza a avaliação de acessibilidade.

Estatísticas:
{json.dumps(stats, ensure_ascii=False, indent=2)}

Perfis:
{json.dumps(self.profiles_data, ensure_ascii=False, indent=2)}

Documento desejado:

# 05 - Avaliação de Acessibilidade

## 1. Visão geral (número por nível)
## 2. Perfis com acesso rápido (como, quem ativa)
## 3. Perfis que exigem esforço adicional
## 4. Estratégia de canais priorizados
## 5. Riscos de recrutamento e mitigação

Texto em português e sem tabelas.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("05-avaliacao-acessibilidade.MD", content)
        return {
            "file_path": str(path),
            "summary": "Acessibilidade avaliada e riscos mapeados",
        }

    def _stage_6_final_package(self) -> Dict[str, Any]:
        """Etapa 6: Documentar pacote final."""
        profiles_summary = json.dumps(self.profiles_data, ensure_ascii=False, indent=2)
        prompt = f"""
Produza o pacote final de perfis considerando os documentos anteriores.

Perfis:
{profiles_summary}

Crie:

# 06 - Pacote Final de Perfis

## 1. Resumo executivo (3-4 bullets)
## 2. Lista dos 5 perfis (prioridade, nome, momento, canal)
## 3. Estratégia de validação em 3 fases
## 4. Recursos necessários e responsáveis
## 5. Próximos passos imediatos

Finalize com referência aos arquivos gerados (nomes) para facilitar o handoff.
"""
        content = self.invoke_llm(prompt)
        path = self.save_document("06-pacote-final.MD", content)
        return {
            "file_path": str(path),
            "summary": "Pacote final pronto para handoff",
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _build_profiles_data(self, documents: List[Path]) -> List[Dict[str, Any]]:
        """Gera dados estruturados dos perfis via LLM."""
        combined = "\n\n".join(
            doc.read_text(encoding="utf-8") if doc.exists() else ""
            for doc in documents
        ).strip()
        if not combined:
            combined = self.hypothesis_statement

        prompt = f"""
Você receberá notas sobre segmentos de usuários. Gere exatamente 5 perfis detalhados em JSON.

Notas:
{combined}

Retorne APENAS JSON com a seguinte estrutura:
[
  {{
    "priority": 1,
    "name": "Perfil descritivo",
    "profession": "Profissão/Função",
    "description": "Resumo do perfil",
    "problem_moment": "Quando sente o problema",
    "primary_pain": "Dor principal",
    "desired_outcome": "O que busca",
    "online_channels": ["canal A", "canal B"],
    "offline_channels": ["evento A", "local B"],
    "communities": ["Comunidade 1", "Comunidade 2"],
    "influencers": ["Influencer 1"],
    "accessibility_level": "Alto|Médio|Baixo",
    "accessibility_reason": "Motivo",
    "primary_channel": "Canal prioritário",
    "contact_strategy": "Resumo da abordagem",
    "sample_contacts": [
      {{"name": "Exemplo", "channel": "LinkedIn", "type": "direto|grupo", "notes": "Observação"}}
    ],
    "validation_goal": "O que validar primeiro"
  }}
]
"""
        content = self.invoke_llm(prompt)
        data = self._extract_json_array(content)
        if not data:
            logger.error("Falha ao extrair JSON de perfis.")
            return []
        return data

    def _calculate_accessibility_stats(self) -> Dict[str, Any]:
        """Calcula métricas básicas de acessibilidade."""
        summary: Dict[str, Any] = {
            "high": [],
            "medium": [],
            "low": [],
        }
        for profile in self.profiles_data:
            level = profile.get("accessibility_level", "").strip().lower()
            if level.startswith("a"):
                summary["high"].append(profile["name"])
            elif level.startswith("m"):
                summary["medium"].append(profile["name"])
            else:
                summary["low"].append(profile["name"])
        return summary

    def _create_consolidated_report(self, results: Dict[str, Any]) -> Path:
        """Gera documento consolidado com principais achados."""
        profile_block = json.dumps(self.profiles_data, ensure_ascii=False, indent=2)
        template = f"""
Crie um relatório consolidado da identificação de usuários.

Dados estruturados:
{profile_block}

Exija o seguinte formato:

# 00 - Consolidado de Usuários

## 1. Contexto da hipótese
## 2. Perfis principais (bullet por perfil)
## 3. Canais e acessibilidade
## 4. Recomendações imediatas
## 5. Próximas ações com responsáveis
"""
        content = self.invoke_llm(template)
        path = self.save_document("00-consolidado-usuarios.MD", content)
        return path

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        """Preenche templates oficiais do processo."""
        context = self._build_template_context(results)

        tasks: List[TemplateTask] = [
            TemplateTask(
                template="template-resumo-executivo.MD",
                instructions=(
                    "Preencha todas as seções com base nos 5 perfis identificados. "
                    "Use as prioridades e canais mencionados no contexto."
                ),
                output_name="resumo-executivo-preenchido.MD",
            ),
            TemplateTask(
                template="template-tabela-comparativa.MD",
                instructions=(
                    "Complete a tabela e análises comparativas usando os dados estruturados "
                    "dos perfis (prioridade, profissão, momento, canal, acessibilidade)."
                ),
                output_name="tabela-comparativa-preenchida.MD",
            ),
        ]

        for idx, profile in enumerate(self.profiles_data, start=1):
            instructions = (
                f"Preencha o template com os dados do Perfil {idx} - {profile.get('name')}. "
                "Inclua canais, momentos, ferramentas, acessibilidade e notas de pesquisa presentes no contexto."
            )
            tasks.append(
                TemplateTask(
                    template="template-perfil-usuario.MD",
                    instructions=instructions,
                    output_name=f"perfis/perfil-{idx:02d}.MD",
                )
            )

        self.template_filler.fill_templates(tasks, context)

    def _create_contact_list_csv(self) -> None:
        """Gera arquivo CSV com contatos potenciais."""
        header = "PerfilPrioritario,Nome,Negocio,Cargo/Relacionamento,CanalOrigem,TipoContato,Contato,Status,Responsavel,DataConvite,Notas"
        lines = [header]
        for profile in self.profiles_data:
            priority = profile.get("priority", "")
            name = profile.get("name", "")
            contacts = profile.get("sample_contacts") or []
            if not contacts:
                contacts = [
                    {
                        "name": "Contato sugerido",
                        "channel": profile.get("primary_channel", ""),
                        "type": "indicacao",
                        "notes": "Placeholder gerado automaticamente",
                    }
                ]
            for contact in contacts:
                line = [
                    str(priority),
                    contact.get("name", ""),
                    "",
                    contact.get("type", ""),
                    contact.get("channel", ""),
                    contact.get("type", ""),
                    contact.get("channel", ""),
                    "Planejado",
                    "",
                    "",
                    contact.get("notes", ""),
                ]
                lines.append(",".join(value.replace(",", ";") for value in line))
        output = "\n".join(lines) + "\n"
        path = self.data_dir / "contact-list.csv"
        path.write_text(output, encoding="utf-8")
        logger.info("Lista de contatos gerada em %s", path)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        """Cria contexto textual para preenchimento de templates."""
        sections = [
            f"Hipótese: {self.hypothesis_statement or 'Não informada'}",
            f"Notas adicionais: {self.context_notes or 'Nenhuma'}",
        ]
        for stage in results["stages"].values():
            path_str = stage.get("file_path")
            if not path_str:
                continue
            path = Path(path_str)
            if path.exists():
                try:
                    sections.append(f"\n=== Documento {path.name} ===\n{path.read_text(encoding='utf-8')}")
                except OSError:
                    continue

        sections.append("\n=== Perfis Estruturados ===")
        for profile in self.profiles_data:
            sections.append(json.dumps(profile, ensure_ascii=False, indent=2))
        return "\n".join(sections)

    def _extract_json_array(self, content: str) -> List[Dict[str, Any]]:
        """Extrai lista JSON de string retornada pelo LLM."""
        try:
            start = content.find("[")
            end = content.rfind("]")
            if start == -1 or end == -1:
                raise ValueError("Conteúdo não contém JSON de lista.")
            json_str = content[start : end + 1]
            data = json.loads(json_str)
            if not isinstance(data, list):
                raise ValueError("JSON não é uma lista.")
            return data
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Erro ao parsear JSON de perfis: %s", exc)
            return []
__all__ = ["TargetUserIdentificationAgent"]
