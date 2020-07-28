import itertools

def convert(number):
    if number == 1:
        return '1'
    
    RAIN_DROPS_MAPPING = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    primes = [1, number]
    primes += list(filter(lambda x: number % x == 0, range(2,number)))
    primes.sort()

    mapping_list = list(map(lambda e: RAIN_DROPS_MAPPING[e], filter(lambda x: x in RAIN_DROPS_MAPPING.keys(), primes)))
    if len(mapping_list) == 0:
        return str(number)
    return ''.join(mapping_list)
