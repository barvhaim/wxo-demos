#!/bin/bash

# Remove existing agents
uv run orchestrate agents remove -n YouTubeVideoInformationAgent -k native
uv run orchestrate agents remove -n YouTubeTranscriberAgent -k native

# Remove existing tools
uv run orchestrate tools remove -n YouTubeVideoInfo
uv run orchestrate tools remove -n YouTubeTranscribe
