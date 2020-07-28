def primes(limit):
    if limit <= 1:
        return []
    numbers = list(range(2, limit+1))
    primes = []
    while len(numbers) > 0:
        primes.append(numbers[0])
        numbers = list(filter(lambda x: x % numbers[0] != 0, numbers))
    
    return primes
