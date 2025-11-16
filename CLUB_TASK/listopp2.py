# 10. Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined list:", combined)

# 11. Find even and odd numbers
even = []
odd = []
for num in combined:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:", even)
print("Odd numbers:", odd)

# 12. Square each number
squares = []
for num in combined:
    squares.append(num * num)
print("Squares:", squares)