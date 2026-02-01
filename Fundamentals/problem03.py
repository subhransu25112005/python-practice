import os

# Specify the directory path (current directory in this case)
directory_path = "."

# Get list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)