import os

def show_menu():
    print("\n===== CLI FILE MANAGER =====")
    print("1. Show Current Directory")
    print("2. List Files")
    print("3. Create Folder")
    print("4. Create File")
    print("5. Read File")
    print("6. Rename File/Folder")
    print("7. Delete File/Folder")
    print("8. Search File")
    print("9. Change Directory")
    print("10. Show Environment Variable")
    print("0. Exit")


def show_current_directory():
    print("Current Directory:", os.getcwd())


def list_files():
    files = os.listdir()
    print("\nFiles & Folders:")
    for file in files:
        print("-", file)


def create_folder():
    name = input("Enter folder name: ")
    try:
        os.mkdir(name)
        print("Folder created successfully.")
    except Exception as e:
        print("Error:", e)


def create_file():
    name = input("Enter file name: ")
    with open(name, "w") as f:
        content = input("Enter content: ")
        f.write(content)
    print("File created successfully.")


def read_file():
    name = input("Enter file name: ")
    if os.path.exists(name):
        with open(name, "r") as f:
            print("\nFile Content:\n")
            print(f.read())
    else:
        print("File does not exist.")


def rename_item():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    try:
        os.rename(old_name, new_name)
        print("Renamed successfully.")
    except Exception as e:
        print("Error:", e)


def delete_item():
    name = input("Enter file/folder name to delete: ")
    if os.path.isfile(name):
        os.remove(name)
        print("File deleted.")
    elif os.path.isdir(name):
        os.rmdir(name)
        print("Folder deleted (must be empty).")
    else:
        print("Item not found.")


def search_file():
    target = input("Enter file name to search: ")
    for root, dirs, files in os.walk(os.getcwd()):
        if target in files:
            print("Found at:", os.path.join(root, target))
            return
    print("File not found.")


def change_directory():
    path = input("Enter directory path: ")
    try:
        os.chdir(path)
        print("Directory changed successfully.")
    except Exception as e:
        print("Error:", e)


def show_env_variable():
    key = input("Enter environment variable name (e.g., PATH): ")
    value = os.environ.get(key)
    if value:
        print(f"{key} = {value[:100]}...")
    else:
        print("Environment variable not found.")


# Main loop
while True:
    show_menu()
    choice = input("Select option: ")

    if choice == "1":
        show_current_directory()
    elif choice == "2":
        list_files()
    elif choice == "3":
        create_folder()
    elif choice == "4":
        create_file()
    elif choice == "5":
        read_file()
    elif choice == "6":
        rename_item()
    elif choice == "7":
        delete_item()
    elif choice == "8":
        search_file()
    elif choice == "9":
        change_directory()
    elif choice == "10":
        show_env_variable()
    elif choice == "0":
        print("Exiting File Manager...")
        break
    else:
        print("Invalid choice.")
