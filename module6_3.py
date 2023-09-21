# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.


def conversion():
    gallons = float(input("How many gallons you want to convert? "))
    while gallons >= 0:
        liters = gallons * 3.78541
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        gallons = float(input("How many gallons you want to convert? "))


conversion()

print("Thanks.")
