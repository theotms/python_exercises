# Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original and the cut-down list.

def even_of_list(input_list):
    for num in input_list:
        if num % 2 != 0:
            input_list.remove(num)
            print(f"{num} was removed from the list because its not even.")


input_str = input("Enter a list of integers separated by spaces: ")

input_list = [int(x) for x in input_str.split()]
print(f"The complete list is {input_list}.")


even_of_list(input_list)
print(f"The list without any uneven number is {input_list}")
