class MyCustomException(Exception):
    pass

x = 2
try:
    if not type(x) is str:
        # raise TypeError("Only string is allowed!")
        raise MyCustomException("Only string is allowed!")
except NameError:
    print("A NameError is occurred.")
except Exception as error:
    print(error)
else:
    print("Else block - no errors were found!")
finally:
    print("Finally block - executed in any case!")
