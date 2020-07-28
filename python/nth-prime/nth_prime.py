def prime(number):
    if number < 1:
        raise ValueError('number should not be negative')
    
    prime_list = [2]
    last_prime = prime_list[-1]
    while len(prime_list) < number:
        last_prime += 1
        if last_prime % 2 == 0:
            continue
        elif any(last_prime % e == 0 for e in prime_list):
            continue
        else:
            prime_list.append(last_prime)

    return prime_list[-1]

