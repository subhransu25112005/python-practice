def star(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper

def percent(func):
    def wrapper():
        print(":)")
        func()
        print("(:")
    return wrapper

@star
@percent
def display():
    print("Python")

display()
