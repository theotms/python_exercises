#Write a program that asks the user for three integer numbers.
#The program prints out the sum, product, and average of the numbers.

num1 = int(input("Write the first integer number: "))
num2 = int(input("Now the second integer number: "))
num3 = int(input("Now the third integer number: "))

soma = num1 + num2 + num3
produto = num1 * num2 * num3
average = soma / 3

print(f"The sum is {soma}, the product is {produto} and the average is {average:.2f}")
