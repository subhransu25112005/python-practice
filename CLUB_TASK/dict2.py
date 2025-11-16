# 6. Input names and marks of 3 students
student_marks = {}
for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks for {name}: "))
    student_marks[name] = mark
print("\nStudent Marks Dictionary:", student_marks)

# 7. Print all key-value pairs using a loop
print("\nAll key-value pairs:")
for name, mark in student_marks.items():
    print(f"{name}: {mark}")

# 8. Merge two dictionaries
extra_marks = {"Ravi": 88, "Sneha": 91}
merged = {**student_marks, **extra_marks}
print("\nMerged Dictionary:", merged)

# 9. Find maximum and minimum marks
max_mark = max(merged.values())
min_mark = min(merged.values())
print("\nMaximum mark:", max_mark)
print("Minimum mark:", min_mark)

# 10. Create a nested dictionary and print one student's data
students = {
    "Amit": {"roll": 101, "branch": "CSE", "marks": 85},
    "Neha": {"roll": 102, "branch": "ECE", "marks": 90},
    "Raj": {"roll": 103, "branch": "ME", "marks": 78}
}
print("\nData for Neha:")
print(students["Neha"])