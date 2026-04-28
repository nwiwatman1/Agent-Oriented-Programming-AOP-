import abc
from typing import Dict, Any
class IAgentContract(abc.ABC):
"""
The 'Adverb' Interface: Defines HOW an agent must perform.
This serves as the 'Instantiation Contract' to manage non-determinism.
"""
@abc.abstractmethod
def validate_output(self, response: str) -> bool:
"""Check if the agent's output meets specific criteria."""
pass
@property
@abc.abstractmethod
def reliability_threshold(self) -> float:
"""The minimum accuracy/success rate required for this agent."""
pass
class TechnicalReviewerContract(IAgentContract):
"""A specific contract for code-focused agents."""
def validate_output(self, response: str) -> bool:
# Example Contract: Output must contain markdown code blocks
return "```" in response
@property
def reliability_threshold(self) -> float:
return 0.98 # Demands 98% reliability