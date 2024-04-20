n = int(input())
m = int(input())

line = ""

for i in range(m):
    line += f"{n}"
    if m != 1:
        line += " "

print(line)