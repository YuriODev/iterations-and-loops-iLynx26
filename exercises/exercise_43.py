biggest_number = 0
second_biggest_number = 0
current_number = 0
infinite_number = 9999

for i in range(infinite_number):
    current_number = int(input())
    if current_number >= biggest_number:
        second_biggest_number = biggest_number
        biggest_number = current_number
    elif current_number > second_biggest_number:
            second_biggest_number = current_number
    if current_number == 0:
        print(second_biggest_number)
