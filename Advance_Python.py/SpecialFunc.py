# Student data
names = ["Amit", "Neha", "Ravi", "Priya", "Karan"]
marks = [35, 78, 42, 90, 25]
completed = [True, True, False, True, True]

#  Combine data using zip
students = zip(names, marks, completed)   

# Filter students who completed course AND passed (>=40)
eligible_students = filter(
    lambda s: s[2] and s[1] >= 40,
    students
)

# Add grace marks using map (5 bonus points)
final_result = map(
    lambda s: (s[0], s[1] + 5),
    eligible_students
)

#  Display result
print("Final Certified Students:")
for student in final_result:
    print(student)
