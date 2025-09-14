#!/bin/bash

# THIS SCRIPT USES CUSTOM MODEL FROM OLLAMA
# ollama pull llama3.2:latest
# export OLLAMA_HOST=0.0.0.0:11434
# ollama serve

# Test ollama model
#curl --request POST \
#  --url http://192.168.68.59:11434/v1/chat/completions \
#  --header 'content-type: application/json' \
#  --data '{
#  "model": "llama3.2:latest",
#  "messages": [
#    {
#      "content": "Hi",
#      "role": "user"
#    }
#  ]
#}'

# orchestrate models import --file models/ollama.yaml

# Import tools
## OpenMeteo
uv run orchestrate tools import -k python -f "tools/weather/openmeteo.py"

# Import agents (custom model!)
## WeatherInfo
uv run orchestrate agents import -f "agents/weather_info_agent.yaml"
