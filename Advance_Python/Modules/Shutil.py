'''📦 “Smart Backup & Deployment Utility”

This ONE program demonstrates:

Copy file

Copy directory

Move file

Delete directory

Create ZIP archive

Extract archive

Check disk usage

All inside one structured workflow.'''

from pathlib import Path
import shutil
import datetime

print("\n===== SMART BACKUP & DEPLOYMENT SYSTEM =====\n")

# -------------------------------------------------
# 1️⃣ Setup Source Project Folder
# -------------------------------------------------
base_dir = Path.cwd()
source = base_dir / "source_project"
backup_root = base_dir / "backups"

source.mkdir(exist_ok=True)
backup_root.mkdir(exist_ok=True)

# Create sample files
(source / "app.py").write_text("print('Hello World')", encoding="utf-8")
(source / "config.json").write_text('{"env": "dev"}', encoding="utf-8")

print("Source project prepared.\n")

# -------------------------------------------------
# 2️⃣ Copy Entire Project (Backup)
# -------------------------------------------------
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = backup_root / f"backup_{timestamp}"

shutil.copytree(source, backup_folder)

print(f"Backup created at: {backup_folder}")

# -------------------------------------------------
# 3️⃣ Copy Single File
# -------------------------------------------------
copied_file = backup_folder / "app_copy.py"
shutil.copy(source / "app.py", copied_file)

print("Single file copied as app_copy.py")

# -------------------------------------------------
# 4️⃣ Move File
# -------------------------------------------------
moved_file = backup_folder / "moved_config.json"
shutil.move(str(source / "config.json"), str(moved_file))

print("config.json moved to backup folder")

# -------------------------------------------------
# 5️⃣ Disk Usage
# -------------------------------------------------
total, used, free = shutil.disk_usage(base_dir)

print("\nDisk Usage Info:")
print(f"Total: {total // (1024**3)} GB")
print(f"Used:  {used // (1024**3)} GB")
print(f"Free:  {free // (1024**3)} GB")

# -------------------------------------------------
# 6️⃣ Create ZIP Archive
# -------------------------------------------------
archive_path = shutil.make_archive(
    base_name=str(backup_folder),
    format="zip",
    root_dir=backup_folder
)

print(f"\nZIP archive created: {archive_path}")

# -------------------------------------------------
# 7️⃣ Extract ZIP Archive
# -------------------------------------------------
extract_folder = backup_root / "extracted_backup"
extract_folder.mkdir(exist_ok=True)

shutil.unpack_archive(archive_path, extract_folder)

print("Archive extracted to:", extract_folder)

# -------------------------------------------------
# 8️⃣ Delete Directory Completely
# -------------------------------------------------
shutil.rmtree(source)
print("Original source_project deleted.")

print("\n===== OPERATION COMPLETED SUCCESSFULLY =====")
