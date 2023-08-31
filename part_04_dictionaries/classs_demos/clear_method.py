this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "optional_colors": ["red", "black"],
    "optional_gears": ("mechanical", "automatically")
}

print(this_dict)
print(id(this_dict))

this_dict.clear()
print(this_dict)
print(id(this_dict))

this_dict["model"] = "AMG"
print(this_dict)
print(id(this_dict))
