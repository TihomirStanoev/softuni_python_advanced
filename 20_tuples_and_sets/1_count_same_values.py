numbers = list(map(float,input().split()))

num_set = set(numbers)

for num in numbers:
    if num in num_set:
        print(f'{num:.1f} - {numbers.count(num)} times')
        num_set.remove(num)

