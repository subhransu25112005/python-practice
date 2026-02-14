def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
@my_decorator
def hello():
    print("Hello Decorator")
hello() 