original_array = [2, 5, 8, 10, 25]

after_map = list(map(lambda x: x ** 2, original_array))


def calculate(x):
    return x ** 2


after_map_2 = list(map(calculate, original_array))

print(original_array)
print(after_map)
print(after_map_2)
