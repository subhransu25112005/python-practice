class SecureFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("🔒 File locked")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("🔓 File unlocked")

        if exc_type:
            print("❌ Error occurred. Changes not saved.")
        else:
            print("✅ File updated successfully")

        # False means exception (if any) will propagate
        return False

print("\n--- Secure File Update System ---\n")

try:
    with SecureFileManager("data.txt", "a") as file:
        text = input("Enter text to save securely: ")
        file.write(text + "\n")

except Exception as e:
    print("Exception:", e)
