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

This package provides the MAGI (Master Agent for Guided Innovation) system,
a multi-agent framework for materials science research that coordinates
specialized sub-agents to support the entire research workflow.
"""

from .agent import create_magi_agent, root_agent

__all__ = ['create_magi_agent', 'root_agent']
