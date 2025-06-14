def list_roman_emperors(*args,**kwargs):
    emperors = {}
    result = []

    for emperor, years in kwargs.items():
        for name, status in args:
            if emperor == name:
                emperors[name] = [years, status]


    true_status = {k:v[0] for k,v in emperors.items() if v[1] == True}
    false_status = {k:v[0] for k,v in emperors.items() if v[1] == False}

    true_status = dict(sorted(true_status.items(), key=lambda kv: (-kv[1], kv[0])))
    false_status = dict(sorted(false_status.items(), key=lambda kv: (kv[1], kv[0])))

    result.append(f'Total number of emperors: {len(emperors)}')

    if true_status:
        result.append('Successful emperors:')
        for emperor, years in true_status.items():
            result.append(f'****{emperor}: {years}')

    if false_status:
        result.append('Unsuccessful emperors:')
        for emperor, years in false_status.items():
            result.append(f'****{emperor}: {years}')


    return '\n'.join(result)





print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))