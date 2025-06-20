from collections import deque

total_fuel = list(map(int, input().split()))
consumption_indexes = deque(map(int, input().split()))
needed_quantities = deque(map(int, input().split()))
altitude_succsess = 0
altitude_unsuccess = 0

while total_fuel and consumption_indexes:
    fuel = total_fuel[-1]
    consumption = consumption_indexes[0]
    quantity = needed_quantities[0]


    if fuel - consumption >= quantity:
        total_fuel.pop()
        consumption_indexes.popleft()
        needed_quantities.rotate(-1)
        altitude_succsess += 1
        print(f'John has reached: Altitude {altitude_succsess}')
    else:
        altitude_unsuccess += 1
        print(f'John did not reach: Altitude {altitude_unsuccess + altitude_succsess}')
        break


if altitude_succsess == 0:
    print('John failed to reach the top.\nJohn didn\'t reach any altitude.')
elif not total_fuel and not consumption_indexes:
    print('John has reached all the altitudes and managed to reach the top!')
else:
    print('John failed to reach the top.')
    print(f'Reached altitudes: {(", ".join(f"Altitude {x}" for x in range(1, altitude_succsess+1)))}')
