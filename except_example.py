def bad_function():
    try:
        result = 1000 / 0
    except ZeroDivisionError:
        result = 0
    return result


# user = {'name': 'Ihor', 'phone': 123456789, 'country': 'Ukraine'}
def process_user(user):
    try:
        process_phone(user['phone'])
    except ValueError:
         pass
    pass

# 1234567890
def process_phone(phone):
    # try:
        raise ValueError
    # except ValueError:
    #     raise ValueError('phone format is not valid')

print(bad_function())