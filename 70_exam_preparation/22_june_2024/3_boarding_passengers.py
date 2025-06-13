def boarding_passengers(capacity, *args):
    benefit_plans = {}
    total_passengers = 0
    all_passengers = 0
    result = 'Boarding details by benefit plan:\n'

    for passengers, plane in args:
        current_passengers = total_passengers
        total_passengers += passengers
        all_passengers += passengers

        if total_passengers <= capacity:
            if plane not in benefit_plans.keys():
                benefit_plans[plane] = passengers
            else:
                benefit_plans[plane] += passengers
        else:
            total_passengers = current_passengers

    for cl, ps in sorted(benefit_plans.items(), key=lambda gp: (-gp[1], gp[0])):
        result += f'## {cl}: {ps} guests\n'

    if capacity < total_passengers or capacity == all_passengers:
        result += 'All passengers are successfully boarded!'
    elif capacity == total_passengers:
        result += 'Boarding unsuccessful. Cruise ship at full capacity.'
    elif capacity > total_passengers:
        result += f'Partial boarding completed. Available capacity: {capacity - total_passengers}.'

    return result



print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))