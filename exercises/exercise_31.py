lowest_temperature = 999

days = int(input())

temperature = 0

for i in range(days):
    temperature = int(input())
    if temperature < lowest_temperature:
        lowest_temperature = temperature

is_very_cold = lowest_temperature < -15

print(lowest_temperature)
if is_very_cold:
    print("Yes")
else:
    print("No")
