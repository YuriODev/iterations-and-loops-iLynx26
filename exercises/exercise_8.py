n = int(input())

line = ""

for i in range(1, n + 1):
    if i % 2 == 0:
        line += str(i) + " " 
    else: 
        continue

print(line)