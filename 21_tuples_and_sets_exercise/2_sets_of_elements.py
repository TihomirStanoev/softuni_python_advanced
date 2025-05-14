n = list(map(int, input().split()))


sets_dict = {'m': set(), 'n': set()}

for key in sets_dict.keys():
    values_number = n.pop()
    sets_dict[key] = set(input() for _ in range(values_number))

result = sets_dict['m'].intersection(sets_dict['n'])

print(*result, sep='\n')