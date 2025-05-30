def concatenate(*args, **kwargs):
    concatenate_string = ''.join(args)

    for k, v in kwargs.items():
        concatenate_string = concatenate_string.replace(k,v)

    return concatenate_string




#print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))