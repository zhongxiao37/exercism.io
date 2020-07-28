from itertools import permutations
from dataclasses import dataclass

@dataclass
class House():

    index: int
    resident: str = None
    color: str = None
    drink: str = None
    pet: str = None
    smoke: str = None
    

def solve():
    orders = list(range(5))
    residents = ['Norwegian', 'Ukrainian', 'Englishman', 'Spaniard', 'Japanese']
    colors = ['yellow', 'blue', 'red', 'ivory', 'green']
    drinks = ['water', 'tea', 'milk', 'orange_juice', 'coffee']
    pets = ['fox', 'horse', 'snail', 'dog', 'zebra']
    smokes = ['Kools', 'Chesterfields', 'Old Gold', 'Lucky Strike', 'Parliaments']

    # reverse here to use max loop to test the performance
    # otherwise, only one loop is executed since above order is the answer
    residents.reverse()
    colors.reverse()
    drinks.reverse()
    pets.reverse()
    smokes.reverse()

    houses = None
    for res in permutations(residents):
        houses = [House(index, res[index]) for index in orders]
        if houses[0].resident == 'Norwegian':
            for color in permutations(colors):
                houses = [House(index, res[index], color[index]) for index in orders]
                if any(house.color == 'red' and house.resident == 'Englishman' for house in houses):
                    if houses[1].color == 'blue':
                        if any(house.color == 'green' and house.index > 0 and houses[house.index - 1].color == 'ivory' for house in houses):
                            for drink in permutations(drinks):
                                houses = [House(index, res[index], color[index], drink[index]) for index in orders]
                                if houses[2].drink == 'milk':
                                    if any(house.drink == 'coffee' and house.color == 'green' for house in houses):
                                        if any(house.resident == 'Ukrainian' and house.drink == 'tea' for house in houses):
                                            for pet in permutations(pets):
                                                houses = [House(index, res[index], color[index], drink[index], pet[index]) for index in orders]
                                                if any(house.pet == 'dog' and house.resident == 'Spaniard' for house in houses):
                                                    for smoke in permutations(smokes):
                                                        houses = [House(index, res[index], color[index], drink[index], pet[index], smoke[index]) for index in orders]
                                                        if any(house.smoke == 'Old Gold' and house.pet == 'snail' for house in houses):
                                                            if any(house.color == 'yellow' and house.smoke == 'Kools' for house in houses):
                                                                if any(house.smoke == 'Lucky Strike' and house.drink == 'orange_juice' for house in houses):
                                                                    if any(house.resident == 'Japanese' and house.smoke == 'Parliaments' for house in houses):
                                                                        if any(abs(a.index - b.index) == 1 and a.smoke == 'Chesterfields' and b.pet == 'fox' for a in houses for b in houses):
                                                                            if any(abs(a.index - b.index) == 1 and a.smoke == 'Kools' and b.pet == 'horse' for a in houses for b in houses):
                                                                                print('Found')
                                                                                print('%12s|%12s|%12s|%12s|%12s' % tuple(house.resident for house in houses))
                                                                                print('%12s|%12s|%12s|%12s|%12s' % tuple(house.color for house in houses))
                                                                                print('%12s|%12s|%12s|%12s|%12s' % tuple(house.drink for house in houses))
                                                                                print('%12s|%12s|%12s|%12s|%12s' % tuple(house.pet for house in houses))
                                                                                print('%12s|%12s|%12s|%12s|%12s' % tuple(house.smoke for house in houses))
                                                                                return houses


def drinks_water():
    houses = solve()
    return [house.resident for house in houses if house.drink == 'water'][0]



def owns_zebra():
    houses = solve()
    return [house.resident for house in houses if house.pet == 'zebra'][0]


import timeit
print(timeit.timeit(solve, number=1))



def main():
    orders = list(range(5))
    perms = list(permutations(orders))

    for (englishman, spaniard, ukrainian, norwegian, japanese) in perms:
        if norwegian == 0:
            for (red, green, yellow, blue, ivory) in perms:
                if red == englishman and abs(norwegian - blue) == 1 and green - ivory == 1:
                    for (dog, fox, horse, snails, zebra) in perms:
                        if dog == spaniard:
                            for (coffee, tea, orange_juice, milk, water) in perms:
                                if milk == 2 and green == coffee and ukrainian == tea:
                                    for (old_gold, chesterfields, lucky_strike, parliaments, kools) in perms:
                                        if old_gold == snails and kools == yellow and abs(chesterfields - fox) == 1 and abs(kools - horse) == 1 and lucky_strike == orange_juice and japanese == parliaments:
                                            print('found')
                                            print(englishman, spaniard, ukrainian, norwegian, japanese)
                                            print(red, green, yellow, blue, ivory)
                                            print(dog, fox, horse, snails, zebra)
                                            print(coffee, tea, orange_juice, milk, water)
                                            print(old_gold, chesterfields, lucky_strike, parliaments, kools)
                                            return None

print(timeit.timeit(main, number=1))