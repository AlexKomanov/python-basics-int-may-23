a = [34, 23, 12, 28, 23]

b = a.pop(-1)
a.pop(0)

print(f"{a = }")
print(f"{b = }")

# a.pop(25) # IndexError: pop index out of range
# [].pop() # IndexError: pop from empty list