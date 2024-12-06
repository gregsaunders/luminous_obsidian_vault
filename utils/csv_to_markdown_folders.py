import csv
import os

INPUT_CSV = "work_items.csv"  # Change to your CSV file name
BASE_DIR = "."  # Base directory from where we create folders

with open(INPUT_CSV, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        path = row["path"].strip()
        filename = row["filename"].strip()
        front_matter = row["front_matter"].strip()
        body = row["body"]

        # Create the directory if it doesn't exist
        dir_path = os.path.join(BASE_DIR, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Construct the markdown content
        # Front matter should be wrapped with ---
        # If front_matter is empty, we still do a front matter block
        # If front_matter is not empty, it likely already contains key: value lines.
        md_content_lines = ["---"]
        if front_matter:
            md_content_lines.extend(front_matter.split("\n"))
        md_content_lines.append("---")
        md_content_lines.append("")
        md_content_lines.append(body.strip())
        md_content = "\n".join(md_content_lines) + "\n"

        # Write the markdown file
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

print("Markdown files and directories created successfully.")
