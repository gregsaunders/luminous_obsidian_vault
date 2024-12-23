import re
import sys
from pathlib import Path

def extract_speaker_and_text(line):
    """Extract speaker name and text from a line with <v> tags."""
    speaker_pattern = r'<v ([^>]+)>(.+)</v>'
    match = re.match(speaker_pattern, line)
    if match:
        return match.group(1), match.group(2)
    return None, line

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

    # Process the content
    markdown_lines = []
    current_timestamp = None
    current_speaker = None
    current_text = []
    
    for line in content:
        line = line.strip()
        
        # Skip empty lines, WEBVTT header, and identifier lines
        if not line or line == 'WEBVTT' or '/' in line:
            continue
        
        # Store timestamp
        if '-->' in line:
            if not current_timestamp:
                current_timestamp = line.split(' --> ')[0]
            continue
        
        # Process text with speaker tags
        speaker, text = extract_speaker_and_text(line)
        if speaker and text:
            # If we have a new speaker, save the previous content
            if current_speaker and speaker != current_speaker:
                if current_text:
                    markdown_lines.append(f"[{current_timestamp}] **{current_speaker}:** {' '.join(current_text)}")
                current_text = []
                current_timestamp = None
            
            current_speaker = speaker
            current_text.append(text)
        elif line:  # Handle lines without speaker tags
            current_text.append(line)
    
    # Add the final block
    if current_speaker and current_text:
        markdown_lines.append(f"[{current_timestamp}] **{current_speaker}:** {' '.join(current_text)}")

    # Create markdown content with line breaks
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