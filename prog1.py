class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

obj = Bus("Volvo", 140, 12)

print(f"Vehicle name: {obj.name}")
print(f"Vehicle Max speed: {obj.max_speed}")
print(f"Vehicle mileage: {obj.mileage}")