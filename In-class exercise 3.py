times = input("How many times do you eat at the students cafeteria in a week? ")
price = input("How much do you pay for the lunch? ")
price_g = input("How much do you spent on groceries on a week? ")

weekly = int(times) * float(price) + float(price_g)
daily = int(weekly) / 7

"""
print("")
print("Average food expenditure:")
print("Weekly:", weekly, "euros.")
print(f"Daily: {daily:.0f} euros.")
"""

print("")
print(f"Average food expenditure:\n Weekly: {weekly:.0f} euros.\n Daily: {daily:.0f} euros.")
