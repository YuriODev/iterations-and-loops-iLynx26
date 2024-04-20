n = int(input())

output = 0

for i in range(1, n + 1):
    original_number = i

    reversed_number = 0

    while original_number > 0:

        digit = original_number % 10
        reversed_number = reversed_number * 10 + digit
        original_number //= 10

    if i == reversed_number:
        print(i, end=" ")
