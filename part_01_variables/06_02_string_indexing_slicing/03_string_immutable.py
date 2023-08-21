name = "Alex Komanov"
print(name)

print(name[0:3] + "y")
print(name + "y")
print(name)
# name[3] = "y" # TypeError: 'str' object does not support item assignment

# print(name)

name = "Jameel"
print(name)

mixed_name = "Alex Jameel"
print(mixed_name)
print(id(mixed_name))
mixed_name = mixed_name[:-1]
print(mixed_name)
mixed_name = mixed_name + "l"
print(mixed_name)
print(id(mixed_name))

