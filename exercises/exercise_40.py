number = int(input())

current_number = 1
previous_number = 1

inf = 9999

output = "1 1 "

for i in range(inf):
    current_number = current_number + previous_number
    previous_number = current_number - previous_number
    if current_number < number:
        output += f"{current_number} "
    else:
        break

print(output)