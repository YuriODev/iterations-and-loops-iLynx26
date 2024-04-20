number_1 = int(input())
number_2 = int(input())

number_1 -= number_1 % 2 == 0

while number_1 >= number_2:
    print(number_1 , end = " ")
    number_1 -= 2
