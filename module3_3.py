gender = str(input("What's your biological gender? "))
hemo = float(input("What's your hemoglobin level in g/l? "))

if gender == "male":
    if 134 <= hemo <= 167:
        print("Value is normal.")

    elif hemo < 134:
        print("Value is lower than normal.")

    else:
        print("Value is higher than normal.")

elif gender == "female":
    if 117 <= hemo <= 155:
        print("Value is normal.")

    elif hemo < 117:
        print("Value is lower than normal.")

    else:
        print("Value is higher than normal.")

else:
    print("Please, enter male or female as a biological gender.")
