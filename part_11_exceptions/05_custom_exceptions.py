arr = ["5", 6, 7]
try:
    if 6 in arr:
        raise NameError("Name Error with custom message")
except Exception as error:
    print(error)
else:
    print("Else block - code finished with success!")
finally:
    print("Finally block!")
