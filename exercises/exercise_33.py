n = int(input('Please, give me your number: '))
a = 0
b = n - 1


for i in range(n):
    print('-1\t' * a + '0\t' + '1\t' * b)
    a += 1
    b -= 1