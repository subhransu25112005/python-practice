from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: int
    course: str
    year: int


# Creating objects
s1 = Student("Subhranshu", 101, "B.Tech CSE", 2)
s2 = Student("Amit", 102, "B.Tech CSE", 2)

# Using objects
print(s1)
print(s2)
