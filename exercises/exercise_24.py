count_even = 0

inputed_number = 1

while inputed_number != 0:
    inputed_number = int(input())
    if inputed_number % 2 == 0 and inputed_number != 0:
        count_even += 1

print(count_even)