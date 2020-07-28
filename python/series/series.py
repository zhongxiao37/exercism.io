from functools import reduce

def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError('invalid length')
    return [series[i:i+length] for i in range(len(series)-length+1)]