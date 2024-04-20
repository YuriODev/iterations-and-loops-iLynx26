number_1 = int(input())
number_2 = int(input())

output = ""

for i in range(number_1, number_2):
    if i % 2 == 0:
        output += f"{i} "