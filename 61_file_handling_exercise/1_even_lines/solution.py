def change_char(old_word: str) ->str:
    return ''.join('@' if letter in  "-,.!?" else letter for letter in old_word)


with open('text.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        if i % 2 == 0:
            reversed_line = line.split()[::-1]
            print(' '.join(change_char(word) for word in reversed_line))
