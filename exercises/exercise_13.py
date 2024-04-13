password = int(input("Please enter your password: "))

while True:
    password_guess = int(input("Please enter your password: "))
    if password_guess == password:
        print("Done")
        break
    else:
        print("Error")