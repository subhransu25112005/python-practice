# Q1
def welcome():
    print("Welcome to Python Class!")

welcome()

# Q2
def multiply(a, b):
    print("Multiplication:", a * b)

multiply(4, 5)

# Q3
def is_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(7)
#Function with return value
# Q4
def cube(num):
    return num ** 3

print("Cube of 3:", cube(3))

# Q5
def max_of_two(a, b):
    return a if a > b else b

print("Max of 10 and 20:", max_of_two(10, 20))

# Q6
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius ** 2

print("Area of circle with radius 5:", area_of_circle(5))