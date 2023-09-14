def check_sum(*arguments):
    summary = 0
    for elem in arguments:
        summary += elem

    print("verification passed") if summary >= 50 else print("not enough")


check_sum(20, 20, 10)
check_sum(20, 10, 10)
