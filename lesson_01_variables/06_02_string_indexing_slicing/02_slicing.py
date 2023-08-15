letters = "abcdefghijklmnop"

print("letters -> ", letters)
print("letters[0:4] -> ", letters[0:4])
print("letters[0:4+1] -> ", letters[0:4 + 1])
print("letters[0:12:1] -> ", letters[0:12:1])  # 1 is a default step
print("letters[0:12:4] -> ", letters[0:12:4])
print("letters[-7:-1] -> ", letters[-7:-1])
print("letters[-7:] -> ", letters[-7:])
print("letters[-1:-7:-1] -> ", letters[-1:-7:-1])
print("letters[::-1] -> ", letters[::-1])
# print("letters[0:12:0] -> ", letters[0:12:0])  # ValueError: slice step cannot be zero
# print("letters[0:12:3.5] -> ", letters[0:12:3.5])  # TypeError: slice indices must be integers or None or have an __index__ method
