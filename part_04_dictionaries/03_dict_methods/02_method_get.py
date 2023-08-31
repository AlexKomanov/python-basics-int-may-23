d = {1: 'one', 2: 'two', 3: 'three'}
print(d.pop(2))
print(d)

deleted_value = d.pop(1)
print(deleted_value)
print(d)

# d.pop(8)  # KeyError: 8

non_existing = d.pop(8, "No such index")
print(non_existing)
