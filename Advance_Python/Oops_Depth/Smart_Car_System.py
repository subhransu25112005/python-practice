class SmartCar:
    # 1️⃣ Object Creation
    def __init__(self, brand, speed, features):
        self.brand = brand
        self.speed = speed
        self.features = features

    # 2️⃣ String Representation
    def __str__(self):
        return f"{self.brand} car running at {self.speed} km/h"

    # 3️⃣ Operator Overloading
    def __add__(self, other):
        return self.speed + other.speed

    # 4️⃣ Comparison
    def __gt__(self, other):
        return self.speed > other.speed

    # 5️⃣ Length
    def __len__(self):
        return len(self.features)

    # 6️⃣ Indexing
    def __getitem__(self, index):
        return self.features[index]

    # 7️⃣ Callable Object
    def __call__(self):
        print(f"🚗 {self.brand} engine started!")

    # 8️⃣ Context Manager
    def __enter__(self):
        print(f"🔓 {self.brand} unlocked")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"🔒 {self.brand} locked")


# ---------------- MAIN PROGRAM ----------------

car1 = SmartCar("BMW", 180, ["AC", "GPS", "Airbags"])
car2 = SmartCar("Audi", 160, ["AC", "Sunroof"])

# __str__
print(car1)

# __add__
print("Combined speed:", car1 + car2)

# __gt__
print("Is BMW faster than Audi?", car1 > car2)

# __len__
print("BMW features count:", len(car1))

# __getitem__
print("First feature of BMW:", car1[0])

# __call__
car1()

# __enter__ and __exit__
with car1:
    print("🚘 Driving the car safely...")
