n = int(input())

if n == 0:
    print(0)
else:
    num = 0

    for current_number in range(100, 1000):
        sum_of_digits = 0
        while current_number > 0:
            last_digit = current_number % 10
            sum_of_digits += last_digit
            current_number //= 10

        if sum_of_digits == n:
            num += 1

    print(num)
