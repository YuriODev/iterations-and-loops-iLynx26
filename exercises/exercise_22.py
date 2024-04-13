number = int(input())

while True:
    if number == 0:
        print(0)
        break
    print(number)
    number = number % 10
