from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission


@tool(
    name="YouTubeVideoInfo",
    description="Gets information about a YouTube video such as title, channel name, etc.",
    permission=ToolPermission.READ_ONLY,
)
def get_youtube_video_info(
    url: str,
) -> dict:
    """
    Gets information about a YouTube video.

    :param url: The YouTube video URL.
    :returns: A dictionary containing video information (title, channel, etc.)
    """
    import yt_dlp

    try:
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

            # Extract only the needed information
            video_info = {
                "title": info.get("title", ""),
                "channel": info.get("channel", ""),
                "upload_date": info.get("upload_date", ""),
                "duration": info.get("duration", 0),
                "view_count": info.get("view_count", 0),
                "like_count": info.get("like_count", 0),
                "id": info.get("id", ""),
                "url": url,
            }

            return video_info

    except Exception as e:
        return {"error": str(e)}
