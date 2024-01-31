class Phone:
    # static
    type = "Phone"
    box_content = ("cable", "charger", "manual")

    def __init__(self, brand: str, color: str, price: float, ):
        self.brand = brand
        self._color = color
        self.__price = price

    def print_info(self):
        print(f"It is a {self.brand} phone with {self._color} color and price of {self.__price} NIS")


phone = Phone("Apple", "black", 4500)

phone.print_info()
print(phone.box_content)
print(Phone.type)
