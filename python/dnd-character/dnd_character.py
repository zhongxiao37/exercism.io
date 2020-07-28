from math import floor
import random

class Character:
    def __init__(self):
        random.seed()
        for i in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            exec(f'self.{i}={self.ability()}')
        self.hitpoints = 10 + modifier(self.constitution)

    
    def ability(self):
        scores = [random.randrange(1,7) for _ in range(4)]
        scores.remove(min(scores))
        return sum(scores)


def modifier(constitution):
    return floor((constitution - 10) / 2)