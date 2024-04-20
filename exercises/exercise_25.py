distance_covered_first_day = int(input())
target_distance = int(input())
current_distance_covered = 0.00
distance_covered_today = distance_covered_first_day

current_day = 1

while True:
    current_distance_covered += distance_covered_today
    distance_covered_today = distance_covered_today * 1.1
    if current_distance_covered >= target_distance:
        print(f"{current_distance_covered:.2f} km, {current_day} days")
        break
    current_day += 1
