from pathlib import Path
import time

print("\n===== MODERN FILE MANAGER USING PATHLIB =====\n")

# -------------------------------------------------
# 1️⃣ Current Working Directory
# -------------------------------------------------
cwd = Path.cwd()
print("Current Working Directory:", cwd)

# -------------------------------------------------
# 2️⃣ Create Project Directory
# -------------------------------------------------
project = cwd / "modern_project"

if not project.exists():
    project.mkdir()
    print("Created folder:", project)
else:
    print("Folder already exists:", project)

# -------------------------------------------------
# 3️⃣ Create Subdirectories
# -------------------------------------------------
data_dir = project / "data"
logs_dir = project / "logs"

data_dir.mkdir(exist_ok=True)
logs_dir.mkdir(exist_ok=True)

print("Created subfolders: data & logs")

# -------------------------------------------------
# 4️⃣ Create and Write File
# -------------------------------------------------
file_path = data_dir / "info.txt"

file_path.write_text("Project: Pathlib Learning\nCreated: " + time.ctime())

print("File created:", file_path)

# -------------------------------------------------
# 5️⃣ Read File
# -------------------------------------------------
content = file_path.read_text()
print("\nFile Content:\n", content)

# -------------------------------------------------
# 6️⃣ File Metadata
# -------------------------------------------------
stats = file_path.stat()

print("\nFile Size:", stats.st_size, "bytes")
print("Last Modified:", time.ctime(stats.st_mtime))

# -------------------------------------------------
# 7️⃣ Rename File
# -------------------------------------------------
new_file = data_dir / "project_info.txt"
file_path.rename(new_file)

print("File renamed to:", new_file.name)

# -------------------------------------------------
# 8️⃣ List Directory Contents
# -------------------------------------------------
print("\nFiles in data directory:")
for item in data_dir.iterdir():
    print("-", item.name)

# -------------------------------------------------
# 9️⃣ Recursive Search
# -------------------------------------------------
print("\nSearching for .txt files recursively:")
for file in project.rglob("*.txt"):
    print("Found:", file)

# -------------------------------------------------
# 🔟 File Type Checking
# -------------------------------------------------
if new_file.is_file():
    print("\nConfirmed:", new_file.name, "is a file")

if data_dir.is_dir():
    print("Confirmed:", data_dir.name, "is a directory")

# -------------------------------------------------
# 1️⃣1️⃣ Parent Directory
# -------------------------------------------------
print("\nParent of data directory:", data_dir.parent)

# -------------------------------------------------
# 1️⃣2️⃣ Absolute Path
# -------------------------------------------------
print("Absolute Path:", new_file.resolve())

# -------------------------------------------------
# 1️⃣3️⃣ Delete File
# -------------------------------------------------
new_file.unlink()
print("Deleted file:", new_file.name)

# -------------------------------------------------
# 1️⃣4️⃣ Remove Directories
# -------------------------------------------------
data_dir.rmdir()
logs_dir.rmdir()
project.rmdir()

print("Cleaned up project directories")

print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")
