# x = 5
try:
    print(x)
except Exception as error:
    print(error)
else:
    print("Else block - code finished with success!")
finally:
    print("Finally block!")
