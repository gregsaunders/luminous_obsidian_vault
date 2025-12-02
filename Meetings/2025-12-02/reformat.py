import re
import os

input_path = "2025-12-02 Jeff Shawn Greg transcript.md"
output_path = "2025-12-02 Jeff Shawn Greg transcript_reformatted.md"

def reformat_transcript(text):
    # Split into sentences (naive split on .!? followed by space or end of string)
    # We use a lookbehind to keep the punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    paragraphs = []
    current_paragraph = []
    current_length = 0
    
    for sentence in sentences:
        current_paragraph.append(sentence)
        current_length += len(sentence)
        
        # Heuristic: Break if paragraph is long enough
        if current_length > 500:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []
            current_length = 0
            
    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))
        
    return "\n\n".join(paragraphs)

def main():
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove existing newlines if any (treat as one block) to ensure clean reformatting
    # But user said "do not alter the text". 
    # If the original has newlines, we should probably respect them or treat them as spaces?
    # The view_file showed it as line 1. So it's likely one line.
    # But just in case, let's replace single newlines with spaces, but keep double newlines?
    # Actually, let's just treat it as a stream.
    content_stream = content.replace('\n', ' ')
    
    reformatted = reformat_transcript(content_stream)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(reformatted)
        
    print(f"Reformatted text written to {output_path}")

if __name__ == "__main__":
    main()
