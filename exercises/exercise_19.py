n = int(input())

num_lst = ""

for i in range(10, 100):
    digit_1 = i%10
    digit_2 = i//10
    
    if (((digit_1 ** 2) + (digit_2 ** 2)) % n) == 0:
        print(i, end=', ')


print(num_lst)

