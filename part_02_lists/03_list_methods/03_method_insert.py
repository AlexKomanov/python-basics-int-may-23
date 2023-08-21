names = ['Erez', 'Zion', 'Siri']
print(f"{names = }")

names.insert(0, ["Shaun", "Lada"])
# names.insert( ["Shaun", "Lada"]) # TypeError: insert expected 2 arguments, got 1
print(f"{names = }")


names.insert(15, 8)
print(f"{names = }")
print(len(names))
