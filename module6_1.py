#Write a function that returns a random dice roll between 1 and 6.
#The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
#The main program should print out the result of each roll.

import random

def roll():
    val = 0
    while val != 6:
        val = random.randrange(1,7)
        print(f"You rolled {val}")

roll()
