# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.

list = []

while True:
    num = ""
    try:
        num = input("Enter a number (or press Enter to quit): ")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    if num == "":
        break
    list.append(num)

if list:

    min = min(list)
    max = max(list)
    print(f"The smallest number is: {min}")
    print(f"The largest number is: {max}")

else:
    print("No numbers were entered.")
