#!/bin/bash

# THIS SCRIPT USES CUSTOM MODEL FROM OLLAMA

# Import tools
## OpenMeteo
uv run orchestrate tools import -k python -f "tools/weather/openmeteo.py"

# Import agents (custom model!)
## WeatherInfo
uv run orchestrate agents import -f "agents/weather_info_agent.yaml"
