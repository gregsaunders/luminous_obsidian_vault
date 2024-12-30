from docx.api import Document
import re
import os

def convert_paragraph_to_markdown(paragraph):
    """Convert a paragraph to markdown format."""
    text = paragraph.text.strip()
    
    # Skip empty paragraphs
    if not text:
        return ""
        
    # Handle different styles
    style_name = paragraph.style.name if paragraph.style and hasattr(paragraph.style, 'name') else ''
    
    if style_name.startswith('Heading 1'):
        return f"# {text}\n"
    elif style_name.startswith('Heading 2'):
        return f"## {text}\n"
    elif style_name.startswith('Heading 3'):
        return f"### {text}\n"
    elif style_name.startswith('List Paragraph'):
        # Check if it's a numbered list
        if re.match(r'^\d+\.', text):
            return f"{text}\n"
        return f"- {text}\n"
    
    # Handle bold and italic text
    markdown_text = text
    for run in paragraph.runs:
        if run.bold:
            markdown_text = markdown_text.replace(run.text, f"**{run.text}**")
        if run.italic:
            markdown_text = markdown_text.replace(run.text, f"*{run.text}*")
    
    return f"{markdown_text}\n"

def docx_to_markdown(input_file, output_file=None):
    """
    Convert a Word document to Markdown format.
    
    Args:
        input_file (str): Path to the input .docx file
        output_file (str, optional): Path to the output markdown file. 
                                   If not provided, will use the same name as input with .md extension
    
    Returns:
        str: Path to the created markdown file
    """
    if not input_file.endswith('.docx'):
        raise ValueError("Input file must be a .docx file")
    
    # Generate output filename if not provided
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.md'
    
    # Read the Word document
    doc = Document(input_file)
    
    # Convert to markdown
    markdown_content = []
    
    for paragraph in doc.paragraphs:
        markdown_content.append(convert_paragraph_to_markdown(paragraph))
    
    # Write to markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    return output_file

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert Word documents to Markdown format')
    parser.add_argument('input_file', help='Path to the input .docx file')
    parser.add_argument('--output', '-o', help='Path to the output markdown file (optional)')
    
    args = parser.parse_args()
    
    try:
        output_path = docx_to_markdown(args.input_file, args.output)
        print(f"Successfully converted {args.input_file} to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}") 
