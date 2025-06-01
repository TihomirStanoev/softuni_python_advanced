from custom_exceptions import PasswordTooCommonError, PasswordTooShortError, PasswordNoSpecialCharactersError, PasswordContainsSpacesError


SPECIAL_CHARACTERS = ('@','*','&','%')
MIN_LENGTH = 8


def is_short(password_len:str) -> bool:
    return len(password_len) < MIN_LENGTH


def is_special(password_special:str, special_tp:tuple) -> map:
    return map(lambda pwd: True if pwd in special_tp else False, password_special)


def space_in_password(passw: str) -> bool:
    return ' ' in passw


def password_too_common_error(current_password:str, special:tuple) ->bool:
    consists_only = {
        'letters': all(map(lambda pwd: pwd.isalpha(), current_password)),
        'digits': all(map(lambda pwd: pwd.isdigit(), current_password)),
        'special characters': all(is_special(current_password, special))}

    return any(consists_only.values())



while True:
    password = input()
    if password == 'Done':
        break


    if is_short(password):
        raise PasswordTooShortError('Password must contain at least 8 characters')

    if space_in_password(password):
        raise PasswordContainsSpacesError('Password must not contain empty spaces')

    if not any(is_special(password, SPECIAL_CHARACTERS)):
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character')

    if password_too_common_error(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')


    print('Password is valid')
