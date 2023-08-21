x = ("Alex", "Andrei", "Erez")
print(type(x))
x = list(x)

print(type(x))

list_of_values = list(map(int, input("Enter values: ").split()))

print(list_of_values)
print(len(list_of_values))

map_of_values = map(int, input("Enter values: ").split())
print(map_of_values)
