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
## Elasticsearch MCP
uv run orchestrate toolkits import \
    --kind mcp \
    --name "elasticsearch" \
    --description "Elasticsearch MCP for search and data management" \
    --package-root . \
    --command "uvx mcp-proxy --headers x-api-key dummy http://$LOCAL_IP:9201/sse" \
    --tools "*"

# Import agents
## ElasticsearchAgent
uv run orchestrate agents import -f "agents/elasticsearch_agent.yaml"