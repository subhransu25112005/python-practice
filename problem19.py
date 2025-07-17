n = int(input("Enter a positive integer: "))

# Initialize variables
sum = 0
i = 1

# Loop to calculate sum
while (i <= n):
    sum += i
    i += 1

# Display the result
print(f"The sum of the first {n} natural numbers is: {sum}")