this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "optional_colors": ["red", "black"],
    "optional_gears": ("mechanical", "automatically")
}

print(this_dict)

print(this_dict.pop("optional_colors"))

print(this_dict)

print(this_dict.pop("aaaaa", "Doesn't exist"))
