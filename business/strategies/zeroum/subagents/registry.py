"""
Registry de Subagentes da Estratégia ZeroUm.

Gerencia descoberta e acesso aos subagentes disponíveis,
facilitando seleção dinâmica baseada em contexto.
"""

from typing import Any, Dict, List, Type
import logging

logger = logging.getLogger(__name__)


class SubagentRegistry:
    """
    Registry centralizado de subagentes disponíveis na estratégia ZeroUm.

    Permite descoberta automática, registro dinâmico e acesso
    aos subagentes implementados.
    """

    _registry: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        subagent_class: Type,
        description: str,
        process_code: str,
        complexity: str = "moderate",
        duration: str = "variable",
    ) -> None:
        """
        Registra um subagente no registry.

        Args:
            name: Nome único do subagente (ex: "problem_hypothesis_express")
            subagent_class: Classe do subagente
            description: Descrição do que o subagente faz
            process_code: Código do processo ZeroUm (ex: "00-ProblemHypothesisExpress")
            complexity: Complexidade do processo (simple/moderate/complex)
            duration: Duração estimada (ex: "30 min", "variável")
        """
        cls._registry[name] = {
            "class": subagent_class,
            "description": description,
            "process_code": process_code,
            "complexity": complexity,
            "duration": duration,
        }
        logger.info(f"Subagente registrado: {name} ({process_code})")

    @classmethod
    def get(cls, name: str) -> Type:
        """
        Obtém a classe de um subagente pelo nome.

        Args:
            name: Nome do subagente

        Returns:
            Classe do subagente

        Raises:
            ValueError: Se o subagente não estiver registrado
        """
        if name not in cls._registry:
            available = ", ".join(cls.list_available())
            raise ValueError(
                f"Subagente '{name}' não encontrado. "
                f"Disponíveis: {available}"
            )
        return cls._registry[name]["class"]

    @classmethod
    def get_info(cls, name: str) -> Dict[str, Any]:
        """
        Obtém informações completas sobre um subagente.

        Args:
            name: Nome do subagente

        Returns:
            Dicionário com informações do subagente

        Raises:
            ValueError: Se o subagente não estiver registrado
        """
        if name not in cls._registry:
            available = ", ".join(cls.list_available())
            raise ValueError(
                f"Subagente '{name}' não encontrado. "
                f"Disponíveis: {available}"
            )
        return cls._registry[name]

    @classmethod
    def list_available(cls) -> List[str]:
        """
        Lista nomes de todos os subagentes registrados.

        Returns:
            Lista de nomes de subagentes
        """
        return list(cls._registry.keys())

    @classmethod
    def list_all(cls) -> Dict[str, Dict[str, Any]]:
        """
        Lista todos os subagentes com suas informações.

        Returns:
            Dicionário completo do registry
        """
        return cls._registry.copy()

    @classmethod
    def find_by_complexity(cls, complexity: str) -> List[str]:
        """
        Encontra subagentes por nível de complexidade.

        Args:
            complexity: Nível desejado (simple/moderate/complex)

        Returns:
            Lista de nomes de subagentes que correspondem
        """
        return [
            name
            for name, info in cls._registry.items()
            if info["complexity"] == complexity
        ]

    @classmethod
    def find_by_process_code(cls, process_code: str) -> str:
        """
        Encontra subagente pelo código do processo ZeroUm.

        Args:
            process_code: Código do processo (ex: "00-ProblemHypothesisExpress")

        Returns:
            Nome do subagente

        Raises:
            ValueError: Se nenhum subagente corresponder ao código
        """
        for name, info in cls._registry.items():
            if info["process_code"] == process_code:
                return name

        raise ValueError(
            f"Nenhum subagente encontrado para processo '{process_code}'"
        )

    @classmethod
    def clear(cls) -> None:
        """Limpa o registry (útil para testes)."""
        cls._registry.clear()
        logger.info("Registry de subagentes limpo")


# Importar e registrar subagentes disponíveis
try:
    from business.strategies.zeroum.subagents.problem_hypothesis_express import (
        ProblemHypothesisExpressAgent,
    )

    SubagentRegistry.register(
        name="problem_hypothesis_express",
        subagent_class=ProblemHypothesisExpressAgent,
        description="Sessão express de 30 minutos para validação de hipóteses de problema",
        process_code="00-ProblemHypothesisExpress",
        complexity="simple",
        duration="30 min",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar ProblemHypothesisExpressAgent: {e}")

try:
    from business.strategies.zeroum.subagents.problem_hypothesis_definition import (
        ProblemHypothesisDefinitionAgent,
    )

    SubagentRegistry.register(
        name="problem_hypothesis_definition",
        subagent_class=ProblemHypothesisDefinitionAgent,
        description="Processo completo para definir hipótese de problema com 6 etapas",
        process_code="01-ProblemHypothesisDefinition",
        complexity="moderate",
        duration="60 min",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar ProblemHypothesisDefinitionAgent: {e}")

try:
    from business.strategies.zeroum.subagents.target_user_identification import (
        TargetUserIdentificationAgent,
    )

    SubagentRegistry.register(
        name="target_user_identification",
        subagent_class=TargetUserIdentificationAgent,
        description="Identifica e documenta 5 perfis de usuários-alvo com canais e acessibilidade",
        process_code="02-TargetUserIdentification",
        complexity="moderate",
        duration="90-120 min",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar TargetUserIdentificationAgent: {e}")

try:
    from business.strategies.zeroum.subagents.user_interview_validation import (
        UserInterviewValidationAgent,
    )

    SubagentRegistry.register(
        name="user_interview_validation",
        subagent_class=UserInterviewValidationAgent,
        description="Planeja e executa 10 entrevistas de validação com síntese completa",
        process_code="03-UserInterviewValidation",
        complexity="complex",
        duration="2-4 dias",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar UserInterviewValidationAgent: {e}")

try:
    from business.strategies.zeroum.subagents.landing_page_creation import (
        LandingPageCreationAgent,
    )

    SubagentRegistry.register(
        name="landing_page_creation",
        subagent_class=LandingPageCreationAgent,
        description="Cria landing pages completas com copy, analytics e QA",
        process_code="04-LandingPageCreation",
        complexity="moderate",
        duration="6-8 horas",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar LandingPageCreationAgent: {e}")

try:
    from business.strategies.zeroum.subagents.checkout_setup import (
        CheckoutSetupAgent,
    )

    SubagentRegistry.register(
        name="checkout_setup",
        subagent_class=CheckoutSetupAgent,
        description="Configura checkout mínimo com testes, notificações e monitoramento",
        process_code="05-CheckoutSetup",
        complexity="moderate",
        duration="≈3 horas",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar CheckoutSetupAgent: {e}")

try:
    from business.strategies.zeroum.subagents.client_delivery import (
        ClientDeliveryAgent,
    )

    SubagentRegistry.register(
        name="client_delivery",
        subagent_class=ClientDeliveryAgent,
        description="Processo completo de entrega ao cliente (6 etapas)",
        process_code="10-ClientDelivery",
        complexity="complex",
        duration="variável (dias)",
    )
except ImportError as e:
    logger.warning(f"Não foi possível registrar ClientDeliveryAgent: {e}")


__all__ = ["SubagentRegistry"]
