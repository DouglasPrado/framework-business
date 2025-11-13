"""
Utilitário para preencher templates de `_DATA` usando contexto gerado pelos subagentes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any, List, Optional, Sequence

from framework.llm.factory import build_llm


@dataclass
class TemplateTask:
    """Representa uma solicitação de preenchimento de template."""

    template: str
    instructions: str = ""
    output_name: Optional[str] = None


class ProcessTemplateFiller:
    """
    Preenche templates de `_DATA` com auxílio do LLM, como faria um operador humano.
    """

    def __init__(
        self,
        process_code: str,
        output_dir: Path,
        strategy_name: str = "ZeroUm",
        llm: Optional[Any] = None,
    ) -> None:
        self.process_code = process_code
        self.output_dir = output_dir
        self.strategy_name = strategy_name
        self.llm = llm or build_llm()

        # __file__ = business/strategies/zeroum/subagents/template_filler.py
        # parents[0] = subagents/
        # parents[1] = zeroum/
        # parents[2] = strategies/
        # parents[3] = business/
        # parents[4] = framework-business/ (repo root) ✓
        repo_root = Path(__file__).resolve().parents[4]
        self.templates_root = (
            repo_root / "process" / strategy_name / process_code / "_DATA"
        )
        if not self.templates_root.exists():
            raise FileNotFoundError(
                f"Templates do processo {process_code} não encontrados em {self.templates_root}."
            )

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def fill_templates(self, tasks: Sequence[TemplateTask], context: str) -> List[Path]:
        """
        Preenche múltiplos templates usando o mesmo contexto base.

        Args:
            tasks: Lista de templates com instruções específicas.
            context: Conteúdo consolidado gerado pelo subagente.

        Returns:
            Lista de caminhos gerados.
        """
        filled_paths: List[Path] = []
        for task in tasks:
            filled_paths.append(self._fill_single_template(task, context))
        return filled_paths

    def _fill_single_template(self, task: TemplateTask, context: str) -> Path:
        template_path = self.templates_root / task.template
        if not template_path.exists():
            raise FileNotFoundError(
                f"Template '{task.template}' não encontrado em {self.templates_root}"
            )

        template_text = template_path.read_text(encoding="utf-8")
        prompt = self._build_prompt(template_text, context, task)

        response = self.llm.invoke(prompt)
        content = getattr(response, "content", None)
        if isinstance(content, list):  # langchain às vezes retorna lista
            filled_text = "\n".join(
                part.get("text", "") if isinstance(part, dict) else str(part)
                for part in content
            )
        else:
            filled_text = content if isinstance(content, str) else str(response)

        output_rel = Path(task.output_name or task.template)
        output_path = self.output_dir / output_rel
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(filled_text.strip() + "\n", encoding="utf-8")
        return output_path

    @staticmethod
    def _build_prompt(template_text: str, context: str, task: TemplateTask) -> str:
        custom_instructions = task.instructions.strip() or (
            "Complete todos os campos com dados específicos da execução. "
            "Nunca deixe traços em branco; use 'Não informado' apenas se realmente não houver dado."
        )
        return dedent(
            f"""
            Você é um especialista operacional que executa processos seguindo AGENTS.MD.
            Use o contexto a seguir para preencher o template como se estivesse preenchendo manualmente um formulário.

            ## Contexto consolidado
            {context.strip()}

            ## Instruções
            {custom_instructions}

            ## Template base
            {template_text.strip()}

            Regras:
            - Preserve a mesma estrutura, títulos e listas.
            - Substitua marcadores vazios por frases completas e específicas.
            - Mantenha o texto 100% em português e sem tabelas adicionais.
            - Caso um campo não faça sentido, registre 'Não informado' em vez de deixar em branco.
            - Não explique o que fez; apenas devolva o template preenchido.
            """
        ).strip()


__all__ = ["ProcessTemplateFiller", "TemplateTask"]

