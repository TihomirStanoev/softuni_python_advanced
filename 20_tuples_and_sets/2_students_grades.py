students = {}

for _ in range(int(input())):
    student, grade = input().split()
    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student].append(float(grade))


for name, grade in students.items():
    avg_grade = sum(grade) / len(grade)
    print(f"{name} -> {' '.join(f'{x:.2f}' for x in grade)} (avg: {avg_grade:.2f})")