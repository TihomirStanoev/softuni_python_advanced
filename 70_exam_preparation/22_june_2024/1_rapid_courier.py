from collections import deque
from string import punctuation


packages_weight = list(map(int, input().split()))
couriers_capacities = deque(map(int, input().split()))
total_weight = 0


while packages_weight and couriers_capacities:
    package = packages_weight.pop()
    courier = couriers_capacities.popleft()

    if courier >= package:
        total_weight += package
        courier -= (package * 2)
        if courier > 0:
            couriers_capacities.append(courier)


    else:
        package -= courier
        total_weight += courier
        if package > 0:
            packages_weight.append(package)

print(f'Total weight: {total_weight} kg')

if not packages_weight and not couriers_capacities:
    print('Congratulations, all packages were delivered successfully by the couriers today.')
elif packages_weight and not couriers_capacities:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages_weight)}")
elif not packages_weight and couriers_capacities:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers_capacities)} but there are no more packages to deliver.")