# YouTube to PPT Converter

A Python tool that converts YouTube video transcripts into PowerPoint presentations.

## Features

- Extract transcripts from YouTube videos
- Automatically group content into slides
- Generate professional PowerPoint presentations
- Customizable presentation title and output filename
- Support for various YouTube URL formats

## Installation

1. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python youtube_to_ppt.py
```

Follow the prompts:
1. Enter the YouTube video URL
2. Enter a title for your presentation (optional)
3. Enter an output filename (optional, default: output.pptx)

### Example

```
Enter YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Video ID: dQw4w9WgXcQ

Fetching transcript...
Transcript fetched successfully (150 entries)

Enter presentation title (or press Enter for default): My Presentation
Enter output filename (default: output.pptx): my_video.pptx

Grouping content into slides...
Created 8 slides

Generating PowerPoint presentation...
Presentation saved as 'my_video.pptx'
```

## Supported URL Formats

- Standard: `https://www.youtube.com/watch?v=VIDEO_ID`
- Short: `https://youtu.be/VIDEO_ID`
- Embed: `https://www.youtube.com/embed/VIDEO_ID`

## Requirements

- Python 3.6+
- youtube-transcript-api
- python-pptx

## Notes

- The video must have captions/subtitles available for the transcript to be extracted
- Slides are automatically created based on content length (default: ~50 words per slide)
- The generated presentation includes a title slide and content slides

## Limitations

- Only works with videos that have available transcripts/captions
- Transcript language depends on what's available for the video
- Does not include video thumbnails or images in the presentation

## License

This project is part of a Python learning repository.
