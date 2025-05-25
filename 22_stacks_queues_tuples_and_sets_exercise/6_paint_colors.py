from collections import deque

def color_filter(main_found,  secondary_colors):
    filtred_color = []

    for fil_color in main_found:
        if fil_color in secondary_colors.keys():
            if secondary_colors[fil_color](main_found):
                filtred_color.append(fil_color)
        else:
            filtred_color.append(fil_color)

    return filtred_color

def last_char_remove(some_string, all_subs):
    indx = len(some_string)//2

    for s in reversed(all_subs):
        cut = s[:-1]
        if cut:
            some_string.insert(indx, cut)

    return some_string




substring = deque(input().split())
all_colors = []

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange':  lambda lst: 'red' in lst and 'yellow' in lst,
    'purple': lambda lst: 'red' in lst and 'blue' in lst,
    'green': lambda lst: 'yellow' in lst and 'blue' in lst,
}


while substring:
    color = ''
    subs = [substring.popleft(), substring.pop() if len(substring) > 0 else '']

    for index, col in enumerate(subs, start=-1):
        color = col + subs[index]

        if (color in main_colors or color in secondary_colors.keys()) and color not in all_colors:
            all_colors.append(color)
            break
    else:
        substring = last_char_remove(substring, subs)


all_colors = color_filter(all_colors,secondary_colors)

print(all_colors)

