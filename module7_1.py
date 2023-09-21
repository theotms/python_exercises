# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

seasons = ("spring", "summer", "autumn", "winter")
month = int(input("What's the number of the month? "))

if month == 12 or month <= 2:
    winters = seasons[3]
    print(f"The month number {month} is in {winters}")

elif 3 <= month <= 5:
    springs = seasons[0]
    print(f"The month number {month} is in {springs}")

elif 6 <= month <= 8:
    summers = seasons[1]
    print(f"The month number {month} is in {summers}")

elif 9 <= month <= 11:
    autumns = seasons[2]
    print(f"The month number {month} is in {autumns}")

else:
    print("Enter a valid month number")
