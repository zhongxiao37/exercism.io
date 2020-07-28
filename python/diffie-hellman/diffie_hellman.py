import math
import random

def private_key(p):
    return random.randrange(2,p)


def public_key(p, g, private):
    return g ** private % p


def secret(p, public, private):
    return public ** private % p


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