# Write a program that asks the user to enter the names of five cities one by one
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

lista = []

for i in range(1, 6):
    city = input(f"Enter the name of city {i}: ")
    lista.append(city)

print("")

for q in range(len(lista)):
    print(lista[q])
