import os
import time

print("\n===== MINI FILE MANAGEMENT SYSTEM USING OS MODULE =====\n")

# -------------------------------------------------
# 1️⃣ Current Working Directory
# -------------------------------------------------
print("Current Working Directory:")
print(os.getcwd())

# -------------------------------------------------
# 2️⃣ Create a Main Project Directory
# -------------------------------------------------
project_dir = "my_project"

if not os.path.exists(project_dir):
    os.mkdir(project_dir)
    print(f"\nCreated directory: {project_dir}")
else:
    print(f"\nDirectory '{project_dir}' already exists")

# -------------------------------------------------
# 3️⃣ Change Directory into Project
# -------------------------------------------------
os.chdir(project_dir)
print("\nChanged directory to:", os.getcwd())

# -------------------------------------------------
# 4️⃣ Create Subdirectories
# -------------------------------------------------
os.makedirs("data/logs", exist_ok=True)
print("Created subdirectories: data/logs")

# -------------------------------------------------
# 5️⃣ Create and Write a File
# -------------------------------------------------
file_path = os.path.join("data", "info.txt")

with open(file_path, "w") as f:
    f.write("Project Name: OS Learning\n")
    f.write("Created At: " + time.ctime() + "\n")

print("Created and wrote to file:", file_path)

# -------------------------------------------------
# 6️⃣ Read File
# -------------------------------------------------
with open(file_path, "r") as f:
    content = f.read()

print("\nFile Content:")
print(content)

# -------------------------------------------------
# 7️⃣ Rename File
# -------------------------------------------------
new_file_path = os.path.join("data", "project_info.txt")
os.rename(file_path, new_file_path)
print("Renamed file to:", new_file_path)

# -------------------------------------------------
# 8️⃣ File Metadata
# -------------------------------------------------
stats = os.stat(new_file_path)
print("\nFile Size:", stats.st_size, "bytes")
print("Last Modified:", time.ctime(stats.st_mtime))

# -------------------------------------------------
# 9️⃣ List Directory Contents
# -------------------------------------------------
print("\nDirectory Contents:")
print(os.listdir("data"))

# -------------------------------------------------
# 🔟 Walk Through Directory Tree
# -------------------------------------------------
print("\nWalking through directory structure:")
for root, dirs, files in os.walk("."):
    print(f"\nCurrent Path: {root}")
    print("Folders:", dirs)
    print("Files:", files)

# -------------------------------------------------
# 1️⃣1️⃣ Environment Variables
# -------------------------------------------------
print("\nEnvironment Variable Example:")
print("PATH:", os.environ.get("PATH")[:100], "...")  # partial print

# Set custom environment variable
os.environ["PROJECT_MODE"] = "Development"
print("Custom Env Variable:", os.environ.get("PROJECT_MODE"))

# -------------------------------------------------
# 1️⃣2️⃣ Change File Permission (Unix Only)
# -------------------------------------------------
try:
    os.chmod(new_file_path, 0o644)
    print("Changed file permissions to 644")
except Exception as e:
    print("Permission change not supported on this OS")

# -------------------------------------------------
# 1️⃣3️⃣ Remove File
# -------------------------------------------------
os.remove(new_file_path)
print("Deleted file:", new_file_path)

# -------------------------------------------------
# 1️⃣4️⃣ Remove Empty Directories
# -------------------------------------------------
os.rmdir("data/logs")
os.rmdir("data")
print("Removed subdirectories")

# Go back to parent directory
os.chdir("..")

# Remove main project directory
os.rmdir(project_dir)
print("Removed main project directory")

print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")
