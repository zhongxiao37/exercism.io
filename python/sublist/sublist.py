"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

import re

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = -1
EQUAL = 0
UNEQUAL = None


def sublist(list_one, list_two):
    string_one = '_'.join(map(str, list_one))
    string_two = '_'.join(map(str, list_two))
    if string_one == string_two:
        return EQUAL

    if re.match(f'.*{string_one}.*', string_two):
        return SUBLIST
    
    if re.match(f'.*{string_two}.*', string_one):
        return SUPERLIST
    
    return UNEQUAL
    