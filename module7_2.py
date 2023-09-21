# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending
# on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.

name_set = set()

while True:
    name = ""
    try:
        name = str(input("Enter a name (or press Enter to quit): "))
        if name_set.__contains__(name):
            print("The name is already in the list.")
        else:
            print("New name added.")

    except ValueError:
        print("Invalid input. Please enter a valid name.")
    if name == "":
        break
    name_set.add(name)

if name_set:
    print("The names on the list are: ")
    for i in name_set:
        print(i)

else:
    print("No names were entered.")
