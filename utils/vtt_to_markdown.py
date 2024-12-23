import re
import sys
from pathlib import Path

def clean_timestamp_line(line):
    """Remove timestamp lines from the VTT content."""
    timestamp_pattern = r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}'
    return bool(re.match(timestamp_pattern, line.strip()))

def convert_vtt_to_markdown(vtt_file_path, output_file_path=None):
    """
    Convert a VTT file to a markdown file.
    
    Args:
        vtt_file_path (str): Path to the input VTT file
        output_file_path (str, optional): Path for the output markdown file.
            If not provided, will create a .md file in the same location as the VTT file.
    """
    try:
        with open(vtt_file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"Error: Could not find VTT file at {vtt_file_path}")
        return
    except Exception as e:
        print(f"Error reading VTT file: {str(e)}")
        return

    # Remove the WebVTT header
    if content and "WEBVTT" in content[0]:
        content = content[1:]

    # Process the content
    markdown_lines = []
    current_paragraph = []
    
    for line in content:
        line = line.strip()
        
        # Skip empty lines and timestamp lines
        if not line or clean_timestamp_line(line) or line.isdigit():
            if current_paragraph:
                markdown_lines.append(' '.join(current_paragraph))
                current_paragraph = []
            continue
        
        current_paragraph.append(line)
    
    # Add the last paragraph if exists
    if current_paragraph:
        markdown_lines.append(' '.join(current_paragraph))

    # Create markdown content with paragraphs
    markdown_content = '\n\n'.join(markdown_lines)

    # Determine output file path
    if output_file_path is None:
        output_file_path = str(Path(vtt_file_path).with_suffix('.md'))

    # Write the markdown file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        print(f"Successfully converted {vtt_file_path} to {output_file_path}")
    except Exception as e:
        print(f"Error writing markdown file: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python vtt_to_markdown.py <vtt_file_path> [output_file_path]")
        sys.exit(1)

    vtt_file_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_vtt_to_markdown(vtt_file_path, output_file_path)

if __name__ == "__main__":
    main() 