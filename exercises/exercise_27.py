number = int(input())

output = 0

for i in range(1, number, 4):
    output += 4/(i - 2)
    output -= 4/i

print(output)
