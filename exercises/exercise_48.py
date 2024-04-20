n = int(input())

output = 0

for i in range(n):
    if len(i) == 1:
        output += 1
    if len(i) == 2:
        if n % 10 == n//10:
            output += 1
    if len(i) == 3:
        if n % 10 == n//100:
            output += 1

print(output)
