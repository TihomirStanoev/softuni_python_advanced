from custom_exceptions import MoneyNotEnoughError, PINCodeError, UnderageTransactionError,MoneyIsNegativeError


def money_validation(acc_balance, sent_money):
    if sent_money > acc_balance:
        raise MoneyNotEnoughError('Insufficient funds for the requested transaction')
    return True

def pin_validation(acc_pin, given_pin):
    if acc_pin != given_pin:
        raise PINCodeError('Invalid PIN code')
    return True

def age_validation(acc_age, adult):
    if acc_age < adult:
        raise UnderageTransactionError('You must be 18 years or older to perform online transactions')
    return True

def is_negative(receive):
    if receive < 0:
        raise MoneyIsNegativeError('The amount of money cannot be a negative number')
    return True


def send_money(acc_balance, money_am):
    new_balance = acc_balance - money_am

    print(f'Successfully sent {money_am:.2f} money to a friend')
    print(f'There is {new_balance:.2f} money left in the bank account')

    return new_balance

def receive_money(acc_balance, received_money, invest):
    money_to_receive = received_money * invest
    new_balance = acc_balance + money_to_receive

    print(f'{money_to_receive:.2f} money went straight into the bank account')

    return new_balance



account_info = input().split(', ')
pin_code, balance, age = account_info[0], float(account_info[1]), int(account_info[2])
ADULT_AGE = 18
invest_percentage = 0.5


while True:
    command = input()
    if command == 'End':
        break
    commands = command.split('#')
    action, money = commands[0], float(commands[1])

    if action == 'Send Money':
        pin = commands[2]

        enough_money = money_validation(balance, money)
        is_valid_pin = pin_validation(pin_code, pin)
        is_adult = age_validation(age, ADULT_AGE)

        if enough_money and is_valid_pin and is_adult:
            balance = send_money(balance, money)

    elif action == 'Receive Money':
        if is_negative(money):
            balance = receive_money(balance, money, invest_percentage)
