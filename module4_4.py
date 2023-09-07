import random
ran = random.randrange(1, 11)
num = int(input("Choose a number from 1 to 10: "))

while num != ran:
    if num > ran:
        print("Too high!")
        num = int(input("Choose a number from 1 to 10: "))
    else:
        print("Too low!")
        num = int(input("Choose a number from 1 to 10: "))

print("You got the number right!")
