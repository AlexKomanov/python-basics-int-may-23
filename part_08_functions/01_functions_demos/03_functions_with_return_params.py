def say_hello(name: str):
    print(f"Hello {name}!")


def calculate_sum(number_1: int, number_2: int):
    return number_1 + number_2


say_hello("Alex")
print(calculate_sum(5, 10))

result = calculate_sum(20, 30)
print("result", result)

# print(say_hello("Berkoni"))  # Return typ -> None
