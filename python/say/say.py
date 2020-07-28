NUM = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1_000_000: 'million',
    1_000_000_000: 'billion'
  }

def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError('Negative number')

    if number == 0:
        return NUM[number]

    number_groups = []
    i = 0
    while number > 0:
        m = number % 1000
        if m > 0:
            if i > 0:
                number_groups.insert(0, NUM[1000**i])
            number_groups.insert(0, say_under_1000_num(m))
  
        number = number // 1000
        i += 1
    
    return ' '.join(number_groups)


def say_under_1000_num(num):
    a = num // 100
    b = num % 100
    num_groups = []
    if a > 0:
        num_groups.append(NUM[a] + ' hundred')
    if b > 0:
        num_groups.append(say_under_100_num(b))
    
    return ' and '.join(num_groups)

def say_under_100_num(num):
    if num in NUM.keys():
        return NUM[num]

    num_groups = []
    a = num // 10 * 10
    b = num % 10
    if a > 0:
        num_groups.append(NUM[a])
    if b > 0:
        num_groups.append(NUM[b])
    
    return '-'.join(num_groups)