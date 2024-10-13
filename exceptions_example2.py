phone = '123456789'
name = 'Ihor'


class WrongNameError(ValueError):
    pass


class WrongPhoneError(ValueError):
    pass

def check_user(name, phone):
    if len(phone) != 10:
        raise WrongNameError
    elif len(name) < 2:
        raise WrongPhoneError
    

try:
    check_user(name, phone)
except WrongNameError:
    pass
except WrongPhoneError:
    pass