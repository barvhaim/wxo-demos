from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
import time

MAX_RETRIES = 10
RETRY_DELAY = 1.0  # seconds


@tool(
    name="YouTubeTranscribe",
    description="Transcribes the audio from a YouTube video ID.",
    permission=ToolPermission.READ_ONLY,
)
def youtube_transcribe(
    video_id: str,
) -> str:
    """
    Transcribes the audio from a YouTube video.

    :param video_id: The YouTube video ID.
    :returns: The transcription of the YouTube video.
    """
    from youtube_transcript_api import YouTubeTranscriptApi

    ytt_api = YouTubeTranscriptApi()
    final_output = ""

    retries = 0
    while retries <= MAX_RETRIES:
        try:
            transcript = ytt_api.fetch(video_id, languages=["en"])

            for snippet in transcript:
                final_output += snippet.text + " "

            return final_output

        except Exception as e:
            retries += 1
            if retries <= MAX_RETRIES:
                # Wait before retrying
                time.sleep(RETRY_DELAY)
                continue
            else:
                return f"Failed to transcribe the video after {MAX_RETRIES} attempts: {str(e)}"

    return final_output
