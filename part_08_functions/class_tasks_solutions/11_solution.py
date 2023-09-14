def only_one_positive(*arguments):
    result = 0
    for elem in arguments:
        if elem > 0:
            result += 1
    return result == 1


# Additional Solution
# def only_one_positive(*args):
#     return len([x for x in args if x > 0]) == 1


print(only_one_positive(1, 2))
print(only_one_positive(-1, 0, -3, 5, -3))
print(only_one_positive())
