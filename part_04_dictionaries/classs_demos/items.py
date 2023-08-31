this_dict = {
    "brand": "Ford",
    "model": "Mustange",
    "year": 1964
}

dict_of_items = this_dict.items()
print(dict_of_items)
print(type(dict_of_items))
print(dict_of_items.__sizeof__())

list_of_items = list(this_dict.items())
print(list_of_items)
print(type(list_of_items))
print(list_of_items.__sizeof__())
