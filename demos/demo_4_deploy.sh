#!/bin/bash

# Check if `TAVILY_API_KEY` is  set
if [ -z "$TAVILY_API_KEY" ]; then
    echo "Error: TAVILY_API_KEY must be set"
    exit 1
fi

# Create connection for Tavily usage
uv run orchestrate connections add --app-id tavily_api_key
uv run orchestrate connections configure --app-id tavily_api_key --env live --kind key_value --type team
uv run orchestrate connections configure --app-id tavily_api_key --env draft --kind key_value --type team
uv run orchestrate connections set-credentials --app-id tavily_api_key --env live -e TAVILY_API_KEY=$TAVILY_API_KEY
uv run orchestrate connections set-credentials --app-id tavily_api_key --env draft -e TAVILY_API_KEY=$TAVILY_API_KEY

# Import tools
## Tavily MCP
uv run orchestrate toolkits import \
    --kind mcp \
    --name tavily \
    --description "tavily search mcp server" \
    --package "tavily-mcp" \
    --command '["npx", "-y", "tavily-mcp"]' \
    --tools "*" \
    --app-id "tavily_api_key"

# Import agents
## TopicResearcherAgent
uv run orchestrate agents import -f "agents/patent_topic_research_agent.yaml"

## IdeasGeneratorAgent
uv run orchestrate agents import -f "agents/patent_ideation_agent.yaml"

## PatentDrafterAgent
uv run orchestrate agents import -f "agents/patent_drafter_agent.yaml"

## PatentSupervisorAgent
uv run orchestrate agents import -f "agents/patent_supervisor_agent.yaml"

