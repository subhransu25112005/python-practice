def my_decorator(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Called", count, "times")
        return func()

    return wrapper
