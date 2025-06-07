#!/bin/bash

# Import tools
## ContentExtractorByUrl
uv run orchestrate tools import -k python -f "tools/docling/content_extractor_by_url.py" -r "tools/docling/requirements.txt"

# Import agents
## ContextExtractorAgent
uv run orchestrate agents import -f "agents/content_extractor_agent.yaml"

