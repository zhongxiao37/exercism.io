def valid_triangle(f):
    return lambda s: all(s) and 2 * max(s) < sum(s) and f(s)


@valid_triangle
def equilateral(sides):
    return len(set(sides)) == 1

@valid_triangle
def isosceles(sides):
    return len(set(sides)) <= 2

@valid_triangle
def scalene(sides):
    return not isosceles(sides)

