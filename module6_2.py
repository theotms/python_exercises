# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues until the program
# gets the maximum number on the dice, which is asked from the user at the beginning.

import random

sides = int(input("How many sides does your dice has? "))


def roll(sides):
    val = 0
    while val != sides:
        val = random.randrange(1, sides+1)
        print(f"You rolled {val}")


roll(sides)
