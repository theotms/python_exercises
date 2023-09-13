# Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.

num = int(input("Give me an integer number: "))

if num > 1:
    is_prime = True
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")

    else:
        print(num, "is not a prime number.")

else:
    print(num, "is not a prime number.")

