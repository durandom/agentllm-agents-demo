"""Factory for creating DemoAgent instances."""

from typing import Any, Dict, Optional
from agentllm.agents.registry import AgentFactory
from agentllm_agents_demo.demo_agent.agent import DemoAgent


class DemoAgentFactory(AgentFactory):
    """Factory for creating DemoAgent instances."""

    @staticmethod
    def create_agent(
        shared_db: Any,
        token_storage: Any,
        user_id: str,
        session_id: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> DemoAgent:
        """Create a DemoAgent instance."""
        return DemoAgent(
            shared_db=shared_db,
            token_storage=token_storage,
            user_id=user_id,
            session_id=session_id,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )

    @staticmethod
    def get_metadata() -> Dict[str, Any]:
        """Get metadata for the DemoAgent."""
        return {
            "name": "demo-agent",
            "description": "Demo agent showcasing AgentLLM features with color tools",
            "mode": "chat",
            "requires_env": ["GEMINI_API_KEY"],
        }
