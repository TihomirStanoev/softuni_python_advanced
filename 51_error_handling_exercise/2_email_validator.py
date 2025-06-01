from custom_exceptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError


VALID_DOMAINS = ('.com', '.bg', '.net', '.org')


while True:
    email_address = input()
    if email_address == 'End':
        break


    if '@' not in email_address:
        raise MustContainAtSymbolError('Email must contain @')


    if len(email_address.split('@')[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')


    is_valid_domain = False
    for domain in VALID_DOMAINS:
        if email_address.endswith(domain):
            is_valid_domain = True
            break

    if not is_valid_domain:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print(email_address)