"""
Subagentes especializados da estratégia ZeroUm.

Cada subagente corresponde a um processo específico do ZeroUm.
"""

from agents.business.strategies.zeroum.subagents.checkout_setup import CheckoutSetupAgent
from agents.business.strategies.zeroum.subagents.client_delivery import ClientDeliveryAgent
from agents.business.strategies.zeroum.subagents.landing_page_creation import (
    LandingPageCreationAgent,
)
from agents.business.strategies.zeroum.subagents.problem_hypothesis_definition import (
    ProblemHypothesisDefinitionAgent,
)
from agents.business.strategies.zeroum.subagents.problem_hypothesis_express import (
    ProblemHypothesisExpressAgent,
)
from agents.business.strategies.zeroum.subagents.target_user_identification import (
    TargetUserIdentificationAgent,
)
from agents.business.strategies.zeroum.subagents.user_interview_validation import (
    UserInterviewValidationAgent,
)
from agents.business.strategies.zeroum.subagents.registry import SubagentRegistry

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
