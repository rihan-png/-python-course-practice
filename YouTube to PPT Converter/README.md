# YouTube to PowerPoint Converter

A Python tool that converts YouTube videos into PowerPoint presentations for teaching purposes. This tool extracts video transcripts and metadata to create educational slides that teachers can use in classrooms.

## Features

- ✅ Extract video title, author, and description
- ✅ Download video transcripts/subtitles automatically
- ✅ Generate PowerPoint slides with organized content
- ✅ Group transcript into logical chunks for better readability
- ✅ Include timestamps for reference
- ✅ Support for both automatic and manual captions
- ✅ Easy-to-use command-line interface

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Convert a YouTube video to PowerPoint:

```bash
python youtube_to_ppt.py <youtube_url>
```

### Specify Output File

```bash
python youtube_to_ppt.py <youtube_url> my_presentation.pptx
```

### Examples

Using a full YouTube URL:
```bash
python youtube_to_ppt.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Using just the video ID:
```bash
python youtube_to_ppt.py dQw4w9WgXcQ
```

With custom output file:
```bash
python youtube_to_ppt.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" my_lesson.pptx
```

## What Gets Created

The tool generates a PowerPoint presentation with:

1. **Title Slide**: Video title and author information
2. **Description Slide**: Video description (first 500 characters)
3. **Content Slides**: Transcript organized into logical chunks with timestamps

Each content slide includes:
- A timestamp showing when the content appears in the video
- The transcript text for that section (60-90 seconds of content)

## How It Works

1. **Fetches Video Information**: Uses pytube to get video metadata (title, author, description)
2. **Downloads Transcript**: Uses YouTube Transcript API to get video subtitles
3. **Organizes Content**: Groups transcript into logical chunks (60-90 seconds each)
4. **Creates Slides**: Generates PowerPoint slides with formatted content
5. **Saves File**: Outputs a .pptx file ready for teaching

## Use Cases

- **Teachers**: Convert educational YouTube videos into slides for classroom presentations
- **Students**: Create study notes from video lectures
- **Trainers**: Transform tutorial videos into training materials
- **Presenters**: Extract key points from informational videos

## Limitations

- The video must have transcripts/captions available (automatic or manual)
- Some videos may have restricted access to transcripts
- Very long videos may generate many slides
- Transcript quality depends on YouTube's auto-generation or creator's captions

## Troubleshooting

### "No transcript available"
- The video doesn't have captions enabled
- Try finding a video with subtitles/captions

### Import errors
- Make sure you installed all requirements: `pip install -r requirements.txt`

### Connection errors
- Check your internet connection
- Verify the YouTube URL is correct
- Some videos may be region-restricted

## Requirements

- Python 3.6+
- Internet connection
- See requirements.txt for Python package dependencies

## Dependencies

- **youtube-transcript-api**: For downloading video transcripts
- **pytube**: For fetching video metadata
- **python-pptx**: For creating PowerPoint presentations

## License

This is a learning project. Feel free to use and modify as needed.

## Tips for Teachers

1. **Review Generated Slides**: Always review and edit slides before presenting
2. **Add Your Notes**: Customize slides with your own annotations
3. **Include Visuals**: Consider adding relevant images or diagrams
4. **Cite Source**: Keep the YouTube link in your presentation for reference
5. **Check Copyright**: Ensure you have rights to use the content for teaching

## Example Workflow

1. Find an educational YouTube video
2. Run the converter: `python youtube_to_ppt.py VIDEO_URL`
3. Open the generated .pptx file in PowerPoint
4. Review and customize the slides
5. Add any additional content, images, or notes
6. Use in your classroom or training session

---

**Note**: This tool is for educational purposes. Always respect copyright and give proper attribution to content creators.
