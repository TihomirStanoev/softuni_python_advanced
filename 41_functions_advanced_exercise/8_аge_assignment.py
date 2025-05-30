def age_assignment(*args, **kwargs):
    names = {}

    for name in args:
        if name[0] in kwargs.keys():
            names[name] = kwargs[name[0]]

    sorted_names = sorted(names.items(), key=lambda kv: kv[0])


    return '\n'.join(f'{name} is {age} years old.' for name,age in sorted_names)





print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))