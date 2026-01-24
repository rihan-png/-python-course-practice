## Python Learning & Practice Repository

This repository is forked from CodeWithHarry's Python course.
I use it to learn Python by rewriting examples,
adding my own practice, notes, and small improvements.

### What I am doing here
- Rewriting course code in my own way
- Adding comments and explanations
- Creating small practice programs
- Learning Git and GitHub workflow

### Featured Project: YouTube to PowerPoint Converter 🎥→📊

A comprehensive toolset that converts YouTube videos into PowerPoint presentations for teaching!

**Location**: `YouTube to PPT Converter/`

**Two Tools Included**:

1. **Transcript Converter** - Extracts spoken text and creates text-based slides
   - Perfect for lectures and audio content
   - Automatic transcript extraction
   - Organized slides with timestamps

2. **Frame Capture** - Captures video frames as images with smart filtering
   - Perfect for visual content (slides, diagrams, math)
   - Smart content detection (skips when teacher blocks slides)
   - Auto-detects slide transitions

**Quick Start**:
```bash
cd "YouTube to PPT Converter"
pip install -r requirements.txt

# Transcript-based (text slides)
python youtube_to_ppt.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Frame capture (image slides with smart detection)
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes
```

**Key Features**:
- ✅ 100% Free and open source
- ✅ No API keys required
- ✅ Smart content detection
- ✅ Works offline after download
- ✅ Two complementary approaches

**Documentation**:
- [Complete Guide](YouTube%20to%20PPT%20Converter/MAIN_README.md) - Everything you need
- [Quick Start](YouTube%20to%20PPT%20Converter/QUICKSTART.md) - Get started in 3 steps
- [Frame Capture Guide](YouTube%20to%20PPT%20Converter/FRAME_CAPTURE_README.md) - Smart image capture
- [Workflow Diagrams](YouTube%20to%20PPT%20Converter/WORKFLOW.md) - Visual explanations

### Status
Ongoing learning (updated weekly)
