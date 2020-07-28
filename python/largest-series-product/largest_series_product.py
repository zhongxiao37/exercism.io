from functools import reduce
def accumulate_plus(nums):
    return reduce(lambda x, y: x * int(y), nums, 1)

def largest_product(series, size):
    if size < 0:
        raise ValueError('Invalid size')
    whole_series = [series[i:i+size] for i in range(len(series)-size+1)]
    return max(map(accumulate_plus, whole_series))
