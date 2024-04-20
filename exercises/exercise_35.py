number = int(input())

output = ""

for i in range(int((number - 1) * "9") + 1, int(number * "9") + 1):
    if i % 2 == 1:
        output += f"{i} "

print(output)