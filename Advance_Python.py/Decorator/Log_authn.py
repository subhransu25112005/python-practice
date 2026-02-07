def login_required(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
            return
        return func(user)
    return wrapper

@login_required
def dashboard(user):
    print(f"Welcome {user}, dashboard loaded")

dashboard("admin")
dashboard("guest")
