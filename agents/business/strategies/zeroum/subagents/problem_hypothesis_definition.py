"""
Subagente: Problem Hypothesis Definition (01-ProblemHypothesisDefinition)

Baseado em: process/ZeroUm/01-ProblemHypothesisDefinition/process.MD

Propósito:
Executar o processo completo de definição da hipótese de problema,
documentando QUEM, RESULTADO e DOR com profundidade suficiente para
alimentar entrevistas, copywriting e validações posteriores.

Etapas:
1. Identificar o usuário-alvo ou beneficiário
2. Definir o resultado ou objetivo desejado
3. Articular a principal dor ou obstáculo
4. Sintetizar em declaração de hipótese
5. Testar clareza e especificidade
6. Documentar hipótese final e contexto
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from agents.framework.llm.factory import build_llm
from agents.framework.tools import AgentType, get_tools
from agents.business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

logger = logging.getLogger(__name__)


class ProblemHypothesisDefinitionAgent:
    """
    Subagente especializado em produzir a hipótese completa de problema.

    Conduz as seis etapas do processo oficial, gera documentos intermediários
    e preenche os templates compartilhados para assegurar rastreabilidade.
    """

    def __init__(
        self,
        workspace_root: Path,
        idea_context: str,
        initial_hypothesis: Optional[str] = None,
        research_notes: Optional[str] = None,
        enable_tools: bool = True,
    ) -> None:
        """
        Args:
            workspace_root: Diretório raiz do workspace/contexto atual
            idea_context: Descrição resumida do problema/ideia fornecida
            initial_hypothesis: Hipótese preliminar já existente (opcional)
            research_notes: Observações ou evidências coletadas (opcional)
            enable_tools: Habilita ferramentas do framework (padrão: True)
        """
        self.workspace_root = workspace_root
        self.idea_context = idea_context.strip()
        self.initial_hypothesis = (initial_hypothesis or "").strip()
        self.research_notes = (research_notes or "").strip()
        self.llm = build_llm()

        self.tools = get_tools(AgentType.PROCESS) if enable_tools else []
        if self.tools:
            logger.info("Tools habilitadas: %s", [tool.name for tool in self.tools])

        self.process_dir = workspace_root / "01-ProblemHypothesisDefinition"
        self.data_dir = self.process_dir / "_DATA"
        self._setup_directories()
        self.template_filler = ProcessTemplateFiller(
            process_code="01-ProblemHypothesisDefinition",
            output_dir=self.data_dir,
            llm=self.llm,
        )

    def _setup_directories(self) -> None:
        """Cria estrutura de diretórios necessária para o processo."""
        self.process_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def execute_full_definition(self) -> Dict[str, Any]:
        """
        Executa todas as etapas da definição de hipótese.

        Returns:
            Dicionário com artefatos e metadados gerados.
        """
        logger.info("Iniciando ProblemHypothesisDefinition")
        results: Dict[str, Any] = {
            "idea_context": self.idea_context,
            "initial_hypothesis": self.initial_hypothesis,
            "research_notes": self.research_notes,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        stage_user = self._stage_1_define_user()
        results["stages"]["target_user"] = stage_user

        stage_result = self._stage_2_define_outcome()
        results["stages"]["desired_outcome"] = stage_result

        stage_pain = self._stage_3_define_pain()
        results["stages"]["core_pain"] = stage_pain

        stage_hypothesis = self._stage_4_synthesize_hypothesis(
            Path(stage_user["file_path"]),
            Path(stage_result["file_path"]),
            Path(stage_pain["file_path"]),
        )
        results["stages"]["hypothesis_statement"] = stage_hypothesis

        stage_quality = self._stage_5_quality_check(Path(stage_hypothesis["file_path"]))
        results["stages"]["quality_review"] = stage_quality

        stage_final = self._stage_6_document_final(Path(stage_hypothesis["file_path"]))
        results["stages"]["final_package"] = stage_final

        results["completed_at"] = datetime.now().isoformat()

        consolidated = self._create_consolidated_report(results)
        results["consolidated_file"] = str(consolidated)

        self._fill_data_templates(results)

        logger.info("Processo ProblemHypothesisDefinition concluído")
        return results

    # ---------------------------------------------------------------------
    # Stage implementations
    # ---------------------------------------------------------------------
    def _stage_1_define_user(self) -> Dict[str, Any]:
        """Etapa 1: Identificar o usuário-alvo ou beneficiário."""
        prompt = f"""
Você é um estrategista ZeroUm e precisa definir o usuário-alvo primário de forma específica e acionável.

Contexto base:
- Ideia: {self.idea_context or 'Não informado'}
- Hipótese preliminar: {self.initial_hypothesis or 'Não definida'}
- Evidências disponíveis: {self.research_notes or 'Sem registros'}

Produza um documento em português (sem tabelas) com a estrutura:

# 01 - Definição do Usuário-Alvo

## 1. Contexto resumido
- Situação atual observada
- Objetivo geral da iniciativa

## 2. Usuário-Alvo Principal (QUEM)
- Descrição detalhada (função, estágio, responsabilidades)
- Momento em que sente o problema
- Motivadores e gatilhos recentes

## 3. Por que este segmento agora
- Evidências ou sinais que justificam a priorização
- Riscos de escolher outro segmento

## 4. Acessibilidade
- Onde encontrá-lo (canais online/offline específicos)
- Contatos ou comunidades de acesso rápido
- Obstáculos para abordá-lo

## 5. Segmentos Alternativos Considerados
- Alternativa 1: descrição + motivo
- Alternativa 2: descrição + motivo
- Alternativa 3: descrição + motivo

## 6. Critérios para validar se é o segmento correto
- 3 a 5 critérios objetivos

Mantenha linguagem clara, utilize listas e destaque decisões críticas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("01-usuario-alvo.MD", content)
        return {
            "file_path": str(path),
            "description": "Usuário primário descrito e alternativas registradas",
        }

    def _stage_2_define_outcome(self) -> Dict[str, Any]:
        """Etapa 2: Definir o resultado ou objetivo desejado."""
        prompt = f"""
Com base no contexto seguinte, documente o RESULTADO que o usuário deseja alcançar.

Contexto base:
- Ideia: {self.idea_context or 'Não informado'}
- Hipótese preliminar: {self.initial_hypothesis or 'Não definida'}
- Evidências: {self.research_notes or 'Sem registros'}

Produza o documento:

# 02 - Resultado Desejado

## 1. Declaração principal
- Frase clara descrevendo o resultado em até 25 palavras

## 2. Quando o usuário percebe sucesso
- Indicadores objetivos (tempo, dinheiro, performance, satisfação)
- Mudanças observáveis no dia a dia

## 3. Barreiras atuais para atingir esse resultado
- Habilidades, recursos ou crenças limitantes

## 4. Impacto esperado
- Benefícios funcionais
- Benefícios emocionais
- Benefícios financeiros ou estratégicos

## 5. Métricas e sinais de progresso
- 3 métricas quantificáveis
- 2 sinais qualitativos

## 6. Como validar este resultado nas entrevistas
- Perguntas-chave
- Evidências que confirmam ou refutam

Use listas e texto corrido. Evite tabelas e mantenha o conteúdo em português.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("02-resultado-desejado.MD", content)
        return {
            "file_path": str(path),
            "description": "Resultado desejado documentado com métricas",
        }

    def _stage_3_define_pain(self) -> Dict[str, Any]:
        """Etapa 3: Articular a principal dor ou obstáculo."""
        prompt = f"""
Mapeie a principal DOR que impede o usuário de alcançar o resultado desejado.

Contexto:
- Ideia: {self.idea_context or 'Não informado'}
- Hipótese preliminar: {self.initial_hypothesis or 'Não definida'}
- Evidências: {self.research_notes or 'Sem registros'}

# 03 - Dor Central

## 1. Descrição da dor
- Situação atual
- Frequência e intensidade

## 2. Consequências
- Financeiras
- Operacionais
- Emocionais

## 3. Soluções atuais inadequadas
- Solução 1: uso e limitação
- Solução 2: uso e limitação
- Solução 3: uso e limitação

## 4. Custos da dor
- Tempo desperdiçado
- Recursos financeiros
- Oportunidades perdidas

## 5. Evidências ou citações
- 3 exemplos textuais (mesmo que fictícios) representando a linguagem real do usuário

## 6. Perguntas para aprofundar em entrevistas
- Lista de 5 perguntas abertas

Escreva em português e utilize apenas texto/lists.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("03-dor-central.MD", content)
        return {
            "file_path": str(path),
            "description": "Dor central e soluções inadequadas descritas",
        }

    def _stage_4_synthesize_hypothesis(
        self,
        user_file: Path,
        outcome_file: Path,
        pain_file: Path,
    ) -> Dict[str, Any]:
        """Etapa 4: Sintetizar declaração de hipótese."""
        user_notes = user_file.read_text(encoding="utf-8")
        outcome_notes = outcome_file.read_text(encoding="utf-8")
        pain_notes = pain_file.read_text(encoding="utf-8")

        prompt = f"""
Você deve combinar QUEM, RESULTADO e DOR em uma declaração de hipótese clara.

Documentos de referência:

=== Usuário ===
{user_notes}

=== Resultado ===
{outcome_notes}

=== Dor ===
{pain_notes}

Crie o documento:

# 04 - Declaração de Hipótese

## 1. Síntese dos elementos
- QUEM:
- RESULTADO:
- DOR:

## 2. Declaração principal
"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]."

## 3. Variantes úteis
- Versão orientada a benefício
- Versão orientada a urgência
- Versão orientada a diferenciação

## 4. Riscos e premissas
- Lista de 5 premissas

## 5. Próximos passos imediatos
- Ações recomendadas antes de avançar para entrevistas

Mantenha o texto em português, claro e sem tabelas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("04-declaracao-hipotese.MD", content)
        return {
            "file_path": str(path),
            "description": "Declaração final e variantes registradas",
        }

    def _stage_5_quality_check(self, hypothesis_file: Path) -> Dict[str, Any]:
        """Etapa 5: Testar clareza e especificidade."""
        hypothesis_text = hypothesis_file.read_text(encoding="utf-8")
        prompt = f"""
Avalie a declaração de hipótese abaixo contra os critérios oficiais (Específica, Valiosa, Dolorosa, Testável, Focada).

Declaração e contexto:
{hypothesis_text}

Produza:

# 05 - Avaliação de Qualidade

## 1. Checklist por critério
- Critério: observações, status (PASSA/FALHA)

## 2. Problemas encontrados
- Lista por critério

## 3. Ajustes sugeridos
- Sugestões numeradas

## 4. Conclusão
- Passa ou precisa de refinamento
- Próximos passos recomendados

Use bullet lists e mantenha português claro.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("05-avaliacao-qualidade.MD", content)
        return {
            "file_path": str(path),
            "description": "Checklist preenchido e ajustes sugeridos",
        }

    def _stage_6_document_final(self, hypothesis_file: Path) -> Dict[str, Any]:
        """Etapa 6: Documentar hipótese final e contexto."""
        hypothesis_text = hypothesis_file.read_text(encoding="utf-8")
        prompt = f"""
Finalize o pacote da hipótese usando o template textual abaixo. Inclua contexto, versões alternativas e próximos passos.

Hipótese base:
{hypothesis_text}

Escreva:

# 06 - Pacote Final da Hipótese

## 1. Resumo executivo
- Problema abordado
- Usuário-alvo
- Resultado e dor em uma frase

## 2. Declaração final
- Versão aprovada
- Motivo da escolha

## 3. Formulações alternativas consideradas
- V1, V2, V3 (com justificativa)

## 4. Premissas principais
- 5 premissas numeradas

## 5. Próximos passos
- Passos imediatos com responsável estimado

## 6. Hand-off
- Processos seguintes recomendados (ex: TargetUserIdentification, UserInterviewValidation)

Produza texto em português sem tabelas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("06-hipotese-final.MD", content)
        return {
            "file_path": str(path),
            "description": "Hipótese final consolidada e planos definidos",
        }

    # ---------------------------------------------------------------------
    # Support methods
    # ---------------------------------------------------------------------
    def _create_consolidated_report(self, results: Dict[str, Any]) -> Path:
        """Gera documento consolidado com resumo executivo do processo."""
        documents: List[str] = []
        for stage in results["stages"].values():
            registered_path = stage.get("file_path")
            if not registered_path:
                continue
            file_path = Path(registered_path)
            if file_path.exists():
                documents.append(file_path.read_text(encoding="utf-8"))

        context_block = "\n\n".join(documents)
        prompt = f"""
Você recebeu os documentos completos do processo de definição da hipótese.
Crie um relatório consolidado e acionável para stakeholders.

Contexto:
{context_block}

Estrutura desejada:

# 00 - Consolidado da Hipótese

## 1. Resumo executivo (4 bullets)
## 2. Principais descobertas (QUEM, RESULTADO, DOR)
## 3. Riscos e premissas críticas
## 4. Recomendações imediatas
## 5. Referências dos artefatos gerados

Tudo em português, sem tabelas.
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("00-consolidado-hipotese.MD", content)
        return path

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        """Preenche templates oficiais do processo."""
        context = self._build_template_context(results)
        tasks = [
            TemplateTask(
                template="template_hypothesis_statement.MD",
                instructions=(
                    "Complete todas as seções com a hipótese final, descrevendo QUEM, RESULTADO e DOR usando os dados gerados nesta execução."
                ),
                output_name="hypothesis_statement-preenchido.MD",
            ),
            TemplateTask(
                template="quality_checklist.MD",
                instructions=(
                    "Avalie cada critério usando os achados da Etapa 5. Marque PASSA/FALHA explicitamente e registre justificativas claras."
                ),
                output_name="quality_checklist-preenchido.MD",
            ),
        ]
        self.template_filler.fill_templates(tasks, context)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        """Monta contexto textual usado para preencher templates."""
        lines = [
            f"Ideia: {self.idea_context or 'Não informado'}",
            f"Hipótese preliminar: {self.initial_hypothesis or 'Não definida'}",
            f"Evidências: {self.research_notes or 'Sem registros'}",
        ]
        for name, stage in results["stages"].items():
            registered_path = stage.get("file_path")
            if not registered_path:
                continue
            path = Path(registered_path)
            if path.exists():
                try:
                    lines.append(f"\n=== Documento {name} ===\n{path.read_text(encoding='utf-8')}")
                except OSError:
                    continue
        return "\n".join(lines)

    def _save_document(self, filename: str, content: str) -> Path:
        """Salva documento no diretório do processo."""
        path = self.process_dir / filename
        path.write_text(content.strip() + "\n", encoding="utf-8")
        logger.info("Documento salvo: %s", path)
        return path

    def _invoke_llm(self, prompt: str) -> str:
        """Invoca LLM e normaliza o conteúdo retornado."""
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


__all__ = ["ProblemHypothesisDefinitionAgent"]
