def handle_key_error(dictionary: dict[str, int], key: str, command: str) -> None:
    try:
        match command:
            case 'get': print(dictionary[key])
            case 'delete': del dictionary[key]

    except KeyError:
        print('Number does not exist in dictionary')


DELETE_KEY = 'delete'
GET_KEY = 'get'
numbers_dictionary = {}

while True:
    line = input()
    if line == 'Search':
        break
    number_as_string = line

    try:
        number_input = input()
        number = int(number_input)

    except ValueError:
        print('The variable number must be an integer')
        continue

    numbers_dictionary[number_as_string] = number


while True:
    line = input()
    if line == 'Remove':
        break

    searched = line
    handle_key_error(numbers_dictionary, searched, GET_KEY)



while line != "End":
    line = input()
    if line == 'End':
        break

    searched = line
    handle_key_error(numbers_dictionary, searched, DELETE_KEY)
    line = input()

print(numbers_dictionary)