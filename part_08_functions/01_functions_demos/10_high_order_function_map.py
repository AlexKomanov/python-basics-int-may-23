original_array = [2, 5, 8, 10, 25]

after_map = map(lambda x: x ** 2, original_array)

print(original_array)
print(tuple(after_map))
print(type(after_map))

new_array = list(map(lambda x: x ** 3, original_array))

print(original_array)
print(new_array)
