"""Subagente responsável por 00-ProblemHypothesisExpress."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from ...utils.instrumentation import (
    GraphCallbackHandler,
    MetricsCollector,
    ProcessGraphRunner,
)
from .base import ZeroUmProcessAgent

logger = logging.getLogger(__name__)

if TYPE_CHECKING:  # pragma: no cover - apenas para type checking
    from deepagents import DeepAgent


class ProblemHypothesisExpressAgent(ZeroUmProcessAgent):
    process_code = "00-ProblemHypothesisExpress"

    def __init__(
        self,
        context_name: str,
        context_description: str,
        pipeline_dir: Path,
        prompt: str | None = None,
        base_path: Path | None = None,
    ) -> None:
        super().__init__(
            process_code=self.process_code,
            context_name=context_name,
            context_description=context_description,
            pipeline_dir=pipeline_dir,
            prompt=prompt or self._build_prompt(),
            base_path=base_path,
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

        # Criar TODOs para o processo
        self.write_todos([
            {"task": "Preparar instruções do processo", "status": "pending", "id": "prep-001"},
            {"task": "Carregar validator.MD para reflexão", "status": "pending", "id": "prep-002"},
            {"task": "Executar LLM (modo simples ou reflexão)", "status": "pending", "id": "exec-001"},
            {"task": "Salvar artefato gerado", "status": "pending", "id": "save-001"},
            {"task": "Publicar manifesto final", "status": "pending", "id": "manifest-001"},
        ])

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

        # Marcar TODO de salvar artefato
        self.todo_manager.update_status("save-001", "in_progress")
        artifact_path = self.save_artifact("problem-hypothesis-express", content)
        self.todo_manager.mark_completed("save-001")

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

        # Marcar TODO de publicar manifesto
        self.todo_manager.update_status("manifest-001", "in_progress")
        self.publish_manifest(manifest)
        self.todo_manager.mark_completed("manifest-001")

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
        self.todo_manager.update_status("prep-001", "in_progress")
        instructions = self._compose_instructions()
        self.todo_manager.mark_completed("prep-001")
        self.todo_manager.mark_completed("prep-002")  # validator.MD é carregado em _compose_instructions
        return {
            "status": "preparado",
            "instructions": instructions,
            "node_tokens": 0,
        }

    def _node_llm_call(self, state: Dict[str, Any]) -> Dict[str, Any]:
        instructions = state.get("instructions", "")

        # Verificar se modo reflexão está habilitado
        reasoning_mode = os.getenv("AGENTS_REASONING_MODE", "simple").lower()
        use_reflection = reasoning_mode in ("reflection", "thinking", "extended")

        self.todo_manager.update_status("exec-001", "in_progress")

        try:
            if use_reflection:
                result = self._invoke_agent_with_reflection(instructions)
            else:
                result = self._invoke_agent(instructions)
            self.todo_manager.mark_completed("exec-001")
        except RuntimeError as exc:
            logger.warning("[%s] Falha na chamada ao LLM: %s", self.process_code, exc)
            self.todo_manager.mark_failed("exec-001", str(exc))
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
        if "thinking_traces" in result:
            payload["thinking_traces"] = result["thinking_traces"]
        if "draft" in result:
            payload["draft"] = result["draft"]
        if "critique" in result:
            payload["critique"] = result["critique"]
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
        result_content = state.get("result_content", "")
        return {
            "status": status,
            "result_status": status,
            "result_content": result_content,
            "notes": notes,
            "node_tokens": 0,
        }

    def _route_after_llm(self, state: Dict[str, Any]) -> str:
        status = str(state.get("status", "")).lower()
        if status in {"erro", "error", "blocked"}:
            return "fallback"
        return "sucesso"

    def _invoke_agent_with_reflection(self, instructions: str) -> Dict[str, Any]:
        """
        Invoca agente com modo de reflexão (draft → critique → refine).
        """
        agent = self.build_agent()

        # Carregar conteúdo do validator.MD para uso na reflexão
        validator_content = self.definition.files.get("validator.MD", "")

        # Verificar se agente suporta reflexão
        if not hasattr(agent, "run_with_reflection"):
            logger.warning(
                "[%s] Agente não suporta reflexão, usando modo simples",
                self.process_code,
            )
            return self._invoke_agent(instructions)

        try:
            # Executar reflexão em 3 estágios
            reflection_result = agent.run_with_reflection(
                instructions=instructions,
                validator_content=validator_content,
                process_code=self.process_code,
            )

            # Extrair conteúdo refinado
            content = reflection_result.get("content", "")
            if not content.strip():
                raise RuntimeError("Reflexão retornou conteúdo vazio.")

            # Preparar payload com traces de thinking
            payload: Dict[str, Any] = {
                "content": content,
                "thinking_traces": reflection_result.get("thinking_traces", {}),
                "draft": reflection_result.get("draft", ""),
                "critique": reflection_result.get("critique", ""),
            }

            # Estimar tokens totais do processo de reflexão
            traces = reflection_result.get("thinking_traces", {})
            if "total_reasoning_tokens" in traces:
                payload["token_usage"] = traces["total_reasoning_tokens"]
            else:
                payload["token_usage"] = self._estimate_tokens(content)

            logger.info(
                "[%s] Reflexão completa: %d tokens totais, improvement ratio: %.2fx",
                self.process_code,
                payload.get("token_usage", 0),
                traces.get("improvement_ratio", 1.0),
            )

            return payload

        except Exception as exc:
            logger.error("[%s] Erro durante reflexão: %s", self.process_code, exc)
            # Fallback para modo simples em caso de erro
            logger.warning("[%s] Fallback para modo simples após erro na reflexão", self.process_code)
            return self._invoke_agent(instructions)

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
