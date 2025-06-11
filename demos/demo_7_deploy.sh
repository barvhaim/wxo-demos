#!/bin/bash
# THIS SCRIPT USES MCP SERVER FROM LANGFLOW!

# Import toolkits
## LangFlow MCP - Joke Generator
uv run orchestrate toolkits import \
    --kind mcp \
    --name "lf-jokes-mcp-server" \
    --description "My Langflow MCP server (hosted, SSE)" \
    --package-root . \
    --command "uvx mcp-proxy --headers x-api-key sk-OylPU6UuY6aWFHGjWr5Hl8ldhmh3nF-dvLZj-DZDd1A http://9.46.73.173:7860/api/v1/mcp/project/40bed7ff-bde1-4fd2-8fe0-90f5663c9740/sse" \
    --tools "*"


# Import agents
## JokesAgent
uv run orchestrate agents import -f "agents/jokes_agent.yaml"