a = int(input())
b = int(input())
c = int(input())

print(f"(a+b*c) = {(a+b*c)}")
print(f"(a*(b+c)) = {(a*(b+c))}")
print(f"(a*b*c) = {(a*b*c)}")
print(f"((a+b)*c) = {((a+b)*c)}")
print(f"(a+b+c) = {(a+b+c)}")

print("max = ", max((a+b*c), (a*(b+c)), (a*b*c), ((a+b)*c), (a+b+c)))


