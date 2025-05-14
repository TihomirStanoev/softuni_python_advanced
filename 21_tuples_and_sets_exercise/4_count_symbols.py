text = list(input())


keys = set(text)

for key in sorted(keys):
    total = text.count(key)
    print(f'{key}: {total} time/s')
