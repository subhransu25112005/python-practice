from abc import ABC, abstractmethod


# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


# Concrete class 1
class Car(Vehicle):
    def start(self):
        print("Car started with key ignition.")

    def stop(self):
        print("Car stopped.")

    def fuel_type(self):
        print("Fuel Type: Petrol / Diesel")


# Concrete class 2
class Bike(Vehicle):
    def start(self):
        print("Bike started with self-start button.")

    def stop(self):
        print("Bike stopped.")

    def fuel_type(self):
        print("Fuel Type: Petrol")


def main():
    print("=== VEHICLE SYSTEM ===")

    print("\n--- Car ---")
    car = Car()
    car.start()
    car.fuel_type()
    car.stop()

    print("\n--- Bike ---")
    bike = Bike()
    bike.start()
    bike.fuel_type()
    bike.stop()


if __name__ == "__main__":
    main()
