n = int(input())

output = ""

for i in range(n):
    if len(i) == 1:
        output += i
    if len(i) == 2:
        if n % 10 == n//10:
            output += i
    if len(i) == 3:
        if n % 10 == n//100:
            output += i

print(output)
