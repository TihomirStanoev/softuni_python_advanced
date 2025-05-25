from collections import deque

def is_pair(pres):
    pair_one = pres['Doll']['count'] and pres['Wooden train']['count']
    pair_two = pres['Teddy bear']['count'] and pres['Bicycle']['count']

    return True if pair_one or pair_two else False




materials_for_crafting = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))
presents = {
    'Bicycle': {'magic': 400, 'count': 0},
    'Doll': {'magic': 150, 'count': 0},
    'Teddy bear': {'magic': 300, 'count': 0},
    'Wooden train': {'magic': 250, 'count': 0},
}
prices = set(price['magic'] for price in presents.values())


while materials_for_crafting and magic_level:
    material = materials_for_crafting[-1]
    magic = magic_level[0]
    product = material * magic


    if material == 0 and magic == 0:
        magic_level.popleft()
        materials_for_crafting.pop()
        continue
    elif magic == 0:
        magic_level.popleft()
        continue
    elif material == 0:
        materials_for_crafting.pop()
        continue


    if product in prices:
        for present in presents.values():
            if present['magic'] == product:
                present['count'] += 1
                break

        materials_for_crafting.pop()
        magic_level.popleft()

    elif product not in prices and product > 0:
        magic_level.popleft()
        materials_for_crafting[-1] += 15

    elif product < 0:
        product = materials_for_crafting.pop() + magic_level.popleft()
        materials_for_crafting.append(product)




if is_pair(presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_for_crafting:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials_for_crafting))}")


if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for present in presents.keys():
    if presents[present]['count'] > 0:
        print(f"{present}: {presents[present]['count']}")