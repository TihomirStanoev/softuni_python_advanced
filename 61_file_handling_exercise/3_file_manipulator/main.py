import os


def create(file_name: str) -> None:
    with open(file_name, 'w') as create_file:
        create_file.write('')


def add(file_name: str, content: str) -> None:
    with open(file_name, 'a') as add_to_file:
        add_to_file.write(f'{content}\n')


def replace(file_name: str, old_string: str, new_string: str) -> None:
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            new_content = content.replace(old_string, new_string)

        with open(file_name, 'w') as file:
            file.write(new_content)

    except FileNotFoundError:
        print(ERROR_MESSAGE)


def delete(file_name: str) -> None:
    try: os.remove(file_name)
    except FileNotFoundError: print(ERROR_MESSAGE)



ERROR_MESSAGE = 'An error occurred'
commands = {
    'Create': create,
    'Add': add,
    'Replace': replace,
    'Delete': delete
}

while True:
    command = input()
    if command == 'End':
        break

    current_command = command.split('-')
    commands[current_command[0]](*current_command[1:])

