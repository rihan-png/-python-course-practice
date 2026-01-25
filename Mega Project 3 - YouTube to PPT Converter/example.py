"""
Example script demonstrating the YouTube to PPT Converter functionality.
This is a non-interactive version for testing purposes.
"""

from youtube_to_ppt import (
    extract_video_id, 
    get_transcript, 
    group_transcript_into_slides,
    create_presentation
)


def test_url_extraction():
    """Test video ID extraction from different URL formats."""
    print("Testing URL extraction...")
    
    test_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://www.youtube.com/embed/dQw4w9WgXcQ"
    ]
    
    for url in test_urls:
        video_id = extract_video_id(url)
        print(f"  {url} -> {video_id}")
    
    print("URL extraction test completed!\n")


def test_transcript_grouping():
    """Test transcript grouping functionality."""
    print("Testing transcript grouping...")
    
    # Mock transcript data
    mock_transcript = [
        {'text': 'This is the first sentence.'},
        {'text': 'This is the second sentence.'},
        {'text': 'This is the third sentence that is a bit longer.'},
        {'text': 'And this is the fourth sentence.'}
    ]
    
    slides = group_transcript_into_slides(mock_transcript, words_per_slide=10)
    print(f"  Created {len(slides)} slides from mock data")
    for i, slide in enumerate(slides, 1):
        print(f"  Slide {i}: {slide[:50]}...")
    
    print("Transcript grouping test completed!\n")


def create_sample_presentation():
    """Create a sample presentation to test functionality."""
    print("Creating sample presentation...")
    
    sample_slides = [
        "This is the content of the first slide. It contains some sample text to demonstrate the presentation creation.",
        "Here is another slide with different content. This shows how multiple slides are created in the presentation.",
        "The final slide in our sample presentation. This demonstrates the complete flow of the converter."
    ]
    
    create_presentation(
        video_title="Sample YouTube to PPT Presentation",
        slides_content=sample_slides,
        output_file="sample_output.pptx"
    )
    
    print("Sample presentation test completed!\n")


if __name__ == "__main__":
    print("=" * 60)
    print("YouTube to PPT Converter - Example/Test Script")
    print("=" * 60)
    print()
    
    # Run tests
    test_url_extraction()
    test_transcript_grouping()
    create_sample_presentation()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
    print("\nTo use with a real YouTube video, run: python youtube_to_ppt.py")
