# Step-by-Step Installation and Usage Guide

This guide provides detailed instructions for installing and running the YouTube to PowerPoint converter tools.

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the Transcript Converter](#running-the-transcript-converter)
4. [Running the Frame Capture Tool](#running-the-frame-capture-tool)
5. [Troubleshooting](#troubleshooting)
6. [Examples](#examples)

---

## Prerequisites

### What You Need
- ✅ Python 3.6 or higher installed
- ✅ Internet connection
- ✅ 500MB+ free disk space (for frame capture tool)
- ✅ Command line/terminal access

### Check If Python Is Installed

**Windows:**
```cmd
python --version
```

**macOS/Linux:**
```bash
python3 --version
```

**Expected Output:** `Python 3.x.x` (where x is 6 or higher)

### If Python Is Not Installed

**Windows:**
1. Download from https://www.python.org/downloads/
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## Installation

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`
- Type `cmd` and press Enter

**macOS:**
- Press `Cmd + Space`
- Type `Terminal` and press Enter

**Linux:**
- Press `Ctrl + Alt + T`

### Step 2: Navigate to Project Directory

```bash
# Replace with your actual path
cd /path/to/-python-course-practice

# Then navigate to the tool folder
cd "YouTube to PPT Converter"
```

**Windows Example:**
```cmd
cd C:\Users\YourName\-python-course-practice\YouTube to PPT Converter
```

**macOS/Linux Example:**
```bash
cd ~/Downloads/-python-course-practice/YouTube\ to\ PPT\ Converter
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**If using pip3:**
```bash
pip3 install -r requirements.txt
```

**Expected Output:**
```
Collecting youtube-transcript-api==0.6.1
Collecting pytube==15.0.0
Collecting python-pptx==0.6.21
Collecting opencv-python==4.8.1.78
Collecting numpy==1.24.3
Installing collected packages: ...
Successfully installed ...
```

⏱️ **Installation takes 1-3 minutes**

---

## Running the Transcript Converter

### What It Does
- Extracts spoken text from video
- Creates text-based PowerPoint slides
- Fast and lightweight

### Basic Usage

```bash
python youtube_to_ppt.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Example with Real Video:**
```bash
python youtube_to_ppt.py "https://www.youtube.com/watch?v=kqtD5dpn9C8"
```

### Custom Output File

```bash
python youtube_to_ppt.py "VIDEO_ID" my_lecture_notes.pptx
```

### What Happens
1. 🔍 Extracts video ID from URL
2. 📥 Downloads video metadata
3. 📝 Downloads transcript/subtitles
4. ✂️ Groups text into chunks
5. 📊 Creates PowerPoint slides
6. 💾 Saves as `youtube_presentation.pptx`

### Output Location
- Same folder where you ran the command
- File name: `youtube_presentation.pptx` (or custom name)

---

## Running the Frame Capture Tool

### What It Does
- Downloads video
- Captures frames as images
- Creates image-based PowerPoint slides
- Smart filtering (skips when teacher blocks slides)

### Method 1: Smart Scene Detection (Recommended)

```bash
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes
```

**What This Does:**
- Automatically detects when slides change
- Only captures when content is visible
- Skips frames where teacher blocks slides

**Example:**
```bash
python youtube_frame_capture.py "kqtD5dpn9C8" --detect-scenes
```

### Method 2: Fixed Interval Capture

```bash
python youtube_frame_capture.py "VIDEO_ID" --interval 30
```

**What This Does:**
- Captures frame every 30 seconds
- Still applies smart filtering
- More predictable number of slides

**Example with 60-second intervals:**
```bash
python youtube_frame_capture.py "kqtD5dpn9C8" --interval 60
```

### Method 3: Capture All Frames (No Filtering)

```bash
python youtube_frame_capture.py "VIDEO_ID" --no-filter
```

**What This Does:**
- Disables smart content detection
- Captures all frames regardless of teacher position
- May include frames where slides are blocked

### Advanced Options

```bash
# Custom output file
python youtube_frame_capture.py "VIDEO_ID" --output my_slides.pptx

# Keep downloaded video
python youtube_frame_capture.py "VIDEO_ID" --keep-video

# Keep captured frame images
python youtube_frame_capture.py "VIDEO_ID" --keep-frames

# Combine options
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes --output lecture.pptx --keep-video
```

### What Happens
1. 📥 Downloads YouTube video (~100MB for 10-min video)
2. 🎬 Opens video with OpenCV
3. 👤 Detects faces in each frame (if filtering enabled)
4. 📸 Captures frames when content is visible
5. 📊 Creates PowerPoint with images
6. 🧹 Cleans up temporary files
7. 💾 Saves as `video_frames.pptx`

### Output Location
- Same folder where you ran the command
- File name: `video_frames.pptx` (or custom name)
- Temporary files deleted automatically (unless `--keep-video` used)

---

## Troubleshooting

### Problem: "Command not found: python"

**Solution:**
```bash
# Try python3 instead
python3 youtube_to_ppt.py "VIDEO_ID"
```

### Problem: "No module named 'cv2'"

**Solution:**
```bash
# Reinstall OpenCV
pip install opencv-python
```

### Problem: "No transcript available"

**Solution:**
- Video doesn't have captions
- Use frame capture tool instead:
  ```bash
  python youtube_frame_capture.py "VIDEO_ID" --detect-scenes
  ```

### Problem: "Video download failed"

**Solutions:**
- Check internet connection
- Verify video is publicly available
- Try a different video
- Check if video is age-restricted

### Problem: "Permission denied"

**Solution:**
```bash
# Use pip with --user flag
pip install --user -r requirements.txt
```

### Problem: Large file sizes (frame capture)

**Solutions:**
- Use higher intervals: `--interval 120`
- Only capture what you need
- Delete video after: Don't use `--keep-video`

### Problem: Too many/too few slides

**For Transcript Converter:**
- Slides are grouped into 60-90 second chunks
- No direct control over number of slides

**For Frame Capture:**
- Increase interval: `--interval 120` (fewer slides)
- Decrease interval: `--interval 15` (more slides)
- Use scene detection for automatic detection

---

## Examples

### Example 1: Quick Lecture Notes (Transcript)

```bash
# Navigate to folder
cd "YouTube to PPT Converter"

# Create text-based slides from lecture
python youtube_to_ppt.py "https://www.youtube.com/watch?v=kqtD5dpn9C8" lecture_notes.pptx

# Open lecture_notes.pptx
```

### Example 2: Math Tutorial (Frame Capture)

```bash
# Navigate to folder
cd "YouTube to PPT Converter"

# Capture slides from math video
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes --output math_tutorial.pptx

# Open math_tutorial.pptx
```

### Example 3: Programming Tutorial (Both Methods)

```bash
# Get text transcript for code examples
python youtube_to_ppt.py "VIDEO_ID" code_transcript.pptx

# Get visual slides for diagrams
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes --output code_visuals.pptx

# Now you have both!
```

### Example 4: Long Webinar (Custom Interval)

```bash
# Capture every 2 minutes (120 seconds)
python youtube_frame_capture.py "VIDEO_ID" --interval 120 --output webinar.pptx
```

---

## Getting Video IDs

### From YouTube URL

**Full URL:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
                                  ↑
                            This is the ID
```

**Short URL:**
```
https://youtu.be/dQw4w9WgXcQ
                 ↑
            This is the ID
```

### You Can Use Either:
```bash
# Full URL
python youtube_to_ppt.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Just the ID
python youtube_to_ppt.py "dQw4w9WgXcQ"
```

---

## Next Steps

After running the tools:

1. **Open the PowerPoint file**
   - Windows: Double-click the .pptx file
   - macOS: Open with Keynote or PowerPoint
   - Linux: Use LibreOffice Impress

2. **Review and Edit**
   - Add your own notes
   - Delete unwanted slides
   - Add images or diagrams
   - Format text

3. **Use for Teaching**
   - Present in class
   - Share with students
   - Upload to learning platform
   - Print handouts

---

## Quick Reference Commands

```bash
# Installation
pip install -r requirements.txt

# Transcript converter
python youtube_to_ppt.py "VIDEO_URL"
python youtube_to_ppt.py "VIDEO_ID" output.pptx

# Frame capture - smart detection
python youtube_frame_capture.py "VIDEO_ID" --detect-scenes

# Frame capture - interval
python youtube_frame_capture.py "VIDEO_ID" --interval 30

# Frame capture - no filtering
python youtube_frame_capture.py "VIDEO_ID" --no-filter

# Get help
python youtube_to_ppt.py
python youtube_frame_capture.py
```

---

## Need More Help?

- **Quick Start**: See [QUICKSTART.md](QUICKSTART.md)
- **Complete Guide**: See [MAIN_README.md](MAIN_README.md)
- **Frame Capture Details**: See [FRAME_CAPTURE_README.md](FRAME_CAPTURE_README.md)
- **Technical Details**: See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

---

**Happy converting!** 🎓✨
