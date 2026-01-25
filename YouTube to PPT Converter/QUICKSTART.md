# Quick Start Guide - YouTube to PPT Converter

Get started in 3 simple steps!

## Step 1: Install Dependencies

```bash
cd "YouTube to PPT Converter"
pip install -r requirements.txt
```

## Step 2: Run the Converter

Choose any YouTube video URL and run:

```bash
python youtube_to_ppt.py "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

Or use just the video ID:

```bash
python youtube_to_ppt.py YOUR_VIDEO_ID
```

## Step 3: Open Your Presentation

The script will create a file named `youtube_presentation.pptx` in the current directory.

Open it with:
- Microsoft PowerPoint
- Google Slides (File → Open → Upload)
- LibreOffice Impress
- Any compatible presentation software

## Common Use Cases

### For Teachers
```bash
# Convert a math tutorial
python youtube_to_ppt.py "https://www.youtube.com/watch?v=math_tutorial_id" math_lesson.pptx

# Convert a science video
python youtube_to_ppt.py "https://www.youtube.com/watch?v=science_video_id" science_class.pptx
```

### For Students
```bash
# Convert a lecture
python youtube_to_ppt.py "https://www.youtube.com/watch?v=lecture_id" my_notes.pptx
```

## What You Get

Your PowerPoint will contain:

1. **Title Slide** - Video title and author
2. **Description Slide** - What the video is about
3. **Content Slides** - Transcript organized by time segments

Each content slide shows:
- Timestamp (e.g., "3:45" for 3 minutes 45 seconds)
- The spoken content from that part of the video
- Properly formatted text for easy reading

## Tips

✅ **Choose videos with captions** - The tool works best with videos that have subtitles

✅ **Review before teaching** - Always review and customize slides before presenting

✅ **Add your own notes** - Feel free to edit the generated slides

✅ **Check video length** - Very long videos create many slides

## Troubleshooting

**Problem**: "No transcript available"
- **Solution**: The video needs to have captions/subtitles enabled

**Problem**: Import errors
- **Solution**: Run `pip install -r requirements.txt`

**Problem**: Can't find video
- **Solution**: Check the URL is correct and the video is public

## Need Help?

See the full README.md for:
- Detailed documentation
- Advanced usage examples
- API reference
- More troubleshooting tips

Happy teaching! 📚✨
