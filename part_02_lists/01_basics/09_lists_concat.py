list_1 = ['Alex', 'Kobi', 'Yoni']

print(f"{list_1 = }")

list_1 += ['Shaun', 'Yan', 'Omri']

print(f"{list_1 = }")

list_1 += 'Noam Noam'
print(f"{list_1 = }")

# list_1 += 888 # TypeError: 'int' object is not iterable

list_1 += [888]
print(f"{list_1 = }")
