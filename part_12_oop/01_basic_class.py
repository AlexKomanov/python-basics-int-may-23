class MyCar:
    year = 2023
    brand = "Tesla"

    def car_drive(self):
        print("Car is driving")

    def go_faster(self, max_speed: int):
        print("Accelerate up to ", max_speed)


tesla = MyCar()
print(type(tesla))

print(tesla.year)
print(tesla.brand)
print(type("Alex"))
tesla.car_drive()
tesla.go_faster(230)
