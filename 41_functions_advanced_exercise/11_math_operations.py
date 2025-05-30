from collections import deque

def math_operations(*args,**kwargs):
    result = ''
    mapper = {
        'a': lambda x: kwargs['a'] + x,
        's': lambda x: kwargs['s'] - x,
        'd': lambda x: kwargs['d'] / x if x != 0 else kwargs['d'] / 1,
        'm': lambda x: kwargs['m'] * x,
    }
    dict_keys = deque(kwargs.keys())


    for el in args:
        letter = dict_keys[0]
        kwargs[letter] = mapper[letter](el)
        dict_keys.rotate(-1)

    kwargs = dict(sorted(kwargs.items(), key=lambda kv: (-kv[1],kv[0])))

    for k,v in kwargs.items():
        result+= f"{k}: {v:.1f}"
        result += '\n'

    return result.strip()




print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
