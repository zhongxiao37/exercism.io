from itertools import product
import time


def time_it(mode='simple'):
    def decorator(func):
        def clock(*args):
            t0 = time.time()
            result = func(*args)
            elapsed = time.time() - t0
            arg_str = ','.join(repr(arg) for arg in args)
            if mode == 'simple':
                output = '%s Total time: %0.8f sec' % (func.__name__, elapsed)
            else:
                output = '%s(%s) = %s Total time: %0.8f sec' % (func.__name__, arg_str, result, elapsed)
            print(output)
            return result
        return clock
    return decorator


def find_fewest_coins(coins, target):
    if target == 0:
        return []
    if target < min(coins):
        raise ValueError('target should be larger than minium coin')
    
    # check if the largets coin can be fully divided by other coins
    # if yes, figure out as many max_coins as possible
    max_coin = max(coins)
    if all(max_coin % c == 0 for c in coins) and target > max_coin:
        fewest_coins = find_fewest_coins(coins, target % max_coin)
        return fewest_coins + [max_coin] * (target // max_coin)

    m = [[]] + [None] * target
    combinations = product(range(len(coins)), range(1, target + 1))
    for c, t in combinations:
        if coins[c] == t:
            m[t] = [coins[c]]
        else:
            existing_coins = [t2 for t2 in range(1, t) if coins[c] + t2 == t and m[t2] is not None]
            for t2 in existing_coins:
                if m[t] is None or len(m[t2]) + 1 < len(m[t]):
                    m[t] = m[t2] + [coins[c]]
    
    if m[target] is None:
        raise ValueError('no combination')
    else:
        return m[target]


@time_it('simple')
def change_dynamic(coins, target):
    memo = [None] * (target+1)
    memo[0] = []
    for i in range(1, target+1):
        res = None
        for coin in coins:
            if coin > i: continue
            tmp = memo[i-coin]
            if tmp is None: continue
            if res is None or len(res) > len(tmp):
                res = tmp + [coin]
        memo[i] = res

    return memo[target]


@time_it('simple')
def change(coins, target):
    memo = dict()
    def dp(n):
        if n in memo:
            return memo[n]
        if n < 0:
            return None
        res = None
        for coin in coins:
            if n == coin:
                res = [coin]
            else:
                subproblem = dp(n - coin)
                if subproblem is None: continue
                if res is None or len(res) > len(subproblem):
                    res = subproblem + [coin]
        
        memo[n] = res
        return res
    return dp(target)


coins = [1, 2, 5, 10, 20, 25, 50, 100]
target = 96
print(change(coins, target))

print(change_dynamic(coins, target))