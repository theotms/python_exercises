# Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


input_str = input("Enter a list of integers separated by spaces: ")

input_list = [int(x) for x in input_str.split()]
print(f"The list is {input_list}.")

result = sum_of_list(input_list)
print(f"The sum of the list is: {result}")
