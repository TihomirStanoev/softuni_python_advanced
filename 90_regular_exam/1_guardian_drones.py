from collections import deque

def any_drones(dron_dct):
    return list(data['is_build'] for dron, data in dron_dct.items())

def drone_assemble(drones_for_assemble, total_power):
    status = ''
    drone_name = ''
    for dron, data in drones_for_assemble.items():
        if total_power == data['req_power'] and not data['is_build']:
            drones_for_assemble[dron]['is_build'] = True
            drone_name = dron
            status = 'new_drone'
            break
        elif total_power > data['req_power'] and not data['is_build']:
            drones_for_assemble[dron]['is_build'] = True
            status = 'next_possible'
            drone_name = dron
            break

    return drones_for_assemble, status, drone_name


drones = {
'Sentinel-X': {'req_power': 100, 'is_build': False},
'Viper-MKII' : {'req_power': 85, 'is_build': False},
'Aegis-7' : {'req_power': 75, 'is_build': False},
'Striker-R' : {'req_power': 65, 'is_build': False},
'Titan-Core' : {'req_power': 55, 'is_build': False},

}

mechanical_parts = list(map(int,input().split()))
power_cells = deque(map(int,input().split()))
built_drones = []

while not all(any_drones(drones)) and mechanical_parts and power_cells:
    mechanical_part = mechanical_parts.pop()
    power_cell = power_cells.popleft()


    power = mechanical_part+power_cell

    drone_assembled, func_status, name = drone_assemble(drones, power)
    if name:
        built_drones.append(name)

    if func_status == 'new_drone':
        continue

    elif func_status == 'next_possible':
        power_cell -= 30

    else:
        power_cell -= 1


    if power_cell > 0:
        power_cells.append(power_cell)


if all(any_drones(drones)):
    print('Mission Accomplished! All Guardian Drones activated!')
else:
    print('Mission Failed! Some drones were not built.')

if any(any_drones(drones)):
    print(f"Assembled Drones: {', '.join(built_drones)}")

if mechanical_parts:
    mechanical_parts.reverse()
    print(f"Mechanical Parts: {', '.join(str(mp) for mp in mechanical_parts)}")
if power_cells:
    print(f"Power Cells: {', '.join(str(pc) for pc in power_cells)}")