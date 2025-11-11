"""Subagente responsável por 00-ProblemHypothesisExpress."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List

from .base import ZeroUmProcessAgent

logger = logging.getLogger(__name__)


class ProblemHypothesisExpressAgent(ZeroUmProcessAgent):
    process_code = "00-ProblemHypothesisExpress"

    def __init__(
        self,
        context_name: str,
        context_description: str,
        pipeline_dir: Path,
        prompt: str | None = None,
        llm_config: Dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            process_code=self.process_code,
            context_name=context_name,
            context_description=context_description,
            pipeline_dir=pipeline_dir,
            prompt=prompt or self._build_prompt(),
            llm_config=llm_config,
        )

    def _build_prompt(self) -> str:
        return (
            "Você é o subagente ProblemHypothesisExpress da estratégia ZeroUm. "
            "Siga todas as regras de AGENTS.MD, leia os arquivos do processo em process/ZeroUm/00-ProblemHypothesisExpress "
            "e produza artefatos numerados em drive/<Contexto>/<Processo>/ sem usar tabelas nem emojis. "
            "Cheque _SHARED antes de propor novos templates e documente bloqueios no manifesto."
        )

    def run(self) -> Dict[str, Any]:
        logger.info("[%s] Iniciando execução para o contexto %s", self.process_code, self.context_name)
        instructions = self._compose_instructions()
        try:
            logger.info("[%s] Enviando instruções para o agente de linguagem", self.process_code)
            agent_result = self._execute_with_agent(instructions)
            artifact_path = self.save_artifact(
                "problem-hypothesis-express",
                agent_result["content"],
            )
            status = agent_result.get("status", "completed")
            notes = agent_result.get("notes", "")
            logger.info("[%s] Artefato principal gerado em %s", self.process_code, artifact_path)
        except RuntimeError as exc:
            logger.warning("[%s] Falha na execução automática: %s", self.process_code, exc)
            artifact_path = self._write_manual_plan(instructions, str(exc))
            status = "blocked_missing_dependency"
            notes = str(exc)

        manifest: Dict[str, Any] = {
            "process": self.process_code,
            "strategy": self.strategy_name,
            "context": self.context_name,
            "status": status,
            "artifacts": [str(artifact_path)],
            "notes": notes,
        }
        self.publish_manifest(manifest)
        logger.info("[%s] Execução finalizada com status %s", self.process_code, status)
        return manifest

    def _compose_instructions(self) -> str:
        sections: List[str] = [
            "## Contexto informado",
            self.context_description or "Nenhum contexto adicional foi fornecido.",
            "",
            f"Destino no drive: drive/{self.context_name}/{self.process_code}/.",
            f"Contexto destino: drive/{self.context_name}/{self.process_code}/.",
            "",
            "## Diretrizes gerais",
            "Execute o processo 00-ProblemHypothesisExpress de ponta a ponta. "
            "Use português claro, siga AGENTS.MD e garanta aderência aos arquivos do processo.",
        ]
        for filename, content in self.definition.files.items():
            if not content.strip():
                continue
            title = filename.replace(".MD", "").upper()
            sections.append(f"## {title}\n{content.strip()}")
        return "\n\n".join(sections)

    def _execute_with_agent(self, instructions: str) -> Dict[str, Any]:
        agent = self.build_agent()
        if hasattr(agent, "run"):
            response = agent.run(instructions)
        elif callable(agent):
            response = agent(instructions)
        else:
            raise RuntimeError("Instância deepagents não oferece método run/call.")

        normalized = self._normalize_response(response)
        if not normalized.strip():
            raise RuntimeError("Agente retornou texto vazio, revise o prompt.")
        return {
            "status": "completed",
            "content": normalized,
        }

    def _normalize_response(self, response: Any) -> str:
        if response is None:
            return ""
        if isinstance(response, str):
            return response.strip()
        if isinstance(response, dict):
            for key in ("output", "content", "result", "text"):
                value = response.get(key)
                if isinstance(value, str) and value.strip():
                    return value.strip()
            return "\n".join(f"{key}: {value}" for key, value in response.items())
        if isinstance(response, list):
            aggregated = [self._normalize_response(item) for item in response if item]
            return "\n\n".join(part for part in aggregated if part)
        return str(response)

    def _write_manual_plan(self, instructions: str, reason: str) -> Path:
        lines = [
            "# Plano manual ProblemHypothesisExpress",
            f"Motivo do fallback: {reason}",
            "",
            "## Instruções previstas para o agente automático",
            instructions,
        ]
        return self.save_artifact("manual-problem-hypothesis", "\n".join(lines))
