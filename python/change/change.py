from itertools import product

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


