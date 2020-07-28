import re
from functools import reduce

def is_armstrong(number):
    numbers = re.findall(r'\d', str(number))
    return number == reduce(lambda x, y: x + int(y)**len(numbers), numbers, 0)