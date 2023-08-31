this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "optional_colors": ["red", "black"],
    "optional_gears": ("mechanical", "automatically")
}

print(this_dict["brand"])
print(this_dict.get("brand"))

# print(this_dict["manufacturer"])
print(this_dict.get("manufacturer"))

expected_key = "manufacturer"
print(this_dict.get(expected_key, f"The '{expected_key}' doesn't exist..."))
