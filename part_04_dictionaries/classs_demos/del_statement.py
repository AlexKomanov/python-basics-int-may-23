this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "optional_colors": ["red", "black"],
    "optional_gears": ("mechanical", "automatically")
}

print(this_dict)
print(id(this_dict))

del this_dict["optional_gears"]
del this_dict["optional_colors"]

print(this_dict)
this_dict.clear()
print(this_dict)
print(id(this_dict))

del this_dict


print(this_dict)
print(this_dict)


