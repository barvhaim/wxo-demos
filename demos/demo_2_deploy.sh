#!/bin/bash

# Import tools
## YouTubeVideoInfo
uv run orchestrate tools import -k python -f "tools/youtube/youtube_info.py" -r "tools/youtube/requirements.txt"

## YouTubeTranscribe
uv run orchestrate tools import -k python -f "tools/youtube/youtube_transcriber.py" -r "tools/youtube/requirements.txt"


# Import agents
## YouTubeVideoInfo
uv run orchestrate agents import -f "agents/youtube_video_info_agent.yaml"

## YouTubeTranscriber
uv run orchestrate agents import -f "agents/youtube_transcriber_agent.yaml"

