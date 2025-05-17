from collections import deque

def str_print(some_list):
    return " ".join(list(map(str, some_list)))

cups_capacity = deque(map(int, input().split()))
bottles_capacity = list(map(int, input().split()))

wasted_liters = 0

while cups_capacity and bottles_capacity:
    cup = cups_capacity.popleft()

    while cup > 0:
        current_bottle = bottles_capacity.pop()
        cup -= current_bottle
        wasted_liters += abs(cup) if cup < 0 else 0



if bottles_capacity:
    bottles = str_print(bottles_capacity)
    print(f'Bottles: {bottles}')
elif cups_capacity:
    cups = str_print(cups_capacity)
    print(f'Cups: {cups}')

print(f'Wasted litters of water: {wasted_liters}')