# YouTube to PowerPoint Converter - Complete Guide

Convert YouTube videos into PowerPoint presentations for classroom teaching! This toolset provides two powerful methods to transform video content into educational slides.

## 🎯 Two Tools, Two Approaches

### 1️⃣ Transcript Converter (`youtube_to_ppt.py`)
**Extracts spoken text** from videos and creates text-based slides.

**Best for:**
- 📝 Audio/lecture content
- 🎤 Videos with good captions
- 📚 Creating study notes
- 💾 Smaller file sizes

### 2️⃣ Frame Capture (`youtube_frame_capture.py`)
**Captures video frames** as images with smart content detection.

**Best for:**
- 📊 Visual content (slides, diagrams)
- 🧮 Math problems on whiteboards
- 👨‍🏫 Teacher presentations
- 🖼️ When you need actual images

## 🚀 Quick Start

### Installation

```bash
cd "YouTube to PPT Converter"
pip install -r requirements.txt
```

### Option 1: Transcript-Based Slides

```bash
# Extract transcript and create text slides
python youtube_to_ppt.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Option 2: Frame Capture with Smart Detection

```bash
# Capture clean slide images (skips when teacher blocks content)
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes

# Or capture every 30 seconds
python youtube_frame_capture.py "VIDEO_ID" --interval 30
```

## 📚 Detailed Documentation

- **[README.md](README.md)** - Transcript converter guide
- **[FRAME_CAPTURE_README.md](FRAME_CAPTURE_README.md)** - Frame capture guide
- **[QUICKSTART.md](QUICKSTART.md)** - 3-step quick start
- **[WORKFLOW.md](WORKFLOW.md)** - Visual workflow diagrams
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Technical details

## ✨ Key Features

### Transcript Converter
- ✅ Extracts video metadata (title, author, description)
- ✅ Downloads transcripts/subtitles automatically
- ✅ Groups content into logical 60-90 second chunks
- ✅ Creates slides with timestamps
- ✅ Works with both manual and auto-generated captions

### Frame Capture (Smart Content Detection)
- ✅ **Intelligent filtering** - Only captures when content is visible
- ✅ **Allows teacher in frame** if standing to the side
- ✅ **Skips blocked frames** when teacher covers slides/board
- ✅ **Two capture modes**: Interval or scene detection
- ✅ **Face detection** using OpenCV
- ✅ **Customizable filtering** with `--no-filter` option

## 📖 Usage Examples

### Transcript Converter

```bash
# Basic usage
python youtube_to_ppt.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Custom output file
python youtube_to_ppt.py "VIDEO_ID" my_notes.pptx

# Programmatic usage
from youtube_to_ppt import YouTubeToPPTConverter
converter = YouTubeToPPTConverter("VIDEO_URL")
converter.generate_presentation("output.pptx")
```

### Frame Capture

```bash
# Smart scene detection (recommended for slide videos)
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes

# Capture every 60 seconds
python youtube_frame_capture.py "VIDEO_ID" --interval 60

# Capture all frames without filtering
python youtube_frame_capture.py "VIDEO_ID" --no-filter

# Custom output and keep files
python youtube_frame_capture.py "VIDEO_ID" --output slides.pptx --keep-video
```

## 🔧 Requirements

- **Python 3.6+**
- **Internet connection** (to download videos/transcripts)
- **Disk space** (for temporary files)

### Dependencies

All free and open source:
- `youtube-transcript-api` - Transcript extraction
- `pytube` - Video download and metadata
- `python-pptx` - PowerPoint generation
- `opencv-python` - Video processing and face detection
- `numpy` - Numerical operations

**No API keys or subscriptions required!** ✅

## 🎓 How It Works

### Transcript Converter Flow
```
YouTube URL → Extract video ID → Fetch metadata
            → Download transcript → Group into chunks
            → Create PowerPoint slides → Output .pptx
```

### Frame Capture Flow
```
YouTube URL → Download video → Extract frames
            → Face detection → Content area analysis
            → Filter blocked frames → Create PowerPoint → Output .pptx
```

### Smart Content Detection

The frame capture tool uses intelligent filtering:

1. **Defines content area**: Center 60%×70% of the frame
2. **Detects faces**: Uses OpenCV Haar Cascade
3. **Calculates overlap**: Between face and content area
4. **Decision**:
   - ✅ Capture if no face detected (clean slide)
   - ✅ Capture if face <30% overlap (teacher to side)
   - ❌ Skip if face >30% overlap (teacher blocking)

## 🎯 Use Cases

### For Teachers
- 📹 Convert tutorial videos into lecture slides
- 📝 Create classroom presentations from online courses
- 🎨 Extract visual aids from educational videos
- 📚 Build teaching materials from video content

### For Students
- 📖 Generate study notes from video lectures
- ✍️ Create revision slides from tutorials
- 🧮 Extract problem sets from math videos
- 📊 Build presentations from research videos

## 🆚 Which Tool Should I Use?

| Feature | Transcript Converter | Frame Capture |
|---------|---------------------|---------------|
| **Output** | Text slides | Image slides |
| **File size** | Small (~50KB) | Larger (~5MB+) |
| **Best for** | Speech/audio | Visual/slides |
| **Requires** | Captions | Video download |
| **Speed** | Fast | Slower |
| **Quality** | Depends on captions | Depends on video quality |

**💡 Tip**: Use both! Generate text slides for notes and image slides for visuals.

## ❓ Troubleshooting

### Common Issues

**"No transcript available"**
- Video doesn't have captions
- Try the frame capture tool instead

**"Import error: cv2"**
- Install OpenCV: `pip install opencv-python`

**"Video download failed"**
- Check internet connection
- Verify video is publicly available
- Some videos may be region-restricted

**Large file sizes (frame capture)**
- Use higher intervals: `--interval 120`
- Only capture what you need
- Delete temporary files after

## 💰 Cost

**100% Free!** ✅
- Open source code
- Free Python libraries
- No API keys needed
- Runs on your computer
- No subscriptions or charges

## 📜 License

This is an educational project. Feel free to use and modify for learning purposes. Always respect copyright when using content from YouTube videos.

## 🙏 Credits

Built with:
- [pytube](https://github.com/pytube/pytube) - YouTube video library
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - Transcript extraction
- [python-pptx](https://github.com/scanny/python-pptx) - PowerPoint generation
- [OpenCV](https://opencv.org/) - Computer vision and face detection

## 📞 Getting Help

1. Check the specific tool README:
   - [Transcript Converter README](README.md)
   - [Frame Capture README](FRAME_CAPTURE_README.md)
2. Review the [Quick Start Guide](QUICKSTART.md)
3. See [Workflow diagrams](WORKFLOW.md)
4. Read [Implementation details](IMPLEMENTATION_SUMMARY.md)

---

**Happy teaching and learning!** 🎓✨
