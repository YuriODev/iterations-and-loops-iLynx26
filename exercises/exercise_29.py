sum_of_squares = 0
normal_sum = 0

while True:
    number = int(input())
    sum_of_squares += number ** 2
    normal_sum += number
    if normal_sum == 0:
        print(sum_of_squares)
        break

