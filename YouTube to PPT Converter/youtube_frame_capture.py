#!/usr/bin/env python3
"""
YouTube Frame Capture to PowerPoint
====================================
This script captures video frames from YouTube videos and creates PowerPoint 
presentations with those images. Perfect for capturing slides from educational videos.

Features:
- Download YouTube videos
- Extract frames at specified intervals or when scene changes
- Create PowerPoint slides with captured images
- Detect slide transitions automatically
- Filter out frames with teacher faces (capture clean slides only)
"""

import sys
import os
import re
from typing import List, Dict, Optional, Tuple
from pathlib import Path

try:
    from pytube import YouTube
    from pptx import Presentation
    from pptx.util import Inches, Pt
    import cv2
    import numpy as np
except ImportError as e:
    print(f"Error: Missing required library - {e}")
    print("\nPlease install required packages:")
    print("pip install -r requirements.txt")
    sys.exit(1)


class YouTubeFrameCapture:
    """Capture video frames from YouTube and create PowerPoint presentations."""
    
    def __init__(self, video_url: str, output_dir: str = "frames"):
        """
        Initialize the frame capturer with a YouTube URL.
        
        Args:
            video_url: YouTube video URL or video ID
            output_dir: Directory to save captured frames
        """
        self.video_url = video_url
        self.video_id = self._extract_video_id(video_url)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.video_info = None
        self.video_path = None
        self.frames = []
        self.face_cascade = None
        self._load_face_detector()
    
    def _load_face_detector(self):
        """Load the face detection cascade classifier."""
        try:
            # Try to load Haar Cascade for face detection
            cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
            if self.face_cascade.empty():
                print("Warning: Could not load face detector. Content filtering will be disabled.")
                self.face_cascade = None
        except Exception as e:
            print(f"Warning: Face detector not available: {e}")
            self.face_cascade = None
    
    def _is_content_blocked(self, frame) -> Tuple[bool, str]:
        """
        Detect if the main content area (center of frame) is blocked by teacher.
        
        Args:
            frame: OpenCV image frame
            
        Returns:
            Tuple of (is_blocked, reason)
            - is_blocked: True if content is blocked, False if content is visible
            - reason: Description of why it was blocked or allowed
        """
        if self.face_cascade is None:
            return (False, "Face detection disabled")
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        if len(faces) == 0:
            return (False, "No teacher in frame - clean slide")
        
        # Get frame dimensions
        height, width = frame.shape[:2]
        
        # Define the central content area (where slides/board usually are)
        # This is typically the center 60% of the frame horizontally and 70% vertically
        content_left = int(width * 0.2)
        content_right = int(width * 0.8)
        content_top = int(height * 0.15)
        content_bottom = int(height * 0.85)
        
        # Check if any face is blocking the central content area
        for (x, y, w, h) in faces:
            face_center_x = x + w // 2
            face_center_y = y + h // 2
            
            # Calculate how much of the face overlaps with content area
            face_right = x + w
            face_bottom = y + h
            
            # Check if face center is in content area or if face significantly overlaps
            in_content_area = (content_left < face_center_x < content_right and 
                             content_top < face_center_y < content_bottom)
            
            # Calculate overlap
            overlap_x = max(0, min(face_right, content_right) - max(x, content_left))
            overlap_y = max(0, min(face_bottom, content_bottom) - max(y, content_top))
            overlap_area = overlap_x * overlap_y
            face_area = w * h
            
            # If more than 30% of face is in content area, consider it blocking
            if face_area > 0 and (overlap_area / face_area) > 0.3:
                return (True, "Teacher blocking main content area")
        
        # Teacher present but not blocking content (likely standing to the side)
        return (False, "Teacher visible but content area is clear")
        
    def _extract_video_id(self, url: str) -> str:
        """
        Extract video ID from YouTube URL.
        
        Args:
            url: YouTube URL or video ID
            
        Returns:
            Video ID string
        """
        # If it's already a video ID (11 characters)
        if len(url) == 11 and not ('/' in url or '.' in url):
            return url
            
        # Extract from various YouTube URL formats
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?]*)',
            r'youtube\.com\/embed\/([^&\n?]*)',
            r'youtube\.com\/v\/([^&\n?]*)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
                
        raise ValueError(f"Could not extract video ID from URL: {url}")
    
    def download_video(self) -> str:
        """
        Download the YouTube video.
        
        Returns:
            Path to downloaded video file
        """
        try:
            print(f"Downloading video: {self.video_id}")
            yt = YouTube(self.video_url)
            
            # Store video info
            self.video_info = {
                'title': yt.title,
                'author': yt.author,
                'length': yt.length,
                'description': yt.description or "No description available"
            }
            
            # Get the highest resolution stream
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            
            if not stream:
                raise ValueError("No suitable video stream found")
            
            # Download to output directory
            print(f"Downloading: {yt.title}")
            video_file = stream.download(output_path=str(self.output_dir), filename=f"{self.video_id}.mp4")
            self.video_path = video_file
            print(f"✓ Video downloaded: {video_file}")
            
            return video_file
            
        except Exception as e:
            print(f"Error downloading video: {e}")
            raise
    
    def capture_frames_interval(self, interval_seconds: int = 30, skip_faces: bool = True) -> List[str]:
        """
        Capture frames at regular intervals.
        
        Args:
            interval_seconds: Seconds between frame captures
            skip_faces: If True, skip frames with detected faces (teacher visible)
            
        Returns:
            List of paths to captured frame images
        """
        if not self.video_path or not os.path.exists(self.video_path):
            raise ValueError("Video not downloaded. Call download_video() first.")
        
        print(f"\nCapturing frames every {interval_seconds} seconds...")
        if skip_faces:
            print("Content detection enabled: Will only capture frames with visible slides/board")
        
        cap = cv2.VideoCapture(self.video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps
        
        print(f"Video: {duration:.1f}s, {fps:.1f} FPS, {total_frames} frames")
        
        frame_interval = int(fps * interval_seconds)
        frame_paths = []
        frame_count = 0
        saved_count = 0
        skipped_blocked = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Capture frame at intervals
            if frame_count % frame_interval == 0:
                timestamp = frame_count / fps
                
                # Check if content is blocked if detection is enabled
                is_blocked = False
                reason = "No filtering"
                if skip_faces:
                    is_blocked, reason = self._is_content_blocked(frame)
                
                if not is_blocked:
                    frame_filename = self.output_dir / f"frame_{saved_count:04d}_{int(timestamp)}s.jpg"
                    cv2.imwrite(str(frame_filename), frame)
                    frame_paths.append(str(frame_filename))
                    saved_count += 1
                    print(f"  ✓ Captured at {timestamp:.1f}s - {reason}")
                else:
                    skipped_blocked += 1
                    print(f"  ✗ Skipped at {timestamp:.1f}s - {reason}")
            
            frame_count += 1
        
        cap.release()
        
        print(f"✓ Captured {saved_count} frames with visible content")
        if skip_faces and skipped_blocked > 0:
            print(f"  Skipped {skipped_blocked} frames where content was blocked")
        self.frames = frame_paths
        return frame_paths
    
    def capture_frames_scene_change(self, threshold: float = 30.0, min_interval: int = 5, skip_faces: bool = True) -> List[str]:
        """
        Capture frames when scene changes are detected (e.g., slide transitions).
        
        Args:
            threshold: Sensitivity for scene change detection (lower = more sensitive)
            min_interval: Minimum seconds between captures to avoid duplicates
            skip_faces: If True, skip frames where content is blocked by teacher
            
        Returns:
            List of paths to captured frame images
        """
        if not self.video_path or not os.path.exists(self.video_path):
            raise ValueError("Video not downloaded. Call download_video() first.")
        
        print(f"\nDetecting scene changes (threshold={threshold})...")
        if skip_faces:
            print("Content detection enabled: Will only capture frames with visible slides/board")
        
        cap = cv2.VideoCapture(self.video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps
        
        print(f"Video: {duration:.1f}s, {fps:.1f} FPS, {total_frames} frames")
        
        frame_paths = []
        prev_frame = None
        frame_count = 0
        saved_count = 0
        skipped_blocked = 0
        last_saved_time = -min_interval
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            current_time = frame_count / fps
            
            # Convert to grayscale for comparison
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            if prev_frame is not None:
                # Calculate difference between frames
                diff = cv2.absdiff(prev_frame, gray)
                mean_diff = np.mean(diff)
                
                # If significant change detected and enough time has passed
                if mean_diff > threshold and (current_time - last_saved_time) >= min_interval:
                    # Check if content is blocked if detection is enabled
                    is_blocked = False
                    reason = "No filtering"
                    if skip_faces:
                        is_blocked, reason = self._is_content_blocked(frame)
                    
                    if not is_blocked:
                        frame_filename = self.output_dir / f"frame_{saved_count:04d}_{int(current_time)}s.jpg"
                        cv2.imwrite(str(frame_filename), frame)
                        frame_paths.append(str(frame_filename))
                        saved_count += 1
                        last_saved_time = current_time
                        print(f"  ✓ Scene change at {current_time:.1f}s - {reason} (diff: {mean_diff:.1f})")
                    else:
                        skipped_blocked += 1
                        print(f"  ✗ Scene change at {current_time:.1f}s - {reason}")
            
            prev_frame = gray
            frame_count += 1
        
        cap.release()
        
        # Always capture first frame if we didn't get any
        if len(frame_paths) == 0:
            print("  No scene changes detected, capturing frames at intervals instead...")
            return self.capture_frames_interval(interval_seconds=30, skip_faces=skip_faces)
        
        print(f"✓ Captured {saved_count} frames with visible content at scene changes")
        if skip_faces and skipped_blocked > 0:
            print(f"  Skipped {skipped_blocked} frames where content was blocked")
        self.frames = frame_paths
        return frame_paths
    
    def create_presentation(self, frame_paths: Optional[List[str]] = None, 
                          output_file: str = "video_frames.pptx") -> str:
        """
        Create a PowerPoint presentation with captured frames.
        
        Args:
            frame_paths: List of frame image paths (uses self.frames if None)
            output_file: Output PowerPoint filename
            
        Returns:
            Path to created presentation
        """
        if frame_paths is None:
            frame_paths = self.frames
        
        if not frame_paths:
            raise ValueError("No frames to create presentation. Capture frames first.")
        
        print(f"\nCreating PowerPoint presentation...")
        
        prs = Presentation()
        
        # Set slide size to 16:9
        prs.slide_width = Inches(10)
        prs.slide_height = Inches(7.5)
        
        # Create title slide
        title_slide = prs.slides.add_slide(prs.slide_layouts[0])
        title = title_slide.shapes.title
        subtitle = title_slide.placeholders[1]
        
        video_title = self.video_info.get('title', 'YouTube Video') if self.video_info else 'YouTube Video'
        video_author = self.video_info.get('author', 'Unknown') if self.video_info else 'Unknown'
        
        title.text = video_title
        subtitle.text = f"By: {video_author}\nCaptured from YouTube\n{len(frame_paths)} slides"
        
        # Add frame slides
        for i, frame_path in enumerate(frame_paths, 1):
            # Use blank layout
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            
            # Extract timestamp from filename
            timestamp_match = re.search(r'_(\d+)s\.jpg$', frame_path)
            timestamp = int(timestamp_match.group(1)) if timestamp_match else 0
            minutes = timestamp // 60
            seconds = timestamp % 60
            
            # Add image to fill the slide
            left = Inches(0)
            top = Inches(0)
            width = prs.slide_width
            height = prs.slide_height
            
            pic = slide.shapes.add_picture(frame_path, left, top, width=width, height=height)
            
            # Add timestamp text box in corner
            left = prs.slide_width - Inches(1.5)
            top = Inches(0.1)
            width = Inches(1.4)
            height = Inches(0.4)
            
            textbox = slide.shapes.add_textbox(left, top, width, height)
            text_frame = textbox.text_frame
            text_frame.text = f"{minutes}:{seconds:02d}"
            
            # Format timestamp
            paragraph = text_frame.paragraphs[0]
            paragraph.font.size = Pt(12)
            paragraph.font.bold = True
            
            print(f"  Added slide {i}/{len(frame_paths)} - {minutes}:{seconds:02d}")
        
        # Save presentation
        prs.save(output_file)
        print(f"✓ Presentation saved: {output_file}")
        
        return output_file
    
    def cleanup_video(self):
        """Delete the downloaded video file to save space."""
        if self.video_path and os.path.exists(self.video_path):
            os.remove(self.video_path)
            print(f"✓ Cleaned up video file: {self.video_path}")
    
    def cleanup_frames(self):
        """Delete all captured frame images."""
        for frame_path in self.frames:
            if os.path.exists(frame_path):
                os.remove(frame_path)
        print(f"✓ Cleaned up {len(self.frames)} frame images")


def main():
    """Main function to run the frame capturer from command line."""
    print("=" * 60)
    print("YouTube Frame Capture to PowerPoint")
    print("=" * 60)
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python youtube_frame_capture.py <youtube_url> [options]")
        print()
        print("Options:")
        print("  --interval <seconds>    Capture frames every N seconds (default: 30)")
        print("  --detect-scenes         Detect scene changes (slide transitions)")
        print("  --output <filename>     Output PowerPoint filename")
        print("  --keep-video           Keep downloaded video (default: delete)")
        print("  --keep-frames          Keep frame images (default: delete)")
        print("  --no-filter            Disable content filtering (capture all frames)")
        print()
        print("Examples:")
        print("  # Capture frames with smart content detection")
        print("  python youtube_frame_capture.py https://www.youtube.com/watch?v=VIDEO_ID")
        print()
        print("  # Detect scene changes (slide transitions)")
        print("  python youtube_frame_capture.py VIDEO_ID --detect-scenes")
        print()
        print("  # Capture every 60 seconds without filtering")
        print("  python youtube_frame_capture.py VIDEO_ID --interval 60 --no-filter")
        print()
        sys.exit(1)
    
    video_url = sys.argv[1]
    
    # Parse options
    detect_scenes = "--detect-scenes" in sys.argv
    keep_video = "--keep-video" in sys.argv
    keep_frames = "--keep-frames" in sys.argv
    skip_faces = "--no-filter" not in sys.argv  # Enable filtering by default
    
    interval = 30
    if "--interval" in sys.argv:
        idx = sys.argv.index("--interval")
        if idx + 1 < len(sys.argv):
            interval = int(sys.argv[idx + 1])
    
    output_file = "video_frames.pptx"
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_file = sys.argv[idx + 1]
    
    try:
        # Create capturer
        capturer = YouTubeFrameCapture(video_url)
        
        # Download video
        capturer.download_video()
        
        # Capture frames
        if detect_scenes:
            capturer.capture_frames_scene_change(skip_faces=skip_faces)
        else:
            capturer.capture_frames_interval(interval_seconds=interval, skip_faces=skip_faces)
        
        # Create presentation
        capturer.create_presentation(output_file=output_file)
        
        # Cleanup
        if not keep_video:
            capturer.cleanup_video()
        
        if not keep_frames:
            capturer.cleanup_frames()
        
        print()
        print("✓ Done! Your presentation is ready.")
        print(f"  Output: {output_file}")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
