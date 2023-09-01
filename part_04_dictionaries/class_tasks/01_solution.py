days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

num_of_month = int(input("Enter a month number: "))
print(days[num_of_month])
print(days.get(num_of_month))
