this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "optional_colors": ["red", "black"],
    "optional_gears": ("mechanical", "automatically")
}

print(this_dict)
print(type(this_dict))
print(len(this_dict))
print(id(this_dict))
this_dict["year"] = 2022
this_dict["isElectrical"] = False

print(this_dict)
print(id(this_dict))
