def create_set(txt):
    a, b = txt.split(',')
    return set(range(int(a), int(b)+1))



longest_intersection = set()

for _ in range(int(input())):
    range_a, range_b = list(input().split('-'))

    range_a = create_set(range_a)
    range_b = create_set(range_b)

    range_intersection = range_a.intersection(range_b)

    if len(range_intersection) > len(longest_intersection):
        longest_intersection = range_intersection


print(f'Longest intersection is {list(sorted(longest_intersection))} with length {len(longest_intersection)}')