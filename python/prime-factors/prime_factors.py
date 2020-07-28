import math

def factors(value):
    if value < 2:
        return []
    if is_prime(value):
        return [value]
    
    prime_factors = []
    last_prime = 2
    while last_prime <= math.floor(math.sqrt(value)):
        if value % last_prime == 0:
            prime_factors.append(last_prime)
            value = value // last_prime
        else:
            last_prime += 1
            while not is_prime(last_prime):
                last_prime += 1
        
    prime_factors.append(value)

    return prime_factors


def is_prime(num):
    if num < 2:
        return False 
    if num % 2 == 0:
        return num == 2 
    if num % 3 == 0:
        return num == 3
    if num < 9:
        return True 
    for e in range(5, math.floor(math.sqrt(num)), 2):
        if num % e == 0:
            return False
    return True