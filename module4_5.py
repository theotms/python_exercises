login = input("Login: ")
password = input("Password: ")

if login != "python" or password != "rules":
    i = 0
    while login != "python" or password != "rules":
        i = i + 1
        print("Wrong credentials, try again!")
        login = input("Login: ")
        password = input("Password: ")
        if i == 4:
            print("You tried too many times!")
            break
    print("Welcome!")

else:
    print("Welcome!")
