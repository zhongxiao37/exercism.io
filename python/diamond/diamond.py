from string import ascii_uppercase
from itertools import chain

def rows(letter):
    letter_index = ascii_uppercase.index(letter)
    index_for_characters = [i for i in chain(range(letter_index + 1), range(letter_index - 1, -1, -1))]
    diamond = []
    for row in index_for_characters:
        row_data = []
        for col in range(len(index_for_characters)):
            row_data.append(ascii_uppercase[row] if abs(col - letter_index) == row else ' ')
        diamond.append(''.join(row_data))
    return diamond