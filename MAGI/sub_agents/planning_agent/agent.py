# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Planning Agent implementation for the MAGI system."""

from typing import Dict, Any, Optional, Callable
from google.adk.agents import LlmAgent, Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search
from . import prompt

# Model to be used by the agent
MODEL = "gemini-2.5-flash"

def planning_agent() -> LlmAgent:
    """Create and return a Planning Agent instance.
        
    Returns:
        LlmAgent: Configured Planning Agent instance.
    """
    # Define tools available to the Planning Agent
    tools = [google_search]
    
    # Create and return the agent
    return LlmAgent(
        name="planning_agent",
        model=MODEL,
        description=(
            "Specialized in research planning, literature review, and experimental design "
            "for materials science research projects."
        ),
        instruction=prompt.PLANNING_AGENT_PROMPT,
        output_key="research_plan",
        tools=tools,
    )