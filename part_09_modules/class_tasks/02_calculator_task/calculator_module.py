def _add(x, y):
    return x + y


def _subtract(x, y):
    return x - y


def _multiply(x, y):
    return x * y


def _divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed!")
    return x / y


def calculate(x: float, y: float, operation: str):
    match operation:
        case "+":
            return _add(x, y)
        case "-":
            return _subtract(x, y)
        case "*":
            return _multiply(x, y)
        case "/":
            return _divide(x, y)
        case _:
            raise ValueError("It is an invalid operation. Please try again...")


# Optional checking of operation
        # operation = int(input("Options: \n1. +\n2. -\n3. *\n4. /\n"))
        # while operation < 1 or operation > 4:
        #     print("Wrong Choice! Please try again")
        #     operation = int(input("Options: \n1. +\n2. -\n3. *\n4. /\n"))
        #
        # if operation == 1:
        #     return _add(x, y)
        # elif operation == 2:
        #     return _subtract(x, y)
        # elif operation == 3:
        #     return _multiply(x, y)
        # elif operation == 4:
        #     return _divide(x, y)
