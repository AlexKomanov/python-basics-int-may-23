list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
print(list(new_list))

print(type(new_list))
# iterate reversed list
for item in new_list:
    print(item)

print(len(list1))

for num in list1[::-1]:
    print(num)

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
