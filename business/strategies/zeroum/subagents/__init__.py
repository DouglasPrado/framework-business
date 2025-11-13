"""
Subagentes especializados da estratégia ZeroUm.

Cada subagente corresponde a um processo específico do ZeroUm.
"""

from business.strategies.zeroum.subagents.checkout_setup import CheckoutSetupAgent
from business.strategies.zeroum.subagents.client_delivery import ClientDeliveryAgent
from business.strategies.zeroum.subagents.landing_page_creation import (
    LandingPageCreationAgent,
)
from business.strategies.zeroum.subagents.problem_hypothesis_definition import (
    ProblemHypothesisDefinitionAgent,
)
from business.strategies.zeroum.subagents.problem_hypothesis_express import (
    ProblemHypothesisExpressAgent,
)
from business.strategies.zeroum.subagents.target_user_identification import (
    TargetUserIdentificationAgent,
)
from business.strategies.zeroum.subagents.user_interview_validation import (
    UserInterviewValidationAgent,
)
from business.strategies.zeroum.subagents.registry import SubagentRegistry

__all__ = [
    "CheckoutSetupAgent",
    "ClientDeliveryAgent",
    "LandingPageCreationAgent",
    "ProblemHypothesisDefinitionAgent",
    "ProblemHypothesisExpressAgent",
    "TargetUserIdentificationAgent",
    "UserInterviewValidationAgent",
    "SubagentRegistry",
]
