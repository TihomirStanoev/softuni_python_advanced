def cookbook(*args):
    cuisine_dict = {}
    result = []

    for recepie, cuisine, ingredient in args:
        if cuisine not in cuisine_dict.keys():
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append({recepie: ingredient})

    cuisine_sorted = dict(sorted(cuisine_dict.items(), key= lambda k: (-len(k[1]), k[0]) ))


    for cuisine, recepies in cuisine_sorted.items():
        result.append(f'{cuisine} cuisine contains {len(recepies)} recipes:')
        recepie_dict = {}
        for recepie in recepies:
            for r, i in recepie.items():
                recepie_dict[r] = i
        recepie_dict = dict(sorted(recepie_dict.items(), key=lambda k: k[0]))
        for recepie, ingredient in recepie_dict.items():
            result.append(f"  * {recepie} -> Ingredients: {', '.join(ingredient)}")

    return '\n'.join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))