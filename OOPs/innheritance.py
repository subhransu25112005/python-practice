# =========================
# BASE CLASS
# =========================
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# =========================
# 1️⃣ SINGLE INHERITANCE
# Person → Student
# =========================
class Student(Person):
    def show_role(self):
        print("Role: Student")


# =========================
# 2️⃣ MULTILEVEL INHERITANCE
# Person → Employee → Manager
# =========================
class Employee(Person):
    def show_employee(self):
        print("Role: Employee")


class Manager(Employee):
    def show_manager(self):
        print("Role: Manager")


# =========================
# 3️⃣ HIERARCHICAL INHERITANCE
# Person → Teacher
# Person → Doctor
# =========================
class Teacher(Person):
    def show_role(self):
        print("Role: Teacher")


class Doctor(Person):
    def show_role(self):
        print("Role: Doctor")


# =========================
# 4️⃣ MULTIPLE INHERITANCE
# =========================
class Skill:
    def skill(self):
        print("Skill: Programming")


class Hobby:
    def hobby(self):
        print("Hobby: Reading")


class Developer(Skill, Hobby):
    def show_profession(self):
        print("Profession: Developer")


# =========================
# 5️⃣ HYBRID INHERITANCE
# (Combination of Multiple + Multilevel)
# =========================
class Human:
    def breathe(self):
        print("Human can breathe")


class Engineer(Human):
    def work(self):
        print("Engineer works on technology")


class Leader:
    def lead(self):
        print("Leader can lead a team")


class TechLead(Engineer, Leader):
    def role(self):
        print("Role: Tech Lead")


# =========================
# MAIN FUNCTION
# =========================
def main():
    print("\n--- SINGLE INHERITANCE ---")
    s = Student("Rahul")
    s.show_name()
    s.show_role()

    print("\n--- MULTILEVEL INHERITANCE ---")
    m = Manager("Amit")
    m.show_name()
    m.show_employee()
    m.show_manager()

    print("\n--- HIERARCHICAL INHERITANCE ---")
    t = Teacher("Sita")
    t.show_name()
    t.show_role()

    d = Doctor("Dr. Ram")
    d.show_name()
    d.show_role()

    print("\n--- MULTIPLE INHERITANCE ---")
    dev = Developer()
    dev.skill()
    dev.hobby()
    dev.show_profession()

    print("\n--- HYBRID INHERITANCE ---")
    tl = TechLead()
    tl.breathe()
    tl.work()
    tl.lead()
    tl.role()


if __name__ == "__main__":
    main()
