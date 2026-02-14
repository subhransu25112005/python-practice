import json
import hashlib
from pathlib import Path

DB_FILE = Path("users.json")


# -------------------------------------------------
# 1️⃣ Load Database
# -------------------------------------------------
def load_users():
    if DB_FILE.exists():
        return json.loads(DB_FILE.read_text(encoding="utf-8"))
    return {}


# -------------------------------------------------
# 2️⃣ Save Database
# -------------------------------------------------
def save_users(users):
    DB_FILE.write_text(json.dumps(users, indent=4), encoding="utf-8")


# -------------------------------------------------
# 3️⃣ Hash Password (Security)
# -------------------------------------------------
def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------------------------------------
# 4️⃣ Register User
# -------------------------------------------------
def register():
    users = load_users()

    username = input("Enter username: ")

    if username in users:
        print("❌ User already exists.")
        return

    password = input("Enter password: ")
    hashed = hash_password(password)

    users[username] = {
        "password": hashed
    }

    save_users(users)
    print("✅ Registration successful.")


# -------------------------------------------------
# 5️⃣ Login User
# -------------------------------------------------
def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("❌ User not found.")
        return None

    hashed = hash_password(password)

    if users[username]["password"] == hashed:
        print("✅ Login successful.")
        return username
    else:
        print("❌ Incorrect password.")
        return None


# -------------------------------------------------
# 6️⃣ Dashboard (Session Simulation)
# -------------------------------------------------
def dashboard(username):
    print(f"\n🎉 Welcome {username}!")
    print("You are logged in.")

    while True:
        print("\n1. Show profile")
        print("2. Logout")

        choice = input("Choose: ")

        if choice == "1":
            print(f"👤 Username: {username}")
        elif choice == "2":
            print("🔓 Logged out.")
            break
        else:
            print("Invalid option.")


# -------------------------------------------------
# 7️⃣ Main App Loop
# -------------------------------------------------
def main():
    while True:
        print("\n===== LOGIN SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                dashboard(user)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
