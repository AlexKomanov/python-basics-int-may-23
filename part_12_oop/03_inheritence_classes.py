class Vehicle:

    def __init__(self, required_brand, required_year):  # Constructor
        self.vehicle_brand = required_brand
        self.vehicle_year = required_year

    def drive(self):
        print("I can't drive - I'm a general vehicle")

    def print_the_info(self):
        print(f"It's {self.vehicle_brand} - {self.vehicle_year}")


class Car(Vehicle):

    def __init__(self, car_brand, car_year):
        super().__init__(car_brand, car_year)

    def drive(self):
        print(f"Car is driving")


class Airplane(Vehicle):

    def __init__(self, plane_brand, plane_year, plane_id):
        super().__init__(plane_brand, plane_year)
        self.plane_id = plane_id

    def drive(self):
        print(f"I'm a plane {self.vehicle_brand} {self.plane_id} and I want to fly!")


vehicle = Vehicle("General" )

# vehicle.drive()

car = Car("Tesla", 2023)

car.drive()

plane = Airplane("Boeing", 1974, "23434-ffgf-3434")

# plane.drive()

# vehicles = [vehicle, car, plane]
#
# for item in vehicles:
#     item.print_the_info()  # Polymorphism
