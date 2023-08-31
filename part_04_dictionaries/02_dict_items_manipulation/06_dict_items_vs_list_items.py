this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dict_items = this_dict.items()
print(type(dict_items))
print(dict_items.__sizeof__())

list_of_items = list(this_dict.items())
print(type(list_of_items))
print(list_of_items.__sizeof__())
