def hello():
    print("Hello Decorator")

def my_dec(func):
    def wrapper():
        print("Before fucntion")
        func()
        print("After function")
    return wrapper   
hello = my_dec(hello) 
hello()
        
