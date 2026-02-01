def security_check(func):
    def wrapper(user):
        print("🔒 Logging entry attempt...")
        if user == "admin":
            print("✅ Authentication successful.")
            func(user)
        else:
            print("❌ Access denied. Unauthorized user.")
    return wrapper


@security_check
def enter_control_room(user):
    print(f"🚀 {user} entered the control room.")


def main():
    print("=== DEFENSE CONTROL ROOM ACCESS ===")

    username = input("Enter username: ")
    enter_control_room(username)


if __name__ == "__main__":
    main()
