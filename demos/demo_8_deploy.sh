#!/bin/bash

# Get local IP address dynamically
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    LOCAL_IP=$(ipconfig getifaddr en0)
    if [ -z "$LOCAL_IP" ]; then
        # Try alternative interface if en0 is not available
        LOCAL_IP=$(ipconfig getifaddr en1)
    fi
else
    # Linux
    LOCAL_IP=$(hostname -I | awk '{print $1}')
fi

if [ -z "$LOCAL_IP" ]; then
    echo "Error: Could not determine local IP address"
    exit 1
fi

echo "Using local IP: $LOCAL_IP"

# Import tools
## Playwright MCP
uv run orchestrate toolkits import \
    --kind mcp \
    --name "playwright" \
    --description "Playwright MCP for browser automation" \
    --package-root . \
    --command "uvx mcp-proxy --headers x-api-key dummy http://$LOCAL_IP:8931/sse" \
    --tools "*"

# Import agents
## UIAutomationTesterAgent
uv run orchestrate agents import -f "agents/ui_automation_tester_agent.yaml"

# WebScrapingAgent
uv run orchestrate agents import -f "agents/web_scraping_agent.yaml"
