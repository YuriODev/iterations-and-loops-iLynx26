number = int(input())

output = ""

if number != 1:
    minimum_digit = int((number - 1) * "9") + 1
else:
    minimum_digit = 1
maximum_digit = int(number * "9") + 1

for i in range(maximum_digit, minimum_digit - 1, -1):
    if i % 2 == 1:
        output += f"{i} "

print(output)