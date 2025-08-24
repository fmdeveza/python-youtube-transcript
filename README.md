# Python YouTube Transcript

Small, single-file script to fetch a YouTube video's transcript using `youtube-transcript-api`.
Works with manual captions and many auto-generated captions (when available).

## Requirements

- Python 3.8+
- Internet access
- (Optional) virtualenv to isolate dependencies

## Install

```bash
# create & activate virtualenv (recommended)
python -m venv venv
source venv/bin/activate   # macOS / Linux

# install requirements
pip install -r requirements.txt
```

## Usage

```bash
python get_youtube_transcript.py "<youtube_url>"
```