# YouTube Frame Capture - Extract Slide Images from Videos

A Python tool that **captures video frames** from YouTube videos and creates PowerPoint presentations with those images. Perfect for capturing slides when teachers present in educational videos.

## What This Tool Does

This tool **captures screenshots/images** from YouTube videos and puts them into PowerPoint slides.

### Smart Content Detection

The tool includes intelligent content detection that:
- ✅ **Captures frames when slides/board content is FULLY VISIBLE**
- ✅ **Allows teacher in frame if standing to the SIDE** (not blocking content)
- ✅ **Skips frames where teacher is blocking the main content area**
- ✅ Focuses on capturing clean, readable slides with math, diagrams, text, etc.

### Two Capture Modes:

1. **Interval Mode** (default): Captures frames every N seconds
2. **Scene Detection Mode**: Automatically detects when slides change and captures those moments

Both modes can filter out frames where the content is blocked.

## Installation

Install required dependencies:
```bash
pip install -r requirements.txt
```

**Note**: This tool requires opencv-python and numpy for video processing.

## Usage

### Basic Usage - Capture Every 30 Seconds (with Smart Content Detection)

```bash
python youtube_frame_capture.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

This will:
1. Download the YouTube video
2. Capture frames every 30 seconds (when content is visible)
3. Skip frames where teacher is blocking the slide/board
4. Create a PowerPoint with clean slide images
5. Clean up temporary files

### Detect Slide Changes Automatically

```bash
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes
```

This automatically detects when slides change in the video and captures those moments (only when content is clearly visible).

### Custom Interval

```bash
python youtube_frame_capture.py "VIDEO_ID" --interval 60
```

Capture frames every 60 seconds instead of 30.

### Custom Output Filename

```bash
python youtube_frame_capture.py "VIDEO_ID" --output my_slides.pptx
```

### Keep Downloaded Files

```bash
python youtube_frame_capture.py "VIDEO_ID" --keep-video --keep-frames
```

By default, the tool deletes the downloaded video and frame images after creating the PowerPoint. Use these flags to keep them.

### Disable Content Filtering (Capture All Frames)

```bash
python youtube_frame_capture.py "VIDEO_ID" --no-filter
```

This disables the smart content detection and captures all frames regardless of whether the teacher is blocking content.

## Complete Options

```bash
python youtube_frame_capture.py <youtube_url> [options]

Options:
  --interval <seconds>    Capture frames every N seconds (default: 30)
  --detect-scenes         Detect scene changes (slide transitions)
  --output <filename>     Output PowerPoint filename (default: video_frames.pptx)
  --keep-video           Keep downloaded video file
  --keep-frames          Keep captured frame images
```

## Examples

### Example 1: Educational Video with Slides
```bash
# Automatically detect when slides change
python youtube_frame_capture.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --detect-scenes
```

### Example 2: Long Lecture
```bash
# Capture every 2 minutes
python youtube_frame_capture.py "dQw4w9WgXcQ" --interval 120 --output lecture.pptx
```

### Example 3: Keep Everything
```bash
# Keep video and frames for manual review
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes --keep-video --keep-frames
```

## How It Works

```
Step 1: Download Video
  └─→ Downloads the YouTube video in MP4 format

Step 2: Capture Frames
  ├─ Interval Mode: Captures every N seconds
  └─ Scene Detection: Detects visual changes (slide transitions)

Step 3: Create PowerPoint
  ├─ Title slide with video info
  └─ One slide per captured frame with timestamp

Step 4: Cleanup (optional)
  ├─ Delete video file
  └─ Delete frame images
```

## Output

The generated PowerPoint contains:
1. **Title Slide**: Video title and author
2. **Frame Slides**: Full-screen images of captured frames with timestamp overlay

Each slide shows:
- The captured video frame as a full-screen image
- Timestamp in the corner (e.g., "3:45")

## Differences from `youtube_to_ppt.py`

| Feature | youtube_to_ppt.py | youtube_frame_capture.py |
|---------|-------------------|--------------------------|
| **What it captures** | Text transcript | Video frames (images) |
| **Output content** | Text on slides | Images on slides |
| **Best for** | Audio/speech content | Visual/slide content |
| **File size** | Small | Larger (contains images) |
| **Requires** | Transcript/captions | Video download |

## When to Use This Tool

✅ **Use frame capture when:**
- Teacher shows slides/presentations in the video
- You want to capture visual content (diagrams, code, slides)
- Video has important visual information
- You want screenshots from the video

❌ **Use transcript version when:**
- You only need the spoken content
- Video doesn't have slides/visuals
- You want smaller file sizes
- Video has good captions

## Troubleshooting

### "No module named 'cv2'"
Install OpenCV: `pip install opencv-python`

### "Video download failed"
- Check your internet connection
- Verify the YouTube URL is correct
- Some videos may be restricted

### "No frames captured"
- Video might be too short
- Try reducing the interval: `--interval 10`
- Try scene detection mode: `--detect-scenes`

### Large file sizes
- Use higher interval values (capture fewer frames)
- The PowerPoint contains full-resolution images
- Use `--interval 60` or higher for long videos

## Requirements

- Python 3.6+
- Internet connection
- Sufficient disk space for video download
- See requirements.txt for dependencies

## Tips

1. **For slide-heavy videos**: Use `--detect-scenes` to automatically capture slide transitions
2. **For long lectures**: Use higher intervals like `--interval 120` (every 2 minutes)
3. **Test first**: Try on a short section before processing a long video
4. **Review frames**: Use `--keep-frames` to review captured images before deleting

## Programmatic Usage

```python
from youtube_frame_capture import YouTubeFrameCapture

# Create capturer
capturer = YouTubeFrameCapture("https://www.youtube.com/watch?v=VIDEO_ID")

# Download video
capturer.download_video()

# Capture frames (choose one method)
capturer.capture_frames_interval(interval_seconds=30)
# OR
capturer.capture_frames_scene_change(threshold=30.0, min_interval=5)

# Create PowerPoint
capturer.create_presentation(output_file="my_slides.pptx")

# Cleanup
capturer.cleanup_video()
capturer.cleanup_frames()
```

---

**Note**: This tool downloads YouTube videos for frame extraction. Ensure you have the right to download and use the content. Always respect copyright and give proper attribution to content creators.
