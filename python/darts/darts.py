from math import sqrt

def score(x, y):
    radius = sqrt(x * x + y * y)
    if radius > 10:
        return 0
    elif radius > 5:
        return 1
    elif radius > 1:
        return 5
    else:
        return 10
