"""
YouTube to PPT Converter
This script extracts content from YouTube videos and creates PowerPoint presentations.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import re
from urllib.parse import urlparse, parse_qs


def extract_video_id(youtube_url):
    """
    Extract the video ID from a YouTube URL.
    
    Args:
        youtube_url (str): YouTube video URL
    
    Returns:
        str: Video ID or None if not found
    """
    # Handle different YouTube URL formats
    if 'youtu.be/' in youtube_url:
        return youtube_url.split('youtu.be/')[-1].split('?')[0]
    elif 'youtube.com/watch' in youtube_url:
        parsed_url = urlparse(youtube_url)
        return parse_qs(parsed_url.query).get('v', [None])[0]
    elif 'youtube.com/embed/' in youtube_url:
        return youtube_url.split('youtube.com/embed/')[-1].split('?')[0]
    return None


def get_transcript(video_id):
    """
    Get transcript for a YouTube video.
    
    Args:
        video_id (str): YouTube video ID
    
    Returns:
        list: List of transcript entries
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        # Catches specific exceptions from youtube-transcript-api
        print(f"Error fetching transcript: {e}")
        print("Make sure the video has captions/subtitles available.")
        return None


def group_transcript_into_slides(transcript, words_per_slide=50):
    """
    Group transcript text into slides based on word count.
    
    Args:
        transcript (list): List of transcript entries
        words_per_slide (int): Number of words per slide
    
    Returns:
        list: List of slide content strings
    """
    if not transcript:
        return []
    
    # Combine all transcript text
    full_text = ' '.join([entry['text'] for entry in transcript])
    
    # Split into sentences (simple split on . ! ?)
    sentences = re.split(r'[.!?]+', full_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Group sentences into slides
    slides = []
    current_slide = []
    current_word_count = 0
    
    for sentence in sentences:
        words = sentence.split()
        word_count = len(words)
        
        if current_word_count + word_count <= words_per_slide:
            current_slide.append(sentence)
            current_word_count += word_count
        else:
            if current_slide:
                slides.append('. '.join(current_slide) + '.')
            current_slide = [sentence]
            current_word_count = word_count
    
    # Add the last slide
    if current_slide:
        slides.append('. '.join(current_slide) + '.')
    
    return slides


def create_presentation(video_title, slides_content, output_file='output.pptx'):
    """
    Create a PowerPoint presentation from slide content.
    
    Args:
        video_title (str): Title for the presentation
        slides_content (list): List of content for each slide
        output_file (str): Output filename
    """
    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Add title slide
    try:
        title_slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        title.text = video_title
        # Try to add subtitle if placeholder exists
        if len(slide.placeholders) > 1:
            subtitle = slide.placeholders[1]
            subtitle.text = "Generated from YouTube Video"
    except (IndexError, KeyError):
        # If standard layout fails, use blank layout for title
        blank_layout = prs.slide_layouts[6] if len(prs.slide_layouts) > 6 else prs.slide_layouts[0]
        slide = prs.slides.add_slide(blank_layout)
        title_shape = slide.shapes.add_textbox(
            Inches(0.5), Inches(2), Inches(9), Inches(2)
        )
        title_frame = title_shape.text_frame
        title_frame.text = video_title
        title_frame.paragraphs[0].font.size = Pt(44)
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    
    # Add content slides
    for i, content in enumerate(slides_content, 1):
        # Use blank layout for more control, or first available layout
        try:
            blank_layout = prs.slide_layouts[6] if len(prs.slide_layouts) > 6 else prs.slide_layouts[0]
        except IndexError:
            blank_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(blank_layout)
        
        # Add title
        title_shape = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(9), Inches(1)
        )
        title_frame = title_shape.text_frame
        title_frame.text = f"Slide {i}"
        title_para = title_frame.paragraphs[0]
        title_para.font.size = Pt(32)
        title_para.font.bold = True
        
        # Add content
        content_shape = slide.shapes.add_textbox(
            Inches(0.5), Inches(1.8), Inches(9), Inches(5)
        )
        content_frame = content_shape.text_frame
        content_frame.text = content
        content_frame.word_wrap = True
        
        # Format content text
        for paragraph in content_frame.paragraphs:
            paragraph.font.size = Pt(18)
            paragraph.alignment = PP_ALIGN.LEFT
    
    # Save presentation
    prs.save(output_file)
    print(f"Presentation saved as '{output_file}'")


def main():
    """Main function to run the YouTube to PPT converter."""
    print("=" * 50)
    print("YouTube to PPT Converter")
    print("=" * 50)
    
    # Get YouTube URL from user
    youtube_url = input("\nEnter YouTube video URL: ").strip()
    
    # Extract video ID
    video_id = extract_video_id(youtube_url)
    if not video_id:
        print("Error: Invalid YouTube URL")
        return
    
    print(f"Video ID: {video_id}")
    
    # Get transcript
    print("\nFetching transcript...")
    transcript = get_transcript(video_id)
    
    if not transcript:
        print("Error: Could not fetch transcript. Make sure the video has captions/subtitles.")
        return
    
    print(f"Transcript fetched successfully ({len(transcript)} entries)")
    
    # Get presentation title
    video_title = input("\nEnter presentation title (or press Enter for default): ").strip()
    if not video_title:
        video_title = f"YouTube Video {video_id}"
    
    # Get output filename
    output_file = input("Enter output filename (default: output.pptx): ").strip()
    if not output_file:
        output_file = "output.pptx"
    elif not output_file.endswith('.pptx'):
        output_file += '.pptx'
    
    # Group transcript into slides
    print("\nGrouping content into slides...")
    slides_content = group_transcript_into_slides(transcript)
    print(f"Created {len(slides_content)} slides")
    
    # Create presentation
    print("\nGenerating PowerPoint presentation...")
    create_presentation(video_title, slides_content, output_file)
    
    print("\n" + "=" * 50)
    print("Conversion completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
