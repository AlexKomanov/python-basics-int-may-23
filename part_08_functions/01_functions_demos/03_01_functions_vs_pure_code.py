a = 5
b = 10

print(a + b ** 4)

a = 50
b = 100

print(a + b ** 2)

a = 1000
b = 200

print(a + b ** 3)

a = 10
b = 20

print((a + b) ** 2)

print("\n====================================\n")


def calculate_sum(c: int, d: int, divider: int = 5):
    result = (c + d) ** 4 / divider
    print(1)
    print(result)


num_1 = 5
num_2 = 20

calculate_sum(num_2, num_1)

num_1 = 50
num_2 = 20

calculate_sum(num_2, num_1)

calculate_sum(1, 2, 10)
