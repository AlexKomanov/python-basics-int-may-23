my_list = [10, 20, 30, 40, 50]

for item in my_list:
    print(item)

for item in enumerate(my_list):
    print(item)

for index, item in enumerate(my_list):
    print(f"{index+1}. {item} - Completed")
