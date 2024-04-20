number = abs(int(input()))


if number == 0 :
    print(False)

else:
    biggest_digit = 0
    smallest_digit = 9

    i = 0
    while True:
        digit = number % 10
        #digit = number % (10**(i+1)) // (10**i)

        if digit > biggest_digit:
            biggest_digit = digit
        if digit < smallest_digit:
            smallest_digit = digit

        number //= 10
        if number == 0:
            break

    print(f"{biggest_digit = } {smallest_digit =}")

    if (biggest_digit - smallest_digit) % 2 != 0:
        print(False)
    else:
        print(True)