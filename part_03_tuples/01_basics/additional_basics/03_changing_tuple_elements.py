# Tuple definition
my_tuple = ('alex', 5, 35, False, 'age', 56)
print(my_tuple)

# Converting tuple to list
my_list = list(my_tuple)
print(my_list)

# Adding elements by append() method or assign a new value to existing element
my_list[2] = 105
my_list.append(True)

# Converting a modified list to be a tuple again
my_tuple = tuple(my_list)
print(my_tuple)

# Converting a tuple to be a list by using * unpacking method
unpacked_list = [*my_tuple, ]

print(f"{unpacked_list = }")
