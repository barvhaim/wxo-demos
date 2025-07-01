#!/bin/bash

# Remove existing agents
## ElasticsearchAgent
uv run orchestrate agents remove -n ElasticsearchAgent -k native

# Remove existing tools
## Elasticsearch MCP
uv run orchestrate toolkits remove -n elasticsearch