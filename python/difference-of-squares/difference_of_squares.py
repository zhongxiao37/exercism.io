
def square_of_sum(number):
    number_sum = sum([i for i in range(1, number+1)])
    return number_sum ** 2


def sum_of_squares(number):
    return sum([i ** 2 for i in range(1, number+1)])


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
