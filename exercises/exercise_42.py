numbers_bigger_then_next_number = 1

current_number = 0
previous_number = 0

while True:
    previous_number = current_number
    current_number = int(input())
    if current_number == 0:
        print(numbers_bigger_then_next_number)
        break
    if previous_number > current_number: 
        numbers_bigger_then_next_number += 1

