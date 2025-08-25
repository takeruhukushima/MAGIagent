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

"""Analysis Agent implementation for the MAGI system."""

from typing import Dict, Any, Optional, List, Union, Callable
import pandas as pd
import numpy as np
from google.adk.agents import LlmAgent, Agent
from google.adk.tools.agent_tool import AgentTool
from . import prompt

# Model to be used by the agent
MODEL = "gemini-2.5-flash"

class PandasAgent(Agent):
    """Wrapper around pandas to make it work as an agent."""
    
    def __init__(self):
        super().__init__(
            name="pandas_agent",
            description="Powerful data manipulation and analysis library.",
            instruction="Use pandas for data manipulation and analysis tasks.",
        )
        
    def __call__(self, query: str) -> str:
        """Handle pandas-related queries."""
        return f"Pandas agent received query: {query}\nUse the pandas library directly for data manipulation."


class NumpyAgent(Agent):
    """Wrapper around numpy to make it work as an agent."""
    
    def __init__(self):
        super().__init__(
            name="numpy_agent",
            description="Fundamental package for scientific computing in Python.",
            instruction="Use numpy for numerical operations and array manipulations.",
        )
        
    def __call__(self, query: str) -> str:
        """Handle numpy-related queries."""
        return f"Numpy agent received query: {query}\nUse the numpy library directly for numerical operations."


def analysis_agent(knowledge_agent: Optional[Any] = None) -> LlmAgent:
    """Create and return an Analysis Agent instance.
    
    Args:
        knowledge_agent: Optional reference to the Knowledge Agent for RAG capabilities.
        
    Returns:
        LlmAgent: Configured Analysis Agent instance.
    """
    # Define tools available to the Analysis Agent
    tools = []
    
    if knowledge_agent:
        tools.append(AgentTool(agent=knowledge_agent))
    
    # Create agent instances for pandas and numpy
    pandas_agent = PandasAgent()
    numpy_agent = NumpyAgent()
    
    # Add data analysis tools
    tools.extend([
        AgentTool(agent=pandas_agent),
        AgentTool(agent=numpy_agent),
    ])
    
    # Create and return the agent
    return LlmAgent(
        name="analysis_agent",
        model=MODEL,
        description=(
            "Specialized in analyzing research data, identifying patterns, "
            "and generating insights from experimental results."
        ),
        instruction=prompt.ANALYSIS_AGENT_PROMPT,
        output_key="analysis_results",
        tools=tools,
    )
