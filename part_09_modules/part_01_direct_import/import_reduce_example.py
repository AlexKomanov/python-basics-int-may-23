from functools import reduce
# from functools import *

my_list = [5, 10, 15, 20, 25]

total = reduce(lambda x, y: x + y, my_list)
print(total)
