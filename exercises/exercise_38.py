number = abs(int(input()))

biggest_digit = 0
smallest_digit = 0

for i in range(10):
    digit = number%(10**(i+1))//(10**i)

    if digit > biggest_digit:
        biggest_digit = digit
    if digit < smallest_digit:
        smallest_digit = digit

    if number//(10**(i)) < 10:
        break

if (biggest_digit - smallest_digit) % 2 == 0:
    print(False)
else:
    print(True)