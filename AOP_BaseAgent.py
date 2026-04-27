import uuid
from typing import Dict, Any, List

class BaseAgent:
    """The Root Template for Agent-Oriented Programming (AOP)"""
    
    def __init__(self, persona: str, tools: List[callable]):
        # Identity: The Noun
        self.uid = uuid.uuid4()
        
        # Properties: The Adjectives (Describing the Noun)
        self.persona = persona
        self.tools = {t.__name__: t for t in tools}
        self.memory: List[Dict[str, str]] = []
        
        # The Interface/Contract (The Adverb)
        self.reliability_threshold = 0.95 

    # Methods: The Verbs (What the Noun does)
    def perceive(self, stimulus: str):
        """Ingest environment data."""
        self.memory.append({"role": "user", "content": stimulus})

    def deliberate(self) -> str:
        """The internal reasoning loop (The 'Brain' call)."""
        # In a real impl, this calls an LLM
        return f"Agent {self.uid} (as {self.persona}) is planning..."

    def execute(self, tool_name: str, **kwargs):
        """Perform an action via authorized tools."""
        if tool_name in self.tools:
            return self.tools[tool_name](**kwargs)
        raise PermissionError(f"Tool {tool_name} not in Authorization Scope.")

    def handshake(self, other_agent: 'BaseAgent'):
        """Standard AOP protocol for agent-to-agent communication."""
        return f"Establishing connection with Agent {other_agent.uid}"