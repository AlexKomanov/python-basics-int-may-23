
class MyExpectedCar:
    def __init__(self, required_brand, required_year):  # Constructor
        self.car_brand = required_brand
        self.year = required_year

    def print_car_info(self):
        print(f"My car is {self.car_brand} {self.year}")


    def go_faster(self, max_speed: int):
        print("Accelerate up to ", max_speed)


tesla = MyExpectedCar("Tesla", 2023)
tesla.print_car_info()

bmw = MyExpectedCar("BMW", 2024)
bmw.print_car_info()

# MyExpectedCar.print_car_info() # static type



