n = int(input("Enter your number: "))
for i in range(1, n+1):
    print(" " * (n - i), end="")      # Leading spaces
    print("*" * (2 * i - 1))          # Stars for the pyramid