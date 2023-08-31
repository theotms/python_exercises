talents = float(input("Enter the amount in talents: "))
pounds = float(input("Enter the amount in pounds: "))
lots = float(input("Enter the amount in lots: "))

full = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
weight_m = full / 1000
weight_r = (full % 1000)

print(f"The modern weight is {weight_m:.2f}kg and {weight_r:.2f}g")
