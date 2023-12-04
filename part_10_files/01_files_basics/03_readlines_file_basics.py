my_file = open("example.txt")
# print(my_file.readlines())
# print(type(my_file.readlines()))

list_of_data = my_file.readlines()

for item in list_of_data:
    print(item, end="")
    # for letter in item:
    #     print(letter)

my_file.close()



