class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of the given number is {self.n ** 2}")

    def cube(self):
        print(f"The cube of the given number is {self.n ** 3}")

    def square_root(self):
        print(f"The square root of the given number is {self.n ** 0.5}")

a = Calculator(int(input("Enter your number: ")))
a.square()
a.cube()
a.square_root()