numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"{numbers_list = }")

numbers_list_new = numbers_list[:]
print(f"{numbers_list_new = }")

print(id(numbers_list))
print(id(numbers_list_new))

numbers_list[1] = 5
numbers_list_new[-1] = 50

print(f"{numbers_list = }")
print(f"{numbers_list_new = }")

print(id(numbers_list))
print(id(numbers_list_new))
