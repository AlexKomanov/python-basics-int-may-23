coffee_cost = 15

amount = int(input("Enter your amount: "))

if amount >= coffee_cost:
    print("Take your coffee!")
else:
    print("Sorry, not enough money")

print("Take your coffee!") if amount >= coffee_cost else print("Sorry, not enough money")
