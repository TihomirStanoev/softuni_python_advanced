from collections import  deque


def get_input():
    petrol_qty, distance = input().split()
    return int(petrol_qty), int(distance)


pumps = deque(get_input() for _ in range(int(input())))

for pump_number in range(len(pumps)):
    fuel = 0
    finish = False
    for pump in pumps:
        fuel += pump[0]
        next_pump = pump[1]
        if fuel >= next_pump:
            fuel -= next_pump
            finish = True
        else:
            finish = False
            break

    if finish:
        print(pump_number)
        break

    pumps.rotate(-1)
