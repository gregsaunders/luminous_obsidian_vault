import os
import csv

INPUT_DIR = "."
OUTPUT_CSV = "tasks.csv"

def parse_front_matter(lines):
    """
    Given a list of lines representing the front matter block,
    return a dictionary of the attributes found.
    """
    fm = {}
    for line in lines:
        line = line.strip()
        if line and ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm

def extract_task_details(content_lines):
    """
    Given the content lines (after front matter), 
    attempt to extract the task and details sections.
    
    We assume the body looks like:
    **Task:** Some task title
    (blank lines or other formatting)
    **Details:**
    - line 1
    - line 2
    etc.
    """
    task_line = ""
    details_lines = []
    in_details = False

    for line in content_lines:
        striped = line.strip()
        if striped.startswith("**Task:**"):
            # Extract everything after "**Task:**"
            task_line = striped.replace("**Task:**", "").strip()
        elif striped.startswith("**Details:**"):
            # Switch to details mode
            in_details = True
        else:
            if in_details:
                # Accumulate detail lines
                details_lines.append(striped)

    details = " ".join(details_lines)
    return task_line, details

# Prepare CSV
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "work_item_id", "due_date", "assignee", "task", "details"])

    # Iterate over all md files in INPUT_DIR
    for fname in os.listdir(INPUT_DIR):
        if fname.endswith(".md"):
            filepath = os.path.join(INPUT_DIR, fname)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Parse the file
            # Front matter is between the first pair of "---"
            # Find first "---"
            # The file format should start with '---', front matter, then '---'
            # Then the content
            if len(lines) < 3:
                # Not a valid file format
                continue
            
            # Identify front matter boundaries
            # First line should be '---'
            # Find the second '---'
            fm_start = None
            fm_end = None
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    if fm_start is None:
                        fm_start = i
                    else:
                        fm_end = i
                        break
            
            if fm_start is None or fm_end is None or fm_end <= fm_start:
                # No valid front matter
                continue

            front_matter_lines = lines[fm_start+1:fm_end]
            fm = parse_front_matter(front_matter_lines)

            content_lines = lines[fm_end+1:]
            # Extract task and details
            task, details = extract_task_details(content_lines)

            work_item_id = fm.get("work_item_id", "")
            due_date = fm.get("due date", "")
            assignee = fm.get("assignee", "")

            writer.writerow([fname, work_item_id, due_date, assignee, task, details])

print(f"Created {OUTPUT_CSV} with combined task data.")
