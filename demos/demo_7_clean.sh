#!/bin/bash

# Remove existing agents
## JokesAgent
uv run orchestrate agents remove -n JokesAgent -k native

# Remove existing toolkits
## Tavily MCP
uv run orchestrate toolkits remove -n lf-jokes-mcp-server

