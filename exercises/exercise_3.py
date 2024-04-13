n = int(input())

line = ""

for i in range(20, n + 1):
    line += f"{i}"
    if i < n:
        line += " "

print(line)