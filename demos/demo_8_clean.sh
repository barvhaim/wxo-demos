#!/bin/bash

# Remove existing agents
## UIAutomationTesterAgent
uv run orchestrate agents remove -n UIAutomationTesterAgent -k native

## WebScrapingAgent
uv run orchestrate agents remove -n WebScrapingAgent -k native

# Remove existing tools
## Playwright MCP
uv run orchestrate toolkits remove -n playwright
