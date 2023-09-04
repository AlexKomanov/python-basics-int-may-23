day_of_week = int(input("What's a day today? "))

match day_of_week:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6 | 7:
        print("Weekend!!!")
    case _:
        print("I don't know what you're talking about.")
