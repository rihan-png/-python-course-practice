#!/usr/bin/env python3
"""
Example usage of YouTube to PPT Converter
==========================================
This script demonstrates how to use the YouTubeToPPTConverter class
in your own Python programs.
"""

from youtube_to_ppt import YouTubeToPPTConverter


def example_basic_usage():
    """Example: Basic usage with a YouTube URL."""
    print("Example 1: Basic Usage")
    print("-" * 40)
    
    # Replace with any YouTube video URL
    video_url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"  # Python tutorial
    
    # Create converter instance
    converter = YouTubeToPPTConverter(video_url)
    
    # Generate presentation
    output_file = converter.generate_presentation("python_tutorial.pptx")
    
    print(f"Created: {output_file}")
    print()


def example_custom_processing():
    """Example: Custom processing with access to video info and transcript."""
    print("Example 2: Custom Processing")
    print("-" * 40)
    
    video_url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"
    converter = YouTubeToPPTConverter(video_url)
    
    # Fetch video info first
    info = converter.fetch_video_info()
    print(f"Video Title: {info['title']}")
    print(f"Author: {info['author']}")
    print(f"Duration: {info['length']} seconds")
    print()
    
    # Fetch transcript
    transcript = converter.fetch_transcript()
    if transcript:
        print(f"Transcript entries: {len(transcript)}")
        print(f"First entry: {transcript[0]['text'][:100]}...")
    print()
    
    # Generate presentation
    converter.generate_presentation("custom_presentation.pptx")
    print()


def example_video_id_usage():
    """Example: Using just the video ID instead of full URL."""
    print("Example 3: Using Video ID")
    print("-" * 40)
    
    # You can use just the video ID (the part after ?v= in YouTube URLs)
    video_id = "kqtD5dpn9C8"
    
    converter = YouTubeToPPTConverter(video_id)
    converter.generate_presentation("from_video_id.pptx")
    print()


def main():
    """Run all examples."""
    print("=" * 60)
    print("YouTube to PPT Converter - Examples")
    print("=" * 60)
    print()
    
    print("Note: These examples use sample video URLs.")
    print("Replace with your own video URLs to test.")
    print()
    
    # Uncomment the examples you want to run:
    
    # example_basic_usage()
    # example_custom_processing()
    # example_video_id_usage()
    
    print("To run examples, uncomment them in the main() function.")


if __name__ == "__main__":
    main()
