def sum_ord(some_name):
    return sum(ord(letter) for letter in some_name)



n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n+1):
    name = input()
    sum_of_values = sum_ord(name) // row
    even_set.add(sum_of_values) if sum_of_values % 2 == 0 else odd_set.add(sum_of_values)


if sum(odd_set) == sum(even_set):
    print(f"{', '.join(str(val) for val in list(odd_set.union(even_set)))}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join(str(val) for val in list(odd_set.difference(even_set)))}")
elif sum(odd_set) < sum(even_set):
    print(f"{', '.join(str(val) for val in list(odd_set.symmetric_difference(even_set)))}")


