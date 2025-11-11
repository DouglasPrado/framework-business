"""Subagente responsável por 00-ProblemHypothesisExpress."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List

from ...utils.instrumentation import (
    GraphCallbackHandler,
    MetricsCollector,
    ProcessGraphRunner,
)
from .base import ZeroUmProcessAgent

logger = logging.getLogger(__name__)


class ProblemHypothesisExpressAgent(ZeroUmProcessAgent):
    process_code = "00-ProblemHypothesisExpress"

    def __init__(self, context_name: str, context_description: str, pipeline_dir: Path, prompt: str | None = None) -> None:
        super().__init__(
            process_code=self.process_code,
            context_name=context_name,
            context_description=context_description,
            pipeline_dir=pipeline_dir,
            prompt=prompt or self._build_prompt(),
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

        metrics = MetricsCollector(
            process=self.process_code,
            context=self.context_name,
            logger=logger,
            cost_calculator=self.cost_calculator,
        )
        callbacks = [
            GraphCallbackHandler(
                process=self.process_code,
                context=self.context_name,
                logger=logger,
            )
        ]
        runner = ProcessGraphRunner(
            process=self.process_code,
            context=self.context_name,
            metrics_collector=metrics,
            callback_handlers=callbacks,
        )

        execution = runner.run(
            prepare=self._node_prepare,
            llm_call=self._node_llm_call,
            fallback=self._node_fallback,
            finalize=self._node_finalize,
            route_after_llm=self._route_after_llm,
            initial_state={"contexto": self.context_description},
        )

        final_state = execution.state
        content = final_state.get("result_content", "")
        if not content.strip():
            content = self._build_empty_result_notice(final_state)
        artifact_path = self.save_artifact("problem-hypothesis-express", content)
        status = (
            final_state.get("result_status")
            or final_state.get("status", "inconclusivo")
            or "inconclusivo"
        )
        notes = final_state.get("notes", final_state.get("error", "")) or ""

        manifest: Dict[str, Any] = {
            "process": self.process_code,
            "strategy": self.strategy_name,
            "context": self.context_name,
            "status": status,
            "artifacts": [str(artifact_path)],
            "notes": notes,
            "metrics": execution.metrics.as_dict(),
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

    def _node_prepare(self, state: Dict[str, Any]) -> Dict[str, Any]:
        instructions = self._compose_instructions()
        return {
            "status": "preparado",
            "instructions": instructions,
            "node_tokens": 0,
        }

    def _node_llm_call(self, state: Dict[str, Any]) -> Dict[str, Any]:
        instructions = state.get("instructions", "")
        try:
            result = self._invoke_agent(instructions)
        except RuntimeError as exc:
            logger.warning("[%s] Falha na chamada ao LLM: %s", self.process_code, exc)
            return {
                "status": "erro",
                "error": str(exc),
                "notes": str(exc),
                "result_status": "erro",
                "node_tokens": 0,
            }

        content = result.get("content", "")
        tokens = result.get("token_usage") or self._estimate_tokens(content)
        payload: Dict[str, Any] = {
            "status": "sucesso",
            "result_status": "completed",
            "result_content": content,
            "notes": result.get("notes", ""),
            "node_tokens": tokens,
        }
        if "raw_response" in result:
            payload["raw_response"] = result["raw_response"]
        return payload

    def _node_fallback(self, state: Dict[str, Any]) -> Dict[str, Any]:
        error = state.get("error") or state.get("notes") or "Falha desconhecida ao invocar o LLM."
        instructions = state.get("instructions", "")
        fallback_payload = self._build_fallback_payload(instructions, str(error))
        tokens = self._estimate_tokens(fallback_payload["content"])
        return {
            "status": "fallback",
            "result_status": "fallback",
            "result_content": fallback_payload["content"],
            "notes": fallback_payload["notes"],
            "node_tokens": tokens,
        }

    def _node_finalize(self, state: Dict[str, Any]) -> Dict[str, Any]:
        status = state.get("result_status") or state.get("status") or "finalizado"
        notes = state.get("notes", "")
        return {
            "status": status,
            "result_status": status,
            "notes": notes,
            "node_tokens": 0,
        }

    def _route_after_llm(self, state: Dict[str, Any]) -> str:
        status = str(state.get("status", "")).lower()
        if status in {"erro", "error", "blocked"}:
            return "fallback"
        return "sucesso"

    def _invoke_agent(self, instructions: str) -> Dict[str, Any]:
        agent = self.build_agent()
        if hasattr(agent, "invoke"):
            response = agent.invoke(instructions)
        elif hasattr(agent, "run"):
            response = agent.run(instructions)
        elif callable(agent):
            response = agent(instructions)
        else:
            raise RuntimeError("Instância deepagents não oferece método invoke/run/call.")

        normalized = self._normalize_response(response)
        if not normalized.strip():
            raise RuntimeError("Agente retornou texto vazio, revise o prompt.")

        payload: Dict[str, Any] = {"content": normalized}
        if isinstance(response, dict):
            notes = response.get("notes") or response.get("status_message")
            if isinstance(notes, str):
                payload["notes"] = notes.strip()
            usage = response.get("usage") or response.get("token_usage")
            if isinstance(usage, dict):
                token_value = None
                for key in ("total_tokens", "total", "tokens"):
                    value = usage.get(key)
                    if isinstance(value, (int, float)):
                        token_value = int(value)
                        break
                if token_value is not None:
                    payload["token_usage"] = token_value
            payload["raw_response"] = response
        return payload

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

    def _build_fallback_payload(self, instructions: str, reason: str) -> Dict[str, str]:
        steps = self._extract_task_steps()
        lines: List[str] = [
            "# Fallback heurístico ProblemHypothesisExpress",
            f"Motivo do fallback automático: {reason}",
            "",
            "## Passos sugeridos",
        ]
        if steps:
            for index, step in enumerate(steps, start=1):
                lines.append(f"{index}. {step}")
        else:
            lines.append("1. Revise os arquivos do processo e adapte o plano ao contexto informado.")
        lines.extend(
            [
                "",
                "## Recomendações",
                "- Consulte process/ZeroUm/00-ProblemHypothesisExpress e process/_SHARED antes de criar novos artefatos.",
                "- Registre bloqueios e dependências críticas no manifesto ao atualizar o drive.",
                "",
                "## Instruções originais enviadas ao LLM",
                instructions or "As instruções originais não estavam disponíveis.",
            ]
        )
        notes = f"Fallback heurístico aplicado após falha do LLM: {reason}"
        return {"content": "\n".join(lines), "notes": notes}

    def _extract_task_steps(self) -> List[str]:
        tasks = self.definition.files.get("tasks.MD", "")
        steps: List[str] = []
        for line in tasks.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("-") or stripped.startswith("*"):
                steps.append(stripped.lstrip("-* "))
                continue
            if stripped[0].isdigit():
                parts = stripped.split(maxsplit=1)
                if len(parts) == 2:
                    steps.append(parts[1].strip())
        return steps

    def _estimate_tokens(self, text: str) -> int:
        if not text:
            return 0
        return max(1, len(text.split()))

    def _build_empty_result_notice(self, state: Dict[str, Any]) -> str:
        reason = state.get("error") or state.get("notes") or "Resultado automático indisponível."
        lines = [
            "# Resultado não gerado automaticamente",
            "Não foi possível obter conteúdo do LLM nem construir fallback heurístico completo.",
            f"Motivo registrado: {reason}",
            "",
            "Revise os logs em drive/_pipeline para retomar a execução manualmente.",
        ]
        return "\n".join(lines)
