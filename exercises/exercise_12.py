n = int(input())

num = 0

for i in range(100, 1000):
    if i % n == 0:
        num += i

print(num)