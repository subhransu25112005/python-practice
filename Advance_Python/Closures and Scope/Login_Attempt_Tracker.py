def login_system():
    attempts = 0

    def login(password):
        nonlocal attempts
        attempts += 1
        if password == "admin123":
            return "Login successful"
        return f"Wrong password. Attempt {attempts}"

    return login

check = login_system()
print(check("123"))
print(check("abc"))
print(check("admin123"))
