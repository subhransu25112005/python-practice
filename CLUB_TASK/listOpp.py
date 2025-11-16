#  List Operations

# Sample list of numbers
numbers = [10, 25, 7, 90, 33, 25, 7, 10, 90, 25]

# 6. Find sum, maximum, and minimum
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
print("Original list:", numbers)
print("Sum:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)

# 7. Count how many times a number occurs
target = 25
count = numbers.count(target)
print(f"{target} occurs {count} times")

# 8. Sort the list in ascending and descending order
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
print("Sorted ascending:", ascending)
print("Sorted descending:", descending)

# 9. Remove all duplicates from the list
unique_numbers = list(set(numbers))
print("List without duplicates:", unique_numbers)