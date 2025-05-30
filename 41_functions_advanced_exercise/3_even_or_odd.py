def even_odd(*args):
    numbers = list(map(int, args[:-1]))
    command = args[-1]

    match command:
        case 'even': return [n for n in numbers if n % 2 == 0]
        case 'odd': return [n for n in numbers if n % 2 != 0]
    return None



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))