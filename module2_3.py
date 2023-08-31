#Write a program that asks the user for the length and width of a rectangle.
#The program then prints out the perimeter and area of the rectangle.
length = float(input("Whats the length of the rectangle? "))
width = float(input("whats the width of the rectangle? "))
peri = 2 * length + 2 * width
area = length * width

print(f"The perimeter is {peri} and the area is {area}")
