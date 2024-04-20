sign_changed = 0


current_number = 0
previous_number = 0

while True:
    current_number = int(input())
    if current_number == 0:
        print(sign_changed)
        break
    elif previous_number == 0:
        continue
    else:
        if previous_number/abs(previous_number) + current_number/abs(current_number) == 0:
            sign_changed += 1

