#!/bin/bash

# Remove existing agents
uv run orchestrate agents remove -n IPReputationChecker -k native

# Remove existing tools
uv run orchestrate tools remove -n CheckIpReputation

# Remove existing connections
uv run orchestrate connections remove --app-id vt_api_key