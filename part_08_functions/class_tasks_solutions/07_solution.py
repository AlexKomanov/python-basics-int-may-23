def list_ends(a_list):
    return [a_list[0], a_list[len(a_list) - 1]]


list_original = [5, 10, 15, 20, 251]

new_list = list_ends(list_original)
print(new_list)
