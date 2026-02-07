def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def message():
    return "@i am the best"

print(message())
