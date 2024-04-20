biggest_number = 0
current_index = 0

biggest_number_index = -1

while True:
    current_number = int(input())
    if current_number >= biggest_number:
        biggest_number = current_number
        biggest_number_index = current_index
    current_index += 1
    if current_number == 0:
        print(biggest_number_index)
        break
