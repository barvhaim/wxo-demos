#!/bin/bash

# Remove existing agents
uv run orchestrate agents remove -n ContextExtractorAgent -k native

# Remove existing tools
uv run orchestrate tools remove -n ContentExtractorByUrl
