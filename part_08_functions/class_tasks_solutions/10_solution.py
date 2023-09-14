def multiply(*arguments):
    result = 1
    for elem in arguments:
        result *= elem
    return result


print(multiply(1, 2, 3))
print(multiply(1, 3))
print(multiply())
print(multiply(0, 2, 3))
