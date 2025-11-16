# 1. Store student names, roll numbers, and marks
names = ["Amit", "Neha", "Raj"]
roll_numbers = (101, 102, 103)
marks = {101: 85, 102: 90, 103: 78}
print("Names:", names)
print("Roll Numbers:", roll_numbers)
print("Marks Dictionary:", marks)

# 2. Create dictionary: name → length of name
name_lengths = {}
for name in names:
    name_lengths[name] = len(name)
print("Name lengths:", name_lengths)

# 3. Convert list of tuples into dictionary
info_list = [('name', 'Ravi'), ('age', 21), ('branch', 'CSE')]
info_dict = dict(info_list)
print("Converted Dictionary:", info_dict)

# 4. Print all keys in a list and all values in a tuple
keys_list = list(info_dict.keys())
values_tuple = tuple(info_dict.values())
print("Keys as list:", keys_list)
print("Values as tuple:", values_tuple)

# 5. Create dictionary: numbers 1–5 → their squares
squares = {}
for i in range(1, 6):
    squares[i] = i * i
print("Squares Dictionary:", squares)