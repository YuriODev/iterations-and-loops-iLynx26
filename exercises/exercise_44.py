biggest_number = 0
current_number = 0

biggest_number_index = -1

infinite_number = 9999

for i in range(infinite_number):
    current_number = int(input())
    if current_number >= biggest_number:
        biggest_number = current_number
        biggest_number_index = i
    if current_number == 0:
        print(biggest_number_index)
