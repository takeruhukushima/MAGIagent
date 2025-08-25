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

"""MAGI: Master Research Agent for Materials Science Research.

This module implements the main MAGI agent that coordinates between specialized
sub-agents to support materials science research workflows.
"""

from typing import Dict, Any, Optional
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

# Import sub-agents
from .sub_agents.planning_agent.agent import planning_agent
from .sub_agents.execution_agent.agent import execution_agent
from .sub_agents.analysis_agent.agent import analysis_agent
from .sub_agents.survey_agent.agent import survey_agent

# Import the master agent prompt
from .prompt import MASTER_AGENT_PROMPT

# Model to be used by the agent
MODEL = "gemini-2.5-flash"


def create_magi_agent() -> LlmAgent:
    """Create and return the MAGI Master Research Agent.
        
    Returns:
        LlmAgent: Configured MAGI agent instance.
    """
    # Initialize other agents with access to the knowledge agent
    planning_agent_instance = planning_agent()
    execution_agent_instance = execution_agent()
    analysis_agent_instance = analysis_agent()
    survey_agent_instance = survey_agent()
    
    # Create the master agent that coordinates between all sub-agents
    magi_agent = LlmAgent(
        name="magi_master_agent",
        model=MODEL,
        description=(
            "MAGI (Manus Artificial General Intelligence) coordinates specialized "
            "AI agents to support materials science research with human oversight."
        ),
        instruction=MASTER_AGENT_PROMPT,
        tools=[
            AgentTool(agent=planning_agent_instance),
            AgentTool(agent=execution_agent_instance),
            AgentTool(agent=analysis_agent_instance),
            AgentTool(agent=survey_agent_instance),
        ],
    )
    
    return magi_agent

# Set the root agent to be the master research agent
root_agent = create_magi_agent()
