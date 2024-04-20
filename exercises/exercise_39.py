number = abs(int(input()))

sum_of_digits = 0

for i in range(10):
    sum_of_digits += number%(10**(i+1))//(10**i)
    if number//(10**(i)) < 10:
        break

print(sum_of_digits)