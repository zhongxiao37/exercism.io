def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Invalid strand length')
    
    if len(strand_a) == 0 or len(strand_b) == 0:
        return 0
    
    return sum(map(lambda x: 0 if list(strand_a)[x] == list(strand_b)[x] else 1, range(0, len(strand_a))))