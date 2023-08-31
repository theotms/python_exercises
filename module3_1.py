#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake and notifies
# the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

size = float(input("Whats the size of the zander in centimeters? "))
diff = 42 - size

if size < 42:
    print(f"Please, release the fish back to the lake, it is {diff:.0f}cm smaller than the limit size.")

else:
    print("The size of the fish is fine!")
