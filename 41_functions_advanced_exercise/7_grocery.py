def grocery_store(**kwargs):
    sort_one = sorted(kwargs.items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))
    return '\n'.join(f'{k}: {v}' for k,v in sort_one)



print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))