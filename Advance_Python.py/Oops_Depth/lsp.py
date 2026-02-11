# ❌ WRONG DESIGN (violates LSP)
# class Vehicle:
#     def start_engine(self):
#         pass
#
# class Bicycle(Vehicle):
#     def start_engine(self):
#         raise Exception("No engine!")


# ✅ CORRECT DESIGN

class Transport:
    def start(self):
        print("Transport started")


class EngineVehicle(Transport):
    def start(self):
        print("Engine vehicle started")


class Bicycle(Transport):
    def start(self):
        print("Pedaling bicycle")


class Car(EngineVehicle):
    pass


def start_trip(vehicle: Transport):
    vehicle.start()


car = Car()
bike = Bicycle()

start_trip(car)
start_trip(bike)
