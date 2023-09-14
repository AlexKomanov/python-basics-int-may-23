def say_hello():
    print("Hello")


say_hello()

greeting = lambda: print("Hello from lambda")
greeting()


def calculate_sum(a, b):
    result = a + b
    return result


answer = calculate_sum(5, 10)
print(answer)

lambd = lambda x, y: x + y
answer = lambd(20, 30)

print(answer)

