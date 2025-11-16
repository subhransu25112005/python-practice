# 1. Create a tuple of 5 numbers and print the first and last elements
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 2. Find the length of the tuple
print("Length of tuple:", len(numbers))

# 3. Tuple slicing: elements from index 1 to 3 (excluding 4)
print("Sliced tuple (index 1 to 3):", numbers[1:4])

# 4. Tuple with mixed data types
mixed_tuple = (101, "Subhransu", 3.14, True, None)
print("Mixed data type tuple:", mixed_tuple)

# 5. Check if an element exists in the tuple
check_value = 30
if check_value in numbers:
    print(f"{check_value} exists in the tuple.")
else:
    print(f"{check_value} does not exist in the tuple.")