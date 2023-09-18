from functools import reduce

# from functools import reduce as re
# import functools
# from functools import *

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = functools.reduce()  # in case of just import functools

# total = re()  # In case of alias reduce as re
total = reduce(lambda x, y: x * y, my_list)

print(total)
