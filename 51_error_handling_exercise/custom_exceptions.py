# 02. Email Validator
class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


# 03. Password Validator
class PasswordTooCommonError(Exception):
    pass

class PasswordTooShortError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

# 04. Rotate Matrix
class MatrixContentError(Exception):
    pass

class MatrixSizeError(Exception):
    pass