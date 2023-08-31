this_dict = {
    "brand": "Ford",  # String as a key
    1: False,  # Integer as a key
    ('year', 'creation'): 1964,  # Tuple as a key
    "colors": ["red", "white", "blue"],
    ['name', 'country']: 'USA'  # Tuple as a key -> TypeError: unhashable type: 'list'
}

print(this_dict)
