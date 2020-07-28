import re

def is_valid(isbn):
    scaned_isbn = list(map(lambda x: 10 if x == 'X' else int(x), re.findall('[\dX]', isbn)))
    if len(scaned_isbn) != 10:
        return False
    elif 10 in scaned_isbn and scaned_isbn.index(10) != 9:
        return False
    else:
        sum_of_isbn = 0
        for i in range(len(scaned_isbn)):
            sum_of_isbn += scaned_isbn[i] * (10 - i)
        return sum_of_isbn % 11 == 0
