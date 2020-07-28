from functools import reduce

def sum_of_multiples(limit, multiples):
    num_of_multiples = set()
    for m in filter(lambda x: x != 0, multiples):
        num_of_multiples.update(list(range(m, max([limit, m]), m)))
    return sum(num_of_multiples)
