def steps(number):
    if number <= 0:
        raise ValueError('number should be positive integer')
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        counter += 1
    
    return counter
