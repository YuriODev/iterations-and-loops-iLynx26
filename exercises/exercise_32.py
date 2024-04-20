cars = int(input())

cars_following_rules = 0
fastest_car = 0
slowest_car = 999

for i in range(cars):
    speed = int(input())
    if speed < slowest_car:
        slowest_car = speed
    if speed > fastest_car:
        fastest_car = speed
    if speed < 30:
        cars_following_rules += 1

print(fastest_car - slowest_car)
print(cars_following_rules)
