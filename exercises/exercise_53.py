number_1 = int(input())
number_2 = int(input())

number_1 += number_1 % 2 == 1

while number_2 >= number_1:
    print(number_1 , end = " ")

    number_1 += 2
