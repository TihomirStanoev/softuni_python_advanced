n = int(input())


elements = []
for _ in range(n):
    line_elements = input().split()
    elements.extend(line_elements)

unique_elements = set(elements)

print(*unique_elements, sep='\n')