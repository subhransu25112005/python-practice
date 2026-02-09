class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"{self.brand} running at {self.speed} km/h"

    def __add__(self, other):
        return self.speed + other.speed

    def __gt__(self, other):
        return self.speed > other.speed

c1 = Car("BMW", 120)
c2 = Car("Audi", 100)

print(c1)
print("Total speed:", c1 + c2)
print("Is BMW faster?", c1 > c2)
