'''A backend service needs to:

Read config from environment variable

Monitor incoming files

Organize them

Backup them

Log operations

Clean old backups

Check disk space'''

import os
import shutil
from pathlib import Path
from datetime import datetime

print("\n===== ENTERPRISE FILE LIFECYCLE MANAGER =====\n")

# -------------------------------------------------
# 1️⃣ Load Configuration (Environment Variable)
# -------------------------------------------------
BASE_STORAGE = os.getenv("FILE_STORAGE_DIR", "enterprise_storage")
base_dir = Path.cwd() / BASE_STORAGE

incoming_dir = base_dir / "incoming"
organized_dir = base_dir / "organized"
backup_dir = base_dir / "backups"
log_dir = base_dir / "logs"

# Create directory structure
for folder in [incoming_dir, organized_dir, backup_dir, log_dir]:
    folder.mkdir(parents=True, exist_ok=True)

print("Directory structure initialized.\n")

# -------------------------------------------------
# 2️⃣ Create Sample Incoming Files (Simulation)
# -------------------------------------------------
sample_files = ["report.pdf", "image.png", "data.csv", "script.py"]

for file in sample_files:
    (incoming_dir / file).write_text("Sample content", encoding="utf-8")

print("Sample incoming files created.\n")

# -------------------------------------------------
# 3️⃣ File Categorization Rules
# -------------------------------------------------
categories = {
    "Documents": [".pdf", ".csv"],
    "Images": [".png", ".jpg"],
    "Code": [".py"]
}

# -------------------------------------------------
# 4️⃣ Logging System
# -------------------------------------------------
log_file = log_dir / "system_log.txt"

with log_file.open("a", encoding="utf-8") as log:

    log.write(f"\nRun started at {datetime.now()}\n")

    # -------------------------------------------------
    # 5️⃣ Organize Incoming Files
    # -------------------------------------------------
    for file in incoming_dir.iterdir():

        if file.is_file():
            moved = False

            for folder, extensions in categories.items():
                if file.suffix.lower() in extensions:
                    target = organized_dir / folder
                    target.mkdir(exist_ok=True)

                    new_path = target / file.name
                    shutil.move(str(file), str(new_path))

                    log.write(f"Moved {file.name} -> {folder}\n")
                    print(f"Moved {file.name} -> {folder}")

                    moved = True
                    break

            if not moved:
                others = organized_dir / "Others"
                others.mkdir(exist_ok=True)

                new_path = others / file.name
                shutil.move(str(file), str(new_path))

                log.write(f"Moved {file.name} -> Others\n")
                print(f"Moved {file.name} -> Others")

    # -------------------------------------------------
    # 6️⃣ Backup Organized Folder
    # -------------------------------------------------
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"backup_{timestamp}"

    shutil.copytree(organized_dir, backup_path)

    log.write(f"Backup created at {backup_path}\n")
    print("\nBackup created successfully.")

    # -------------------------------------------------
    # 7️⃣ Disk Usage Monitoring
    # -------------------------------------------------
    total, used, free = shutil.disk_usage(base_dir)

    log.write(f"Disk Usage - Free: {free // (1024**2)} MB\n")
    print(f"\nFree Disk Space: {free // (1024**2)} MB")

    # -------------------------------------------------
    # 8️⃣ Cleanup Old Backups (Keep Latest 3)
    # -------------------------------------------------
    backups = sorted(backup_dir.iterdir(), key=os.path.getmtime)

    if len(backups) > 3:
        for old_backup in backups[:-3]:
            shutil.rmtree(old_backup)
            log.write(f"Deleted old backup: {old_backup.name}\n")
            print(f"Deleted old backup: {old_backup.name}")

    log.write("Run completed.\n")

print("\n===== SYSTEM EXECUTION COMPLETE =====")
