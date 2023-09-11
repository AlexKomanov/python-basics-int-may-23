my_list = ["apple", 'orange', 'banana', 'grape', 'watermelon']

for elem in enumerate(my_list):
    print(elem)

for index, elem in enumerate(my_list, start=32):
    print(index, elem)
