# a, b, c, d = map(int, input("Please enter 4 numbers: ").split())
#
# print((a+b+c+d)/4)


# OR

# print(sum(list(map(int, input("put the score here: ").split()))) / 4)

list_of_nums = list(map(int, input("put the score here: ").split()))
print(list_of_nums)
print((len(list_of_nums)))
print(sum(list_of_nums) / len(list_of_nums))

