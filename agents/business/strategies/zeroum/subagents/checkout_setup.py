"""
Subagente: Checkout Setup (05-CheckoutSetup)

Baseado em: process/ZeroUm/05-CheckoutSetup/process.MD

Propósito:
Publicar e validar um checkout mínimo funcional, documentando seleção de
gateway, configuração de conta, criação do link, testes end-to-end,
notificações e plano de monitoramento antes do go-live.

Etapas:
1. Definir requisitos e selecionar gateway
2. Criar conta e habilitar recebimentos
3. Configurar produto e checkout
4. Testar fluxo e notificações
5. Preparar thank you page, e-mails e recibos
6. Documentar monitoramento financeiro e handoff
"""

from __future__ import annotations

import json
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


class CheckoutSetupAgent:
    """
    Subagente especializado em configurar checkouts mínimos para ZeroUm.
    """

    def __init__(
        self,
        workspace_root: Path,
        product_name: str,
        offer_description: str,
        price: str,
        owner: str,
        preferred_gateway: str,
        landing_url: str,
        thankyou_url: str,
        support_email: str,
        enable_tools: bool = True,
    ) -> None:
        """
        Args:
            workspace_root: Diretório raiz do contexto (drive/<Contexto>)
            product_name: Nome do produto/oferta
            offer_description: Descrição resumida da oferta
            price: Condição de preço (ex.: "R$ 497 à vista ou 6x sem juros")
            owner: Responsável principal pelo checkout
            preferred_gateway: Gateway desejado ou aprovado
            landing_url: URL da landing page que direciona para o checkout
            thankyou_url: URL/slug da thank you page
            support_email: E-mail usado nas notificações
            enable_tools: Controla uso de ferramentas do framework
        """
        self.workspace_root = workspace_root
        self.product_name = product_name.strip()
        self.offer_description = offer_description.strip()
        self.price = price.strip()
        self.owner = owner.strip() or "Owner não definido"
        self.preferred_gateway = preferred_gateway.strip()
        self.landing_url = landing_url.strip()
        self.thankyou_url = thankyou_url.strip()
        self.support_email = support_email.strip()
        self.llm = build_llm()

        self.tools = get_tools(AgentType.PROCESS) if enable_tools else []
        if self.tools:
            logger.info("Tools habilitadas: %s", [tool.name for tool in self.tools])

        self.process_dir = workspace_root / "05-CheckoutSetup"
        self.data_dir = self.process_dir / "_DATA"
        self._setup_directories()
        self.template_filler = ProcessTemplateFiller(
            process_code="05-CheckoutSetup",
            output_dir=self.data_dir,
            llm=self.llm,
        )

        self.gateway_decision: Optional[str] = None
        self.checkout_configuration: Optional[str] = None
        self.test_results: Optional[str] = None
        self.notifications_plan: Optional[str] = None

    def _setup_directories(self) -> None:
        """Garante a estrutura de diretórios exigida pelo processo."""
        dirs = [
            self.process_dir,
            self.data_dir,
            self.data_dir / "evidencias",
            self.data_dir / "assets",
        ]
        for path in dirs:
            path.mkdir(parents=True, exist_ok=True)

    def execute_full_setup(self) -> Dict[str, Any]:
        """
        Executa todas as etapas do processo de CheckoutSetup.
        """
        logger.info("Iniciando CheckoutSetup para %s", self.product_name)
        results: Dict[str, Any] = {
            "product_name": self.product_name,
            "offer_description": self.offer_description,
            "price": self.price,
            "owner": self.owner,
            "preferred_gateway": self.preferred_gateway,
            "landing_url": self.landing_url,
            "thankyou_url": self.thankyou_url,
            "support_email": self.support_email,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        stage_gateway = self._stage_1_gateway_selection()
        results["stages"]["gateway_selection"] = stage_gateway

        stage_account = self._stage_2_account_setup(stage_gateway["file_path"])
        results["stages"]["account_setup"] = stage_account

        stage_checkout = self._stage_3_checkout_configuration(stage_account["file_path"])
        results["stages"]["checkout_configuration"] = stage_checkout

        stage_tests = self._stage_4_tests(stage_checkout["file_path"])
        results["stages"]["tests"] = stage_tests

        stage_notifications = self._stage_5_notifications()
        results["stages"]["notifications"] = stage_notifications

        stage_handoff = self._stage_6_monitoring()
        results["stages"]["monitoring"] = stage_handoff

        results["completed_at"] = datetime.now().isoformat()
        consolidated = self._create_consolidated_report(results)
        results["consolidated_file"] = str(consolidated)

        self._fill_data_templates(results)

        logger.info("CheckoutSetup concluído para %s", self.product_name)
        return results

    # ------------------------------------------------------------------
    # Stages
    # ------------------------------------------------------------------
    def _stage_1_gateway_selection(self) -> Dict[str, Any]:
        prompt = f"""
Você precisa selecionar o gateway ideal para o produto abaixo.

Produto: {self.product_name}
Oferta: {self.offer_description}
Preço: {self.price}
Gateway preferido: {self.preferred_gateway or 'Não informado'}
Owner: {self.owner}

Produza um documento com:
- Critérios obrigatórios
- Comparação de 3 gateways (taxas, pagamentos, repasse, riscos)
- Requisitos legais/documentais
- Decisão final com justificativa e próximos passos
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("01-gateway-selection.MD", content)
        self.gateway_decision = content
        return {
            "file_path": str(path),
            "summary": "Gateway avaliado e escolhido",
        }

    def _stage_2_account_setup(self, reference_file: str) -> Dict[str, Any]:
        prompt = f"""
Com base na decisão abaixo, elabore um plano de configuração de conta.

{Path(reference_file).read_text(encoding='utf-8')}

Inclua:
- Status da conta
- Documentos necessários
- Configuração de segurança (2FA, usuários)
- Limites e políticas antifraude
- Checklist de aprovação com responsáveis e prazos
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("02-account-setup.MD", content)
        return {
            "file_path": str(path),
            "summary": "Conta configurada e verificação documentada",
        }

    def _stage_3_checkout_configuration(self, reference_file: str) -> Dict[str, Any]:
        prompt = f"""
Use os dados abaixo para configurar o checkout.

Conta/gateway:
{Path(reference_file).read_text(encoding='utf-8')}

Detalhes adicionais:
- Produto: {self.product_name}
- Descrição: {self.offer_description}
- Preço: {self.price}
- Landing page: {self.landing_url}
- Thank you page: {self.thankyou_url}
- E-mail de suporte: {self.support_email}

Crie um documento com:
- Dados do produto
- Condições comerciais
- URL do checkout (sugira slug)
- Campos obrigatórios
- Termos e políticas vinculadas
- Integrações e webhooks
- Evidências esperadas (prints/logs)
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("03-checkout-config.MD", content)
        self.checkout_configuration = content
        return {
            "file_path": str(path),
            "summary": "Checkout configurado com URL e integrações",
        }

    def _stage_4_tests(self, reference_file: str) -> Dict[str, Any]:
        prompt = f"""
Planeje e registre testes obrigatórios do checkout abaixo.

Checkout:
{Path(reference_file).read_text(encoding='utf-8')}

Inclua:
- Lista de testes (modo teste e live)
- Métodos simulados (PIX, cartão, boleto)
- IDs de transações fictícias
- Registro de notificações recebidas
- Checklist de correções
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("04-test-log.MD", content)
        self.test_results = content
        return {
            "file_path": str(path),
            "summary": "Testes executados e evidências registradas",
        }

    def _stage_5_notifications(self) -> Dict[str, Any]:
        prompt = f"""
Defina o pacote de notificações e materiais pós-compra para o produto {self.product_name}.

Inclua:
- Brief da thank you page
- Estrutura do e-mail de confirmação
- Conteúdo do recibo simples
- Checklist de notificações (cliente, time interno, webhooks, CRM)
- Plano para tracker financeiro semanal
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("05-notificacoes-e-assets.MD", content)
        self.notifications_plan = content
        return {
            "file_path": str(path),
            "summary": "Notificações e materiais definidos",
        }

    def _stage_6_monitoring(self) -> Dict[str, Any]:
        prompt = f"""
Crie um plano de monitoramento e handoff financeiro para o checkout de {self.product_name}.

O plano deve cobrir:
- Responsáveis por acompanhar transações
- Rotina de conciliação
- Plano de contingência para falhas
- Handoff para times de vendas/entrega
- Métricas diárias e semanais
"""
        content = self._invoke_llm(prompt)
        path = self._save_document("06-integration-log.MD", content)
        return {
            "file_path": str(path),
            "summary": "Monitoramento e handoff documentados",
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _create_consolidated_report(self, results: Dict[str, Any]) -> Path:
        data = {
            "product": self.product_name,
            "price": self.price,
            "owner": self.owner,
            "gateway_decision": self.gateway_decision,
            "checkout_configuration": self.checkout_configuration,
            "tests": self.test_results,
            "notifications": self.notifications_plan,
        }
        prompt = f"""
Produza um consolidado executivo do checkout com:
- Resumo executivo
- Gateway escolhido e status
- Detalhes do checkout (URL, métodos, integrações)
- Situação dos testes e notificações
- Próximas ações e responsáveis

Dados:
{json.dumps(data, ensure_ascii=False, indent=2)}
"""
        content = self._invoke_llm(prompt)
        return self._save_document("00-consolidado-checkout.MD", content)

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        context = self._build_template_context(results)
        tasks: List[TemplateTask] = [
            TemplateTask(
                template="gateway-selection.MD",
                instructions="Preencha com a análise e decisão final desta execução.",
                output_name="gateway-selection-preenchido.MD",
            ),
            TemplateTask(
                template="checkout-config.MD",
                instructions="Atualize todos os campos com dados reais do checkout configurado.",
                output_name="checkout-config-preenchido.MD",
            ),
            TemplateTask(
                template="test-log.MD",
                instructions="Registre pelo menos três testes com resultados e notificações.",
                output_name="test-log-preenchido.MD",
            ),
            TemplateTask(
                template="notification-checklist.MD",
                instructions="Marque cada item com status e responsável definido.",
                output_name="notification-checklist-preenchido.MD",
            ),
            TemplateTask(
                template="integration-log.MD",
                instructions="Documente handoff, responsáveis e pendências desta rodada.",
                output_name="integration-log-preenchido.MD",
            ),
            TemplateTask(
                template="thankyou-page-brief.MD",
                instructions="Escreva o conteúdo planejado para a thank you page e CTAs de follow-up.",
                output_name="thankyou-page-brief-preenchido.MD",
            ),
            TemplateTask(
                template="confirmation-email.MD",
                instructions="Preencha o e-mail de confirmação com dados do produto, suporte e próximos passos.",
                output_name="confirmation-email-preenchido.MD",
            ),
            TemplateTask(
                template="receipt-template.MD",
                instructions="Complete o recibo com valores, impostos e contatos relevantes.",
                output_name="receipt-template-preenchido.MD",
            ),
            TemplateTask(
                template="payment-tracker-guidelines.MD",
                instructions="Defina rotina de atualização do tracker e métricas obrigatórias.",
                output_name="payment-tracker-guidelines-preenchido.MD",
            ),
        ]
        self.template_filler.fill_templates(tasks, context)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        sections = [
            f"Produto: {self.product_name}",
            f"Oferta: {self.offer_description}",
            f"Preço: {self.price}",
            f"Owner: {self.owner}",
            f"Gateway preferido: {self.preferred_gateway}",
            f"Landing page: {self.landing_url}",
            f"Thank you page: {self.thankyou_url}",
            f"Suporte: {self.support_email}",
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
        sections.append(
            f"\n=== Testes JSON ===\n{json.dumps(self.test_results or '', ensure_ascii=False)}"
        )
        return "\n".join(sections)

    def _save_document(self, filename: str, content: str) -> Path:
        path = self.process_dir / filename
        path.write_text(content.strip() + "\n", encoding="utf-8")
        logger.info("Documento salvo: %s", path)
        return path

    def _invoke_llm(self, prompt: str) -> str:
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


__all__ = ["CheckoutSetupAgent"]
