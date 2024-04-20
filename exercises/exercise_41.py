number = int(input())

current_number = 1
previous_number = 0

for i in range(number-1):
    current_number = current_number + previous_number
    previous_number = current_number - previous_number

print(current_number)


