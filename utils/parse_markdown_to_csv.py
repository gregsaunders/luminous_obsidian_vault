import os
import csv

output_file = "output.csv"

def parse_markdown_file(filepath):
    """
    Parse a markdown file to extract front matter and body.
    Returns front_matter (list of lines), body (list of lines).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Identify front matter
    front_matter = []
    body = []
    fm_start = None
    fm_end = None

    for i, line in enumerate(lines):
        if line.strip() == "---":
            if fm_start is None:
                fm_start = i
            elif fm_end is None:
                fm_end = i
                break

    if fm_start is not None and fm_end is not None and fm_end > fm_start:
        front_matter = lines[fm_start+1:fm_end]
        body = lines[fm_end+1:]
    else:
        # No valid front matter found, treat entire file as body
        front_matter = []
        body = lines

    # Strip trailing newlines
    front_matter = [l.rstrip('\n') for l in front_matter]
    body = [l.rstrip('\n') for l in body]

    return front_matter, body


def format_body(body_lines):
    """
    Format the body:
    - After **Task:** add a blank line, then the task text on its own line, then another blank line.
    - After **Details:** add a blank line, then split bullets onto their own lines, each starting with "- ".
    """
    formatted = []
    i = 0
    while i < len(body_lines):
        line = body_lines[i].strip()

        if line.startswith("**Task:**"):
            # Extract the task description after **Task:**
            task_text = line.replace("**Task:**", "").strip()
            # Format as requested:
            # **Task:**
            #
            # [task_text]
            #
            formatted.append("**Task:**")
            formatted.append("")  # blank line after **Task:**
            if task_text:
                formatted.append(task_text)
            formatted.append("")  # another blank line after the task text
            i += 1
        elif line.startswith("**Details:**"):
            # **Details:**
            #
            # - bullet1
            # - bullet2
            #
            formatted.append("**Details:**")
            formatted.append("")  # blank line after **Details:**
            i += 1
            if i < len(body_lines):
                details_line = body_lines[i].strip()
                if details_line:
                    details_parts = details_line.split(" - ")
                    for part in details_parts:
                        part = part.strip()
                        if not part.startswith('-'):
                            part = "- " + part
                        formatted.append(part)
                i += 1
            else:
                i += 1
        else:
            # Normal line
            formatted.append(line)
            i += 1

    return "\n".join(formatted)


# Collect all files recursively
all_files = []
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".md"):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, ".")
            dir_path = os.path.dirname(rel_path)
            if dir_path == "":
                dir_path = "."
            all_files.append((dir_path, f, full_path))

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["path", "filename", "front_matter", "body"])

    for dir_path, filename, full_path in all_files:
        front_matter, body = parse_markdown_file(full_path)
        formatted_body = format_body(body)

        # Join front matter lines into a single string
        fm_str = "\n".join(front_matter)

        writer.writerow([dir_path, filename, fm_str, formatted_body])

print(f"Created {output_file} with parsed file data.")
