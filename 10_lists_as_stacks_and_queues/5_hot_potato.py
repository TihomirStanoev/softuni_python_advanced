from collections import deque


kids_names = deque(input().split())
n_toss = int(input())


removed_kid =''
while len(kids_names) != 1:
    kids_names.rotate(-(n_toss-1))
    removed_kid = kids_names.popleft()
    print(f'Removed {removed_kid}')

print(f'Last is {kids_names[0]}')
