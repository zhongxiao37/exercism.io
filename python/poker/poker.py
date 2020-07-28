from itertools import groupby

RANKING_CATEGORIES = {
    'straight_flush': 9,
    'square': 8,
    'full': 7,
    'flush': 6,
    'straight': 5,
    'three': 4,
    'two_pairs': 3,
    'one_pair': 2,
    'high_card': 1
  }

CARD_RANKING = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
  }

def best_hands(hands):
    ranked_hands = [Hand(hand) for hand in hands]
    ranked_hands.sort(key=lambda x: [x.rank, x.points], reverse=True)
    best_hands = list(filter(lambda h: h.rank == ranked_hands[0].rank, ranked_hands))
    if len(best_hands) == 1:
        return [b.orig_cards for b in best_hands]
    else:
        return [b.orig_cards for b in filter(lambda h: h.points == best_hands[0].points, best_hands)]


class Hand():
    def __init__(self, cards):
        self.orig_cards = cards
        self.cards = cards.split(' ')
        self.card_numbers = self.card_numbers()
        self.card_number_groups = [[k, list(g)] for k, g in groupby(self.card_numbers)]
        self.rank = self.rank()
        self.points = self.points()
    
    def rank(self):
        return max([v if getattr(self, k)() else 0 for k, v in RANKING_CATEGORIES.items()])
    
    def points(self):
        if self.square():
            return list(filter(lambda g: len(g[1]) == 4, self.card_number_groups))[0][1] + [t[0] for t in list(filter(lambda g: len(g[1]) == 1, reversed(self.card_number_groups)))]
        elif self.three():
            return list(filter(lambda g: len(g[1]) == 3, self.card_number_groups))[0][1] + [t[0] for t in list(filter(lambda g: len(g[1]) == 1, reversed(self.card_number_groups)))]
        elif self.full():
            return list(filter(lambda g: len(g[1]) == 3, self.card_number_groups))[0][1] + list(filter(lambda g: len(g[1]) == 2, self.card_number_groups))[0][1]
        elif self.two_pairs() or self.one_pair():
            return [t[0] for t in list(filter(lambda g: len(g[1]) == 2, reversed(self.card_number_groups)))] + [t[0] for t in list(filter(lambda g: len(g[1]) == 1, reversed(self.card_number_groups)))]
        elif self.straight():
            return 1 if self.card_numbers == [2,3,4,5,14] else min(self.card_numbers)
        else:
            return list(reversed(self.card_numbers))

    
    def card_numbers(self):
        card_numbers = [CARD_RANKING[card[0:-1]] for card in self.cards]
        card_numbers.sort()
        return card_numbers

    def straight_flush(self):
        return self.straight() and self.flush()

    def flush(self):
        return len(set([card[-1] for card in self.cards])) == 1
    
    def straight(self):
        return self.all_5_different_numbers() and (max(self.card_numbers) - min(self.card_numbers) == 4 or self.card_numbers == [2,3,4,5,14])

    def square(self):
        return any(len(v) == 4 for k, v in self.card_number_groups)

    def full(self):
        return any(len(v) == 3 for k, v in self.card_number_groups) and any(len(v) == 2 for k, v in self.card_number_groups)

    def three(self):
        return any(len(v) == 3 for k, v in self.card_number_groups) and len(self.card_number_groups) == 3
    
    def two_pairs(self):
        return any(len(v) == 2 for k, v in self.card_number_groups) and len(self.card_number_groups) == 3
    
    def one_pair(self):
        return len(self.card_number_groups) == 4
    
    def high_card(self):
        return self.all_5_different_numbers() and not self.straight()

    def all_5_different_numbers(self):
        return len(self.card_number_groups) == 5
