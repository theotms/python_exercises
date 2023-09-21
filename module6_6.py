# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides
# better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
import math


def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    unit_price_per_sqm = price / (area / 10000)

    return unit_price_per_sqm


diameter1 = float(input("Enter the diameter of the first pizza (in centimeters): "))
price1 = float(input("Enter the price of the first pizza (in euros): "))

diameter2 = float(input("Enter the diameter of the second pizza (in centimeters): "))
price2 = float(input("Enter the price of the second pizza (in euros): "))

unit_price1 = unit_price(diameter1, price1)
print(f"The price for square meter for the first pizza is {unit_price1:.2f} euros.")
unit_price2 = unit_price(diameter2, price2)
print(f"The price for square meter for the second pizza is {unit_price2:.2f} euros.")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas have the same unit price.")
