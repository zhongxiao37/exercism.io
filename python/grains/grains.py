def square(number):
    if number < 1 or number > 64:
        raise ValueError('Invalid number')
    return 2 ** (number - 1)


def total(number):
    if number < 1 or number > 64:
        raise ValueError('Invalid number')
    return 2 ** 64 - 1
