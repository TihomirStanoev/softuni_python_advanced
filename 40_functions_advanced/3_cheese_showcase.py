def sorting_cheeses(**kwargs):
    result = ''

    cheeses = dict(sorted(kwargs.items(), key=lambda k: (-len(k[1]),k[0])))

    for cheese, qty in cheeses.items():
        result += f"{cheese}\n"
        for qt in sorted(qty, reverse=True):
            result += f'{qt}\n'

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)