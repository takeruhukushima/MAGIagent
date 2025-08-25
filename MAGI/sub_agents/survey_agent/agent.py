"""Survey Agent implementation for the MAGI system."""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from . import prompt

# Model to be used by the agent
MODEL = "gemini-2.5-flash"

def survey_agent() -> LlmAgent:
    """Create and return a Survey Agent instance.
        
    Returns:
        LlmAgent: Configured Survey Agent instance.
    """
    # Define tools available to the Survey Agent
    tools = [google_search]
    
    # Create and return the agent
    return LlmAgent(
        name="survey_agent",
        model=MODEL,
        description=(
            "Specialized in conducting literature surveys using Google Search."
        ),
        instruction=prompt.SURVEY_AGENT_PROMPT,
        tools=tools,
    )
