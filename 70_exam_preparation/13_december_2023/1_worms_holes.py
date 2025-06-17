from collections import deque

worms = list(map(int, input().split()))
holes =  deque(map(int, input().split()))
worms_count = len(worms)
matches = 0

while worms and holes:
    if worms[-1] <= 0:
        worms.pop()
        continue

    worm = worms[-1]
    hole = holes[0]

    if worm == hole:
        matches += 1
        worms.pop()
        holes.popleft()
        continue
    else:
        holes.popleft()
        worms[-1] -= 3



if matches:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')

if matches == worms_count:
    print('Every worm found a suitable hole!')

elif not worms and matches != worms_count:
    print('Worms left: none')
elif worms:
    print(f"Worms left: {', '.join(str(w) for w in worms)}")

if not holes:
    print('Holes left: none')
else:
    print(f"Holes left: {', '.join(str(h) for h in holes)}")