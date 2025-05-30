def even_odd_filter(**kwargs):
    filtered_numbers = dict(sorted(kwargs.items(), key=lambda kv: kv[0]))

    for command, value_list in filtered_numbers.items():
        if command == 'odd':
            filtered_numbers['odd'] = [x for x in value_list if x % 2 != 0]
        elif command == 'even':
            filtered_numbers['even'] = [x for x in value_list if x % 2 == 0]

    return filtered_numbers



print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))