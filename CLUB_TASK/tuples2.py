# Tuple Operations 
# 6. Convert a tuple to list, modify, and convert back
original_tuple = (1, 2, 3, 4, 5)
temp_list = list(original_tuple)
temp_list[2] = 99  # Change the third element
modified_tuple = tuple(temp_list)
print("Modified tuple:", modified_tuple)

# 7. Find max and min in a tuple
print("Maximum:", max(modified_tuple))
print("Minimum:", min(modified_tuple))

# 8. Count how many times a value appears
count_value = 99
count = modified_tuple.count(count_value)
print(f"{count_value} appears {count} time(s)")

# 9. Join two tuples
tuple_a = (10, 20, 30)
tuple_b = (40, 50)
joined_tuple = tuple_a + tuple_b
print("Joined tuple:", joined_tuple)

# 10. Create a nested tuple and access an element
nested = ((1, 2), (3, 4), (5, (6, 7)))
print("Element inside nested tuple:", nested[2][1][0]) 

# Tuple Tasks 11 & 12

# 11. Unpack the tuple into three variables
info = ('Python', 3.10, 'Language')
name, version, category = info
print("Name:", name)
print("Version:", version)
print("Category:", category)

# 12. Calculate average of student marks
marks = (85, 90, 78, 92, 88)
average = sum(marks) / len(marks)
print("Student marks:", marks)
print("Average mark:", average)