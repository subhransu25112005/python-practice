class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before")
        self.func()
        print("After")

@Decorator
def hello():
    print("Hello")

hello()
