class SafeDivision:
    def __enter__(self):
        return self

    def divide(self, a, b):
        return a / b

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == ZeroDivisionError:
            print("Division by zero handled")
            return True   

with SafeDivision() as s:
    print(s.divide(10, 0))
