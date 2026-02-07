def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))
