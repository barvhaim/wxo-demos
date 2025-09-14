#!/bin/bash
# THIS SCRIPT USES MCP SERVER FROM LANGFLOW!

# Import toolkits
## LangFlow MCP - Joke Generator
uv run orchestrate toolkits import \
    --kind mcp \
    --name "lf-jokes-mcp-server" \
    --description "My Langflow MCP server (hosted, SSE)" \
    --package-root . \
    --command "uvx mcp-proxy http://9.46.65.96/api/v1/mcp/project/db85c7cb-6d13-4821-9e07-1ccbb38a0116/sse" \
    --tools "*"


# Import agents
## JokesAgent
uv run orchestrate agents import -f "agents/jokes_agent.yaml"