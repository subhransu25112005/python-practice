'''🗂 “Project Auto Organizer System”
🎯 Problem Statement (Real Scenario)

Suppose you download many files:

.pdf

.jpg

.png

.txt

.py

.csv

All go into one folder like:

Downloads/
    report.pdf
    image.png
    notes.txt
    data.csv
    script.py


You want:

Automatically create folders

Move files into categorized directories

Create logs folder

Maintain structure safely

✅ What This Program Does

✔ Scans a directory
✔ Creates categorized folders
✔ Moves files based on extension
✔ Creates log file
✔ Uses only pathlib (modern way)'''

from pathlib import Path
import shutil
import datetime

print("\n===== AUTO FILE ORGANIZER SYSTEM =====\n")

# -------------------------------------------------
# 1️⃣ Define Target Directory
# -------------------------------------------------
base_dir = Path.cwd() / "downloads_simulation"
base_dir.mkdir(exist_ok=True)

# -------------------------------------------------
# 2️⃣ Create Sample Files (Simulation)
# -------------------------------------------------
sample_files = [
    "report.pdf",
    "image.jpg",
    "notes.txt",
    "data.csv",
    "script.py"
]

for file in sample_files:
    file_path = base_dir / file
    file_path.write_text("Sample content", encoding="utf-8")

print("Sample files created.\n")

# -------------------------------------------------
# 3️⃣ Define Extension Categories
# -------------------------------------------------
categories = {
    "Documents": [".pdf", ".txt", ".csv"],
    "Images": [".jpg", ".png"],
    "Code": [".py"]
}

# -------------------------------------------------
# 4️⃣ Organize Files
# -------------------------------------------------
log_file = base_dir / "organizer_log.txt"

with log_file.open("w", encoding="utf-8") as log:

    log.write(f"Organizer Run: {datetime.datetime.now()}\n\n")

    for file in base_dir.iterdir():

        if file.is_file() and file.name != "organizer_log.txt":

            moved = False

            for folder, extensions in categories.items():

                if file.suffix.lower() in extensions:

                    target_folder = base_dir / folder
                    target_folder.mkdir(exist_ok=True)

                    new_path = target_folder / file.name
                    shutil.move(str(file), str(new_path))

                    log.write(f"Moved {file.name} -> {folder}\n")
                    print(f"Moved {file.name} -> {folder}")

                    moved = True
                    break

            if not moved:
                others = base_dir / "Others"
                others.mkdir(exist_ok=True)

                new_path = others / file.name
                shutil.move(str(file), str(new_path))

                log.write(f"Moved {file.name} -> Others\n")
                print(f"Moved {file.name} -> Others")

print("\nFile organization completed successfully.")
