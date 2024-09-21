# Alex Lewis / Assignment 3A
# The system prompts user for monthly expenses and calculates the total, highest, and lowest expense.

import functools

item = []
costs = []

# Prompts user for expense and expense type
def expenses():
    cont = "y"
    num = 0

    while cont.lower() == "y":
        item.append(input("Expense type: "))
        costs.append(float(input(f"Cost of {item[num]}: ")))
        num += 1

        print("")
        cont = input('Input "y" to continue: ')

    return costs
    return item

expenses()

print("")
print("")


# Calculates and prints total expense
def total():
    print("Total costs of expenses: $", end="")
    print(functools.reduce(lambda a, b: a+b, costs))

# Calculates and prints highest expense
def expensive():
    highest = (functools.reduce(lambda a, b: a if a > b else b, costs))
    index = costs.index(highest)
    print(f"The highest expense was {item[index]} for ${highest}")

# Calculates and prints lowest expense
def cheap():
    lowest = (functools.reduce(lambda a, b: a if a < b else b, costs))
    index = costs.index(lowest)
    print(f"The lowest expense was {item[index]} for ${lowest}")

total()
expensive()
cheap()