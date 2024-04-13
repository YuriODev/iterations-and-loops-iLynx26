number = int(input())

output = 0

for i in range(0, number, 4):
    output += 4/(i - 2)
    output -= 4/i

print(output)
