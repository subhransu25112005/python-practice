# 1. Create a list of 5 fruits and print the 2nd and last fruit
fruits = ["Apple", "Banana", "Cherry", "Orange", "Grapes"]
print("Original list of fruits:", fruits)
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# 2. Add "Mango" using append() and "Pineapple" using insert()
fruits.append("Mango")
fruits.insert(2, "Pineapple") 
print("After adding Mango and Pineapple:", fruits)

# 3. Remove last item using pop() and specific item using remove()
fruits.pop()           
fruits.remove("Banana")  
print("After removing last item and Banana:", fruits)

# 4. Find the length of the list
print("Length of the list:", len(fruits))

# 5. Reverse the list using slicing
reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)


