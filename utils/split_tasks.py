import os
import re
import sys

def parse_front_matter(lines):
    fm = {}
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                key, val = parts
                fm[key.strip()] = val.strip()
    return fm

def sanitize_filename(title):
    # Remove surrounding quotes if present
    if title.startswith('"') and title.endswith('"'):
        title = title[1:-1]
    # Replace forward slashes with a space
    title = title.replace('/', ' ')
    # You can add more rules here if needed
    return title

# Get filename from command line or default
input_file = "combined_tasks.md"
if len(sys.argv) > 1:
    input_file = sys.argv[1]

if not os.path.exists(input_file):
    print(f"Error: {input_file} does not exist.")
    sys.exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read().strip()

# Split on "\n---\n"
blocks = content.split("\n---\n")

if len(blocks) % 2 != 0:
    print("Error: Unexpected format. The combined file should have pairs of front matter and content blocks.")
    sys.exit(1)

output_dir = "output_tasks"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

task_count = 0
for i in range(0, len(blocks), 2):
    front_matter_block = blocks[i].strip()
    content_block = blocks[i+1].strip()

    fm_lines = front_matter_block.split('\n')
    fm = parse_front_matter(fm_lines)

    title = fm.pop('title', None)
    if not title:
        print(f"Error: No title found in front matter block starting at index {i}.")
        sys.exit(1)

    # Sanitize title
    filename_title = sanitize_filename(title)
    filename = filename_title + ".md"
    
    # Rebuild front matter without title
    output_lines = ["---"]
    for k, v in fm.items():
        output_lines.append(f"{k}: {v}")
    output_lines.append("---")
    output_lines.append(content_block)
    output_content = "\n".join(output_lines) + "\n"

    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as out_f:
        out_f.write(output_content)
    task_count += 1

print(f"Successfully split {task_count} tasks into the '{output_dir}' directory.")
