number = int(input())
digit = int(input())

if digit in number.split(""):
    for i in range(10):
        if i%(10**(i+1))//(10**i) == digit:
            print(i+1)
else:
    print(0)
