import random

# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
dice = int(input("How many dices do you wanna roll? "))
novo = 0

for i in range(dice):
    xis = random.randrange(1, 7)
    print(f"Rolled {xis}")
    novo += xis

print(f"The sum of your {dice} dices is {novo}")
