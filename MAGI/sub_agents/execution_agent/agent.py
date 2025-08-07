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

"""Execution Agent implementation for the MAGI system."""

from typing import Dict, Any, Optional, List
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt

# Model to be used by the agent
MODEL = "gemini-2.5-pro"

def execution_agent(knowledge_agent: Optional[Any] = None) -> LlmAgent:
    """Create and return an Execution Agent instance.
    
    Args:
        knowledge_agent: Optional reference to the Knowledge Agent for RAG capabilities.
        
    Returns:
        LlmAgent: Configured Execution Agent instance.
    """
    # Define tools available to the Execution Agent
    tools = []
    
    if knowledge_agent:
        tools.append(AgentTool(agent=knowledge_agent))
    
    # Create and return the agent
    return LlmAgent(
        name="execution_agent",
        model=MODEL,
        description=(
            "Specialized in executing research protocols, running simulations, "
            "and managing experimental procedures for materials science research."
        ),
        instruction=prompt.EXECUTION_AGENT_PROMPT,
        output_key="execution_results",
        tools=tools,
    )
