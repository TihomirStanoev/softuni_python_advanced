from collections import deque


def green_check():
    lights = {'green_time': green_sec, 'free_window': free_window}
    hit_char = ''
    crashed = False
    total_cars = 0
    car = ''

    while cars and not crashed:
        if lights['green_time'] > 0:
            car = cars.popleft()
            current_car = deque(car)
            for _ in range(len(current_car)):
                hit_char = current_car.popleft()
                if lights['green_time'] > 0:
                    lights['green_time'] -= 1

                elif lights['free_window'] > 0:
                    lights['free_window'] -= 1

                else:
                    crashed = True
                    break

            total_cars += 1
        else:
            break

    return crashed, hit_char, total_cars, car


green_sec = int(input())
free_window = int(input())
command = input()


cars = deque()
total_passed_cards = 0
is_crashed = False
last_char = ''
the_car = ''

while True:
    if command == 'END' or is_crashed:
        break

    elif command == 'green':
        result = green_check()
        is_crashed = result[0]
        last_char = result[1]
        total_passed_cards += result[2]
        the_car = result[3]

    else:
        cars.append(command)

    command = input()


if is_crashed:
    print(f'A crash happened!\n{the_car} was hit at {last_char}.')
else:
    print(f'Everyone is safe.\n{total_passed_cards} total cars passed the crossroads.')