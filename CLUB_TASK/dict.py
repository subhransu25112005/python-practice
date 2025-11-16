# Dictionary Tasks 1–5

# 1. Create a dictionary and print all values
student = {
    "name": "Subhransu",
    "roll": 308,
    "branch": "Computer Science"
}
print("Student Details (Values):")
for value in student.values():
    print(value)

# 2. Print only the keys
print("\nKeys in the dictionary:")
print(student.keys())

# 3. Add a new key-value pair "year": 3
student["year"] = 3
print("\nAfter adding 'year':")
print(student)

# 4. Delete one key using pop()
student.pop("branch")
print("\nAfter removing 'branch':")
print(student)

# 5. Check if key "age" exists
if "age" in student:
    print("\nKey 'age' exists in the dictionary.")
else:
    print("\nKey 'age' does NOT exist in the dictionary.")