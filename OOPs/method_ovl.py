class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


def main():
    calc = Calculator()

    print(calc.add(5))         
    print(calc.add(5, 10))      
    print(calc.add(5, 10, 15))  


if __name__ == "__main__":
    main()
