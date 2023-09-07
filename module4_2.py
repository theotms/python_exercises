# Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.
cm = float(input("Write a value in cm: "))

while cm >= 0:
    inch = cm * 0.393701
    print(f"That's equivalent to {inch:.1f} inches.")
    cm = float(input("Write a value in cm: "))

print("Thank you!")

