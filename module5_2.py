# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

list_num = []

while True:
    num = input("Add a number to the list (or press Enter to quit): ")

    if num == "":
        break

    if num.isnumeric():
        list_num.append(int(num))

    else:
        print("Invalid input. Please enter a valid number.")

if len(list_num) < 5:
    print("You entered fewer than five numbers.")

else:
    list_max = sorted(list_num, reverse=True)
    print("The five greatest numbers are:", list_max[:5])
