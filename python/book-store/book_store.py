from itertools import groupby

BOOK_PRICES = {
    1: 800,
    2: 1520,
    3: 2160,
    4: 2560,
    5: 3000
}

def total(basket):
    if len(basket) == 0:
        return 0

    groups = [list(g) for k, g in groupby(sorted(basket))]
    groups.sort(key=lambda x: len(x), reverse=True)
    
    min_size = len(groups[-1])
    if min_size > 1 and all(len(g) % min_size == 0 for g in groups):
        groups = list(map(lambda x: x[0:(len(x) // min_size)], groups))
    else:
        min_size = 1

    basket_by_group = [[] for i in groups[0]]
    for g in groups:
        if len(g) == 1:
            break
        for i in range(len(g)):
            basket_by_group[i].append(g[i])
    remaning_groups = list(filter(lambda x: len(x) == 1, groups))
    if len(basket_by_group[0]) == 2 and len(remaning_groups) == 2:
        for x in remaning_groups:
            basket_by_group[0].append(x[0]) 
    else:
        for i in range(len(remaning_groups)):
            basket_by_group[i%len(basket_by_group)].append(remaning_groups[i][0])

    total_price = sum(map(lambda x: BOOK_PRICES[len(x)], basket_by_group)) * min_size

    return total_price

