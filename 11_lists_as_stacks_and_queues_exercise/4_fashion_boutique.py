box_clothes = list(map(int,input().split()))
rack_capacity = int(input())

'''
5 4 8 6 3 8 7 7 9
16
1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20
'''

total_racks = 0

clothes = []

while box_clothes:
    current_clothes = box_clothes.pop()

    if sum(clothes) + current_clothes <= rack_capacity:
        clothes.append(current_clothes)
        continue

    box_clothes.append(current_clothes)
    total_racks += 1
    clothes.clear()


if clothes:
    total_racks += 1

print(total_racks)
