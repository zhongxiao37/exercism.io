from itertools import combinations

def maximum_value(maximum_weight, items):
    candidates = [i for i in items if i['weight'] <= maximum_weight]
    possible_combinations = []
    for i in range(len(candidates)):
        for comb in combinations(candidates, i):
            if sum(i['weight'] for i in comb) <= maximum_weight:
                possible_combinations.append(comb)

    if len(possible_combinations) == 0:
        return 0
    return max(sum(i['value'] for i in t)
               for t in possible_combinations)