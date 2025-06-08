#!/bin/bash

# Remove existing agents
## PatentSupervisorAgent
uv run orchestrate agents remove -n PatentSupervisorAgent -k native

## TopicResearcherAgent
uv run orchestrate agents remove -n TopicResearcherAgent -k native

## IdeasGeneratorAgent
uv run orchestrate agents remove -n IdeasGeneratorAgent -k native

## PatentDrafterAgent
uv run orchestrate agents remove -n PatentDrafterAgent -k native

# Remove existing tools
## Tavily MCP
uv run orchestrate toolkits remove -n tavily

# Remove existing connections
uv run orchestrate connections remove --app-id tavily_api_key