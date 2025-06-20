def plant_garden(garden_space,*args,**kwargs):
    result = []
    existed_plants = {}
    plants_status = {'planted': 0, 'total': 0}
    planted_plants = {}

    for plant, quantity in kwargs.items():
        for plt, space in args:
            if plt == plant:
                plants_status['total'] += quantity
                existed_plants[plant] = [quantity, space]

    sorted_requests = dict(sorted(existed_plants.items(), key=lambda p: p[0]))
    for plant, data in sorted_requests.items():
        plants_count, needed_space = data
        if needed_space <= garden_space:
            plants = min(int(garden_space//needed_space),plants_count)
            plants_status['planted'] += plants
            planted_plants[plant] = plants
            garden_space -= plants * needed_space


    if plants_status['planted'] == plants_status['total']:
        garden_space = f'{garden_space:.1f}' if garden_space > 0 else '0.0'
        result.append(f'All plants were planted! Available garden space: {garden_space} sq meters.')

    else:
        result.append('Not enough space to plant all requested plants!')

    if planted_plants:
        result.append('Planted plants:')
        for plant, pieces in planted_plants.items():
            result.append(f'{plant}: {pieces}')
    return '\n'.join(result)


print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))