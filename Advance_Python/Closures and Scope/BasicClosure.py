def outer(msg):
    def inner():
        print(msg)
    return inner

func = outer("Hello Python")
func()   
