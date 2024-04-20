sign_changed = 0

previous_number = int(input())

while True:
    current_number = int(input())

    print(f"{previous_number = } {current_number = } {sign_changed = }")
    if current_number == 0:
        print(sign_changed)
        break

    elif previous_number/abs(previous_number) + current_number/abs(current_number) == 0:
        # if previous_number * current_number < 0:
        sign_changed += 1

    previous_number = current_number 
