from add_mod import add


def mul(num1: int, num2: int):
    result = 0
    for a in range(num2):
        result = add(result, num1)

    return result

# 5 * 3 -> 0 + 5 + 5 + 5

# range(3) 0, |  1, 2
