my_list = []

# for i in range(100000):
#     file = open("passwords.txt", "w")
#     my_list.append(file)
#     # file.close()
# print("end")

for i in range(100000):
    with open("passwords.txt", "w") as file:
        my_list.append(file)

print("end")
print(file)
