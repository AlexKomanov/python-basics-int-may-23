list_a = ["b", "g", "a", "d", "f", "c", "h", "e"]
sorted_list_a = sorted(list_a)
reverse_sorted_list_a = sorted(list_a, reverse=True)
print(sorted_list_a)
print(reverse_sorted_list_a)

list_b = [1, 7, -6, 1000, -600, 20000, 5000]
sorted_list_b = sorted(list_b)
reverse_sorted_list_b = sorted(list_b, reverse=True)
print(sorted_list_b)
print(reverse_sorted_list_b)

list_c = [1, 7, -6, 1000, -600, 20000, "Alex"]
# sorted_list_c = sorted(list_c) # TypeError: '<' not supported between instances of 'str' and 'int'
