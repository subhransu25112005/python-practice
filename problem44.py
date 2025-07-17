class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 1293747, 756001)
r = Programmer("Rahul", 120095, 567743)

print(p.name, p.salary, p.pin, p.company)
print(r.name, r.salary, r.pin, r.company)