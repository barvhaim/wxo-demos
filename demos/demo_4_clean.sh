#!/bin/bash

# Remove existing agents
## TopicResearchAgent
uv run orchestrate agents remove -n TopicResearchAgent -k native

# Remove existing tools
## Tavily MCP
uv run orchestrate toolkits remove -n tavily

# Remove existing connections
uv run orchestrate connections remove --app-id tavily_api_key