# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
i = 1
while i != 1001:
    i += 1
    if i % 3 == 0:
        print(i)
