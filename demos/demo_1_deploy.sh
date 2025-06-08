#!/bin/bash

# Check if `VIRUSTOTAL_API_KEY` is  set
if [ -z "$VIRUSTOTAL_API_KEY" ]; then
    echo "Error: VIRUSTOTAL_API_KEY must be set"
    exit 1
fi

# Create connection for VirusTotal usage
uv run orchestrate connections add --app-id vt_api_key
uv run orchestrate connections configure --app-id vt_api_key --env live --kind api_key --type team
uv run orchestrate connections configure --app-id vt_api_key --env draft --kind api_key --type team
uv run orchestrate connections set-credentials --app-id vt_api_key --env live --api-key $VIRUSTOTAL_API_KEY
uv run orchestrate connections set-credentials --app-id vt_api_key --env draft --api-key $VIRUSTOTAL_API_KEY

# Import tools
## CheckIpReputation
uv run orchestrate tools import -k python -f "tools/virustotal/check_ip_reputation.py" -r "tools/virustotal/requirements.txt" --app-id vt_api_key

# Import agents
## IPReputationCheckerAgent
uv run orchestrate agents import -f "agents/ip_reputation_agent.yaml"
