import math

def classify(number):
    if number < 1:
        raise ValueError('invalid number')
    factors = parse_factors(number)

    if sum(factors) == number and number !=  1:
        return 'perfect'
    elif sum(factors) > number:
        return 'abundant'
    else:
        return 'deficient'


def parse_factors(number):
    factors = [1]
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    return factors