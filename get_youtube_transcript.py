#!/usr/bin/env python3
"""
Fetch YouTube transcript (captions) using youtube-transcript-api.

Usage:
    python get_youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

Examples:
    python get_youtube_transcript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
"""
import re
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

def extract_video_id(url: str) -> str:
    m = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if m:
        return m.group(1)
    raise ValueError("Couldn't extract video id from URL: " + url)

def fetch_transcript(video_id: str):
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id, languages=['pt'])
        return transcript  # list of {"text","start","duration"}
    except TranscriptsDisabled:
        raise RuntimeError("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise RuntimeError("No transcript found for this video (in requested languages).")
    except VideoUnavailable:
        raise RuntimeError("Video unavailable.")
    except Exception as e:
        raise RuntimeError("Error fetching transcript: " + str(e))

def transcript_to_text(transcript):
    return " ".join(item.text.strip() for item in transcript)

def main():
    if len(sys.argv) < 2:
        print("Usage: python get_youtube_transcript.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        vid = extract_video_id(url)
        transcript = fetch_transcript(vid)
        text = transcript_to_text(transcript)
        print("----- Transcript (preview) -----")
        print(text[:1000] + ("..." if len(text) > 1000 else ""))
        out = f"{vid}_transcript.txt"
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\nFull transcript saved to: {out}")
    except Exception as e:
        print("Failed:", e)
        sys.exit(2)

if __name__ == "__main__":
    main()
