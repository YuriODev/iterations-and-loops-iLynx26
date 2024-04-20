number_1 = int(input())
number_2 = int(input())

gcd = 1

for i in range(1, number_2 + number_1):
    if number_1 % i == 0 and number_2 % i == 0:
        if gcd < i:
            gcd = i

print(gcd)