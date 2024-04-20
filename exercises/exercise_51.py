number_1 = int(input())
number_2 = int(input())

output = ""

for i in range(number_1, number_2):
    i1 = i%10
    i2 = i%100//10
    i3 = i%1000//100
    i4 = i//1000
    if i1 == i2 == i3 or i1 == i2 == i4 or i2 == i3 == i4 or i1 == i3 == i4:
        output += f"{i} "

print(output)