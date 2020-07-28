import itertools

def full_house(dice):
    group_num = list(list(g) for k, g in itertools.groupby(dice))
    if any(len(k) == 2 for k in group_num) and any(len(k) == 3 for k in group_num):
        return sum(dice)
    else:
        return 0

def four_of_a_kind(dice):
    group_num = list(list(g) for k, g in itertools.groupby(dice))
    if any(len(k) >= 4 for k in group_num):
        return sum(list(filter(lambda x: len(x) >= 4, group_num))[0][:4])
    else:
        return 0

def little_straight(dice):
    if len(set(dice)) == 5 and dice[-1] == 5:
        return 1
    else:
        return 0

def big_straight(dice):
    if len(set(dice)) == 5 and dice[0] == 2:
        return 1
    else:
        return 0


# Score categories
# Change the values as you see fit
YACHT = { 'check': lambda x: 1 if len(set(x)) == 1 else 0, 'score': 50 }
ONES = { 'check': lambda x: len(list(filter(lambda y: y == 1, x))), 'score': 1 }
TWOS = { 'check': lambda x: len(list(filter(lambda y: y == 2, x))), 'score': 2 }
THREES = { 'check': lambda x: len(list(filter(lambda y: y == 3, x))), 'score': 3 }
FOURS = { 'check': lambda x: len(list(filter(lambda y: y == 4, x))), 'score': 4 }
FIVES = { 'check': lambda x: len(list(filter(lambda y: y == 5, x))), 'score': 5 }
SIXES = { 'check': lambda x: len(list(filter(lambda y: y == 6, x))), 'score': 6 }
FULL_HOUSE = { 'check': full_house, 'score': 1 }
FOUR_OF_A_KIND = { 'check': four_of_a_kind, 'score': 1} 
LITTLE_STRAIGHT = { 'check': little_straight, 'score': 30 }
BIG_STRAIGHT = { 'check': big_straight, 'score': 30 }
CHOICE = { 'check': lambda x: sum(x), 'score': 1 }


def score(dice, category):
    dice.sort()
    return category['score'] * category['check'](dice)

