number_1 = int(input())
number_2 = int(input())

remainder = -1
divide = -1

for i in range(number_1):
    if i * number_2 > number_1:
        remainder = number_1 - number_2 * (i - 1)
        divide = i - 1
        break

print(f"{divide} {remainder}")