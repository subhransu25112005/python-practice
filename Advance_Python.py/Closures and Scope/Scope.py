x = 10          # Global scope

def outer():
    y = 20      # Enclosing scope

    def inner():
        z = 30  # Local scope
        print("Local z:", z)
        print("Enclosing y:", y)
        print("Global x:", x)
        print("Built-in len:", len([1, 2, 3]))

    inner()

outer()
#L -> E -> G -> B