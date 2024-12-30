import re
import sys
from pathlib import Path

def extract_speaker_and_text(line):
    """Extract speaker name and text from a line with <v> tags."""
    speaker_pattern = r'<v ([^>]+)>(.+)</v>'
    match = re.match(speaker_pattern, line.strip())
    if match:
        return match.group(1), match.group(2)
    return None, line

def convert_vtt_to_markdown(vtt_file_path, output_file_path=None):
    """
    Convert a VTT file to a markdown file, combining consecutive segments from the same speaker.
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
    current_speaker = None
    current_segments = []
    current_timestamp = None
    
    for line in content:
        line = line.strip()
        
        # Skip empty lines, WEBVTT header, and identifier lines with UUIDs
        if not line or line == 'WEBVTT' or (line and '/' in line and '-' in line):
            continue
        
        # Handle timestamp lines
        if '-->' in line:
            current_timestamp = line.split(' --> ')[0]
            continue
        
        # Process text with speaker tags
        if '<v ' in line and '</v>' in line:
            speaker, text = extract_speaker_and_text(line)
            
            # If we have a new speaker, save the previous speaker's combined text
            if current_speaker and speaker != current_speaker and current_segments:
                combined_text = ' '.join(segment[1] for segment in current_segments)
                markdown_lines.append(f"[{current_segments[0][0]}] **{current_speaker}:** {combined_text}")
                current_segments = []
            
            current_speaker = speaker
            current_segments.append((current_timestamp, text))

    # Add the final speaker's text
    if current_speaker and current_segments:
        combined_text = ' '.join(segment[1] for segment in current_segments)
        markdown_lines.append(f"[{current_segments[0][0]}] **{current_speaker}:** {combined_text}")

    # Create markdown content with line breaks between speakers
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