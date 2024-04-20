number = int(input())
digit = int(input())

i = 0
while True:
    if number%10 == digit:
        print(i+1)
        break
    number //= 10
    if number == 0:
        print(0)
        break
    i += 1
