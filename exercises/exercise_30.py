number = int(input())

output = 1

if number > 2:
    for i in range(1, number, 3):
        output *= 2

print(output)