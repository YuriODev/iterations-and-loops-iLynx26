sum = 0

inputed = 1
num_of_inputs = 0

while inputed != 0:
    inputed = int(input())
    sum += inputed
    if inputed != 0:
        num_of_inputs += 1

if num_of_inputs != 0:
    print(sum/num_of_inputs)
else: 
    print(0)
