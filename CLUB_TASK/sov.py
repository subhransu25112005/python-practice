# Q7: Local vs Global
count = 10  # Global variable

def demo():
    count = 5  # Local variable
    print("Inside function, count =", count)

demo()
print("Outside function, count =", count)

# Q8: Using global keyword
total = 0

def add_to_total(x):
    global total
    total += x

add_to_total(10)
add_to_total(20)
print("Total after additions:", total)