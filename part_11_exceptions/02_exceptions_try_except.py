x = 6
try:
    print(f"{x = }")
    # print(x / 0)
    print(x + "text")
except NameError:
    print("NameError  - please try again")
except ZeroDivisionError:
    print("No option to divide ny zero....")
except Exception as error:
    print(error)

# print("text" + 5)