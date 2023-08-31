this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    'isElectrical': False
}

print(this_dict)

del this_dict["isElectrical"]

del this_dict["color"]  # KeyError: 'color'  <---- Comment it after presenting an error

print(this_dict)
