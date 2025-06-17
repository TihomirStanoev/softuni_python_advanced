def softuni_students(*args, **kwargs):
    result = []
    students = {}
    invalid_students = []
    for ID, student in args:
        if ID in kwargs.keys():
            students[student] = kwargs[ID]
        else:
            invalid_students.append(student)

    for student, course in sorted(students.items(), key=lambda s: s[0]):
        result.append(f'*** A student with the username {student} has successfully finished the course {course}!')

    if invalid_students:
        invalid_students.sort()
        result.append(f"!!! Invalid course students: {', '.join(invalid_students)}")

    return '\n'.join(result)



print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))