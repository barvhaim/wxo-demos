import logging
import os
import re
import time
from typing import Optional
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_RETRIES = 10
RETRY_DELAY = 5.0


def _extract_sentence(line):
    # Get the initial word before any timestamp
    first_word = line.split("<")[0].strip()

    # Find all words inside <c>...</c>
    words = re.findall(r"<c>\s?([^<]+)</c>", line)

    # Combine first word with the rest
    full_sentence = " ".join([first_word] + [w.strip() for w in words])
    return full_sentence


def _get_video_transcript(
    video_id: str,
) -> Optional[str]:
    """
    Transcribes the audio from a YouTube video using its ID.

    :param video_id: The YouTube video ID.
    :returns: The transcription of the YouTube video.
    """
    import yt_dlp

    retries = 0
    subtitle_files = []  # Track files to clean up later

    while retries <= MAX_RETRIES:
        try:
            # Configure yt-dlp to write subtitles
            ydl_opts = {
                "quiet": True,
                "skip_download": True,
                "writesubtitles": True,
                "writeautomaticsub": True,
                "subtitleslangs": ["en", "en-US"],
                "subtitlesformat": "vtt",
                "outtmpl": "%(id)s.%(ext)s",
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                info_dict = ydl.extract_info(video_url, download=True)

                if not info_dict:
                    logger.error(f"Failed to extract info for video {video_id}")
                    return None

                # Check if we have actual or auto-generated subtitles
                if (
                    "requested_subtitles" in info_dict
                    and info_dict["requested_subtitles"]
                ):
                    subtitle_info = info_dict["requested_subtitles"]
                    lang = next(
                        (lang for lang in ["en", "en-US"] if lang in subtitle_info),
                        None,
                    )

                    if lang:
                        # The subtitle file is downloaded locally
                        subtitle_file = f"{video_id}.{lang}.vtt"
                        subtitle_files.append(subtitle_file)  # Add to cleanup list

                        try:
                            with open(subtitle_file, "r", encoding="utf-8") as file:
                                content = file.read()

                                # Basic parsing of VTT format
                                # Skip header
                                lines = content.split("\n")
                                transcript = []
                                capture = False

                                for line in lines:
                                    # Skip timing lines and empty lines
                                    if (
                                        "-->" in line
                                        or not line.strip()
                                        or line.strip() == "WEBVTT"
                                        or line.strip() == "Kind: captions"
                                        or line.strip() == "Language: en-US"
                                        or line.strip() == "Language: en"
                                    ):
                                        capture = True
                                        continue

                                    # If we've started capturing and line has content, add to transcript
                                    if capture and line.strip():
                                        # Extract the sentence from the line
                                        parsed_line = _extract_sentence(line.strip())
                                        transcript.append(parsed_line.strip())

                                # Clean up before returning
                                _cleanup_files(subtitle_files)
                                return " ".join(transcript)

                        except Exception as e:
                            logger.error(f"Error reading subtitle file: {str(e)}")
                            _cleanup_files(subtitle_files)
                            return None

                logger.error(f"No English subtitles found for video {video_id}")
                _cleanup_files(subtitle_files)
                return None

        except Exception as e:
            retries += 1
            if retries <= MAX_RETRIES:
                # Wait before retrying
                logger.warning(
                    f"Attempt {retries} failed: {str(e)}. Retrying in {RETRY_DELAY} seconds..."
                )
                time.sleep(RETRY_DELAY)
                continue
            else:
                logger.error(
                    f"Failed to transcribe the video after {MAX_RETRIES} attempts: {str(e)}"
                )
                _cleanup_files(subtitle_files)
                return None

    _cleanup_files(subtitle_files)
    return None


def _cleanup_files(files):
    """
    Removes the specified files from disk.

    :param files: List of file paths to remove.
    """
    for file in files:
        try:
            if os.path.exists(file):
                os.remove(file)
                logger.debug(f"Removed file: {file}")
        except Exception as e:
            logger.warning(f"Failed to remove file {file}: {str(e)}")


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
    if not video_id:
        logger.error("No video ID provided.")
        return "No video ID provided."

    logger.info(f"Transcribing video with ID: {video_id}")
    transcript = _get_video_transcript(video_id)

    if transcript:
        logger.info(f"Transcription successful for video {video_id}")
        return transcript
    else:
        logger.error(f"Failed to transcribe video {video_id}")
        return "Failed to transcribe video."
