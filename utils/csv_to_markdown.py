import csv
import os

INPUT_CSV = "tasks.csv"  # Update if your CSV file has a different name
OUTPUT_DIR = "from_csv_output"

# Create output directory if not exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open(INPUT_CSV, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract fields
        filename = row.get("filename", "Untitled.md")
        work_item_id = row.get("work_item_id", "")
        due_date = row.get("due_date", "")
        responsible = row.get("responsible", "")
        accountable = row.get("accountable", "")
        consulted = row.get("consulted", "")
        informed = row.get("informed", "")
        task = row.get("task", "")
        details = row.get("details", "")

        # Build front matter
        front_matter = [
            "---",
            f"work_item_id: {work_item_id}",
            f"due date: {due_date}",
            f"responsible: {responsible}",
            f"accountable: {accountable}",
            f"consulted: {consulted}",
            f"informed: {informed}",
            "---"
        ]

        # Build content
        # We use the same format as before:
        # **Task:** {task}
        # **Details:**
        # {details lines...}

        # Details are currently in one line. If you want to restore bullet points:
        # The CSV seems to have details separated by " - ". We can split on " - " and reformat.
        # If the details already contain bullet points, we can leave as-is.
        # Let's leave as-is for now since the CSV already has bullet formatting.

        content_lines = [
            "**Task:** " + task,
            "**Details:**",
            details
        ]

        output_content = "\n".join(front_matter) + "\n\n" + "\n".join(content_lines) + "\n"

        # Write to file
        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_content)

print(f"Markdown files created in '{OUTPUT_DIR}' directory.")
